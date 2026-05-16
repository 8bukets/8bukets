import { NextResponse } from 'next/server';
import { getMongoClient } from '@/lib/mongodb';
import fs from 'fs';
import path from 'path';

export const dynamic = 'force-dynamic';
import arcjet, { detectPromptInjection, sensitiveInfo } from "@arcjet/next";

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
    let activeWorkOrders: Record<string, unknown>[] = [];
    let systemState: Record<string, unknown> | null = null;
    let latestSnapshot = null;
    let activeWorkOrders: any[] = [];
    let activeWorkOrders: unknown[] = [];
    let systemState = null;

    try {
      const client = await getMongoClient();
      const db = client.db(process.env.MONGODB_DB || 'software_reviews');

      // Fetch latest intelligence snapshot
      latestSnapshot = await db.collection('system_intelligence')
        .findOne({}, { sort: { timestamp: -1 } });

      // Fetch active work orders from MongoDB
      activeWorkOrders = await db.collection('work_orders')
        .find({ status: { $in: ['pending', 'executing', 'PENDING', 'IN_PROGRESS'] } })
        .sort({ created_at: -1 })
        .limit(5)
        .toArray();

      // Fetch latest system state
      systemState = await db.collection('system_state')
        .findOne({ systemId: 'antigravity-alpha-01' });
    } catch (dbErr) {
      console.warn('MongoDB connection failed, providing limited response', dbErr);
    }

    // Read latest cognitive logs (fallback to file if needed, but preferably from DB in future)
    const logPath = path.join(process.cwd(), '../logs/autonomous.log');
    let recentLogs = [];
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

    // Read local links.json for real-time market data
    // Use multiple path strategies for cross-environment robustness (Cloud vs Local)
    const possiblePaths = [
      path.join(process.cwd(), '../links.json'),
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
    return NextResponse.json({ error: (err as Error).message }, { status: 500 });
  }
}