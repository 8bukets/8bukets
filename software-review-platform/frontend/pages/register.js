import Link from "next/link";
import AuthForm from "../components/auth-form";

export default function RegisterPage() {
  return (
    <div className="container auth-shell">
      <AuthForm mode="register" />
      <p className="auth-switch">
        Already have an account? <Link href="/login">Log in</Link>
      </p>
    </div>
  );
}
