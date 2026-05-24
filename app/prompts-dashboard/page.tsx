"use client";

import React, { useState, useEffect } from 'react';

// Adjusting the interfaces slightly since we'll fetch from the raw json
interface Prompt {
  number: number;
  category: string;
  title: string;
  description: string;
  variables: string[];
  prompt: string;
}

export default function PromptsDashboard() {
  const [prompts, setPrompts] = useState<Prompt[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectedCategory, setSelectedCategory] = useState<string>('All');
  const [search, setSearch] = useState('');

  useEffect(() => {
    // In a real Next.js app we'd fetch this from an API route or import directly.
    // We'll simulate loading it via an API endpoint that we assume serves the JSON
    // Or we could just import it if it's inside the src directory.
    // Since it's in the root directory, let's create a quick API route or fetch a static file.
    fetch('/api/prompts')
      .then(res => res.json())
      .then(data => {
        setPrompts(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Failed to load prompts", err);
        setLoading(false);
      });
  }, []);

  const categories = ['All', ...Array.from(new Set(prompts.map(p => p.category)))];

  const filteredPrompts = prompts.filter(p => {
    const matchesCategory = selectedCategory === 'All' || p.category === selectedCategory;
    const matchesSearch = p.title.toLowerCase().includes(search.toLowerCase()) ||
                          p.prompt.toLowerCase().includes(search.toLowerCase());
    return matchesCategory && matchesSearch;
  });

  if (loading) {
    return <div className="p-10 text-center text-xl font-bold">Loading Dashboard...</div>;
  }

  // Analytics for the visualization
  const totalPrompts = prompts.length;
  const totalVariables = prompts.reduce((acc, p) => acc + (p.variables?.length || 0), 0);
  const categoryCounts = categories.filter(c => c !== 'All').map(c => ({
    name: c,
    count: prompts.filter(p => p.category === c).length
  }));

  return (
    <div className="min-h-screen bg-gray-50 text-gray-900 p-8">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-4xl font-extrabold mb-2 text-indigo-700">Prompt Intelligence Dashboard</h1>
        <p className="text-gray-600 mb-8">Visualize and navigate the 50-prompt architectural framework.</p>

        {/* Top Analytics Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
          <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex flex-col items-center justify-center">
            <span className="text-5xl font-black text-indigo-600">{totalPrompts}</span>
            <span className="text-sm text-gray-500 font-semibold uppercase tracking-wider mt-2">Total Prompts</span>
          </div>
          <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex flex-col items-center justify-center">
            <span className="text-5xl font-black text-emerald-600">{categories.length - 1}</span>
            <span className="text-sm text-gray-500 font-semibold uppercase tracking-wider mt-2">Categories</span>
          </div>
          <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex flex-col items-center justify-center">
            <span className="text-5xl font-black text-amber-500">{totalVariables}</span>
            <span className="text-sm text-gray-500 font-semibold uppercase tracking-wider mt-2">Dynamic Variables</span>
          </div>
        </div>

        {/* Category Visualization Bar */}
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 mb-10">
          <h2 className="text-lg font-bold mb-4 text-gray-800">Prompt Distribution</h2>
          <div className="flex h-8 w-full rounded-full overflow-hidden bg-gray-100">
            {categoryCounts.map((cat, i) => (
              <div
                key={cat.name}
                className={`h-full cursor-pointer transition-all hover:opacity-80`}
                style={{
                  width: `${(cat.count / totalPrompts) * 100}%`,
                  backgroundColor: ['#4f46e5', '#0ea5e9', '#10b981', '#f59e0b', '#ec4899'][i % 5]
                }}
                title={`${cat.name}: ${cat.count} prompts`}
                onClick={() => setSelectedCategory(cat.name)}
              />
            ))}
          </div>
          <div className="flex flex-wrap gap-4 mt-4 text-sm text-gray-600">
             {categoryCounts.map((cat, i) => (
               <div key={cat.name} className="flex items-center">
                 <div className="w-3 h-3 rounded-full mr-2" style={{ backgroundColor: ['#4f46e5', '#0ea5e9', '#10b981', '#f59e0b', '#ec4899'][i % 5] }} />
                 {cat.name.split(':')[0]} ({cat.count})
               </div>
             ))}
          </div>
        </div>

        {/* Controls */}
        <div className="flex flex-col md:flex-row justify-between mb-6 gap-4">
          <div className="flex overflow-x-auto pb-2 gap-2 hide-scrollbar">
            {categories.map(c => (
              <button
                key={c}
                onClick={() => setSelectedCategory(c)}
                className={`px-4 py-2 rounded-full whitespace-nowrap text-sm font-medium transition-colors ${selectedCategory === c ? 'bg-indigo-600 text-white shadow-md' : 'bg-white text-gray-600 border border-gray-200 hover:bg-gray-50'}`}
              >
                {c.split(':')[0]}
              </button>
            ))}
          </div>
          <input
            type="text"
            placeholder="Search prompts..."
            className="px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 w-full md:w-64"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
        </div>

        {/* Prompts Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
          {filteredPrompts.map(prompt => (
            <div key={prompt.number} className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow flex flex-col h-full">
              <div className="p-5 border-b border-gray-100 bg-gray-50">
                <div className="flex justify-between items-start mb-2">
                  <span className="inline-block px-2 py-1 bg-indigo-100 text-indigo-800 text-xs font-bold rounded">
                    #{prompt.number}
                  </span>
                  <span className="text-xs font-medium text-gray-500 truncate max-w-[200px]" title={prompt.category}>
                    {prompt.category.split(':')[0]}
                  </span>
                </div>
                <h3 className="font-bold text-lg text-gray-900 leading-tight">{prompt.title}</h3>
              </div>
              <div className="p-5 flex-grow flex flex-col">
                <p className="text-gray-600 text-sm mb-4 line-clamp-2">{prompt.description}</p>
                <div className="mt-auto">
                  <h4 className="text-xs font-bold text-gray-400 uppercase tracking-wider mb-2">Variables ({prompt.variables?.length || 0})</h4>
                  <div className="flex flex-wrap gap-1">
                    {prompt.variables?.slice(0, 3).map(v => (
                      <span key={v} className="px-2 py-1 bg-gray-100 text-gray-600 rounded text-xs truncate max-w-[120px]" title={v}>
                        {v}
                      </span>
                    ))}
                    {(prompt.variables?.length || 0) > 3 && (
                      <span className="px-2 py-1 bg-gray-100 text-gray-500 rounded text-xs">
                        +{(prompt.variables?.length || 0) - 3} more
                      </span>
                    )}
                  </div>
                </div>
              </div>
            </div>
          ))}
          {filteredPrompts.length === 0 && (
            <div className="col-span-full py-12 text-center text-gray-500">
              No prompts found matching your criteria.
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
