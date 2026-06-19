export interface RetrievalEngine {
    semanticSearch(query: string): string[];
    buildDependencyGraph(entryFile: string): any;
    rankFileRelevance(files: string[]): string[];
}
