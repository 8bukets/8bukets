import { observeGithubDocs } from '../antigravity/services/github_docs_observer'
import fs from 'fs'
import path from 'path'

async function testKnowledgeIntegration() {
  console.log('🧪 Testing GitHub Docs Knowledge Integration...')

  const repo = 'bmewburn/intelephense-docs'
  const files = ['features.md', 'installation.md', 'gettingStarted.md']

  const insights = await observeGithubDocs(repo, files)

  console.log(`\n📊 Extraction Results:`)
  console.log(`Files scanned: ${insights.length}`)

  insights.forEach(insight => {
    console.log(`- ${insight.file}: ${insight.sections.length} sections found.`)
  })

  if (insights.length > 0) {
    console.log('\n✅ Extraction logic seems to work.')

    // Test the data format that will be saved in jules.ts
    const consolidatedKnowledge = {
      github: insights,
      lastUpdated: new Date().toISOString()
    }

    const testJsonPath = path.join(process.cwd(), 'test_knowledge_output.json')
    fs.writeFileSync(testJsonPath, JSON.stringify(consolidatedKnowledge, null, 2))
    console.log(`📝 Sample output written to ${testJsonPath}`)
  } else {
    console.error('\n❌ No insights extracted. Check network or repository details.')
  }
}

testKnowledgeIntegration().catch(err => {
  console.error('💥 Test failed:', err)
  process.exit(1)
})
