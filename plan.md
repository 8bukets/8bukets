1. **Update `urlsToObserve` in `antigravity/jules.ts`:**
   - Modify the array to *only* contain `https://www.investopedia.com/` as requested ("always pull knowledge from investopedia.com").
2. **Enhance Investopedia integration in `scripts/ingest_investopedia.ts` and `antigravity/services/knowledge.ts`:**
   - To "integrate all knowledge", we'll improve the scraping to crawl beyond just the front page.
   - We will implement a deep crawl inside `ingest_investopedia.ts` by fetching links from the main page and passing them to `observeKnowledge`.
   - Update `observeKnowledge` in `antigravity/services/knowledge.ts` to cleanly handle subpages and aggregate the knowledge efficiently in `KNOWLEDGE_MERGE.md`.
3. **Execute ingestion & pre-commit tests:**
   - Run the modified script: `npx tsx scripts/ingest_investopedia.ts` to actually pull the knowledge and generate the KNOWLEDGE_MERGE updates.
   - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
4. **Submit changes:**
   - Submit the PR with the integrated Investopedia scraping enhancements.
