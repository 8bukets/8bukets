import fs from 'fs'
import path from 'path'

export async function generateCreationReport(rootOrderId: string) {
  'use cache'
  console.log(`📊 [Reporting] Generating comprehensive creation report for pulse: ${rootOrderId}`)
  const reportPath = path.join(process.cwd(), 'data/latest_creation_order.md')
  const storagePath = path.join(process.cwd(), 'data/work_orders.json')

  try {
    if (!await fs.promises.access(storagePath).then(() => true).catch(() => false)) {
      throw new Error('Work orders file not found.')
    }

    const allOrders = JSON.parse(await fs.promises.readFile(storagePath, 'utf8'))

    // Find session orders (transitive dependencies)
    const sessionOrderIds = new Set<string>([rootOrderId])
    let expanded = true
    while (expanded) {
      expanded = false
      for (const order of allOrders) {
        if (!sessionOrderIds.has(order.id) && order.dependsOn?.some((depId: string) => sessionOrderIds.has(depId))) {
          sessionOrderIds.add(order.id)
          expanded = true
        }
      }
    }

    const sessionOrders = allOrders.filter((o: any) => sessionOrderIds.has(o.id))

    let report = `# Antigravity Autonomous Creation Report\n\n`
    report += `**Root Pulse ID:** ${rootOrderId}\n`
    report += `**Generated At:** ${new Date().toISOString()}\n\n`

    report += `## 📜 Execution Sequence\n`
    if (sessionOrders.length === 0) {
      report += `_No orders were recorded in this pulse._\n`
    } else {
      sessionOrders.forEach((o: any) => {
        const statusIcon = o.status === 'completed' ? '✅' : o.status === 'failed' ? '❌' : '⏳'
        report += `### ${statusIcon} [${o.status.toUpperCase()}] ${o.type}\n`
        report += `- **Goal:** ${o.goal}\n`
        report += `- **ID:** \`${o.id}\`\n`
        if (o.dependsOn && o.dependsOn.length > 0) {
          report += `- **Depends On:** ${o.dependsOn.map((id: string) => `\`${id}\``).join(', ')}\n`
        }
        if (o.result) {
          report += `- **Result:** \`${JSON.stringify(o.result)}\`\n`
        }
        if (o.error) {
          report += `- **Error:** \`${o.error}\`\n`
        }
        report += `\n`
      })
    }

    report += `\n---\n*Generated autonomously by the Antigravity Reporting Service.*`

    await fs.promises.mkdir(path.dirname(reportPath), { recursive: true })
    await fs.promises.writeFile(reportPath, report)
    console.log(`✅ [Reporting] Report saved to ${reportPath}`)
  } catch (err: any) {
    console.error(`❌ [Reporting] Failed to generate report:`, err.message)
  }
}
