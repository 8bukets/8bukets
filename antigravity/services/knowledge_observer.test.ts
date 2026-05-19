import { describe, it, expect, beforeEach, afterEach } from 'vitest'
import fs from 'fs'
import path from 'path'
import { KnowledgeObserver } from './knowledge_observer'

describe('KnowledgeObserver', () => {
  const testStorageDir = path.join(process.cwd(), 'data/knowledge_test')

  beforeEach(() => {
    if (fs.existsSync(testStorageDir)) {
      fs.rmSync(testStorageDir, { recursive: true, force: true })
    }
  })

  afterEach(() => {
    if (fs.existsSync(testStorageDir)) {
      fs.rmSync(testStorageDir, { recursive: true, force: true })
    }
  })

  it('should process content into structured sections', () => {
    const raw = '# Header 1\nContent 1\n# Header 2\nContent 2'
    const result = KnowledgeObserver.processContent('Test Title', raw, 'test-source')

    expect(result.title).toBe('Test Title')
    expect(result.sections).toHaveLength(2)
    expect(result.sections[0].header).toBe('Header 1')
    expect(result.sections[0].content).toBe('Content 1')
    expect(result.sections[1].header).toBe('Header 2')
    expect(result.sections[1].content).toBe('Content 2')
  })

  it('should handle Title Case headers', () => {
    const raw = 'Introduction\nThis is the intro.\nGetting Started\nStep 1...'
    const result = KnowledgeObserver.processContent('Test Title', raw, 'test-source')

    expect(result.sections).toHaveLength(2)
    expect(result.sections[0].header).toBe('Introduction')
    expect(result.sections[1].header).toBe('Getting Started')
  })

  it('should handle uppercase headers and skip code blocks', () => {
    const raw = `INTRODUCTION
This is an introduction.
<?php
class SkipMe {}
?>
DETAILS
Some details here.`
    const result = KnowledgeObserver.processContent('Test Title', raw, 'test-source')

    expect(result.sections).toHaveLength(2)
    expect(result.sections[0].header).toBe('INTRODUCTION')
    expect(result.sections[1].header).toBe('DETAILS')
    // Ensure the PHP class didn't become a header
    expect(result.sections.find(s => s.header === 'class SkipMe {}')).toBeUndefined()
  })

  it('should persist knowledge to custom directory', async () => {
    const observer = new KnowledgeObserver(testStorageDir)
    const knowledge = KnowledgeObserver.processContent('Persist Test', '# Section\nContent', 'source')

    await observer.persistKnowledge(knowledge)

    expect(fs.existsSync(path.join(testStorageDir, 'system_knowledge.json'))).toBe(true)
    expect(fs.existsSync(path.join(testStorageDir, 'ai_agents_knowledge.md'))).toBe(true)

    const systemKnowledge = JSON.parse(fs.readFileSync(path.join(testStorageDir, 'system_knowledge.json'), 'utf8'))
    expect(systemKnowledge.typescript_sections[0].title).toBe('Persist Test')
  })

  it('should handle acronyms and technical terms in headers', () => {
    const raw = 'DNF Types\nContent about DNF.\nLSP\nLanguage Server Protocol.'
    const result = KnowledgeObserver.processContent('Test Title', raw, 'test-source')

    expect(result.sections).toHaveLength(2)
    expect(result.sections[0].header).toBe('DNF Types')
    expect(result.sections[1].header).toBe('LSP')
  })

  it('should NOT treat PHP attributes or markdown comments as headers', () => {
    const raw = `Appendix
Here is some code:
\`\`\`php
#[Attribute]
class MyClass {}
# This is a comment
\`\`\`
More content.`
    const result = KnowledgeObserver.processContent('Test Title', raw, 'test-source')

    expect(result.sections).toHaveLength(1)
    expect(result.sections[0].header).toBe('Appendix')
    expect(result.sections[0].content).toContain('#[Attribute]')
    expect(result.sections[0].content).toContain('# This is a comment')
  })
})
