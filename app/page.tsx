import Image from "next/image";
import Link from "next/link";
import { Suspense } from "react";
import { PageProps } from "@/antigravity/core";
import { getAppStats } from "@/antigravity/services/stats";

/**
 * Launch Page: Scaled and Boosted
 * Demonstrates connectivity, caching, and instant navigations.
 */
export default async function LaunchPage({ params, searchParams }: PageProps) {
  // Await mandatory async APIs
  await Promise.all([params, searchParams]);

  return (
    <div className="flex flex-col flex-1 bg-zinc-50 font-sans dark:bg-black overflow-hidden">
      {/* Visual background element */}
      <div className="absolute top-[-20%] left-[-10%] w-[50%] h-[50%] bg-blue-500/10 blur-[120px] rounded-full pointer-events-none" />
      <div className="absolute bottom-[-20%] right-[-10%] w-[50%] h-[50%] bg-purple-500/10 blur-[120px] rounded-full pointer-events-none" />

      <main className="relative flex flex-col flex-1 w-full max-w-6xl mx-auto py-12 px-8 lg:py-24">
        {/* Header Section */}
        <header className="flex items-center justify-between mb-16 animate-in fade-in slide-in-from-top-4 duration-1000">
          <div className="flex items-center gap-4">
            <Image
              className="dark:invert"
              src="/next.svg"
              alt="Next.js logo"
              width={100}
              height={20}
              priority
            />
            <span className="text-xl font-light text-zinc-400">/</span>
            <h1 className="text-xl font-bold tracking-tight">Antigravity V1</h1>
          </div>
          <div className="flex items-center gap-3">
            <Suspense fallback={<div className="h-6 w-32 bg-zinc-200 dark:bg-zinc-800 rounded animate-pulse" />}>
              <SystemStatus />
            </Suspense>
          </div>
        </header>

        {/* Hero Section */}
        <section className="mb-24 max-w-2xl animate-in fade-in slide-in-from-left-4 duration-1000 delay-200">
          <h2 className="text-6xl font-bold leading-[1.1] mb-8 tracking-tighter bg-gradient-to-r from-zinc-950 to-zinc-500 dark:from-white dark:to-zinc-500 bg-clip-text text-transparent">
            Build, Boost, and Scale at Light Speed.
          </h2>
          <p className="text-xl text-zinc-600 dark:text-zinc-400 mb-10 leading-relaxed">
            Your system is now fully synchronized with Next.js 16, MongoDB, and Supabase. 
            Experience zero-latency navigations and schema-safe data scaling.
          </p>
          <div className="flex flex-wrap gap-4">
            <Link
              href="/store/featured"
              className="px-8 py-4 bg-black text-white dark:bg-white dark:text-black rounded-full font-bold hover:scale-105 active:scale-95 transition-all shadow-xl shadow-black/10"
            >
              Enter the Store
            </Link>
            <a
              href="https://github.com"
              target="_blank"
              className="px-8 py-4 border border-zinc-200 dark:border-zinc-800 rounded-full font-medium hover:bg-zinc-100 dark:hover:bg-zinc-900 transition-colors"
            >
              Sync to GitHub
            </a>
          </div>
        </section>

        {/* Feature Grid */}
        <section className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16 animate-in fade-in slide-in-from-bottom-8 duration-1000 delay-500">
          <FeatureCard 
            title="Turbopack Boosted" 
            desc="Blazing fast HMR and incremental builds with filesystem caching." 
            icon="⚡"
          />
          <FeatureCard 
            title="Database Ready" 
            desc="Pre-configured MongoDB and Supabase layers with connection pooling." 
            icon="📦"
          />
          <FeatureCard 
            title="Data Integrity" 
            desc="Zod-validated schema-safe fetching with Next.js 16 Cache Components." 
            icon="🛡️"
          />
        </section>

        {/* Action Center */}
        <footer className="mt-auto pt-12 border-t border-zinc-200 dark:border-zinc-800 flex flex-col sm:flex-row justify-between items-center gap-6 text-zinc-500 text-sm">
          <div className="flex gap-8">
            <Link href="/shop/legacy" className="hover:text-black dark:hover:text-white transition-colors underline decoration-zinc-300 underline-offset-4">Legacy Proxy Link</Link>
            <Link href="/store/shoes" className="hover:text-black dark:hover:text-white transition-colors">Instant Navigation: Shoes</Link>
            <Link href="/store/hats" className="hover:text-black dark:hover:text-white transition-colors">Instant Navigation: Hats</Link>
          </div>
          <p>© 2026 Antigravity IDE • Next.js 16.2.3</p>
        </footer>
      </main>
    </div>
  );
}

async function SystemStatus() {
  const stats = await getAppStats();
  
  return (
    <div className="flex gap-4">
      <StatusIndicator label="MongoDB" status={stats.mongoStatus} />
      <StatusIndicator label="Supabase" status={stats.supabaseStatus} />
    </div>
  );
}

function StatusIndicator({ label, status }: { label: string, status: 'connected' | 'disconnected' }) {
  return (
    <div className="flex items-center gap-2 px-3 py-1 bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-full text-xs font-medium">
      <div className={`w-2 h-2 rounded-full ${status === 'connected' ? 'bg-green-500 shadow-[0_0_8px_rgba(34,197,94,0.5)]' : 'bg-red-500'}`} />
      <span>{label}</span>
    </div>
  );
}

function FeatureCard({ title, desc, icon }: { title: string, desc: string, icon: string }) {
  return (
    <div className="p-8 bg-white dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-900 rounded-3xl hover:border-zinc-400 dark:hover:border-zinc-700 transition-colors group">
      <div className="text-3xl mb-4 group-hover:scale-110 transition-transform origin-left">{icon}</div>
      <h3 className="text-lg font-bold mb-2">{title}</h3>
      <p className="text-zinc-500 dark:text-zinc-400 text-sm leading-relaxed">{desc}</p>
    </div>
  );
}
