import { NextResponse } from 'next/server';
import { getMongoClient } from '@/lib/mongodb';
import fs from 'fs';
import path from 'path';

export const dynamic = 'force-dynamic';

export async function GET() {
  try {
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
  } catch (err: unknown) {
    return NextResponse.json({ error: (err as Error).message }, { status: 500 });
  }
}
