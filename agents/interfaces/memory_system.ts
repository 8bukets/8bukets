export interface MemorySystem {
    storeSessionMemory(key: string, value: any): void;
    retrieveSessionMemory(key: string): any;
    storeTaskMemory(taskId: string, memory: any): void;
}
