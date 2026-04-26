const core = require('@actions/core');

try {
  core.info('Post-job: Cleaning up the custom action environment...');
  // Boilerplate logic for post-action cleanup
  // For example, removing temporary files or terminating processes
  core.info('Post-job cleanup complete.');
} catch (error) {
  core.setFailed(`Post-job failed: ${error.message}`);
}
