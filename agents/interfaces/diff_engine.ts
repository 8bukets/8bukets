export interface DiffEngine {
    applyPatch(filePath: string, patch: string): boolean;
    mergeDiff(diffA: string, diffB: string): string;
    preserveFormatting(filePath: string): void;
}
