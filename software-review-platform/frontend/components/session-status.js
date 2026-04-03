"use client";

import { useEffect, useState } from "react";
import { clearSession, getStoredUser } from "../lib/session";

export default function SessionStatus() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    setUser(getStoredUser());
  }, []);

  if (!user) {
    return <div className="session-status">Anonymous session</div>;
  }

  return (
    <div className="session-status">
      Signed in as {user.email} ({user.role})
      <button
        type="button"
        className="btn btn-subtle"
        onClick={() => {
          clearSession();
          window.location.reload();
        }}
      >
        Log out
      </button>
    </div>
  );
}
