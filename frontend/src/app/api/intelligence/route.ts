import { NextResponse } from 'next/server';
import dbConnect from '@/lib/mongodb';

export async function GET() {
  try {
    const mongooseClient = await dbConnect();
    const db = mongooseClient.connection.db;

    if (!db) {
        throw new Error("Database not connected");
    }

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
  }
}
