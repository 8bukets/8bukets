import { Jules } from '../antigravity/jules'

async function main() {
  console.log('🚀 Starting Knowledge Integration...')
  try {
    const jules = await Jules.create()
    await jules.observeKnowledge()
    console.log('✅ Knowledge Integration Complete.')
  } catch (err) {
    console.error('❌ Knowledge Integration Failed:', err)
    process.exit(1)
  }
}

main()
