"use client";

import { useEffect, useState } from "react";
import { getStoredToken, getStoredUser } from "../lib/session";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:5000/api";

export default function AdminQueue() {
  const [queue, setQueue] = useState([]);
  const [error, setError] = useState("");
  const [message, setMessage] = useState("");
  const [authorized, setAuthorized] = useState(false);

  async function loadQueue() {
    const token = getStoredToken();
    const user = getStoredUser();

    if (!token || !user || user.role !== "admin") {
      setAuthorized(false);
      return;
    }

    setAuthorized(true);

    try {
      const response = await fetch(`${API_URL}/reviews/pending`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
        cache: "no-store",
      });

      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.error || "Failed to load moderation queue");
      }

      setQueue(data);
    } catch (loadError) {
      setError(loadError.message);
    }
  }

  useEffect(() => {
    loadQueue();
  }, []);

  async function moderate(reviewId, status) {
    const token = getStoredToken();
    setMessage("");
    setError("");

    try {
      const response = await fetch(`${API_URL}/reviews/${reviewId}/moderate`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          status,
          reason: status === "approved" ? "Approved by admin" : "Rejected by admin",
        }),
      });

      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.error || "Moderation failed");
      }

      setMessage(`Review ${reviewId} marked as ${data.status}.`);
      await loadQueue();
    } catch (moderateError) {
      setError(moderateError.message);
    }
  }

  if (!authorized) {
    return (
      <div className="card">
        <h2>Moderation queue</h2>
        <p className="muted">
          Log in as an admin to access this panel. You can register an admin account with the invite code defined in backend env.
        </p>
      </div>
    );
  }

  return (
    <div className="stack">
      <div className="card">
        <h2>Moderation queue</h2>
        <p className="muted">Approve or reject pending reviews before they appear on public software pages.</p>
        {message ? <p className="message-success">{message}</p> : null}
        {error ? <p className="message-error">{error}</p> : null}
      </div>
      {queue.map((item) => (
        <article key={item.id} className="card queue-item">
          <div className="inline-meta">
            <span className="pill">{item.status}</span>
            <span>{item.software_name}</span>
            <span>{item.author_email}</span>
          </div>
          <div>
            <h3>{item.title}</h3>
            <p>{item.content}</p>
          </div>
          <div className="inline-meta">
            <span>Sentiment {item.sentiment_score}</span>
          </div>
          <div className="admin-actions">
            <button className="btn btn-primary" type="button" onClick={() => moderate(item.id, "approved")}>
              Approve
            </button>
            <button className="btn btn-outline" type="button" onClick={() => moderate(item.id, "rejected")}>
              Reject
            </button>
          </div>
        </article>
      ))}
      {queue.length === 0 ? (
        <div className="card">
          <p className="muted">No pending reviews right now.</p>
        </div>
      ) : null}
    </div>
  );
}
