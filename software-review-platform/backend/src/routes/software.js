// software-review-platform/backend/src/routes/software.js
import { Router } from "express";
import { getSoftware, getSoftwareBySlug } from "../controllers/softwareController.js";

const router = Router();

router.get("/", getSoftware);
router.get("/:slug", getSoftwareBySlug);

export default router;
