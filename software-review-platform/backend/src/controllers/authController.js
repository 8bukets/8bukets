// software-review-platform/backend/src/controllers/authController.js
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";
import db from "../db/index.js";
import { isValidEmail, isValidPassword, normalizedString } from "../utils/validation.js";

export const register = async (req, res) => {
  const email = normalizedString(req.body.email).toLowerCase();
  const password = req.body.password;
  const invite_code = normalizedString(req.body.invite_code);

  if (!email || !password) {
    return res.status(400).json({ error: "Email and password are required" });
  }

  if (!isValidEmail(email)) {
    return res.status(400).json({ error: "Enter a valid email address" });
  }

  if (!isValidPassword(password)) {
    return res.status(400).json({ error: "Password must be at least 8 characters long" });
  }

  try {
    const hash = await bcrypt.hash(password, 10);
    const role =
      invite_code && invite_code === process.env.ADMIN_INVITE_CODE ? "admin" : "user";
    const result = await db.query(
      "INSERT INTO users (email, password_hash, role) VALUES ($1, $2, $3) RETURNING id, email, role",
      [email, hash, role]
    );
    res.status(201).json(result.rows[0]);
  } catch (error) {
    console.error("Registration failed:", error);
    if (error.code === "23505") {
      return res.status(409).json({ error: "User already exists" });
    }
    res.status(500).json({ error: "Registration failed" });
  }
};

export const login = async (req, res) => {
  const email = normalizedString(req.body.email).toLowerCase();
  const password = req.body.password;

  if (!email || !password) {
    return res.status(400).json({ error: "Email and password are required" });
  }

  if (!isValidEmail(email)) {
    return res.status(400).json({ error: "Enter a valid email address" });
  }

  if (!process.env.JWT_SECRET) {
    return res.status(500).json({ error: "JWT secret is not configured" });
  }

  try {
    const result = await db.query("SELECT * FROM users WHERE email = $1", [email]);
    const user = result.rows[0];

    if (!user || !(await bcrypt.compare(password, user.password_hash))) {
      return res.status(401).json({ error: "Invalid credentials" });
    }

    const token = jwt.sign(
      { id: user.id, email: user.email, role: user.role },
      process.env.JWT_SECRET,
      { expiresIn: "7d" }
    );
    res.json({ token, user: { id: user.id, email: user.email, role: user.role } });
  } catch (error) {
    console.error("Login failed:", error);
    res.status(500).json({ error: "Login failed" });
  }
};

export const me = async (req, res) => {
  const header = req.headers.authorization;

  if (!header || !header.startsWith("Bearer ")) {
    return res.status(401).json({ error: "No token" });
  }

  try {
    const token = header.slice(7);
    if (!process.env.JWT_SECRET) {
      return res.status(500).json({ error: "JWT secret is not configured" });
    }

    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    res.json({
      id: decoded.id,
      email: decoded.email,
      role: decoded.role,
    });
  } catch (error) {
    console.error("Fetch current user failed:", error);
    res.status(401).json({ error: "Invalid token" });
  }
};
