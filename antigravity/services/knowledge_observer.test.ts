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

    expect(fs.existsSync(path.join(testStorageDir, 'ai_agents_knowledge.json'))).toBe(true)
    expect(fs.existsSync(path.join(testStorageDir, 'ai_agents_knowledge.md'))).toBe(true)

    const json = JSON.parse(fs.readFileSync(path.join(testStorageDir, 'ai_agents_knowledge.json'), 'utf8'))
    expect(json[0].title).toBe('Persist Test')
  })
})
