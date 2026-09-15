import { getFeedbackAnalysisServiceData } from '../services/feedback_analysis';

async function run() {
  const data = await getFeedbackAnalysisServiceData();
  console.log('✅ [Workflow] Feedback Analysis complete:', JSON.stringify(data, null, 2));
}

run().catch((err) => {
  console.error('❌ [Workflow] Feedback Analysis failed:', err);
  process.exit(1);
});
