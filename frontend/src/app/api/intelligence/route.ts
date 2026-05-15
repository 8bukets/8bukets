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
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } as any);

    if (decision.isDenied()) {
      if (decision.reason.isPromptInjection()) {
        return NextResponse.json({ error: "Prompt injection detected" }, { status: 403 });
      }
      if (decision.reason.isSensitiveInfo()) {
        return NextResponse.json({ error: "Sensitive information detected" }, { status: 400 });
      }
      return NextResponse.json({ error: "Forbidden" }, { status: 403 });
    }

    const client = await getMongoClient();
    const db = client.db(process.env.MONGODB_DB || 'software_reviews');

    // Fetch latest intelligence snapshot
    const latestSnapshot = await db.collection('system_intelligence')
      .findOne({}, { sort: { timestamp: -1 } });

    // Fetch active work orders (mocked for now, integrate with Jules agent layer)
    const workOrdersPath = path.join(process.cwd(), '../data/work_orders.json');
    let activeWorkOrders = [];
    if (fs.existsSync(workOrdersPath)) {
      const allOrders = JSON.parse(fs.readFileSync(workOrdersPath, 'utf8'));
      activeWorkOrders = allOrders.filter((o: { status: string; type: string; id: string; goal: string }) => o.status === 'pending' || o.status === 'executing').slice(0, 5);
    }

    // Read latest cognitive logs
    const logPath = path.join(process.cwd(), '../logs/autonomous.log');
    let recentLogs = [];
    if (fs.existsSync(logPath)) {
      const logContent = fs.readFileSync(logPath, 'utf8');
      recentLogs = logContent.split('\n').filter(l => l).slice(-15).map(l => JSON.parse(l)).reverse();
    }

    return NextResponse.json({
      snapshot: latestSnapshot,
      workOrders: activeWorkOrders,
      logs: recentLogs,
      timestamp: new Date().toISOString()
    });
  } catch (err) {
    const error = err as Error;
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}