import { observeKnowledge } from '../antigravity/services/knowledge';

async function ingestAdsKnowledge() {
  const urls = [
    "https://support.google.com/google-ads/answer/2459326?hl=en&ref_topic=10289453&sjid=5167206403107665975-EU",
    "https://business.google.com/uk/ad-tools/bidding/?hl=en",
    "https://business.google.com/uk/resources/?hl=en",
    "https://developers.google.com/ad-manager?hl=en",
    "https://developers.google.com/ad-manager/dynamic-ad-insertion?hl=en",
    "https://developers.google.com/ad-manager/dynamic-ad-insertion/full-service?hl=en",
    "https://developers.google.com/ad-manager/dynamic-ad-insertion/pod-serving?hl=en",
    "https://developers.google.com/ad-manager/api/start?hl=en",
    "https://admanager.google.com/home/resources/?hl=en",
    "https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/overview?hl=en"
  ];

  console.log(`Starting ingestion of ${urls.length} URLs...`);

  for (const url of urls) {
    await observeKnowledge(url);
    // Add a small delay to avoid hitting rate limits
    await new Promise(resolve => setTimeout(resolve, 1000));
  }

  console.log('Ingestion complete!');
}

ingestAdsKnowledge().catch(err => {
  console.error('Failed to ingest knowledge:', err);
  process.exit(1);
});
