export interface SafetySystem {
    isExecutionAllowed(command: string): boolean;
    requiresUserApproval(action: any): boolean;
    isPathReadOnly(path: string): boolean;
}
