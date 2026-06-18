export interface AgentHarness {
    executeCommand(command: string): Promise<string>;
    manageMemory(state: any): void;
    provideContext(): any;
    controlLoop(): void;
    sandboxExecution(): boolean;
}
