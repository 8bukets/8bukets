"use client";

import { useChat } from "@ai-sdk/react";
import { useEffect, useState } from 'react';

type IntelligenceResponse = {
  snapshot: { evolution?: { parameter_shifts?: { current_version?: string } } } | null;
  workOrders: { id: string; type: string; status: string; goal: string; createdAt: string }[];
  logs: { time: string; type: string; agent: string; message: string; msg?: string }[];
};

export default function Home() {
  const [intel, setIntel] = useState<IntelligenceResponse | null>(null);
  const [loading, setLoading] = useState(true);

  const [input, setInput] = useState("");
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const { messages, sendMessage } = useChat({
    onError: async (e) => setErrorMessage(e.message),
  });

  useEffect(() => {
    async function fetchData() {
      try {
        const intelRes = await fetch('/api/intelligence');
        const intelData = await intelRes.json();
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
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start max-w-4xl w-full">
        <div className="flex flex-col sm:flex-row justify-between items-end w-full gap-4">
          <div>
            <h1 className="text-4xl font-bold tracking-tight mb-2">Googleov Full-Stack Ekosustav</h1>
            <p className="text-zinc-500">Autonomous Cloud Intelligence Layer v{intel?.snapshot?.evolution?.parameter_shifts?.current_version || '1.0'}</p>
          </div>
          <div className="flex items-center gap-2 px-3 py-1 bg-green-500/10 text-green-500 rounded-full text-xs font-bold animate-pulse">
            <div className="w-2 h-2 bg-green-500 rounded-full"></div>
            SYSTEM ONLINE
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 w-full">
          <div className="w-full bg-white dark:bg-zinc-900 rounded-xl shadow-md overflow-hidden border border-zinc-200 dark:border-zinc-800 flex flex-col h-[500px]">
            <div className="p-6 border-b border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-800/50">
              <h2 className="text-xl font-semibold mb-2">Command Chat</h2>
              <p className="text-xs text-zinc-500">Secured via @arcjet/next integration</p>
            </div>

            <div className="flex-1 overflow-y-auto p-6 space-y-4">
              {messages.length === 0 ? (
                <div className="text-center text-zinc-400 mt-10">
                  <p>System initialized.</p>
                  <p>Awaiting commands...</p>
                </div>
              ) : (
                messages.map((message) => (
                  <div key={message.id} className={`flex flex-col ${message.role === "user" ? "items-end" : "items-start"}`}>
                    <span className="text-xs font-mono mb-1 text-zinc-500">{message.role === "user" ? "GUEST" : "JULES.AI"}</span>
                    <div className={`px-4 py-2 rounded-lg max-w-[85%] ${message.role === "user" ? "bg-blue-600 text-white" : "bg-zinc-100 dark:bg-zinc-800"}`}>
                      {message.parts.map((part, i) => {
                        switch (part.type) {
                          case "text":
                            return <div key={`${message.id}-${i}`} className="whitespace-pre-wrap">{part.text}</div>;
                        }
                      })}
                    </div>
                  </div>
                ))
              )}
            </div>

            <div className="p-4 border-t border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900">
              {errorMessage && (
                <div className="text-red-500 text-sm mb-3 px-2 py-1 bg-red-500/10 rounded">{errorMessage}</div>
              )}

              <form
                onSubmit={(e) => {
                  e.preventDefault();
                  if (!input.trim()) return;
                  sendMessage({ text: input });
                  setInput("");
                  setErrorMessage(null);
                }}
                className="flex gap-2"
              >
                <input
                  className="flex-1 px-4 py-2 border border-zinc-300 dark:border-zinc-700 rounded-lg bg-transparent focus:outline-none focus:ring-2 focus:ring-blue-500"
                  value={input}
                  placeholder="Execute command..."
                  onChange={(e) => setInput(e.currentTarget.value)}
                />
                <button type="submit" className="px-4 py-2 bg-zinc-900 dark:bg-white text-white dark:text-zinc-900 rounded-lg font-medium hover:opacity-90 transition-opacity">
                  Send
                </button>
              </form>
            </div>
          </div>

          <div className="space-y-8 flex flex-col">
            <div className="w-full bg-white dark:bg-zinc-900 rounded-xl shadow-md border border-zinc-200 dark:border-zinc-800 p-6 flex-1">
              <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
                <span className="inline-block w-2 h-2 rounded-full bg-blue-500"></span>
                Active Work Orders
              </h2>
              {loading ? (
                <p className="text-zinc-500 animate-pulse font-mono text-sm">Loading queue...</p>
              ) : intel?.workOrders && intel.workOrders.length > 0 ? (
                <div className="space-y-3 max-h-[150px] overflow-y-auto pr-2 custom-scrollbar">
                  {intel.workOrders.map((order) => (
                    <div key={order.id} className="p-3 bg-zinc-50 dark:bg-zinc-800 rounded-lg border-l-2 border-blue-500">
                      <div className="flex justify-between items-start mb-1">
                        <span className="text-xs font-bold text-blue-500 uppercase tracking-wider">{order.type}</span>
                        <span className="text-[10px] text-zinc-400 font-mono bg-zinc-200 dark:bg-zinc-900 px-1 rounded">{order.id.substring(0, 8)}...</span>
                      </div>
                      <p className="text-sm text-zinc-700 dark:text-zinc-300 leading-snug">{order.goal}</p>
                    </div>
                  ))}
                </div>
              ) : (
                <div className="flex items-center justify-center h-[100px] border border-dashed border-zinc-300 dark:border-zinc-700 rounded-lg">
                  <p className="text-zinc-500 italic text-sm">No active tasks in the swarm queue.</p>
                </div>
              )}
            </div>

            <div className="w-full bg-black rounded-xl shadow-md border border-zinc-800 p-6 font-mono flex-1">
              <h2 className="text-green-500 text-sm font-bold mb-4 uppercase tracking-widest flex items-center gap-2">
                <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
                Cognitive Matrix Terminal
              </h2>
              <div className="text-xs h-[150px] overflow-y-auto pr-2 flex flex-col-reverse custom-scrollbar">
                {loading ? (
                  <p className="text-zinc-500 animate-pulse text-green-500/50">Initializing cognitive link...</p>
                ) : intel?.logs && intel.logs.length > 0 ? (
                  <div className="space-y-2">
                    {intel.logs.map((log, i: number) => (
                      <div key={i} className="flex gap-2">
                        <span className="text-zinc-500 shrink-0">[{new Date(log.time).toLocaleTimeString()}]</span>
                        <span className={`shrink-0 ${log.type === 'error' ? 'text-red-400' : 'text-blue-400'}`}>
                          {log.type.toUpperCase()}:
                        </span>
                        <span className="text-green-400 opacity-90 break-all">{log.msg || log.message}</span>
                      </div>
                    ))}
                  </div>
                ) : (
                  <p className="text-green-500/50 italic">Waiting for telemetry data...</p>
                )}
                {!loading && <div className="animate-pulse mt-2 text-green-500 inline-block w-2 h-4 bg-green-500"></div>}
              </div>
            </div>
          </div>
        </div>

        <div className="w-full mt-4">
          <h3 className="text-lg font-medium mb-4 flex items-center gap-2">
            System Architecture
          </h3>
          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3">
            <div className="flex flex-col p-3 bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-lg shadow-sm hover:shadow-md transition-shadow">
              <span className="text-xs text-zinc-500 uppercase font-bold tracking-wider mb-1">IDE/AI</span>
              <span className="text-sm font-medium">Google IDX / Jules</span>
            </div>
            <div className="flex flex-col p-3 bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-lg shadow-sm hover:shadow-md transition-shadow">
              <span className="text-xs text-zinc-500 uppercase font-bold tracking-wider mb-1">Framework</span>
              <span className="text-sm font-medium">Next.js 16</span>
            </div>
            <div className="flex flex-col p-3 bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-lg shadow-sm hover:shadow-md transition-shadow">
              <span className="text-xs text-zinc-500 uppercase font-bold tracking-wider mb-1">Hosting</span>
              <span className="text-sm font-medium">Vercel Cloud</span>
            </div>
            <div className="flex flex-col p-3 bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-lg shadow-sm hover:shadow-md transition-shadow">
              <span className="text-xs text-zinc-500 uppercase font-bold tracking-wider mb-1">Relational</span>
              <span className="text-sm font-medium">Supabase PG</span>
            </div>
            <div className="flex flex-col p-3 bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-lg shadow-sm hover:shadow-md transition-shadow">
              <span className="text-xs text-zinc-500 uppercase font-bold tracking-wider mb-1">Document</span>
              <span className="text-sm font-medium">MongoDB Atlas</span>
            </div>
            <div className="flex flex-col p-3 bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-lg shadow-sm hover:shadow-md transition-shadow">
              <span className="text-xs text-zinc-500 uppercase font-bold tracking-wider mb-1">Autonomy</span>
              <span className="text-sm font-medium">GH Actions 24/7</span>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
