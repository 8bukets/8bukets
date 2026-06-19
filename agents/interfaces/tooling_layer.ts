export interface ToolingLayer {
    executeTerminal(command: string): string;
    manageGit(action: string, args: string[]): boolean;
    manageFileSystem(action: string, path: string): boolean;
}
