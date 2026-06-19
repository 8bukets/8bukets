export interface VerificationLayer {
    checkBuild(): boolean;
    runTests(): boolean;
    checkLint(): boolean;
}
