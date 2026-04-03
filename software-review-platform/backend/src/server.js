import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import authRoutes from "./routes/auth.js";
import reviewRoutes from "./routes/reviews.js";
import softwareRoutes from "./routes/software.js";

dotenv.config();

export function createApp() {
  const app = express();

  app.use(
    cors({
      origin: process.env.CLIENT_ORIGIN || "http://localhost:3000",
    })
  );
  app.use(express.json());

  app.get("/api/health", (_req, res) => {
    res.json({ ok: true, service: "software-review-platform-backend" });
  });

  app.use("/api/auth", authRoutes);
  app.use("/api/reviews", reviewRoutes);
  app.use("/api/software", softwareRoutes);

  return app;
}

const app = createApp();

if (process.env.NO_LISTEN !== "1") {
  const port = process.env.PORT || 5000;
  const host = process.env.HOST || "127.0.0.1";

  app.listen(port, host, () => {
    console.log(`Server running on http://${host}:${port}`);
  });
}
