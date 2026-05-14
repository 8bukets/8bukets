import { z } from 'zod';
import fetch from 'node-fetch';

/**
 * ANTIGRAVITY JENKINS SERVICE
 * Manages CI/CD pipeline integration, monitoring, and triggering.
 */

const JenkinsConfigSchema = z.object({
  url: z.string().url(),
  user: z.string(),
  token: z.string(),
  job: z.string()
});

export async function getJenkinsConfig() {
  const url = process.env.JENKINS_URL || 'http://localhost:8080';
  const user = process.env.JENKINS_USER || 'admin';
  const token = process.env.JENKINS_TOKEN || 'token';
  const job = process.env.JENKINS_JOB || 'antigravity-pipeline';

  return { url, user, token, job };
}

export async function getLatestBuildStatus() {
  try {
    const { url, user, token, job } = await getJenkinsConfig();
    const apiUrl = `${url}/job/${job}/lastBuild/api/json`;

    // Basic Mock for missing env / local testing if no real Jenkins
    if (url === 'http://localhost:8080' && !process.env.JENKINS_URL) {
      console.log('⚠️ [Jenkins] Using mock build status (No JENKINS_URL provided)');
      return {
        status: 'SUCCESS',
        number: 42,
        timestamp: Date.now(),
        url: `${url}/job/${job}/42/`
      };
    }

    const auth = Buffer.from(`${user}:${token}`).toString('base64');
    const response = await fetch(apiUrl, {
      headers: {
        'Authorization': `Basic ${auth}`
      }
    });

    if (!response.ok) {
      throw new Error(`Jenkins API error: ${response.statusText}`);
    }

    const data = await response.json() as any;
    return {
      status: data.result || 'IN_PROGRESS',
      number: data.number,
      timestamp: data.timestamp,
      url: data.url
    };
  } catch (error) {
    console.error('❌ [Jenkins] Failed to get latest build status:', error);
    return {
      status: 'UNKNOWN',
      number: 0,
      timestamp: 0,
      url: ''
    };
  }
}

export async function triggerBuild() {
  try {
    const { url, user, token, job } = await getJenkinsConfig();
    const apiUrl = `${url}/job/${job}/build`;

    if (url === 'http://localhost:8080' && !process.env.JENKINS_URL) {
      console.log('⚠️ [Jenkins] Mocking build trigger (No JENKINS_URL provided)');
      return { success: true, message: 'Mock build triggered' };
    }

    const auth = Buffer.from(`${user}:${token}`).toString('base64');
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Authorization': `Basic ${auth}`
      }
    });

    if (!response.ok) {
      throw new Error(`Jenkins API error: ${response.statusText}`);
    }

    console.log('✅ [Jenkins] Build triggered successfully.');
    return { success: true, message: 'Build triggered' };
  } catch (error) {
    console.error('❌ [Jenkins] Failed to trigger build:', error);
    return { success: false, message: (error as Error).message };
  }
}
