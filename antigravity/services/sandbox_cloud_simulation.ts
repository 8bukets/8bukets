import { logAutonomousAction } from '../core'
import * as os from 'os';

export class SandboxCloudSimulation {
  public isCloudModeActive(): boolean {
    return process.env.MACBOOK_CLOUD_SIMULATION === 'true' || process.env.AUTONOMOUS_MODE === 'cloud';
  }

  public enforceCloudExecutionState(): void {
    if (this.isCloudModeActive()) {
      logAutonomousAction('☁️ [SandboxCloudSimulation] Cloud Simulation Active: Bypassing local checks and forcing online presence.', 'info');
      process.env.DOCKER_BYPASS = 'true';
      process.env.GITLAB_BYPASS = 'true';
      process.env.GITHUB_BYPASS = 'true';
      process.env.CLOUD_PROVIDER = 'autonomous-cloud';
    } else {
      logAutonomousAction('💻 [SandboxCloudSimulation] Local Mode Active.', 'info');
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
