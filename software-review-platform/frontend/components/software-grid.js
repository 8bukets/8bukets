import Link from "next/link";

function formatRating(value) {
  return Number(value || 0).toFixed(1);
}

export default function SoftwareGrid({ software }) {
  if (!software.length) {
    return (
      <div className="card">
        <h3>No software matched your filters</h3>
        <p className="muted">Try clearing filters or using a broader search term.</p>
      </div>
    );
  }

  return (
    <div className="software-grid">
      {software.map((item) => (
        <article key={item.id} className="card software-card">
          <div className="meta-row">
            <span className="pill">{item.category}</span>
            <span className="stars">★ {formatRating(item.average_rating)}</span>
          </div>
          <div>
            <h3>{item.name}</h3>
            <p className="muted">{item.description}</p>
          </div>
          <div className="inline-meta">
            <span>{item.review_count} approved reviews</span>
            {item.website_url ? <span>{item.website_url}</span> : null}
          </div>
          <Link href={`/software/${item.slug}`} className="btn btn-outline">
            View software page
          </Link>
        </article>
      ))}
    </div>
  );
}
