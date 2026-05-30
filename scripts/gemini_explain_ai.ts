import * as dotenv from 'dotenv';
import path from 'path';

// Load environment variables from .env file if it exists
try {
  dotenv.config({ path: path.resolve(process.cwd(), '.env') });
} catch (e) {
  // dotenv might not be installed, ignore and rely on process.env
}

async function main() {
  const apiKey = process.env.GEMINI_API_KEY;

  if (!apiKey) {
    console.error('Error: GEMINI_API_KEY environment variable is not set.');
    console.error('Please set it using: export GEMINI_API_KEY="your_api_key" or add it to your .env file.');
    process.exit(1);
  }

  const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent`;

  const payload = {
    contents: [
      {
        parts: [
          {
            text: "Explain how AI works in a few words"
          }
        ]
      }
    ]
  };

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'x-goog-api-key': apiKey,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error(`API Error (${response.status} ${response.statusText}):\n${errorText}`);
      process.exit(1);
    }

    const data = await response.json();

    // Attempt to parse the text response
    const text = data?.candidates?.[0]?.content?.parts?.[0]?.text;
    if (text) {
      console.log('AI Response:\n' + text);
    } else {
      console.log('Response successfully received but format was unexpected:');
      console.log(JSON.stringify(data, null, 2));
    }

  } catch (error) {
    console.error('Failed to make request:', error);
    process.exit(1);
  }
}

main();
