import Link from "next/link";
import { Suspense } from "react";

export default function DownloadPage() {
  return (
    <Suspense fallback={<div>Loading Download Portal...</div>}>
      <DownloadPageContent />
    </Suspense>
  );
}

function DownloadPageContent() {

  return (
    <div className="flex flex-col min-h-screen bg-zinc-50 dark:bg-[#050505] text-zinc-900 dark:text-zinc-100 font-sans selection:bg-blue-500/30">
      {/* Dynamic Background */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-[-20%] right-[-10%] w-[50%] h-[50%] bg-blue-600/10 blur-[140px] rounded-full animate-pulse" />
        <div className="absolute bottom-[-20%] left-[-10%] w-[50%] h-[50%] bg-purple-600/10 blur-[140px] rounded-full animate-pulse" />
      </div>

      <main className="relative z-10 flex flex-col w-full max-w-5xl mx-auto p-6 md:p-12 gap-12 flex-1">

        {/* Navigation */}
        <header className="flex justify-between items-center border-b border-zinc-200 dark:border-zinc-800 pb-6">
          <div className="flex items-center gap-3">
            <Link href="/" className="w-10 h-10 bg-black dark:bg-white rounded-xl flex items-center justify-center hover:scale-105 transition-transform">
              <span className="text-white dark:text-black font-black text-xl">A</span>
            </Link>
            <h1 className="text-xl font-bold tracking-tight">Antigravity Downloads</h1>
          </div>
          <nav className="flex items-center gap-2">
            <Link href="/" className="px-4 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 rounded-full text-sm transition-colors font-medium">Back to Command</Link>
          </nav>
        </header>

        {/* Hero Section */}
        <section className="flex flex-col items-center text-center mt-10 gap-6">
          <div className="inline-block px-3 py-1 bg-blue-500/10 border border-blue-500/20 text-blue-500 text-xs font-bold rounded-full mb-2 uppercase tracking-widest">
            Latest Release • v2.5.0
          </div>
          <h2 className="text-5xl md:text-7xl font-black tracking-tighter bg-clip-text text-transparent bg-gradient-to-br from-zinc-900 to-zinc-500 dark:from-white dark:to-zinc-500">
            Install the CLI
          </h2>
          <p className="text-lg text-zinc-500 max-w-2xl leading-relaxed mt-4">
            The Antigravity CLI bridges your local environment with the autonomous ecosystem. Manage agents, trigger cloud deployments, and sync iCloud operations directly from your terminal.
          </p>
        </section>

        {/* Installation Terminal */}
        <section className="w-full max-w-3xl mx-auto mt-8" id="antigravity-cli">
          <div className="bg-zinc-900 rounded-2xl overflow-hidden border border-zinc-800 shadow-2xl">
            {/* Terminal Header */}
            <div className="flex items-center justify-between px-4 py-3 bg-zinc-950 border-b border-zinc-800">
              <div className="flex gap-2">
                <div className="w-3 h-3 rounded-full bg-red-500/80" />
                <div className="w-3 h-3 rounded-full bg-yellow-500/80" />
                <div className="w-3 h-3 rounded-full bg-green-500/80" />
              </div>
              <span className="text-xs font-mono text-zinc-500">bash — antigravity-cli</span>
              <div className="w-12" /> {/* Spacer */}
            </div>

            {/* Terminal Body */}
            <div className="p-6 font-mono text-sm leading-relaxed text-zinc-300">
              <div className="mb-4">
                <span className="text-green-400"># Install globally via npm</span><br/>
                <span className="text-purple-400">$</span> npm install -g @antigravity/cli
              </div>

              <div className="mb-4 opacity-0 animate-[fadeIn_0.5s_ease-out_0.5s_forwards]">
                <span className="text-green-400"># Verify installation</span><br/>
                <span className="text-purple-400">$</span> antigravity --version<br/>
                <span className="text-zinc-500">Antigravity CLI v2.5.0 (Node.js v20+)</span>
              </div>

              <div className="opacity-0 animate-[fadeIn_0.5s_ease-out_1s_forwards]">
                <span className="text-green-400"># Authenticate with the ecosystem</span><br/>
                <span className="text-purple-400">$</span> antigravity login<br/>
                <span className="text-blue-400 animate-pulse">Authenticating with Google Cloud... Success.</span>
              </div>
            </div>
          </div>
        </section>

        {/* Alternative Downloads */}
        <section className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-16 max-w-4xl mx-auto w-full">
          {[
            { os: "macOS", arch: "Apple Silicon / Intel", icon: "🍎", cmd: "brew install antigravity" },
            { os: "Windows", arch: "x64 / ARM64", icon: "🪟", cmd: "winget install antigravity" },
            { os: "Linux", arch: "Debian / Ubuntu", icon: "🐧", cmd: "apt-get install antigravity-cli" }
          ].map((item, i) => (
            <div key={i} className="flex flex-col p-6 bg-white dark:bg-white/5 border border-zinc-200 dark:border-white/10 rounded-2xl hover:border-blue-500/50 transition-colors group cursor-pointer">
              <div className="text-3xl mb-4">{item.icon}</div>
              <h3 className="font-bold text-lg mb-1">{item.os}</h3>
              <p className="text-xs text-zinc-500 mb-6 font-medium">{item.arch}</p>

              <div className="mt-auto pt-4 border-t border-zinc-100 dark:border-white/10">
                <code className="text-xs font-mono text-zinc-600 dark:text-zinc-400 block break-all">
                  {item.cmd}
                </code>
              </div>
            </div>
          ))}
        </section>

      </main>

      {/* Footer */}
      <footer className="mt-auto border-t border-zinc-200 dark:border-zinc-800 p-6 flex justify-center">
        <p className="text-[10px] text-zinc-500 font-mono">
          © 2026 Antigravity IDE • Download Portal secured by Jules
        </p>
      </footer>

      {/* Required basic animations */}
      <style dangerouslySetInnerHTML={{__html: `
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(5px); }
          to { opacity: 1; transform: translateY(0); }
        }
      `}} />
    </div>
  );
}
