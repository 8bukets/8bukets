"use client";

import { useState } from "react";
import { getStoredToken } from "../lib/session";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:5000/api";

export default function ReviewForm({ softwareId }) {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [score, setScore] = useState(5);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();
    setMessage("");
    setError("");

    const token = getStoredToken();
    if (!token) {
      setError("Log in before submitting a review.");
      return;
    }

    try {
      const response = await fetch(`${API_URL}/reviews`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          software_id: softwareId,
          title,
          content,
          score: Number(score),
        }),
      });

      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.error || "Failed to submit review");
      }

      setMessage(`Review submitted with status: ${data.status}`);
      setTitle("");
      setContent("");
      setScore(5);
    } catch (submitError) {
      setError(submitError.message);
    }
  }

  return (
    <div className="card">
      <h3>Write a review</h3>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label className="label">Title</label>
          <input className="input" value={title} onChange={(event) => setTitle(event.target.value)} required />
        </div>
        <div className="form-group">
          <label className="label">Overall score</label>
          <select className="input" value={score} onChange={(event) => setScore(event.target.value)}>
            {[5, 4, 3, 2, 1].map((value) => (
              <option key={value} value={value}>
                {value} / 5
              </option>
            ))}
          </select>
        </div>
        <div className="form-group">
          <label className="label">Review</label>
          <textarea className="textarea" value={content} onChange={(event) => setContent(event.target.value)} required />
        </div>
        <button type="submit" className="btn btn-primary">Submit review</button>
      </form>
      {message ? <p className="message-success" style={{ marginTop: "16px" }}>{message}</p> : null}
      {error ? <p className="message-error" style={{ marginTop: "16px" }}>{error}</p> : null}
    </div>
  );
}
