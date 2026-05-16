import { NextResponse } from 'next/server';
import { getMongoClient } from '@/lib/mongodb';
import fs from 'fs';
import path from 'path';
import arcjet, { detectPromptInjection, sensitiveInfo } from "@arcjet/next";

export const dynamic = 'force-dynamic';

const aj = arcjet({
  key: process.env.ARCJET_KEY!,
  rules: [
    detectPromptInjection({
      mode: "LIVE",
    }),
    sensitiveInfo({
      mode: "LIVE",
      deny: ["EMAIL", "PHONE_NUMBER"],
    }),
  ],
});

export async function GET(req: Request) {
  try {
    const url = new URL(req.url);
    const queryParameterToCheck = url.searchParams.get("query") || "";

    const decision = await aj.protect(req, {
      detectPromptInjectionMessage: queryParameterToCheck,
      sensitiveInfoValue: queryParameterToCheck,
    } as never);

    if (decision.isDenied()) {
      if (decision.reason.isPromptInjection()) {
        return NextResponse.json({ error: "Prompt injection detected" }, { status: 403 });
      }
      if (decision.reason.isSensitiveInfo()) {
        return NextResponse.json({ error: "Sensitive information detected" }, { status: 400 });
      }
      return NextResponse.json({ error: "Forbidden" }, { status: 403 });
    }

    let latestSnapshot: Record<string, unknown> | null = null;
    let systemState: Record<string, unknown> | null = null;
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    let activeWorkOrders: any[] = [];

    // Phase 12 Optimization: Unified Database Probing with Graceful Degradation
    try {
      const client = await getMongoClient();
      const db = client.db(process.env.MONGODB_DB || 'software_reviews');

      const [snapshot, workOrders, state] = await Promise.all([
        db.collection('system_intelligence').findOne({}, { sort: { timestamp: -1 } }),
        db.collection('work_orders')
          .find({ status: { $in: ['pending', 'executing', 'PENDING', 'IN_PROGRESS'] } })
          .sort({ created_at: -1 })
          .limit(5)
          .toArray(),
        db.collection('system_state').findOne({ systemId: 'antigravity-alpha-01' })
      ]);

      latestSnapshot = snapshot;
      activeWorkOrders = workOrders;
      systemState = state;
    } catch (dbErr) {
      console.warn('⚠️ [Intelligence API] MongoDB layer unavailable. Falling back to local data.', dbErr);
    }

    // Read latest cognitive logs (fallback to file if needed, but preferably from DB in future)
    const logPath = path.join(/* turbopackIgnore: true */ process.cwd(), '../logs/autonomous.log');
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    let recentLogs: any[] = [];
    if (fs.existsSync(logPath)) {
      try {
        const logContent = fs.readFileSync(logPath, 'utf8');
        recentLogs = logContent.split('\n')
          .filter(l => l.trim())
          .slice(-15)
          .map(l => {
            try { return JSON.parse(l); } catch { return { msg: l, time: new Date().toISOString(), type: 'raw' }; }
          })
          .reverse();
      } catch {
        console.error('Failed to read logs');
      }
    }

    // Market Intelligence: Multi-path probing for environment resilience
    const possiblePaths = [
      path.join(/* turbopackIgnore: true */ process.cwd(), '../links.json'),
      path.join(process.cwd(), 'links.json'),
      '/app/links.json'
    ];

    let marketLinks = [];
    for (const p of possiblePaths) {
      if (fs.existsSync(p)) {
        try {
          marketLinks = JSON.parse(fs.readFileSync(p, 'utf8')).slice(0, 5);
          break;
        } catch {
          console.error(`Failed to read market data from ${p}:`);
        }
      }
    }

    return NextResponse.json({
      snapshot: latestSnapshot,
      state: systemState,
      workOrders: activeWorkOrders,
      logs: recentLogs,
      marketLinks,
      timestamp: new Date().toISOString()
    });
  } catch (err: unknown) {
    console.error('❌ [Intelligence API] Critical failure:', err);
    return NextResponse.json({ error: (err as Error).message }, { status: 500 });
  }
}
