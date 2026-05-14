import { NextResponse } from 'next/server';
import { getMongoClient } from '@/lib/mongodb';
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
    const db = client.db('markposition_db');

    // 1. Fetch latest system snapshot
    const snapshot = await db.collection('system_snapshots')
      .find({})
      .sort({ timestamp: -1 })
      .limit(1)
      .toArray();

    // 2. Fetch active work orders
    const workOrders = await db.collection('work_orders')
      .find({ status: { $in: ['pending', 'executing', 'IN_PROGRESS'] } })
      .sort({ created_at: -1 })
      .toArray();

    // 3. Fetch recent cognitive logs (from snapshot if available, or just mock for now)
    const recentLogs = snapshot[0]?.logs || [];

    return NextResponse.json({
      snapshot: snapshot[0] || null,
      workOrders,
      logs: recentLogs,
      timestamp: new Date().toISOString()
    });
  } catch (err: unknown) {
    return NextResponse.json({ error: (err as Error).message }, { status: 500 });
  } catch (err) {
    const error = err as Error;
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}