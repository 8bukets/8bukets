"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { API_URL } from "../lib/config";
import { storeSession } from "../lib/session";

export default function AuthForm({ mode }) {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [inviteCode, setInviteCode] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();
    setMessage("");
    setError("");

    try {
      const response = await fetch(`${API_URL}/auth/${mode}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          email,
          password,
          invite_code: mode === "register" ? inviteCode : undefined,
        }),
      });

      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.error || "Authentication failed");
      }

      if (mode === "login") {
        storeSession(data.token, data.user);
        router.push("/");
        router.refresh();
        return;
      }

      setMessage("Registration complete. You can log in now.");
      setPassword("");
    } catch (submitError) {
      setError(submitError.message);
    }
  }

  return (
    <div className="card">
      <h2>{mode === "login" ? "Welcome back" : "Create your account"}</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label className="label">Email address</label>
          <input
            type="email"
            className="input"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
            placeholder="name@example.com"
            required
          />
        </div>
        <div className="form-group">
          <label className="label">Password</label>
          <input
            type="password"
            className="input"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
            placeholder="••••••••"
            required
          />
        </div>
        {mode === "register" ? (
          <div className="form-group">
            <label className="label">Admin invite code (optional)</label>
            <input
              type="text"
              className="input"
              value={inviteCode}
              onChange={(event) => setInviteCode(event.target.value)}
              placeholder="Leave empty for regular user"
            />
          </div>
        ) : null}
        <button type="submit" className="btn btn-primary" style={{ width: "100%" }}>
          {mode === "login" ? "Log in" : "Register"}
        </button>
      </form>
      {message ? <p className="message-success" style={{ marginTop: "16px" }}>{message}</p> : null}
      {error ? <p className="message-error" style={{ marginTop: "16px" }}>{error}</p> : null}
    </div>
  );
}
