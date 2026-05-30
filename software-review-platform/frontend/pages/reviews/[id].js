import CommentForm from "../../components/comment-form";
import ReviewRatingForm from "../../components/review-rating-form";
import { getReviewDetail } from "../../lib/api";

export default function ReviewDetailPage({ review, comments }) {
  if (!review) {
    return (
      <div className="container">
        <div className="card">
          <h1>Review not found</h1>
        </div>
      </div>
    );
  }

  const formatRating = (value) => Number(value || 0).toFixed(1);

  return (
    <div className="container">
      <section className="detail-shell">
        <div className="stack">
          <article className="card review-card">
            <div className="inline-meta">
              <span className="pill">{review.status}</span>
              <span>{review.software_name}</span>
              <span>{review.author_email}</span>
              <span>★ {formatRating(review.review_rating)}</span>
            </div>
            <div>
              <h1>{review.title}</h1>
              <p>{review.content}</p>
            </div>
            <div className="inline-meta">
              <span>Sentiment {review.sentiment_score}</span>
            </div>
          </article>

          <div className="card">
            <h2>Discussion</h2>
            <div className="comment-list">
              {comments.map((comment) => (
                <div key={comment.id} className="comment">
                  <div className="inline-meta">
                    <span>{comment.author_email}</span>
                    <span>{new Date(comment.created_at).toLocaleString()}</span>
                  </div>
                  <p>{comment.content}</p>
                </div>
              ))}
              {comments.length === 0 ? <p className="muted">No comments yet.</p> : null}
            </div>
          </div>
        </div>
        <div className="stack">
          <ReviewRatingForm reviewId={review.id} />
          <CommentForm reviewId={review.id} />
        </div>
      </section>
    </div>
  );
}

export async function getServerSideProps({ params }) {
  const { id } = params;
  try {
    const data = await getReviewDetail(id);
    if (!data) {
      return { props: { review: null, comments: [] } };
    }
    return {
      props: {
        review: data.review,
        comments: data.comments,
      },
    };
  } catch (error) {
    return { props: { review: null, comments: [] } };
  }
}
