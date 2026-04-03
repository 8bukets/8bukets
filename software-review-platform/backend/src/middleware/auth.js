import jwt from "jsonwebtoken";

export default function (req, res, next) {
  if (!process.env.JWT_SECRET) {
    return res.status(500).json({ error: "JWT secret is not configured" });
  }

  const header = req.headers.authorization;

  if (!header || !header.startsWith("Bearer ")) {
    return res.status(401).json({ error: "No token" });
  }

  try {
    const token = header.slice(7);
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch {
    res.status(401).json({ error: "Invalid token" });
  }
}
