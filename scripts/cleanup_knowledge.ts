import fs from 'fs-extra'
import path from 'path'

async function cleanup() {
  console.log('🧹 Starting Knowledge Base Cleanup...')

  const storageDir = path.join(process.cwd(), 'data/knowledge')
  const jsonStore = path.join(storageDir, 'system_knowledge.json')
  const mdStore = path.join(storageDir, 'ai_agents_knowledge.md')

  if (!fs.existsSync(jsonStore)) {
    console.log('❌ JSON store not found.')
    return
  }

  const systemKnowledge = fs.readJsonSync(jsonStore)
  const originalCount = systemKnowledge.typescript_sections.length

  // Deduplicate and cleanup
  const titlesSeen = new Set<string>()
  systemKnowledge.typescript_sections = systemKnowledge.typescript_sections.filter((k: any) => {
    // 1. Remove obvious redundants
    if (k.title === 'intelephense_docs.md') return false

    // 2. Rename caio_role_docs.md to "Chief AI Officer (CAIO) Role"
    if (k.title === 'caio_role_docs.md') {
       k.title = 'Chief AI Officer (CAIO) Role'
    }

    // 3. Keep only unique titles, preferring the ones we just updated
    if (titlesSeen.has(k.title)) return false
    titlesSeen.add(k.title)

    return true
  })

  console.log(`✅ Removed ${originalCount - systemKnowledge.typescript_sections.length} redundant entries from JSON store.`)
  fs.writeJsonSync(jsonStore, systemKnowledge, { spaces: 2 })

  // Rebuild Markdown from cleaned JSON
  let mdContent = `# ANTIGRAVITY AI AGENTS KNOWLEDGE BASE\n\n*Last Updated: ${new Date().toISOString()}*\n\n`

  for (const k of systemKnowledge.typescript_sections) {
    mdContent += `## DOCUMENT: ${k.title}\n`
    mdContent += `**Source:** ${k.metadata.source.trim()}  \n`
    mdContent += `**Ingested At:** ${k.metadata.ingestedAt}\n\n`

    for (const section of k.sections) {
      if (section.content.trim() || ['Getting Started', 'Features', 'Installation'].includes(section.header)) {
        mdContent += `### ${section.header}\n${section.content.trim()}\n\n`
      }
    }
    mdContent += `---\n\n`
  }

  fs.writeFileSync(mdStore, mdContent)
  console.log('✅ Markdown knowledge base rebuilt and cleaned.')
}

cleanup().catch(console.error)
