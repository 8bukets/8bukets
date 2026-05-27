import fs from 'fs';
import path from 'path';

export interface SystemInsights {
  docker: {
    hasDockerfile: boolean;
    hasCompose: boolean;
    status: string;
  };
  collaboration: {
    status: string;
    lastSync: string | null;
  };
  timestamp: string;
}

export function getSystemInsights(): SystemInsights {
  const hasDockerfile = fs.existsSync(path.join(process.cwd(), 'Dockerfile'));
  const hasCompose = fs.existsSync(path.join(process.cwd(), 'docker-compose.yml'));

  let collabStatus = 'PENDING';
  let lastSync = null;

  const statePath = path.join(process.cwd(), 'autonomous_state.json');
  if (fs.existsSync(statePath)) {
    const state = JSON.parse(fs.readFileSync(statePath, 'utf8'));
    collabStatus = state.status || 'UNKNOWN';
    lastSync = state.last_sync || null;
  }

  return {
    docker: {
      hasDockerfile,
      hasCompose,
      status: (hasDockerfile && hasCompose) ? 'VERIFIED' : 'INCOMPLETE'
    },
    collaboration: {
      status: collabStatus,
      lastSync
    },
    timestamp: new Date().toISOString()
  };
}
