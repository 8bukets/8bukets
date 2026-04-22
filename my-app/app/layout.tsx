import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Next.js 16 Scaled App",
  description: "Scaling Next.js 16 breaking changes with best practices.",
};

export default function RootLayout({
  children,
}: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
