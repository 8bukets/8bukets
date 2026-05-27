import { pipe, asyncPipe, map, filter, reduce } from '../antigravity/utils/fp';

// Example 1: Synchronous Data Processing Pipeline
console.log('--- Synchronous Pipeline ---');

const rawKnowledgeItems = [
  { id: 1, text: ' Google Ads allows Bidding   ', confidence: 0.95 },
  { id: 2, text: 'Invalid entry', confidence: 0.3 },
  { id: 3, text: '  Dynamic Ad Insertion is powerful ', confidence: 0.88 },
  { id: 4, text: '', confidence: 0.9 } // Empty text
];

// Pure functions for our pipeline
const extractConfidentItems = filter((item: any) => item.confidence > 0.8);
const trimWhitespace = map((item: any) => ({ ...item, text: item.text.trim() }));
const removeEmptyText = filter((item: any) => item.text.length > 0);
const toMarkdownList = map((item: any) => `- ${item.text} (Confidence: ${item.confidence})`);
const joinList = (arr: string[]) => arr.join('\n');

const processKnowledge = (data: any[]) => pipe(
  data,
  extractConfidentItems,
  trimWhitespace,
  removeEmptyText,
  toMarkdownList,
  joinList
);

const processedMarkdown = processKnowledge(rawKnowledgeItems);
console.log('Processed Result:\n' + processedMarkdown);
console.log('\n');


// Example 2: Asynchronous Pipeline
console.log('--- Asynchronous Pipeline ---');

// Mock asynchronous operations
const fetchRawData = async () => ['  Cloud   ', 'AI', '  Docker  '];
const asyncTrim = async (arr: string[]) => arr.map(s => s.trim());
const asyncToUpperCase = async (arr: string[]) => arr.map(s => s.toUpperCase());

async function runAsyncPipeline() {
  const result = await asyncPipe(
    fetchRawData(),
    asyncTrim,
    asyncToUpperCase,
    (arr) => arr.join(' -> ')
  );

  console.log('Async Pipeline Result:', result);
}

runAsyncPipeline().catch(console.error);
