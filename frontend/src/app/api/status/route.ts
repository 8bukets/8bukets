import { NextResponse } from 'next/server';
import { supabase } from '@/lib/supabase';
import dbConnect from '@/lib/mongodb';

export async function GET() {
  const results: {
    supabase: { status: string; error: string | null };
    mongodb: { status: string; error: string | null };
    evolution: { version: string; sigma: number };
  } = {
    supabase: { status: 'pending', error: null },
    mongodb: { status: 'pending', error: null },
    evolution: { version: 'N/A', sigma: 0 }
  };

  try {
    // Check Supabase by calling auth.getSession() which doesn't require complex tables
    const { error } = await supabase.auth.getSession();
    if (error) {
      results.supabase = { status: 'error', error: error.message };
    } else {
      results.supabase = { status: 'connected', error: null };
    }
  } catch (err: unknown) {
    const errorMsg = err instanceof Error ? err.message : 'Unknown error';
    results.supabase = { status: 'error', error: errorMsg };
  }

  try {
    // Check MongoDB connection
    const db = await dbConnect();
    results.mongodb = { status: 'connected', error: null };

    // Fetch latest evolution data if possible
    if (db.connection.db) {
      const snapshots = db.connection.db.collection('system_snapshots');
      const latest = await snapshots.find().sort({ timestamp: -1 }).limit(1).toArray();
      if (latest.length > 0) {
        results.evolution = {
          version: latest[0].evolution?.parameter_shifts?.current_version || '1.0',
          sigma: latest[0].sigma_status?.average_impact_score || 0
        };
      }
    }
  } catch (err: unknown) {
    const errorMsg = err instanceof Error ? err.message : 'Unknown error';
    results.mongodb = { status: 'error', error: errorMsg };
  }

  return NextResponse.json(results);
}
