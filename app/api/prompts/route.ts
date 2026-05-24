import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

export async function GET() {
  try {
    const jsonPath = path.join(process.cwd(), '50ty.json');
    const fileContents = fs.readFileSync(jsonPath, 'utf8');
    return new NextResponse(fileContents, {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (_e: unknown) {
    return NextResponse.json({ error: 'Failed to read prompts JSON' }, { status: 500 });
  }
}
