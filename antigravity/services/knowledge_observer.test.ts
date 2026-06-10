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
<<<<<<< HEAD
    const raw = '# Header 1\nContent 1\n# Header 2\nContent 2'
=======
    const raw = '# Header 1\nContent 1 is long enough to pass filter\n# Header 2\nContent 2 is also long enough'
>>>>>>> main
    const result = KnowledgeObserver.processContent('Test Title', raw, 'test-source')

    expect(result.title).toBe('Test Title')
    expect(result.sections).toHaveLength(2)
    expect(result.sections[0].header).toBe('Header 1')
<<<<<<< HEAD
    expect(result.sections[0].content).toBe('Content 1')
    expect(result.sections[1].header).toBe('Header 2')
    expect(result.sections[1].content).toBe('Content 2')
  })

  it('should handle Title Case headers', () => {
    const raw = 'Introduction\nThis is the intro.\nGetting Started\nStep 1...'
=======
    expect(result.sections[0].content).toBe('Content 1 is long enough to pass filter')
    expect(result.sections[1].header).toBe('Header 2')
    expect(result.sections[1].content).toBe('Content 2 is also long enough')
  })

  it('should handle Title Case headers', () => {
    const raw = '# Introduction\nThis is the intro and it is long enough.\n# Getting Started\nStep 1 is also long enough.'
>>>>>>> main
    const result = KnowledgeObserver.processContent('Test Title', raw, 'test-source')

    expect(result.sections).toHaveLength(2)
    expect(result.sections[0].header).toBe('Introduction')
    expect(result.sections[1].header).toBe('Getting Started')
  })

  it('should handle uppercase headers and skip code blocks', () => {
<<<<<<< HEAD
    const raw = `INTRODUCTION
=======
    const raw = `# INTRODUCTION
>>>>>>> main
This is an introduction.
<?php
class SkipMe {}
?>
<<<<<<< HEAD
DETAILS
Some details here.`
    const result = KnowledgeObserver.processContent('Test Title', raw, 'test-source')

    // console.log('DEBUG result sections:', result.sections)
    expect(result.sections.length).toBeGreaterThanOrEqual(2)
    expect(result.sections[0].header).toBe('INTRODUCTION')
    // Find section with header DETAILS
    const details = result.sections.find(s => s.header === 'DETAILS')
    expect(details).toBeDefined()
=======
# DETAILS
Some details here.`
    const result = KnowledgeObserver.processContent('Test Title', raw, 'test-source')

    expect(result.sections).toHaveLength(2)
    expect(result.sections[0].header).toBe('INTRODUCTION')
    expect(result.sections[1].header).toBe('DETAILS')
>>>>>>> main
    // Ensure the PHP class didn't become a header
    expect(result.sections.find(s => s.header === 'class SkipMe {}')).toBeUndefined()
  })

  it('should persist knowledge to custom directory', async () => {
    const observer = new KnowledgeObserver(testStorageDir)
<<<<<<< HEAD
    const knowledge = KnowledgeObserver.processContent('Persist Test', '# Section 1\nThis is the content.', 'source')
=======
    const knowledge = KnowledgeObserver.processContent('Persist Test', '# Section\nContent', 'source')
>>>>>>> main

    await observer.persistKnowledge(knowledge)

    expect(fs.existsSync(path.join(testStorageDir, 'system_knowledge.json'))).toBe(true)
<<<<<<< HEAD

    const json = JSON.parse(fs.readFileSync(path.join(testStorageDir, 'system_knowledge.json'), 'utf8'))
    expect(json['Persist Test']).toBeDefined()
    expect(json['Persist Test'].sections).toBeDefined()
    expect(json['Persist Test'].sections.length).toBeGreaterThan(0)
    expect(json['Persist Test'].sections[0].header).toBe('Section 1')
    expect(json['Persist Test'].sections[0].content).toBe('This is the content.')
  })
=======
    expect(fs.existsSync(path.join(testStorageDir, 'ai_agents_knowledge.md'))).toBe(true)

    const systemKnowledge = JSON.parse(fs.readFileSync(path.join(testStorageDir, 'system_knowledge.json'), 'utf8'))
    expect(systemKnowledge.typescript_sections[0].title).toBe('Persist Test')
  })



>>>>>>> main
})
