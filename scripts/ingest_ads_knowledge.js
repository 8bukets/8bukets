const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

async function ingestAdsKnowledge() {
  const baseUrls = [
    'https://support.google.com/google-ads/answer/2459326',
    'https://business.google.com/uk/ad-tools/bidding/',
    'https://business.google.com/uk/resources/',
    'https://developers.google.com/ad-manager',
    'https://developers.google.com/ad-manager/dynamic-ad-insertion',
    'https://developers.google.com/ad-manager/dynamic-ad-insertion/full-service',
    'https://developers.google.com/ad-manager/dynamic-ad-insertion/pod-serving',
    'https://developers.google.com/ad-manager/api/start',
    'https://admanager.google.com/home/resources/',
    'https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/overview'
  ];

  console.log(`Starting ingestion of ${baseUrls.length} URLs...`);

  let mdContentTotal = '\n## Google Ads Knowledge Ingestion\n\n';
  const jsonResults = [];

  const browser = await puppeteer.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  for (let rawUrl of baseUrls) {
    console.log(`Fetching ${rawUrl}...`);
    try {
      const page = await browser.newPage();

      // Attempt to hide navigation boilerplate by extracting main content
      await page.goto(rawUrl, { waitUntil: 'networkidle2', timeout: 60000 });

      // Simple extractor: grab paragraphs and headings from the main body
      const content = await page.evaluate(() => {
        let title = document.title || 'No Title';

        // Try to find the main content area to avoid nav bars
        let main = document.querySelector('main') ||
                   document.querySelector('article') ||
                   document.querySelector('.devsite-article-body') ||
                   document.body;

        let elements = main.querySelectorAll('h1, h2, h3, p, li');
        let textArr = [];

        elements.forEach(el => {
            // Very basic filtering to ignore short menu links
            let text = el.textContent.replace(/\s+/g, ' ').trim();
            if (text.length > 20 || el.tagName.startsWith('H')) {
                if (el.tagName.startsWith('H')) {
                    textArr.push(`\n### ${text}\n`);
                } else if (el.tagName === 'LI') {
                    textArr.push(`- ${text}`);
                } else {
                    textArr.push(`${text}\n`);
                }
            }
        });

        return {
            title: title,
            text: textArr.join('\n')
        };
      });

      // Filter out common boilerplate
      let cleanedText = content.text
        .replace(/Sign out of all accounts/g, '')
        .replace(/Add another account/g, '')
        .replace(/Access your Google accounts in one place/g, '');

      mdContentTotal += `### Source: ${rawUrl}\n**Title**: ${content.title}\n\n${cleanedText}\n\n---\n\n`;

      jsonResults.push({
          url: rawUrl,
          title: content.title,
          contentPreview: cleanedText.substring(0, 1000) + '...'
      });

      await page.close();
      await new Promise(resolve => setTimeout(resolve, 1000));
    } catch (err) {
      console.error(`Failed to fetch ${rawUrl}:`, err);
    }
  }

  await browser.close();

  // Write MD
  const mdPath = path.join(process.cwd(), 'data', 'knowledge', 'google_ads_docs.md');
  const dirPath = path.dirname(mdPath);
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
  }

  if (fs.existsSync(mdPath)) {
    let existingContent = fs.readFileSync(mdPath, 'utf8');
    // Append instead of overwrite
    existingContent += mdContentTotal;
    fs.writeFileSync(mdPath, existingContent, 'utf8');
  } else {
    fs.writeFileSync(mdPath, '# Google Ads and Ad Manager Documentation\n\n' + mdContentTotal, 'utf8');
  }

  // Write JSON
  const jsonPath = path.join(process.cwd(), 'data', 'knowledge', 'system_knowledge.json');
  let sysKnowledge = {};
  if (fs.existsSync(jsonPath)) {
      sysKnowledge = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  }
  sysKnowledge['google_ads'] = jsonResults;

  // Use 2-space indentation for system_knowledge.json
  fs.writeFileSync(jsonPath, JSON.stringify(sysKnowledge, null, 2), 'utf8');

  console.log('Ingestion complete!');
}

ingestAdsKnowledge().catch(err => {
  console.error('Failed to ingest knowledge:', err);
  process.exit(1);
});
