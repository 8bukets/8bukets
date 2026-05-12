import Link from "next/link";
import AuthForm from "../components/auth-form";

export default function LoginPage() {
  return (
    <div className="container auth-shell">
      <AuthForm mode="login" />
      <p className="auth-switch">
        Don't have an account? <Link href="/register">Sign up</Link>
      </p>
    </div>
  );
}
