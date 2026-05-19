import fs from 'fs';
import path from 'path';

// Define types based on our ingested JSON structure
interface Section {
  heading: string;
  content: string[];
}

interface RenderDocsData {
  title: string;
  url: string;
  sections: Section[];
}

export default async function RenderDocsPage() {
  // Read the ingested JSON data
  const jsonPath = path.join(process.cwd(), '..', 'render_docs.json');
  let data: RenderDocsData | null = null;

  try {
    const fileContents = fs.readFileSync(jsonPath, 'utf8');
    data = JSON.parse(fileContents);
  } catch (error) {
    console.error('Failed to read render_docs.json:', error);
  }

  if (!data) {
    return (
      <div className="min-h-screen p-8 sm:p-20 font-[family-name:var(--font-geist-sans)]">
        <h1 className="text-4xl font-bold tracking-tight mb-4 text-red-500">Error Loading Documentation</h1>
        <p>Could not load Render documentation data. Please run the ingestion script.</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen p-8 sm:p-20 font-[family-name:var(--font-geist-sans)] bg-white dark:bg-zinc-950 text-zinc-900 dark:text-zinc-100">
      <main className="max-w-4xl mx-auto flex flex-col gap-8">

        {/* Header Header */}
        <div className="border-b border-zinc-200 dark:border-zinc-800 pb-8">
          <h1 className="text-5xl font-bold tracking-tight mb-4 bg-clip-text text-transparent bg-gradient-to-r from-purple-500 to-indigo-600">
            {data.title}
          </h1>
          <p className="text-xl text-zinc-500 dark:text-zinc-400">
            Learn how to deploy and scale apps on the Render platform.
          </p>
          <a href={data.url} target="_blank" rel="noreferrer" className="text-sm text-indigo-500 hover:underline mt-4 inline-block">
            View Official Docs
          </a>
        </div>

        {/* Dynamic Sections */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mt-4">
          {data.sections.map((section, idx) => (
            <div key={idx} className="bg-zinc-50 dark:bg-zinc-900 p-6 rounded-2xl border border-zinc-200 dark:border-zinc-800 shadow-sm">
              <h2 className="text-2xl font-semibold mb-4 text-zinc-800 dark:text-zinc-200 border-b border-zinc-200 dark:border-zinc-800 pb-2">
                {section.heading}
              </h2>
              <ul className="space-y-3">
                {section.content.map((item, itemIdx) => (
                  <li key={itemIdx} className="flex items-start gap-2">
                    <span className="text-indigo-500 mt-1">✓</span>
                    <span className="text-sm text-zinc-600 dark:text-zinc-400">{item}</span>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

      </main>
    </div>
  );
}
