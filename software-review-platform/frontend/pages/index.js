import Link from "next/link";
import SoftwareGrid from "../components/software-grid";
import { getFilteredSoftwareList, getSoftwareList } from "../lib/api";

export default function Home({ software, categories, filters }) {
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

      <section className="card filter-card">
        <form method="get" action="/" className="filter-form">
          <div className="filter-field">
            <label className="label" htmlFor="q">Search</label>
            <input
              id="q"
              name="q"
              className="input"
              defaultValue={filters.q}
              placeholder="Search software by name or description"
            />
          </div>
          <div className="filter-field">
            <label className="label" htmlFor="category">Category</label>
            <select id="category" name="category" className="input" defaultValue={filters.category}>
              <option value="">All categories</option>
              {categories.map((category) => (
                <option key={category} value={category}>
                  {category}
                </option>
              ))}
            </select>
          </div>
          <div className="filter-actions">
            <button type="submit" className="btn btn-primary">Apply filters</button>
            <Link href="/" className="btn btn-outline">Reset</Link>
          </div>
        </form>
      </section>

      <section className="section-head">
        <div>
          <h2>{software.length} Software Results</h2>
          <p className="section-copy">
            {filters.q || filters.category
              ? "Filtered view of the seeded launch catalog."
              : "Browse the seeded launch catalog and open individual software pages."}
          </p>
        </div>
      </section>

      <SoftwareGrid software={software} />
    </div>
  );
}

export async function getServerSideProps({ query }) {
  const filters = {
    q: typeof query.q === "string" ? query.q : "",
    category: typeof query.category === "string" ? query.category : "",
  };

  const [allSoftware, software] = await Promise.all([
    getSoftwareList(),
    getFilteredSoftwareList(filters),
  ]);

  const categories = [...new Set(allSoftware.map((item) => item.category).filter(Boolean))].sort();

  return {
    props: {
      software,
      categories,
      filters,
    },
  };
}
