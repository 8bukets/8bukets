// software-review-platform/backend/src/controllers/reviewController.js
import db from "../db/index.js";
import { analyzeSentiment } from "../utils/moderation.js";

export const getReviews = async (req, res) => {
  const { software_id, status } = req.query;
  const params = [];
  const filters = [];

  if (software_id) {
    params.push(software_id);
    filters.push(`r.software_id = $${params.length}`);
  }

  if (status) {
    params.push(status);
    filters.push(`r.status = $${params.length}`);
  }

  const whereClause = filters.length ? `WHERE ${filters.join(" AND ")}` : "";

  try {
    const result = await db.query(
      `SELECT r.id, r.title, r.content, r.status, r.sentiment_score, r.created_at,
              u.email AS author_email, s.name AS software_name,
              COALESCE(AVG(rt.score), 0) AS review_rating,
              COUNT(DISTINCT c.id) AS comment_count
       FROM reviews r
       JOIN users u ON r.user_id = u.id
       JOIN software s ON r.software_id = s.id
       LEFT JOIN ratings rt ON rt.review_id = r.id
       LEFT JOIN comments c ON c.review_id = r.id
       ${whereClause}
       GROUP BY r.id, u.email, s.name
       ORDER BY r.created_at DESC`,
      params
    );
    res.json(result.rows);
  } catch (error) {
    console.error("Failed to fetch reviews:", error);
    res.status(500).json({ error: "Failed to fetch reviews" });
  }
};

export const getPendingReviews = async (req, res) => {
  if (req.user.role !== "admin") {
    return res.status(403).json({ error: "Admin access required" });
  }

  try {
    const result = await db.query(
      `SELECT r.id, r.title, r.content, r.status, r.sentiment_score, r.created_at,
              u.email AS author_email, s.name AS software_name
       FROM reviews r
       JOIN users u ON r.user_id = u.id
       JOIN software s ON r.software_id = s.id
       WHERE r.status = 'pending'
       ORDER BY r.created_at ASC`
    );

    res.json(result.rows);
  } catch (error) {
    console.error("Failed to fetch moderation queue:", error);
    res.status(500).json({ error: "Failed to fetch moderation queue" });
  }
};

export const getReviewById = async (req, res) => {
  try {
    const reviewResult = await db.query(
      `SELECT r.id, r.title, r.content, r.status, r.sentiment_score, r.created_at,
              u.email AS author_email, s.name AS software_name, s.slug AS software_slug,
              COALESCE(AVG(rt.score), 0) AS review_rating
       FROM reviews r
       JOIN users u ON u.id = r.user_id
       JOIN software s ON s.id = r.software_id
       LEFT JOIN ratings rt ON rt.review_id = r.id
       WHERE r.id = $1
       GROUP BY r.id, u.email, s.name, s.slug`,
      [req.params.id]
    );

    const review = reviewResult.rows[0];
    if (!review) return res.status(404).json({ error: "Review not found" });

    const commentsResult = await db.query(
      `SELECT c.id, c.content, c.created_at, u.email AS author_email
       FROM comments c
       JOIN users u ON u.id = c.user_id
       WHERE c.review_id = $1
       ORDER BY c.created_at ASC`,
      [req.params.id]
    );

    res.json({ review, comments: commentsResult.rows });
  } catch (error) {
    console.error("Failed to fetch review detail:", error);
    res.status(500).json({ error: "Failed to fetch review detail" });
  }
};

export const createReview = async (req, res) => {
  const { software_id, title, content, score } = req.body;

  if (!software_id || !title || !content || !score) {
    return res.status(400).json({ error: "software_id, title, content, and score are required" });
  }

  try {
    const reviewInsert = await db.query(
      `INSERT INTO reviews (user_id, software_id, title, content, status)
       VALUES ($1, $2, $3, $4, 'pending') RETURNING *`,
      [req.user.id, software_id, title, content]
    );

    const review = reviewInsert.rows[0];

    // AI analiza (mock)
    const sentiment = analyzeSentiment(content);

    await db.query(
      `UPDATE reviews SET sentiment_score=$1 WHERE id=$2`,
      [sentiment, review.id]
    );

    // stavi u moderation
    await db.query(
      `INSERT INTO moderation (review_id, status) VALUES ($1, 'pending')`,
      [review.id]
    );

    await db.query(
      `INSERT INTO ratings (user_id, review_id, score)
       VALUES ($1, $2, $3)`,
      [req.user.id, review.id, score]
    );

    res.status(201).json({ ...review, score, moderation_reason: "Awaiting moderation" });
  } catch (error) {
    console.error("Failed to create review:", error);
    res.status(500).json({ error: "Failed to create review" });
  }
};

export const addComment = async (req, res) => {
  const { content } = req.body;

  if (!content) {
    return res.status(400).json({ error: "Comment content is required" });
  }

  try {
    const result = await db.query(
      `INSERT INTO comments (user_id, review_id, content)
       VALUES ($1, $2, $3)
       RETURNING id, content, created_at`,
      [req.user.id, req.params.id, content]
    );

    res.status(201).json(result.rows[0]);
  } catch (error) {
    console.error("Failed to add comment:", error);
    res.status(500).json({ error: "Failed to add comment" });
  }
};

export const rateReview = async (req, res) => {
  const { score } = req.body;

  if (!score || score < 1 || score > 5) {
    return res.status(400).json({ error: "Score must be between 1 and 5" });
  }

  try {
    const result = await db.query(
      `INSERT INTO ratings (user_id, review_id, score)
       VALUES ($1, $2, $3)
       ON CONFLICT (user_id, review_id)
       DO UPDATE SET score = EXCLUDED.score
       RETURNING id, score`,
      [req.user.id, req.params.id, score]
    );

    res.status(201).json(result.rows[0]);
  } catch (error) {
    console.error("Failed to save rating:", error);
    res.status(500).json({ error: "Failed to save rating" });
  }
};

export const moderateReview = async (req, res) => {
  const { status, reason } = req.body;

  if (req.user.role !== "admin") {
    return res.status(403).json({ error: "Admin access required" });
  }

  if (!["approved", "rejected"].includes(status)) {
    return res.status(400).json({ error: "Status must be approved or rejected" });
  }

  try {
    const result = await db.query(
      `UPDATE reviews SET status = $1 WHERE id = $2 RETURNING *`,
      [status, req.params.id]
    );

    const review = result.rows[0];
    if (!review) return res.status(404).json({ error: "Review not found" });

    await db.query(
      `INSERT INTO moderation (review_id, status, reason, reviewed_by)
       VALUES ($1, $2, $3, $4)`,
      [req.params.id, status, reason || null, req.user.id]
    );

    res.json(review);
  } catch (error) {
    console.error("Failed to moderate review:", error);
    res.status(500).json({ error: "Failed to moderate review" });
  }
};
