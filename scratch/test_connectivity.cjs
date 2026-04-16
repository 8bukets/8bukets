const { MongoClient } = require('mongodb');
const { createClient } = require('@supabase/supabase-js');

async function test() {
  const MONGODB_URI = "mongodb+srv://filkes:Celebrex30!@cluster0.nc9rsuw.mongodb.net/?appName=Cluster0";
  const SUPABASE_URL = "https://tevdxaufsnpsbvvurddg.supabase.co";
  const SUPABASE_KEY = "sb_publishable_OxM7iE43GT9Iyk66JEFrfg_zsZm57QY";

  console.log("--- 1. Testing MongoDB ---");
  try {
    const client = new MongoClient(MONGODB_URI);
    await client.connect();
    await client.db("admin").command({ ping: 1 });
    console.log("✅ MongoDB Connected Successfully");
    await client.close();
  } catch (err) {
    console.error("❌ MongoDB Connection Failed:", err.message);
  }

  console.log("\n--- 2. Testing Supabase ---");
  try {
    const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);
    const { data, error } = await supabase.from('_health').select('id').limit(1);
    if (error && error.code !== 'PGRST116') {
        throw error;
    }
    console.log("✅ Supabase Connectivity Verified");
  } catch (err) {
    console.error("❌ Supabase Connection Failed:", err.message);
  }
}

test();
