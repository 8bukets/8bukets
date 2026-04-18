import Image from "next/image";
import Link from "next/link";
import { Suspense } from "react";
import { PageProps, resolve, getSystemInsights } from "@/antigravity/core";
import { getAppStats } from "@/antigravity/services/stats";

export default async function CommandCenter({
  'use cache' params, searchParams }: PageProps) {
  await Promise.all([resolve(params), resolve(searchParams)]);

  return (
    <div className="flex flex-col min-h-screen bg-zinc-50 dark:bg-[#050505] text-zinc-900 dark:text-zinc-100 font-sans selection:bg-blue-500/30">
      {/* Dynamic Background */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-blue-600/10 blur-[120px] rounded-full animate-pulse" />
        <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-purple-600/10 blur-[120px] rounded-full animate-pulse" />
      </div>

      <main className="relative z-10 flex flex-col w-full max-w-7xl mx-auto p-6 md:p-12 gap-12">
        {/* Top Navigation */}
        <header className="flex flex-col md:flex-row md:items-center justify-between gap-6 border-b border-zinc-200 dark:border-zinc-800 pb-8">
          <div className="flex items-center gap-4">
            <div className="w-10 h-10 bg-black dark:bg-white rounded-xl flex items-center justify-center">
              <span className="text-white dark:text-black font-black text-xl">A</span>
            </div>
            <div>
              <h1 className="text-2xl font-bold tracking-tight">Antigravity Command</h1>
              <p className="text-zinc-500 text-sm font-medium">Autonomous Ecosystem v1.0 • Phase 6</p>
            </div>
          </div>
          <nav className="flex items-center gap-2 bg-white dark:bg-zinc-900 p-1 rounded-full border border-zinc-200 dark:border-zinc-800 shadow-sm">
            <Link href="/" className="px-4 py-2 bg-zinc-100 dark:bg-zinc-800 rounded-full text-sm font-bold">Dashboard</Link>
            <Link href="/store/featured" className="px-4 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 rounded-full text-sm transition-colors">Store</Link>
            <a href="https://github.com/8bukets/8bukets" className="px-4 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 rounded-full text-sm transition-colors">GitHub</a>
          </nav>
        </header>

        {/* Dashboard Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          
          {/* Main Status Column */}
          <div className="lg:col-span-2 flex flex-col gap-8">
            <section className="p-8 bg-white dark:bg-zinc-900/50 border border-zinc-200 dark:border-zinc-800 rounded-[2rem] shadow-sm">
              <h2 className="text-sm font-bold uppercase tracking-widest text-zinc-400 mb-6">Autonomous Systems Status</h2>
              <Suspense fallback={<div className="h-24 w-full bg-zinc-100 dark:bg-zinc-800 animate-pulse rounded-2xl" />}>
                <SystemHealthGrid />
              </Suspense>
            </section>

            <section className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div className="p-8 bg-gradient-to-br from-blue-600 to-blue-700 text-white rounded-[2rem] shadow-xl shadow-blue-500/20">
                <h3 className="text-lg font-bold mb-2">Predictive Scaling</h3>
                <Suspense fallback={<div className="h-20 animate-pulse" />}>
                  <AnalyticsForecast />
                </Suspense>
              </div>
              <div className="p-8 bg-white dark:bg-zinc-900/50 border border-zinc-200 dark:border-zinc-800 rounded-[2rem]">
                <h3 className="text-lg font-bold mb-2">Self-Healing</h3>
                <p className="text-zinc-500 dark:text-zinc-400 text-sm mb-6">Circuit breakers are active. Current state: <span className="text-green-500 font-bold">Stable</span></p>
                <div className="flex gap-2">
                  <div className="w-2 h-2 rounded-full bg-green-500" />
                  <div className="w-2 h-2 rounded-full bg-green-500/30" />
                  <div className="w-2 h-2 rounded-full bg-green-500/30" />
                </div>
              </div>
            </section>
          </div>

          {/* Right Sidebar: Cognitive Insights & Logs */}
          <div className="flex flex-col gap-8">
            <aside className="p-8 bg-zinc-900 text-white rounded-[2rem] flex flex-col gap-8">
              <div>
                <div className="flex items-center gap-2 mb-6">
                  <span className="text-xl">🧠</span>
                  <h2 className="text-lg font-bold">Cognitive Evolution</h2>
                </div>
                <Suspense fallback={<div className="h-20 bg-white/5 rounded-xl animate-pulse" />}>
                  <EvolutionInsights />
                </Suspense>
              </div>

              <div>
                <h3 className="text-xs font-black uppercase tracking-widest text-zinc-500 mb-4">Autonomous Activity</h3>
                <Suspense fallback={<div className="h-40 bg-white/5 rounded-xl animate-pulse" />}>
                  <ActivityFeed />
                </Suspense>
              </div>

              <button className="w-full py-4 bg-white text-black rounded-2xl font-bold hover:bg-zinc-200 transition-colors active:scale-95 text-sm">
                Apply Optimizations
              </button>
            </aside>
          </div>

        </div>

        {/* Footer info */}
        <footer className="flex justify-between items-center text-zinc-400 text-xs py-8">
          <p>Next.js 16.2.3 • Turbopack Optimized</p>
          <div className="flex gap-4">
            <span>Docker: Active</span>
            <span>Mongo: Healthy</span>
            <span>Supabase: Healthy</span>
          </div>
        </footer>
      </main>
    </div>
  );
}

async function SystemHealthGrid() {
  const stats = await getAppStats();
  const insights = await getSystemInsights();

  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
      <StatusItem label="MongoDB" value={stats.mongoStatus} ok={stats.mongoStatus === 'healthy'} />
      <StatusItem label="Supabase" value={stats.supabaseStatus} ok={stats.supabaseStatus === 'healthy' || stats.supabaseStatus === 'connected'} />
      <StatusItem label="Users" value={stats.activeUsers.toString()} ok={true} />
      <StatusItem label="Uptime" value={`${Math.floor(insights.uptime / 60)}m`} ok={true} />
    </div>
  )
}

