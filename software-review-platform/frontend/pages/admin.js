import AdminQueue from "../components/admin-queue";

export default function AdminPage() {
  return (
    <div className="container">
      <section className="section-head">
        <h1>Admin moderation</h1>
        <p className="section-copy">Review pending submissions and decide what goes live.</p>
      </section>
      <AdminQueue />
    </div>
  );
}
