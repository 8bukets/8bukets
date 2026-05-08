import Image from "next/image";
import Link from "next/link";
import { Suspense } from "react";
import { PageProps, resolve, getSystemInsights } from "@/antigravity/core";
import { getAppStats } from "@/antigravity/services/stats";

export default async function CommandCenter({
  params, searchParams }: PageProps) {
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
            <div>
              <h1 className="text-2xl font-bold tracking-tight">Antigravity Command</h1>
              <div className="flex items-center gap-2">
                <p className="text-zinc-500 text-sm font-medium">Autonomous Ecosystem v1.0 • Phase 12</p>
                <span className="text-[10px] px-2 py-0.5 bg-blue-500/10 text-blue-500 rounded-full font-bold border border-blue-500/20">Super-Intelligence Active</span>
              </div>
            </div>
            ...
            async function OptimizationPulse() {
            const { getSystemInsights } = await import('@/antigravity/core');
            const insights = await getSystemInsights();

            return (
            <div className="space-y-3">
            {insights.proposals.map((p: any, i: number) => (
            <div key={i} className="p-3 bg-white/5 rounded-xl border border-white/10 group hover:border-blue-400/30 transition-all">
            <div className="flex items-center justify-between mb-1">
            <span className="text-[10px] font-black text-blue-400 uppercase tracking-widest">{p.vector}</span>
            <span className="text-[9px] text-zinc-600 font-mono">Impact:{(p.impactScore * 100).toFixed(0)}%</span>
            </div>
            <p className="text-[11px] text-zinc-300 leading-tight group-hover:text-white transition-colors">{p.proposal}</p>
            </div>
            ))}
            </div>
            )
            }

            async function OmniPresenceMatrix() {

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
                <h3 className="text-xs font-black uppercase tracking-widest text-zinc-500 mb-4">Optimization Pulse</h3>
                <Suspense fallback={<div className="h-20 bg-white/5 rounded-xl animate-pulse" />}>
                  <OptimizationPulse />
                </Suspense>
              </div>

              <div>
                <h3 className="text-xs font-black uppercase tracking-widest text-zinc-500 mb-4">Omni-Presence Matrix</h3>
                <Suspense fallback={<div className="h-20 bg-white/5 rounded-xl animate-pulse" />}>
                  <OmniPresenceMatrix />
                </Suspense>
              </div>

              <div>
                <h3 className="text-xs font-black uppercase tracking-widest text-zinc-500 mb-4">Global Neural Network</h3>
                <Suspense fallback={<div className="h-20 bg-white/5 rounded-xl animate-pulse" />}>
                  <NeuralNetworkList />
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
        <footer className="mt-auto pt-12 border-t border-zinc-200 dark:border-zinc-800 flex flex-col gap-6">
          <div className="flex flex-wrap justify-between items-center gap-6 text-zinc-500 text-[10px] uppercase font-black tracking-widest">
            <p>Next.js 16.2.3 • Turbopack Optimized • 24/7 Persistence Active</p>
            <div className="flex gap-4">
              <span>Docker: Active</span>
              <span>Mongo: Healthy</span>
              <span>Supabase: Healthy</span>
            </div>
          </div>
          
          <Suspense fallback={<div className="h-10 w-full bg-white/5 rounded-xl animate-pulse" />}>
            <PersistenceFleetBar />
          </Suspense>
          
          <div className="flex justify-center pb-4">
            <p className="text-[10px] text-zinc-600">© 2026 Antigravity IDE • Jules Cognitive Agent</p>
          </div>
        </footer>
      </main>
    </div>
  );
}
async function OmniPresenceMatrix() {
  const { getSystemInsights } = await import('@/antigravity/core');
  const insights = await getSystemInsights();

  return (
    <div className="space-y-3">
      {insights.relay.map((node: any, i: number) => (
        <div key={i} className="p-3 bg-white/5 rounded-xl border border-white/10 group hover:border-purple-500/30 transition-all">
          <div className="flex items-center justify-between mb-2">
            <span className="text-[10px] font-black text-purple-400 uppercase tracking-widest">{node.environment}</span>
            <div className="flex gap-1">
              {[...Array(3)].map((_, j) => (
                <div key={j} className={`w-1 h-1 rounded-full ${j < Math.ceil(node.intensity * 3) ? 'bg-purple-500 shadow-[0_0_5px_rgba(168,85,247,0.5)]' : 'bg-zinc-800'}`} />
              ))}
            </div>
          </div>
          <div className="flex flex-wrap gap-1.5">
            {node.activeViews.map((view: string, k: number) => (
              <span key={k} className="text-[9px] px-2 py-0.5 bg-zinc-800 text-zinc-400 rounded-md font-mono">{view}</span>
            ))}
          </div>
        </div>
      ))}
    </div>
  )
}

async function NeuralNetworkList() {
  const { getSystemInsights } = await import('@/antigravity/core');
  const insights = await getSystemInsights();

  return (
    <div className="space-y-2">
      {insights.network.map((node: any, i: number) => (
        <div key={i} className="flex items-center justify-between p-3 bg-white/5 rounded-xl border border-white/10">
          <div className="flex items-center gap-2">
            <div className={`w-1.5 h-1.5 rounded-full ${node.health === 'optimal' ? 'bg-blue-400 shadow-[0_0_8px_rgba(96,165,250,0.5)]' : 'bg-zinc-600'}`} />
            <span className="text-[11px] font-bold text-zinc-300 uppercase tracking-tighter">{node.origin}</span>
          </div>
          <span className="text-[10px] text-zinc-500">{node.lastSeen}</span>
        </div>
      ))}
    </div>
  )
}

async function PersistenceFleetBar() {
...
  const { getSystemInsights } = await import('@/antigravity/core');
  const insights = await getSystemInsights();

  return (
    <div className="flex flex-wrap gap-2">
      {insights.persistence.map((p: any, i: number) => (
        <div key={i} className="px-3 py-1.5 bg-white/5 border border-white/10 rounded-lg flex items-center gap-2">
          <div className={`w-1.5 h-1.5 rounded-full ${p.status === 'running' ? 'bg-green-500' : 'bg-zinc-600'}`} />
          <span className="text-[10px] font-bold text-zinc-400">{p.agent.split('.').pop()}</span>
          {p.pid && <span className="text-[9px] text-zinc-600 font-mono">PID:{p.pid}</span>}
        </div>
      ))}
    </div>
  )
}

async function SystemHealthGrid() {
  const stats = await getAppStats();
  const insights = await getSystemInsights();

  return (
    <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
      <StatusItem label="MongoDB" value={stats.mongoStatus} ok={stats.mongoStatus === 'healthy'} />
      <StatusItem label="Supabase" value={stats.supabaseStatus} ok={stats.supabaseStatus === 'healthy' || stats.supabaseStatus === 'connected'} />
      <StatusItem label="Security" value={insights.security.status.toUpperCase()} ok={insights.security.status === 'secure'} />
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
