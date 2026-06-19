export interface AutonomyEngine {
    analyzeState(state: any): any;
    executeChange(change: any): boolean;
    validateExecution(): boolean;
    retryOperation(operation: () => boolean, maxAttempts: number): boolean;
}
