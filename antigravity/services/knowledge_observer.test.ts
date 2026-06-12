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
    const raw = '# Header 1\nContent 1 is long enough\n# Header 2\nContent 2 is also long enough'
    const result = KnowledgeObserver.processContent('Test Title', raw, 'test-source')

    expect(result.title).toBe('Test Title')
    expect(result.sections?.length).toBeGreaterThanOrEqual(2)
    expect(result.sections?.[0].header).toBe('Header 1')
    expect(result.sections?.[0].content).toContain('Content 1')
  })

  it('should handle Title Case headers', () => {
    const raw = 'Introduction\nThis is the introduction and it needs to be long enough.\nGetting Started\nStep 1 is also required to be long enough to pass filters.'
    const result = KnowledgeObserver.processContent('Test Title', raw, 'test-source')

    expect(result.sections?.length).toBeGreaterThanOrEqual(2)
    expect(result.sections?.[0].header).toBe('Introduction')
    expect(result.sections?.[1].header).toBe('Getting Started')
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

    // console.log('DEBUG result sections:', result.sections)
    expect(result.sections.length).toBeGreaterThanOrEqual(2)
    expect(result.sections[0].header).toBe('INTRODUCTION')
    // Find section with header DETAILS
    const details = result.sections.find(s => s.header === 'DETAILS')
    expect(details).toBeDefined()
    // Ensure the PHP class didn't become a header
    expect(result.sections.find(s => s.header === 'class SkipMe {}')).toBeUndefined()
  })

  it('should persist knowledge to custom directory', async () => {
    const observer = new KnowledgeObserver(testStorageDir)
    const knowledge = KnowledgeObserver.processContent('Persist Test', '# Section 1\nThis is the content and it is long enough.', 'source')

    await observer.persistKnowledge(knowledge)

    expect(fs.existsSync(path.join(testStorageDir, 'system_knowledge.json'))).toBe(true)

    const json = JSON.parse(fs.readFileSync(path.join(testStorageDir, 'system_knowledge.json'), 'utf8'))
    expect(json.typescript_sections).toBeDefined()
    const section = json.typescript_sections.find((s: any) => s.title === 'Persist Test')
    expect(section).toBeDefined()
    expect(section.sections).toBeDefined()
    expect(section.sections.length).toBeGreaterThan(0)
    expect(section.sections[0].header).toBe('Section 1')
    expect(section.sections[0].content).toContain('This is the content')
  })
})
