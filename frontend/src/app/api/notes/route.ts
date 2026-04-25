import { NextResponse } from 'next/server';
import dbConnect from '@/lib/mongodb';
import { Note } from '@/models/Note';

export async function GET(req: Request) {
  try {
    const { searchParams } = new URL(req.url);
    const userId = searchParams.get('userId');

    if (!userId) {
      return NextResponse.json({ error: 'User ID is required' }, { status: 400 });
    }

    await dbConnect();
    const notes = await Note.find({ userId }).sort({ createdAt: -1 });
    return NextResponse.json({ notes });
  } catch (err) {
    console.error('Failed to fetch notes:', err);
    return NextResponse.json({ error: 'Failed to fetch notes' }, { status: 500 });
  }
}

export async function POST(req: Request) {
  try {
    const { content, userId } = await req.json();

    if (!content || !userId) {
      return NextResponse.json({ error: 'Content and User ID are required' }, { status: 400 });
    }

    await dbConnect();
    const newNote = await Note.create({ content, userId });
    return NextResponse.json({ note: newNote }, { status: 201 });
  } catch (err) {
    console.error('Failed to create note:', err);
    return NextResponse.json({ error: 'Failed to create note' }, { status: 500 });
  }
}
