"use client";

import { useChat } from "@ai-sdk/react";
import { useEffect, useState } from 'react';
import { TelemetryProvider } from '@/lib/telemetry-context';
import { TelemetryHeader } from '@/components/telemetry/TelemetryHeader';

type StatusResponse = {
  supabase: { status: string; error: string | null };
  mongodb: { status: string; error: string | null };
};

type IntelligenceResponse = {
  snapshot: {
    evolution?: {
      parameter_shifts?: {
        current_version?: string;
      };
    };
    research?: {
      market_trends: string[];
    };
  } | null;
  state: {
    execution_mode?: string;
    cloud_provider?: string;
    last_sync?: string;
  } | null;
  workOrders: {
    id: string;
    type: string;
    goal: string;
  }[];
  logs: {
    time: string;
    type: string;
    msg: string;
  }[];
  marketLinks: {
    title: string;
    date: string;
    external_link: string;
    domain: string;
  }[];
};

function DashboardContent() {
  const [status, setStatus] = useState<StatusResponse | null>(null);
  const [intel, setIntel] = useState<IntelligenceResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [input, setInput] = useState("");
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const { messages, append } = useChat({
    onError: (e) => setErrorMessage(e.message),
  }) as any; // Cast to any to handle experimental useChat types in this environment

  useEffect(() => {
    async function fetchData() {
      try {
        const [statusRes, intelRes] = await Promise.all([
          fetch('/api/status'),
          fetch('/api/intelligence')
        ]);
        const statusData = await statusRes.json();
        const intelData = await intelRes.json();
        setStatus(statusData);
        setIntel(intelData);
      } catch (err) {
        console.error('Failed to fetch data', err);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  return (
    <div className="grid grid-rows-[auto_1fr_auto] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start max-w-4xl w-full">
        <div className="flex flex-col sm:flex-row justify-between items-end w-full gap-4">
          <div>
            <h1 className="text-4xl font-bold tracking-tight mb-2">Googleov Full-Stack Ekosustav</h1>
            <p className="text-zinc-500">Autonomous Cloud Intelligence Layer v{intel?.snapshot?.evolution?.parameter_shifts?.current_version || '1.0'}</p>
          </div>
          <div className="flex flex-col items-end gap-2">
            <div className="flex items-center gap-2 px-3 py-1 bg-green-500/10 text-green-500 rounded-full text-xs font-bold animate-pulse">
              <div className="w-2 h-2 bg-green-500 rounded-full"></div>
              SYSTEM ONLINE
            </div>
            {intel?.state?.execution_mode === 'cloud' && (
              <div className="flex items-center gap-2 px-3 py-1 bg-blue-500/10 text-blue-500 rounded-full text-[10px] font-bold border border-blue-500/20">
                <span className="relative flex h-2 w-2">
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
                  <span className="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
                </span>
                CLOUD AUTONOMY ACTIVE ({intel.state.cloud_provider?.toUpperCase()})
              </div>
            )}
          </div>
        </div>

        {/* Live Telemetry Header */}
        <TelemetryHeader />

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 w-full">
          {/* Section 1: Health & Connectivity */}
          <div className="bg-white dark:bg-zinc-900 rounded-xl shadow-md overflow-hidden border border-zinc-200 dark:border-zinc-800">
            <div className="p-6">
              <h2 className="text-xl font-semibold mb-4">Connectivity Hub</h2>
              {loading ? (
                <p className="text-zinc-500 animate-pulse">Checking connections...</p>
              ) : status ? (
                <div className="space-y-3">
                  <div className="flex items-center justify-between p-3 bg-zinc-50 dark:bg-zinc-800 rounded-lg">
                    <div className="flex items-center gap-3">
                      <div className={`w-2.5 h-2.5 rounded-full ${status.supabase.status === 'connected' ? 'bg-green-500' : 'bg-red-500'}`}></div>
                      <span className="font-medium text-sm">Supabase</span>
                    </div>
                    <span className="text-xs font-mono text-zinc-500">{status.supabase.status}</span>
                  </div>
                  <div className="flex items-center justify-between p-3 bg-zinc-50 dark:bg-zinc-800 rounded-lg">
                    <div className="flex items-center gap-3">
                      <div className={`w-2.5 h-2.5 rounded-full ${status.mongodb.status === 'connected' ? 'bg-green-500' : 'bg-red-500'}`}></div>
                      <span className="font-medium text-sm">MongoDB</span>
                    </div>
                    <span className="text-xs font-mono text-zinc-500">{status.mongodb.status}</span>
                  </div>
                </div>
              ) : (
                <p className="text-red-500">Failed to load status.</p>
              )}
            </div>
          </div>

          {/* Section 2: Market Intelligence */}
          <div className="bg-white dark:bg-zinc-900 rounded-xl shadow-md overflow-hidden border border-zinc-200 dark:border-zinc-800">
            <div className="p-6">
              <div className="flex justify-between items-center mb-4">
                <h2 className="text-xl font-semibold">Market Intelligence</h2>
                <a href="https://markposition.wordpress.com" target="_blank" className="text-[10px] text-zinc-400 hover:text-green-500">markposition.wordpress.com</a>
              </div>
              {loading ? (
                <p className="text-zinc-500 animate-pulse">Scanning market...</p>
              ) : intel?.marketLinks && intel.marketLinks.length > 0 ? (
                <div className="space-y-3">
                  {intel.marketLinks.map((link, idx) => (
                    <div key={idx} className="p-3 bg-zinc-50 dark:bg-zinc-800 rounded-lg border-l-4 border-green-500">
                      <div className="flex justify-between items-start mb-1">
                        <span className="text-[10px] font-bold text-green-600 uppercase">{link.domain || 'Direct Link'}</span>
                        <span className="text-[10px] text-zinc-400 font-mono">{link.date}</span>
                      </div>
                      <a href={link.external_link} target="_blank" className="text-sm font-medium hover:underline block truncate">{link.title}</a>
                    </div>
                  ))}
                </div>
              ) : (
                <div className="flex flex-col items-center justify-center py-8 text-zinc-400">
                  <span className="text-sm">No market data found. Scraper pending.</span>
                </div>
              )}

              {intel?.snapshot?.research?.market_trends && intel.snapshot.research.market_trends.length > 0 && (
                <div className="mt-6 border-t border-zinc-100 dark:border-zinc-800 pt-4">
                  <h3 className="text-sm font-bold text-zinc-500 mb-2 uppercase">Emerging Trends</h3>
                  <ul className="space-y-2">
                    {intel.snapshot.research.market_trends.map((trend, i) => (
                      <li key={i} className="text-xs flex items-start gap-2">
                        <span className="text-green-500">📈</span>
                        <span>{trend}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          </div>

          {/* Section 3: Active Work Orders */}
          <div className="bg-white dark:bg-zinc-900 rounded-xl shadow-md overflow-hidden border border-zinc-200 dark:border-zinc-800">
            <div className="p-6">
              <h2 className="text-xl font-semibold mb-4">Active Work Orders</h2>
              {loading ? (
                <p className="text-zinc-500 animate-pulse">Loading queue...</p>
              ) : intel?.workOrders && intel.workOrders.length > 0 ? (
                <div className="space-y-3">
                  {intel.workOrders.map((order) => (
                    <div key={order.id} className="p-3 bg-zinc-50 dark:bg-zinc-800 rounded-lg border-l-4 border-blue-500">
                      <div className="flex justify-between items-start mb-1">
                        <span className="text-xs font-bold text-blue-500 uppercase">{order.type}</span>
                        <span className="text-[10px] text-zinc-400 font-mono">{order.id}</span>
                      </div>
                      <p className="text-sm font-medium">{order.goal}</p>
                    </div>
                  ))}
                </div>
              ) : (
                <div className="flex flex-col items-center justify-center py-8 text-zinc-400">
                  <span className="text-sm">Queue is empty. System is optimal.</span>
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Section 4: Cognitive Action Logs */}
        <div className="w-full bg-white dark:bg-zinc-900 rounded-xl shadow-md overflow-hidden border border-zinc-200 dark:border-zinc-800">
          <div className="p-6">
            <h2 className="text-xl font-semibold mb-4">Cognitive Stream</h2>
            <div className="bg-black text-green-500 font-mono text-xs p-4 rounded-lg h-48 overflow-y-auto">
              {loading ? (
                <p className="animate-pulse">Fetching latest insights...</p>
              ) : intel?.logs && intel.logs.length > 0 ? (
                intel.logs.map((log, i: number) => (
                  <div key={i} className="mb-1">
                    <span className="text-zinc-500">[{log.time}]</span>{' '}
                    <span className={log.type === 'error' ? 'text-red-400' : 'text-green-400'}>
                      {log.type.toUpperCase()}:
                    </span>{' '}
                    {log.msg}
                  </div>
                ))
              ) : (
                <p className="text-zinc-600 italic">No recent cognitive activity logged.</p>
              )}
              {!loading && <div className="animate-pulse mt-2">_</div>}
            </div>
          </div>
        </div>

        {/* AI Assistant Section */}
        <div className="w-full mt-4 bg-white dark:bg-zinc-900 rounded-xl shadow-md p-6 border border-zinc-200 dark:border-zinc-800">
          <h2 className="text-xl font-semibold mb-4">AI Assistant</h2>
          <div className="flex flex-col w-full min-h-[300px]">
            <div className="flex-1 overflow-y-auto mb-4 space-y-4">
              {messages.map((message: any) => (
                <div key={message.id} className="whitespace-pre-wrap">
                  <span className="font-bold">{message.role === "user" ? "You: " : "AI: "}</span>
                  {message.parts ? message.parts.map((part: any, i: number) => {
                    switch (part.type) {
                      case "text":
                        return <span key={`${message.id}-${i}`}>{part.text}</span>;
                      default:
                        return null;
                    }
                  }) : (typeof message.content === 'string' ? message.content : JSON.stringify(message.content))}
                </div>
              ))}
            </div>

            {errorMessage && (
              <div className="text-red-500 text-sm mb-4">{errorMessage}</div>
            )}

            <form
              onSubmit={(e) => {
                e.preventDefault();
                if (!input.trim()) return;
                append({ role: 'user', content: input });
                setInput("");
                setErrorMessage(null);
              }}
              className="flex gap-2"
            >
              <input
                className="flex-1 p-2 border border-zinc-300 dark:border-zinc-700 bg-transparent rounded shadow-sm focus:outline-none focus:ring-2 focus:ring-green-500"
                value={input}
                placeholder="Ask about the ecosystem..."
                onChange={(e) => setInput(e.currentTarget.value)}
              />
              <button type="submit" className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded font-medium transition-colors">
                Send
              </button>
            </form>
          </div>
        </div>

        <div className="w-full">
          <h3 className="text-lg font-medium mb-3 mt-4">System Architecture</h3>
          <ul className="grid grid-cols-2 sm:grid-cols-3 gap-4 text-sm text-zinc-600 dark:text-zinc-400">
            <li className="flex flex-col p-3 bg-zinc-50 dark:bg-zinc-800 rounded-lg">
              <b>IDE/AI</b>
              <span>Google IDX / Jules</span>
            </li>
            <li className="flex flex-col p-3 bg-zinc-50 dark:bg-zinc-800 rounded-lg">
              <b>Framework</b>
              <span>Next.js 16</span>
            </li>
            <li className="flex flex-col p-3 bg-zinc-50 dark:bg-zinc-800 rounded-lg">
              <b>Hosting</b>
              <span>Vercel Cloud</span>
            </li>
            <li className="flex flex-col p-3 bg-zinc-50 dark:bg-zinc-800 rounded-lg">
              <b>Relational</b>
              <span>Supabase PG</span>
            </li>
            <li className="flex flex-col p-3 bg-zinc-50 dark:bg-zinc-800 rounded-lg">
              <b>Document</b>
              <span>MongoDB Atlas</span>
            </li>
            <li className="flex flex-col p-3 bg-zinc-50 dark:bg-zinc-800 rounded-lg">
              <b>Autonomy</b>
              <span>GH Actions 24/7</span>
            </li>
          </ul>
        </div>
      </main>
    </div>
  );
}

export default function Home() {
  return (
    <TelemetryProvider>
      <DashboardContent />
    </TelemetryProvider>
  );
}
