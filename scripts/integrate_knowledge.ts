import { Jules } from '../antigravity/jules'

async function main() {
  console.log('🚀 Starting Knowledge Integration...')
  try {
    const jules = new Jules()
    await jules.executeWorkCycle()
    console.log('✅ Knowledge Integration Complete.')
  } catch (err) {
    console.error('❌ Knowledge Integration Failed:', err)
    process.exit(1)
  }
}

main()
