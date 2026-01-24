## 2026-01-24 - TextBlob Re-parsing Optimization
**Learning:** In the `AnalyzerAgent`, creating a giant `TextBlob` from concatenated strings of individual posts caused a redundant and expensive O(N) tokenization pass. Accumulating tokens from the individual post blobs (which were already created for sentiment analysis) saved ~22% execution time on a mock dataset.
**Action:** When performing multiple NLP tasks (sentiment + keyword extraction) on a collection of texts, reuse the parsed objects (tokens/words) from the first pass instead of concatenating and re-parsing the aggregate.
