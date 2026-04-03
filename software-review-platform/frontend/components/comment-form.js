"use client";

import { useState } from "react";
import { getStoredToken } from "../lib/session";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:5000/api";

export default function CommentForm({ reviewId }) {
  const [content, setContent] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();
    setMessage("");
    setError("");

    const token = getStoredToken();
    if (!token) {
      setError("Log in before posting a comment.");
      return;
    }

    try {
      const response = await fetch(`${API_URL}/reviews/${reviewId}/comments`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ content }),
      });

      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.error || "Failed to post comment");
      }

      setMessage("Comment posted.");
      setContent("");
    } catch (submitError) {
      setError(submitError.message);
    }
  }

  return (
    <div className="card">
      <h3>Add comment</h3>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <textarea className="textarea" value={content} onChange={(event) => setContent(event.target.value)} required />
        </div>
        <button className="btn btn-primary" type="submit">Post comment</button>
      </form>
      {message ? <p className="message-success" style={{ marginTop: "16px" }}>{message}</p> : null}
      {error ? <p className="message-error" style={{ marginTop: "16px" }}>{error}</p> : null}
    </div>
  );
}
