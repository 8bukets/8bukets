import * as os from 'os';

export class SandboxCloudSimulation {
  public isCloudModeActive(): boolean {
    return process.env.MACBOOK_CLOUD_SIMULATION === 'true' || process.env.AUTONOMOUS_MODE === 'cloud';
  }

  public enforceCloudExecutionState(): void {
    if (this.isCloudModeActive()) {
      console.log('☁️ [SandboxCloudSimulation] Cloud Simulation Active: Bypassing local checks and forcing online presence.');
      process.env.DOCKER_BYPASS = 'true';
      process.env.GITLAB_BYPASS = 'true';
      process.env.GITHUB_BYPASS = 'true';
      process.env.CLOUD_PROVIDER = 'autonomous-cloud';
    } else {
      console.log('💻 [SandboxCloudSimulation] Local Mode Active.');
    }
  }

  public generateTelemetry(): Record<string, any> {
    return {
      simulationActive: this.isCloudModeActive(),
      timestamp: new Date().toISOString(),
      platform: os.platform(),
      hostname: os.hostname(),
      simulatedProvider: this.isCloudModeActive() ? 'autonomous-cloud' : 'none',
      bypassedChecks: this.isCloudModeActive() ? ['Docker', 'GitLab', 'GitHub'] : [],
    };
  }
}
