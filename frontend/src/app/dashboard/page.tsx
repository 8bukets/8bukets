'use client';

import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';
import { useRouter } from 'next/navigation';
import { User } from '@supabase/supabase-js';

type Note = {
  _id: string;
  content: string;
  createdAt: string;
};

export default function Dashboard() {
  const [user, setUser] = useState<User | null>(null);
  const [notes, setNotes] = useState<Note[]>([]);
  const [newNote, setNewNote] = useState('');
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    const fetchNotes = async (userId: string) => {
      try {
        const res = await fetch(`/api/notes?userId=${userId}`);
        if (res.ok) {
          const data = await res.json();
          setNotes(data.notes);
        }
      } catch (error) {
        console.error('Failed to fetch notes:', error);
      } finally {
        setLoading(false);
      }
    };

    const checkUser = async () => {
      const { data: { session } } = await supabase.auth.getSession();
      if (!session) {
        router.push('/login');
      } else {
        setUser(session.user);
        fetchNotes(session.user.id);
      }
    };

    checkUser();
  }, [router]);

  const handleAddNote = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newNote.trim() || !user) return;

    try {
      const res = await fetch('/api/notes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ content: newNote, userId: user.id }),
      });

      if (res.ok) {
        const data = await res.json();
        setNotes([data.note, ...notes]);
        setNewNote('');
      }
    } catch (error) {
      console.error('Failed to add note:', error);
    }
  };

  const handleSignOut = async () => {
    await supabase.auth.signOut();
    router.push('/login');
  };

  if (loading || !user) {
    return <div className="min-h-screen flex items-center justify-center bg-zinc-50 dark:bg-zinc-950">Loading...</div>;
  }

  return (
    <div className="min-h-screen bg-zinc-50 dark:bg-zinc-950 p-8">
      <div className="max-w-4xl mx-auto space-y-8">
        <header className="flex justify-between items-center bg-white dark:bg-zinc-900 p-6 rounded-xl shadow-sm border border-zinc-200 dark:border-zinc-800">
          <div>
            <h1 className="text-2xl font-bold text-zinc-900 dark:text-zinc-50">Dashboard</h1>
            <p className="text-zinc-500 dark:text-zinc-400 text-sm">Welcome, {user.email}</p>
          </div>
          <button
            onClick={handleSignOut}
            className="px-4 py-2 bg-zinc-100 dark:bg-zinc-800 text-zinc-900 dark:text-zinc-50 rounded-md hover:bg-zinc-200 dark:hover:bg-zinc-700 transition-colors text-sm font-medium"
          >
            Sign Out
          </button>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="md:col-span-1 space-y-4">
            <div className="bg-white dark:bg-zinc-900 p-6 rounded-xl shadow-sm border border-zinc-200 dark:border-zinc-800">
              <h2 className="text-lg font-semibold mb-4 text-zinc-900 dark:text-zinc-50">Add a New Note</h2>
              <form onSubmit={handleAddNote} className="space-y-4">
                <textarea
                  value={newNote}
                  onChange={(e) => setNewNote(e.target.value)}
                  className="w-full h-32 p-3 rounded-md border border-zinc-300 dark:border-zinc-700 bg-transparent text-zinc-900 dark:text-zinc-50 placeholder:text-zinc-400 focus:ring-2 focus:ring-blue-500 outline-none resize-none"
                  placeholder="Type something unstructured here..."
                  required
                />
                <button
                  type="submit"
                  className="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-500 transition-colors font-medium text-sm"
                >
                  Save Note to MongoDB
                </button>
              </form>
            </div>
          </div>

          <div className="md:col-span-2">
            <div className="bg-white dark:bg-zinc-900 p-6 rounded-xl shadow-sm border border-zinc-200 dark:border-zinc-800 min-h-[400px]">
              <h2 className="text-lg font-semibold mb-4 text-zinc-900 dark:text-zinc-50">Your Notes</h2>
              {notes.length === 0 ? (
                <div className="text-center text-zinc-500 dark:text-zinc-400 py-12">
                  No notes found. Create your first one!
                </div>
              ) : (
                <ul className="space-y-4">
                  {notes.map((note) => (
                    <li key={note._id} className="p-4 rounded-lg bg-zinc-50 dark:bg-zinc-800 border border-zinc-100 dark:border-zinc-700">
                      <p className="text-zinc-800 dark:text-zinc-200 whitespace-pre-wrap">{note.content}</p>
                      <span className="text-xs text-zinc-400 block mt-2">
                        {new Date(note.createdAt).toLocaleString()}
                      </span>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
