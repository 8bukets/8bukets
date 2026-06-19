export interface UXLayer {
    formatOutput(data: any): string;
    explainAction(action: string, reason: string): void;
    renderTerminalUI(): void;
}
