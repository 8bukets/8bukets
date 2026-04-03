import Link from "next/link";
import SoftwareGrid from "../components/software-grid";
import { getSoftwareList } from "../lib/api";

export default function Home({ software }) {
  return (
    <div className="container">
      <section className="hero">
        <div className="hero-copy">
          <span className="eyebrow">Review platform starter</span>
          <h1>Find the right software with trust, moderation, and structured reviews.</h1>
          <p>
            This MVP starter includes auth, software pages, ratings, comments,
            moderation, and a deployable Next.js plus Express plus PostgreSQL foundation.
          </p>
          <div className="hero-actions">
            <Link href="/register" className="btn btn-primary">Create account</Link>
            <Link href="/admin" className="btn btn-outline">Open moderation panel</Link>
          </div>
          <p className="muted" style={{ marginTop: "16px" }}>
            Demo seed includes approved reviews, comments, ratings, and one pending moderation example.
          </p>
        </div>
        <div className="hero-panel card">
          <div className="stat-row">
            <strong>{software.length}</strong>
            <span>Seeded software profiles</span>
          </div>
          <div className="stat-row">
            <strong>Auth</strong>
            <span>JWT login and role-aware admin flow</span>
          </div>
          <div className="stat-row">
            <strong>Moderation</strong>
            <span>Pending, approved, rejected with AI placeholders</span>
          </div>
        </div>
      </section>

      <section className="section-head">
        <div>
          <h2>Featured Software</h2>
          <p className="section-copy">Browse products, open their review pages, and test the end-to-end flow.</p>
        </div>
      </section>

      <SoftwareGrid software={software} />
    </div>
  );
}

export async function getServerSideProps() {
  const software = await getSoftwareList();
  return {
    props: {
      software,
    },
  };
}
