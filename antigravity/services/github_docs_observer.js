import { logAutonomousAction } from '../core';
import { z } from 'zod';
import { autonomousFetch } from '@/antigravity/core';
export const GithubDocSectionSchema = z.object({
    title: z.string(),
    content: z.string()
});
export const GithubDocsSchema = z.object({
    repo: z.string(),
    file: z.string(),
    sections: z.array(GithubDocSectionSchema),
    rawUrl: z.string(),
    lastUpdated: z.string()
});
/**
 * GITHUB DOCS OBSERVER
 * Autonomously extracts technical sections from raw GitHub markdown files.
 */
export class GithubDocsObserver {
    constructor() {
        this.baseUrl = 'https://raw.githubusercontent.com';
    }
    /**
     * fetchDoc: Retrieves and parses a markdown file from GitHub.
     */
    async fetchDoc(owner, repo, path, branch = 'master') {
        const rawUrl = `${this.baseUrl}/${owner}/${repo}/${branch}/${path}`;
        return autonomousFetch(GithubDocsSchema, async () => {
            logAutonomousAction(`📡 [GithubDocsObserver] Fetching: ${owner}/${repo}/${path}...`, 'info');
            const response = await fetch(rawUrl);
            if (!response.ok) {
                throw new Error(`Failed to fetch doc from GitHub: ${response.statusText}`);
            }
            const markdown = await response.text();
            const sections = this.parseMarkdown(markdown);
            return {
                repo: `${owner}/${repo}`,
                file: path,
                sections,
                rawUrl,
                lastUpdated: new Date().toISOString()
            };
        }, { life: 'catalog', tags: [`github-docs-${repo}-${path.replace(/\//g, '-')}`] });
    }
    /**
     * parseMarkdown: Extracts sections based on markdown headers.
     * Improved to handle empty sections and nested headers.
     */
    parseMarkdown(markdown) {
        const sections = [];
        const lines = markdown.split('\n');
        let currentTitle = 'Overview';
        let currentContent = [];
        for (const line of lines) {
            const headerMatch = line.match(/^#+\s+(.*)$/);
            if (headerMatch) {
                // Save previous section if it has content or isn't the default Overview
                if (currentContent.length > 0 || currentTitle !== 'Overview') {
                    sections.push({
                        title: currentTitle,
                        content: currentContent.join('\n').trim()
                    });
                }
                currentTitle = headerMatch[1];
                currentContent = [];
            }
            else {
                currentContent.push(line);
            }
        }
        // Push final section
        sections.push({
            title: currentTitle,
            content: currentContent.join('\n').trim()
        });
        return sections.filter(s => s.title !== 'Overview' || s.content !== '');
    }
}
export const githubDocsObserver = new GithubDocsObserver();
