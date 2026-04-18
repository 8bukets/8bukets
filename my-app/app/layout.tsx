import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import { LayoutProps } from "@/antigravity/core";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Next.js 16 Scaled App",
  description: "Scaling Next.js 16 breaking changes with best practices.",
};

export default function RootLayout({
  children,
}: LayoutProps) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
      data-scroll-behavior="smooth"
    >
      {/* 
        Scalable Pattern: View Transitions
        When using Next.js 16, adding viewTransition: true to your next.config.ts 
        and using the ViewTransition API in React 19.2 allows you to scale 
        your UI animations without extra JS weight.
      */}
      <body className="min-h-full flex flex-col">{children}</body>
    </html>
  );
}
