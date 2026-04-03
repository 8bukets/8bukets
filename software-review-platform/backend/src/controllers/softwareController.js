// software-review-platform/backend/src/controllers/softwareController.js
import db from "../db/index.js";

export const getSoftware = async (req, res) => {
  try {
    const result = await db.query(
      `SELECT s.*,
              COALESCE(AVG(rt.score), 0) AS average_rating,
              COUNT(DISTINCT r.id) AS review_count
       FROM software s
       LEFT JOIN reviews r ON r.software_id = s.id AND r.status = 'approved'
       LEFT JOIN ratings rt ON rt.review_id = r.id
       GROUP BY s.id
       ORDER BY s.name ASC`
    );
    res.json(result.rows);
  } catch (error) {
    console.error("Failed to fetch software list:", error);
    res.status(500).json({ error: "Failed to fetch software" });
  }
};

export const getSoftwareBySlug = async (req, res) => {
  const { slug } = req.params;
  try {
    const softwareResult = await db.query(
      `SELECT s.*,
              COALESCE(AVG(rt.score), 0) AS average_rating,
              COUNT(DISTINCT r.id) AS review_count
       FROM software s
       LEFT JOIN reviews r ON r.software_id = s.id AND r.status = 'approved'
       LEFT JOIN ratings rt ON rt.review_id = r.id
       WHERE s.slug = $1
       GROUP BY s.id`,
      [slug]
    );

    const software = softwareResult.rows[0];
    if (!software) return res.status(404).json({ error: "Software not found" });

    const reviewsResult = await db.query(
      `SELECT r.id, r.title, r.content, r.status, r.sentiment_score, r.created_at,
              u.email AS author_email,
              COALESCE(AVG(rt.score), 0) AS review_rating,
              COUNT(DISTINCT c.id) AS comment_count
       FROM reviews r
       JOIN users u ON u.id = r.user_id
       LEFT JOIN ratings rt ON rt.review_id = r.id
       LEFT JOIN comments c ON c.review_id = r.id
       WHERE r.software_id = $1 AND r.status = 'approved'
       GROUP BY r.id, u.email
       ORDER BY r.created_at DESC`,
      [software.id]
    );

    res.json({ software, reviews: reviewsResult.rows });
  } catch (error) {
    console.error("Failed to fetch software detail:", error);
    res.status(500).json({ error: "Failed to fetch software" });
  }
};
