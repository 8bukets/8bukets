import "../styles/globals.css";
import Link from "next/link";
import SessionStatus from "../components/session-status";

function MyApp({ Component, pageProps }) {
  return (
    <>
      <nav className="navbar">
        <div className="container navbar-inner">
          <Link href="/" className="logo">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect width="32" height="32" rx="8" fill="#9f4b20" />
              <path d="M16 7L18.45 12.18L24 12.97L20 16.92L20.95 22.5L16 19.82L11.05 22.5L12 16.92L8 12.97L13.55 12.18L16 7Z" fill="white" />
            </svg>
            <span>SOR Platform</span>
          </Link>
          <div className="nav-links">
            <Link href="/admin" className="btn btn-subtle">Admin</Link>
            <Link href="/login" className="btn btn-outline">Log in</Link>
            <Link href="/register" className="btn btn-primary">Sign up</Link>
          </div>
        </div>
      </nav>
      <main className="main-content">
        <div className="container" style={{ paddingTop: "16px" }}>
          <SessionStatus />
        </div>
        <Component {...pageProps} />
      </main>
      <footer className="footer">
        <div className="container">
          <p>&copy; 2026 Software Online Review Platform. MVP starter for software-online-review.com.</p>
        </div>
      </footer>
    </>
  );
}

export default MyApp;
