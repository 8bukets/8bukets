import { NextResponse } from 'next/server';
import { supabase } from '@/lib/supabase';
import dbConnect from '@/lib/mongodb';

export async function GET() {
  const results: {
    supabase: { status: string; error: string | null };
    mongodb: { status: string; error: string | null };
  } = {
    supabase: { status: 'pending', error: null },
    mongodb: { status: 'pending', error: null }
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
    await dbConnect();
    results.mongodb = { status: 'connected', error: null };
  } catch (err: unknown) {
    const errorMsg = err instanceof Error ? err.message : 'Unknown error';
    results.mongodb = { status: 'error', error: errorMsg };
  }

  return NextResponse.json(results);
}
