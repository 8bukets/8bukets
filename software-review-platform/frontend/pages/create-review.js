import { useRouter } from "next/router";
import ReviewForm from "../components/review-form";

export default function CreateReviewPage() {
  const router = useRouter();
  const { softwareId, name } = router.query;

  return (
    <div className="container">
      <section className="section-head">
        <h1>Submit a Review</h1>
        {name && <p className="section-copy">Sharing your experience with <strong>{name}</strong></p>}
      </section>
      
      <div className="card-shell" style={{ maxWidth: '600px' }}>
        {softwareId ? (
          <ReviewForm softwareId={softwareId} />
        ) : (
          <div className="card">
            <p className="muted">Please select a software from the homepage to write a review.</p>
          </div>
        )}
      </div>
    </div>
  );
}
