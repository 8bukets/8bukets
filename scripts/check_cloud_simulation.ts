import { getDockerFleetStatus, checkDockerHealth } from '../antigravity/services/docker';
import { reactService } from '../antigravity/services/react';
import { cloudWorkflowAgent } from '../antigravity/services/cloud_workflow';

async function main() {
  console.log('--- Verifying MACBOOK_CLOUD_SIMULATION Effect ---');

  console.log('\n[1] Docker Fleet Status:');
  const fleet = await getDockerFleetStatus();
  console.log(fleet);

  console.log('\n[2] Docker Health:');
  const health = await checkDockerHealth();
  console.log(health);

  console.log('\n[3] Cloud Workflow Agent Telemetry:');
  const telemetry = await cloudWorkflowAgent.evaluateTelemetry();
  console.log('Docker fullyOnline:', telemetry.docker?.fullyOnline);
  console.log('GitLab fullyOnline:', telemetry.gitlab?.fullyOnline);

  console.log('\n[4] ReAct Service (Simulation mode exit check):');
  const steps = await reactService.executeCycle('Test Simulation', {
    testTool: () => 'Testing'
  });
  console.log('Steps length:', steps.length);
  if (steps.length > 1) {
    console.log('Last Action:', steps[1].action);
  }

  console.log('\n✅ Verification Complete.');
}

main().catch(console.error);
