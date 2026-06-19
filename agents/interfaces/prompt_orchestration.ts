export interface PromptOrchestration {
    generateSystemPrompt(role: string): string;
    decomposeTask(task: string): string[];
    performSelfCheck(output: string): boolean;
}
