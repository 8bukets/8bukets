'use client';

import { useEffect, useState } from 'react';

type StatusResponse = {
  supabase: { status: string; error: string | null };
  mongodb: { status: string; error: string | null };
};

export default function Home() {
  const [status, setStatus] = useState<StatusResponse | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchStatus() {
      try {
        const res = await fetch('/api/status');
        const data = await res.json();
        setStatus(data);
      } catch (err) {
        console.error('Failed to fetch status', err);
      } finally {
        setLoading(false);
      }
    }
    fetchStatus();
  }, []);

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start max-w-2xl w-full">
        <h1 className="text-4xl font-bold tracking-tight mb-4">Googleov Full-Stack Ekosustav</h1>

        <div className="w-full bg-white dark:bg-zinc-900 rounded-xl shadow-md overflow-hidden border border-zinc-200 dark:border-zinc-800">
          <div className="p-6">
            <h2 className="text-xl font-semibold mb-4">Database Synchronization Status</h2>

            {loading ? (
              <p className="text-zinc-500 animate-pulse">Checking connections...</p>
            ) : status ? (
              <div className="space-y-4">
                <div className="flex items-center justify-between p-4 bg-zinc-50 dark:bg-zinc-800 rounded-lg">
                  <div className="flex items-center gap-3">
                    <div className={`w-3 h-3 rounded-full ${status.supabase.status === 'connected' ? 'bg-green-500' : 'bg-red-500'}`}></div>
                    <span className="font-medium">Supabase (Relational & Auth)</span>
                  </div>
                  <span className="text-sm font-mono text-zinc-500">{status.supabase.status}</span>
                </div>
                {status.supabase.error && <p className="text-sm text-red-500 px-4">Error: {status.supabase.error}</p>}

                <div className="flex items-center justify-between p-4 bg-zinc-50 dark:bg-zinc-800 rounded-lg">
                  <div className="flex items-center gap-3">
                    <div className={`w-3 h-3 rounded-full ${status.mongodb.status === 'connected' ? 'bg-green-500' : 'bg-red-500'}`}></div>
                    <span className="font-medium">MongoDB (Unstructured Data)</span>
                  </div>
                  <span className="text-sm font-mono text-zinc-500">{status.mongodb.status}</span>
                </div>
                {status.mongodb.error && <p className="text-sm text-red-500 px-4">Error: {status.mongodb.error}</p>}
              </div>
            ) : (
              <p className="text-red-500">Failed to load status.</p>
            )}
          </div>
        </div>

        <div className="w-full">
          <h3 className="text-lg font-medium mb-3 mt-4">Architecture Roles</h3>
          <ul className="space-y-2 text-sm text-zinc-600 dark:text-zinc-400">
            <li className="flex gap-2"><b>IDE/AI:</b> <span>Google IDX / Jules (Code writing & automation)</span></li>
            <li className="flex gap-2"><b>Framework:</b> <span>Next.js (UI and API routes)</span></li>
            <li className="flex gap-2"><b>Hosting:</b> <span>Vercel (App delivery to users)</span></li>
            <li className="flex gap-2"><b>BaaS:</b> <span>Supabase (Authentication and SQL DB)</span></li>
            <li className="flex gap-2"><b>Database:</b> <span>MongoDB (Unstructured data storage)</span></li>
            <li className="flex gap-2"><b>Virtualization:</b> <span>Docker (Environment standardization)</span></li>
          </ul>
        </div>
      </main>
    </div>
  );
}
