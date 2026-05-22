import { getDockerFleetStatus, checkDockerHealth } from './antigravity/services/docker'

async function run() {
  console.log('Testing Docker service...');
  const fleet = await getDockerFleetStatus();
  console.log('Fleet:', fleet);
  const health = await checkDockerHealth();
  console.log('Health:', health);
}

run();
