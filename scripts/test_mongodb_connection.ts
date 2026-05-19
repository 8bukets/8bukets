import mongoose from 'mongoose';
import * as readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const uriTemplate = 'mongodb+srv://Vercel-Admin-atlas-beige-envelope:<db_password>@atlas-beige-envelope.xdsv2yt.mongodb.net/?appName=atlas-beige-envelope';

rl.question('Please enter your MongoDB database password: ', async (password) => {
  const uri = uriTemplate.replace('<db_password>', encodeURIComponent(password));

  console.log('\nAttempting to connect to MongoDB Atlas...');

  try {
    await mongoose.connect(uri);
    console.log('✅ Connection successful! You are connected to MongoDB Atlas.');

    // Optional: List databases to verify access
    if (mongoose.connection.db) {
        const adminDb = mongoose.connection.db.admin();
        const info = await adminDb.listDatabases();
        console.log('\nAvailable databases:');
        info.databases.forEach((db: any) => console.log(` - ${db.name}`));
    }
  } catch (error) {
    console.error('❌ Connection failed:');
    console.error(error);
  } finally {
    await mongoose.disconnect();
    rl.close();
  }
});
