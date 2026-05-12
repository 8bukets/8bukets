// software-review-platform/backend/src/routes/reviews.js
import { Router } from "express";
import {
  addComment,
  createReview,
  getPendingReviews,
  getReviewById,
  getReviews,
  moderateReview,
  rateReview,
} from "../controllers/reviewController.js";
import authMiddleware from "../middleware/auth.js";

const router = Router();

router.get("/", getReviews);
router.get("/pending", authMiddleware, getPendingReviews);
router.get("/:id", getReviewById);
router.post("/", authMiddleware, createReview);
router.post("/:id/comments", authMiddleware, addComment);
router.post("/:id/ratings", authMiddleware, rateReview);
router.patch("/:id/moderate", authMiddleware, moderateReview);

export default router;
