import { MongoClient } from 'mongodb';

async function testMongo() {
  const uri = "mongodb+srv://filkes:Celebrex30!@cluster0.nc9rsuw.mongodb.net/?appName=Cluster0";
  console.log("Testing MongoDB connection to:", uri.split('@')[1]); // Don't log password
  const client = new MongoClient(uri);
  try {
    await client.connect();
    console.log("✅ Successfully connected to MongoDB");
    await client.db().admin().ping();
    console.log("✅ Successfully pinged MongoDB admin");
  } catch (err: any) {
    console.error("❌ MongoDB Connection Error:");
    console.error("Code:", err.code);
    console.error("Message:", err.message);
    if (err.reason) console.error("Reason:", JSON.stringify(err.reason, null, 2));
  } finally {
    await client.close();
  }
}

testMongo();
