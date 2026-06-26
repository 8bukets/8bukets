const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

async function ingestAdsKnowledge() {
  const baseUrls = [
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
  ];
  // Authorized syntactic adjustment to trigger clean commit
// Agent - Logika ponašanja
// Agent odlučuje:
// * što napraviti,
// * kojim redoslijedom,
// * treba li koristiti alat,
// * treba li iterirati,
// * treba li popraviti grešku.
// To je “brain workflow”.
//
// Harness - Execution/runtime layer
// * poziva alate,
// * izvršava komande,
// * upravlja memoryjem,
// * daje modelu context,
// * kontrolira loop,
// * upravlja retryjima,
// * sandboxa sustav,
// * prati stanje taska.
// To je “operating environment”.
//
// Tooling layer - vrlo bitno. ima duboku integraciju s:
// * terminalom,
// * gitom,
// * file systemom,
// * test runnerima,
// * package managerima,
// * editorima,
// * shellom.
// To nije isto što i harness.
// To su konkretni capability adapteri.
//
// Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje:
// * koje fileove učitati,
// * što sažeti,
// * što odbaciti,
// * kako pakirati repo,
// * kako komprimirati history,
// * što pokazati modelu.
//
// To je ogromna razlika između:
//
// * “AI razumije projekt”
//     i
// * “AI je izgubljen”.
//
// Prompt orchestration -  ima:
// * system promptove,
// * hidden chain strukture,
// * task decomposition promptove,
// * reflection promptove,
// * self-check promptove.
// To su višeslojni prompt sistemi, ne jedan prompt.
//
// Autonomy loop -  ovo je posebno bitno. Loop izgleda:
// * analiziraj,
// * napravi promjenu,
// * pokreni,
// * vidi grešku,
// * popravi,
// * retry,
// * validiraj,
// * nastavi.
// Kvaliteta tog loopa jako određuje kvalitetu agenta.
//
// Repo indexing / retrieval system - sigurno ima sofisticirani:
// * semantic search,
// * dependency graph,
// * file relevance ranking,
// * retrieval pipeline.
// Da bi znao:
// * koje fileove otvoriti,
// * koje ignorirati.
//
// Diff / edit engine -  vrlo podcijenjeno. Nije isto:
//
// * generirati kod
//     i
// * sigurno editirati postojeći repo.
//
// Bitno je:
// * kako radi patching,
// * kako spaja diffove,
// * kako izbjegava corruption,
// * kako čuva formatting,
// * kako radi partial edits.
//
// Verification layer - vrlo važan dio modernih agenata. Sustav provjerava:
// * build prolazi li,
// * testovi prolaze li,
// * lint prolazi li,
// * runtime errori postoje li.
// Bez toga agent često “samouvjereno halucinira”.
//
// Memory system - može biti:
// * session memory,
// * task memory,
// * repo memory,
// * preference memory.
// To omogućuje dugotrajan rad bez gubitka konteksta.
//
// Safety / permission system - vrlo bitno za autonomne agente.
// Sustav odlučuje:
// * što agent smije izvršiti,
// * kada mora pitati korisnika,
// * što je opasno,
// * što je readonly.
//
// UX layer - djeluje dobro i zato što:
// * output izgleda smisleno,
// * agent objašnjava što radi,
// * flow djeluje prirodno,
// * terminal UX je dobro dizajniran.
// To dramatično mijenja percepciju kvalitete.
//
//
// * model,
// * agent logic,
// * harness/runtime,
// * tooling,
// * context system,
// * retrieval engine,
// * prompting architecture,
// * autonomy engine,
// * verification system,
// * memory,
// * permissions,
// * UX.

// create agent Chief AI Officer

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
