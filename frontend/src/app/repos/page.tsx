'use client';

import { useEffect, useState } from 'react';
import { Github, Star, GitFork, AlertCircle, Clock, ExternalLink } from 'lucide-react';

interface RepoData {
  name: string;
  full_name?: string;
  description?: string;
  html_url?: string;
  stargazers_count?: number;
  open_issues_count?: number;
  forks_count?: number;
  updated_at?: string;
  language?: string;
  error?: string;
}

export default function ReposDashboard() {
  const [repos, setRepos] = useState<RepoData[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchRepos = async () => {
      try {
        const res = await fetch('/api/github');
        if (!res.ok) throw new Error('Failed to fetch data');
        const data = await res.json();
        if (data.error) throw new Error(data.error);

        setRepos(data.repositories || []);
      } catch (err: any) {
        setError(err.message || 'An error occurred');
      } finally {
        setLoading(false);
      }
    };

    fetchRepos();
  }, []);

  const formatDate = (dateString?: string) => {
    if (!dateString) return 'Unknown';
    const date = new Date(dateString);
    return new Intl.DateTimeFormat('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric'
    }).format(date);
  };

  return (
    <div className="min-h-screen bg-zinc-50 dark:bg-zinc-950 text-zinc-900 dark:text-zinc-100 p-8">
      <div className="max-w-7xl mx-auto flex flex-col gap-8">

        <header className="flex flex-col gap-2">
          <div className="flex items-center gap-3">
            <Github className="w-8 h-8" />
            <h1 className="text-3xl font-bold">Collaboration Dashboard</h1>
          </div>
          <p className="text-zinc-500 dark:text-zinc-400">
            Monitoring across the 8bukets ecosystem.
          </p>
        </header>

        {loading && (
          <div className="flex items-center justify-center p-12">
            <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-zinc-900 dark:border-white"></div>
          </div>
        )}

        {error && (
          <div className="bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 p-4 rounded-lg border border-red-200 dark:border-red-800">
            {error}
          </div>
        )}

        {!loading && !error && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {repos.map((repo) => (
              <div
                key={repo.name}
                className="bg-white dark:bg-zinc-900 rounded-xl shadow-sm border border-zinc-200 dark:border-zinc-800 p-6 flex flex-col h-full hover:shadow-md transition-shadow"
              >
                <div className="flex justify-between items-start mb-4">
                  <h2 className="text-xl font-semibold break-all">
                    {repo.html_url ? (
                      <a href={repo.html_url} target="_blank" rel="noopener noreferrer" className="hover:text-blue-600 dark:hover:text-blue-400 flex items-center gap-2">
                        {repo.name}
                        <ExternalLink className="w-4 h-4" />
                      </a>
                    ) : (
                      repo.name
                    )}
                  </h2>
                </div>

                {repo.error ? (
                  <div className="text-red-500 flex items-center gap-2 mt-auto">
                    <AlertCircle className="w-4 h-4" />
                    <span className="text-sm">{repo.error}</span>
                  </div>
                ) : (
                  <>
                    <p className="text-zinc-600 dark:text-zinc-400 text-sm mb-6 flex-grow line-clamp-3">
                      {repo.description || 'No description provided.'}
                    </p>

                    <div className="flex flex-col gap-4 mt-auto pt-4 border-t border-zinc-100 dark:border-zinc-800">
                      <div className="flex flex-wrap items-center gap-4 text-sm text-zinc-600 dark:text-zinc-400">
                        {repo.language && (
                          <div className="flex items-center gap-1.5">
                            <span className="w-2.5 h-2.5 rounded-full bg-blue-500"></span>
                            <span>{repo.language}</span>
                          </div>
                        )}
                        <div className="flex items-center gap-1.5" title="Stars">
                          <Star className="w-4 h-4" />
                          <span>{repo.stargazers_count || 0}</span>
                        </div>
                        <div className="flex items-center gap-1.5" title="Forks">
                          <GitFork className="w-4 h-4" />
                          <span>{repo.forks_count || 0}</span>
                        </div>
                        <div className="flex items-center gap-1.5" title="Open Issues">
                          <AlertCircle className="w-4 h-4" />
                          <span>{repo.open_issues_count || 0}</span>
                        </div>
                      </div>

                      <div className="flex items-center gap-1.5 text-xs text-zinc-500">
                        <Clock className="w-3.5 h-3.5" />
                        <span>Updated {formatDate(repo.updated_at)}</span>
                      </div>
                    </div>
                  </>
                )}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
