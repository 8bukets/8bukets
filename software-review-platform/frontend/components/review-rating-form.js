"use client";

import { useState } from "react";
import { API_URL } from "../lib/config";
import { getStoredToken } from "../lib/session";

export default function ReviewRatingForm({ reviewId }) {
  const [score, setScore] = useState(5);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  async function handleSubmit(event) {
    event.preventDefault();
    setMessage("");
    setError("");

    const token = getStoredToken();
    if (!token) {
      setError("Log in before rating a review.");
      return;
    }

    setIsSubmitting(true);

    try {
      const response = await fetch(`${API_URL}/reviews/${reviewId}/ratings`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ score: Number(score) }),
      });

      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.error || "Failed to save rating");
      }

      setMessage(`Saved score ${data.score}/5`);
    } catch (submitError) {
      setError(submitError.message);
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <div className="card">
      <h3>Rate this review</h3>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <select className="input" value={score} onChange={(event) => setScore(event.target.value)}>
            {[5, 4, 3, 2, 1].map((value) => (
              <option key={value} value={value}>
                {value} / 5
              </option>
            ))}
          </select>
        </div>
        <button className="btn btn-outline" type="submit" disabled={isSubmitting}>
          {isSubmitting ? "Saving..." : "Save rating"}
        </button>
      </form>
      {message ? <p className="message-success" style={{ marginTop: "16px" }}>{message}</p> : null}
      {error ? <p className="message-error" style={{ marginTop: "16px" }}>{error}</p> : null}
    </div>
  );
}
