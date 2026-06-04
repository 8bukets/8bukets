import { NextResponse } from 'next/server';

const REPOSITORIES = [
  '8bukets',
  'web-app',
  'sor8bukets',
  'eight-bukets',
  'finance-app',
  'MapAntigravity',
  'arcjet-example-nextjs'
];

const ORG_NAME = '8bukets';

export async function GET() {
  try {
    const headers: HeadersInit = {
      'Accept': 'application/vnd.github.v3+json',
    };

    if (process.env.GITHUB_TOKEN) {
      headers['Authorization'] = `token ${process.env.GITHUB_TOKEN}`;
    }

    const fetchRepoData = async (repo: string) => {
      try {
        // Fetch basic repo info
        const repoRes = await fetch(`https://api.github.com/repos/${ORG_NAME}/${repo}`, {
          headers,
          next: { revalidate: 60 } // cache for 60 seconds
        });

        if (!repoRes.ok) {
          if (repoRes.status === 404) return { name: repo, error: 'Not Found' };
          throw new Error(`GitHub API error: ${repoRes.status}`);
        }

        const data = await repoRes.json();

        return {
          name: data.name,
          full_name: data.full_name,
          description: data.description,
          html_url: data.html_url,
          stargazers_count: data.stargazers_count,
          open_issues_count: data.open_issues_count,
          forks_count: data.forks_count,
          updated_at: data.updated_at,
          language: data.language
        };
      } catch (err) {
        console.error(`Error fetching ${repo}:`, err);
        return { name: repo, error: 'Failed to load' };
      }
    };

    const results = await Promise.all(REPOSITORIES.map(fetchRepoData));

    return NextResponse.json({ repositories: results });
  } catch (error) {
    console.error('GitHub API route error:', error);
    return NextResponse.json({ error: 'Failed to fetch GitHub data' }, { status: 500 });
  }
}