function StatusItem({ label, value, ok }: { label: string, value: string, ok: boolean }) {
  return (
    <div className="flex flex-col gap-1">
      <span className="text-[10px] font-black uppercase text-zinc-400">{label}</span>
      <span className={`text-xl font-bold ${ok ? 'text-zinc-900 dark:text-white' : 'text-red-500'}`}>{value}</span>
    </div>
  )
}
async function AnalyticsForecast() {
  const { getRecentAnalytics } = await import('@/antigravity/services/analytics');
  const events = await getRecentAnalytics(3);

  if (events.length === 0) {
    return (
      <>
        <p className="text-blue-100 text-sm mb-6 leading-relaxed">The engine is currently learning from traffic patterns to optimize cache volatility.</p>
        <div className="h-1 bg-white/20 rounded-full overflow-hidden">
          <div className="h-full bg-white w-[35%] animate-pulse" />
        </div>
      </>
    )
  }

  return (
    <div className="space-y-3">
      {events.map((e: any, i: number) => (
        <div key={i} className="text-[11px] bg-white/10 p-2 rounded-lg border border-white/10">
          <span className="font-bold mr-2 text-white">[{e.tag}]</span>
          <span className="text-blue-200">New volatility pattern analyzed</span>
        </div>
      ))}
      <p className="text-[10px] text-blue-200 italic mt-2">Historical trends saved to MongoDB for forecasting.</p>
    </div>
  )
}

async function EvolutionInsights() {
...
  const insights = await getSystemInsights();
  
  return (
    <div className="space-y-4">
      {insights.ideas.map((idea: any, i: number) => (
        <div key={i} className="p-4 bg-white/5 rounded-2xl border border-white/10 hover:border-blue-500/50 transition-colors group">
          <div className="flex items-center justify-between mb-2">
            <p className="text-[10px] font-black uppercase text-blue-500 tracking-tighter">New Idea Synthesized</p>
            <span className="text-[10px] px-2 py-0.5 bg-blue-500 text-white rounded-full font-bold">{idea.complexity}</span>
          </div>
          <p className="text-sm font-bold mb-1 group-hover:text-blue-400 transition-colors">{idea.feature}</p>
          <p className="text-[11px] text-zinc-500 leading-relaxed">{idea.rationale}</p>
        </div>
      ))}
      <div className="p-4 bg-white/5 rounded-2xl border border-white/10 italic">
        <p className="text-[11px] text-zinc-500">Autonomous brain is scanning for more architectural gaps...</p>
      </div>
    </div>
  )
}

async function ActivityFeed() {
  const insights = await getSystemInsights();
  const { getNotifications } = await import('@/antigravity/services/notification');
  const notifications = await getNotifications();
  
  // Merge logs and notifications for the feed
  const feed = [
    ...notifications.map(n => ({ msg: n.message, time: new Date(n.timestamp).toLocaleTimeString(), type: n.type })),
    ...insights.logs
  ].sort((a, b) => b.time.localeCompare(a.time));

  const finalFeed = feed.length > 0 ? feed : [{ msg: 'System initialized. Awaiting autonomous signals...', time: '--:--', type: 'init' }];

  return (
    <div className="flex flex-col gap-3 max-h-[300px] overflow-y-auto pr-2 scrollbar-thin scrollbar-thumb-zinc-800">
      {finalFeed.map((log, i) => (
        <div key={i} className="flex gap-3 text-[11px] leading-relaxed animate-in fade-in slide-in-from-left-2">
          <span className="text-zinc-600 font-mono whitespace-nowrap">{log.time}</span>
          <p className={`${log.type === 'init' ? 'text-zinc-500 italic' : 'text-zinc-300'}`}>
            <span className={`font-bold mr-1 ${log.type === 'health' ? 'text-red-500' : 'text-blue-500'}`}>[{log.type.toUpperCase()}]</span>
            {log.msg}
          </p>
        </div>
      ))}
    </div>
  )
}
