export interface ContextEngineering {
    loadRelevantFiles(query: string): string[];
    summarizeContent(content: string): string;
    packageRepository(): string;
}
