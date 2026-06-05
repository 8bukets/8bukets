import Link from "next/link";
import ReviewForm from "../../components/review-form";
import { getSoftwareDetail } from "../../lib/api";

export default function SoftwareDetailPage({ software, reviews }) {
  if (!software) {
    return (
      <div className="container">
        <div className="card">
          <h1>Software not found</h1>
          <p className="muted">The requested software page could not be loaded.</p>
        </div>
      </div>
    );
  }

  const formatRating = (value) => Number(value || 0).toFixed(1);

  return (
    <div className="container">
      <section className="section-head">
        <span className="eyebrow">{software.category}</span>
        <h1>{software.name}</h1>
        <div className="inline-meta">
          <span className="pill">★ {formatRating(software.average_rating)}</span>
          <span>{software.review_count} approved reviews</span>
          {software.website_url ? <span>{software.website_url}</span> : null}
        </div>
        <p className="section-copy">{software.description}</p>
      </section>

      <section className="detail-shell">
        <div className="review-list">
          {reviews.map((review) => (
            <article key={review.id} className="card review-card">
              <div className="inline-meta">
                <span className="pill">{review.status}</span>
                <span>{review.author_email}</span>
                <span>★ {formatRating(review.review_rating)}</span>
                <span>{review.comment_count} comments</span>
              </div>
              <div>
                <h3>{review.title}</h3>
                <p>{review.content}</p>
              </div>
              <div className="inline-meta">
                <span>Sentiment {review.sentiment_score}</span>
              </div>
              <Link href={`/reviews/${review.id}`} className="btn btn-outline">
                Open review discussion
              </Link>
            </article>
          ))}
          {reviews.length === 0 ? (
            <div className="card">
              <p className="muted">No approved reviews yet. Be the first to submit one.</p>
            </div>
          ) : null}
        </div>
        <div className="stack">
          <div className="card">
            <h3>Publishing flow</h3>
            <div className="stack">
              <div className="status-banner"><strong>1.</strong><span>User submits review</span></div>
              <div className="status-banner"><strong>2.</strong><span>AI placeholder computes sentiment and spam risk</span></div>
              <div className="status-banner"><strong>3.</strong><span>Admin approves or rejects</span></div>
              <div className="status-banner"><strong>4.</strong><span>Approved reviews become visible here</span></div>
            </div>
            <div style={{ marginTop: '16px' }}>
                <Link href={`/create-review?softwareId=${software.id}&name=${encodeURIComponent(software.name)}`} className="btn btn-primary">
                    Write standalone review
                </Link>
            </div>
          </div>
          <ReviewForm softwareId={software.id} />
        </div>
      </section>
    </div>
  );
}

export async function getServerSideProps({ params }) {
  const { slug } = params;
  try {
    const data = await getSoftwareDetail(slug);
    if (!data) {
      return { props: { software: null, reviews: [] } };
    }
    return {
      props: {
        software: data.software,
        reviews: data.reviews,
      },
    };
  } catch (error) {
    return { props: { software: null, reviews: [] } };
  }
}
