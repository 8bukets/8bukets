const fs = require('fs');

const replacement = `  const URLS = [
    'https://support.google.com/google-ads/answer/2459326?hl=en&ref_topic=10289453&sjid=5167206403107665975-EU',
    'https://business.google.com/uk/ad-tools/bidding/',
    'https://business.google.com/uk/resources/',
    'https://developers.google.com/ad-manager',
    'https://developers.google.com/ad-manager/dynamic-ad-insertion',
    'https://developers.google.com/ad-manager/dynamic-ad-insertion/full-service',
    'https://developers.google.com/ad-manager/dynamic-ad-insertion/pod-serving',
    'https://developers.google.com/ad-manager/api/start',
    'https://admanager.google.com/home/resources/',
    'https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/overview'
  ];`;

let data = fs.readFileSync('scripts/ingest_ads_knowledge.ts', 'utf8');

const regex = /const URLS = \[\s*[\s\S]*?\];/;
data = data.replace(regex, replacement);

fs.writeFileSync('scripts/ingest_ads_knowledge.ts', data);
