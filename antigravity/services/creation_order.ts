import fs from 'fs'
import path from 'path'
import { workOrderService, WorkOrder } from './work_order'
import { logAutonomousAction } from '../core'

/**
 * ANTIGRAVITY CREATION ORDER SERVICE (Phase 26)
 * Autonomously identifies system gaps and generates hierarchical work order chains.
 * Ports and evolves logic from Python WorkOrderAgent.
 */
export class CreationOrderService {
  /**
   * Scans the system state and identifies required work orders.
   */
  public async identifyAndCreateOrders(): Promise<WorkOrder[]> {
    logAutonomousAction('📝 [CreationOrder] Identifying new autonomous work orders...', 'info')

    const newOrders: WorkOrder[] = []
    const existingOrders = workOrderService.getAllOrders()

    // 1. Identify Missing Technical Documentation
    const techDocs = ['JULES_CLI.md', 'JULES_TOOLS.md', 'SYSTEM_PATENT.md']
    for (const doc of techDocs) {
      if (!fs.existsSync(path.join(process.cwd(), doc))) {
        if (!this.orderExists(existingOrders, `GENERATE_${doc.replace(/\./g, '_').toUpperCase()}`)) {
           const order = await workOrderService.createOrder(
             'CONTENT_GENERATION',
             `Generate missing technical documentation: ${doc}`,
             { document: doc }
           )
           newOrders.push(order)
        }
      }
    }

    // 2. Identify Stale Intelligence Reports
    const intelReport = path.join(process.cwd(), 'CONSOLIDATED_INTELLIGENCE.md')
    if (fs.existsSync(intelReport)) {
      const stats = fs.statSync(intelReport)
      const ageHours = (Date.now() - stats.mtimeMs) / (1000 * 60 * 60)
      if (ageHours > 24) {
        if (!this.orderExists(existingOrders, 'REFRESH_INTELLIGENCE')) {
          const researchOrder = await workOrderService.createOrder(
            'RESEARCH',
            'Refresh consolidated system intelligence (Stale > 24h)',
            { reason: 'stale_intelligence' }
          )
          newOrders.push(researchOrder)

          const mergeOrder = await workOrderService.createOrder(
            'KNOWLEDGE_MERGE',
            'Consolidate refreshed intelligence',
            { dependsOn: [researchOrder.id] },
            [researchOrder.id]
          )
          newOrders.push(mergeOrder)
        }
      }
    } else {
      // Missing report, trigger initial research
      if (!this.orderExists(existingOrders, 'INITIAL_RESEARCH')) {
        const researchOrder = await workOrderService.createOrder(
          'RESEARCH',
          'Initial market intelligence gathering',
          { reason: 'missing_report' }
        )
        newOrders.push(researchOrder)
      }
    }

    // 3. Identify Evolutionary Gaps (Deployment/Smoke Test)
    // In a real scenario, we'd check current_version vs deployed_version
    // For now, we check if evolution.ts suggests something
    try {
      const { evolve } = await import('../evolution')
      const suggestions = await evolve()
      if (suggestions.length > 0) {
        if (!this.orderExists(existingOrders, 'SYSTEM_REFACTOR_EVOLUTION')) {
           const refactorOrder = await workOrderService.createOrder(
             'REFACTOR_SYSTEM',
             `Apply ${suggestions.length} autonomous evolution suggestions`,
             { suggestions }
           )
           newOrders.push(refactorOrder)

           const smokeOrder = await workOrderService.createOrder(
             'SMOKE_TEST',
             'Verify system stability post-refactor',
             { reason: 'post_refactor' },
             [refactorOrder.id]
           )
           newOrders.push(smokeOrder)
        }
      }
    } catch (e) {}

    // 4. Content Generation from Market Trends
    const knowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json')
    if (fs.existsSync(knowledgePath)) {
      try {
        const knowledge = JSON.parse(fs.readFileSync(knowledgePath, 'utf8'))
        const trends = knowledge.market_trends || []
        for (const trend of trends) {
          const trendId = `CONTENT_${trend.replace(/\s+/g, '_').replace(/\./g, '').toUpperCase()}`
          if (!this.orderExists(existingOrders, trendId)) {
            const order = await workOrderService.createOrder(
              'CONTENT_GENERATION',
              `Generate structured content for trend: ${trend}`,
              { trend }
            )
            newOrders.push(order)
          }
        }
      } catch (e) {}
    }

    if (newOrders.length > 0) {
      logAutonomousAction(`✅ [CreationOrder] Identified and created ${newOrders.length} new work orders.`, 'info')
    } else {
      logAutonomousAction('✨ [CreationOrder] System state is optimal. No new orders required.', 'info')
    }

    return newOrders
  }

  private orderExists(orders: WorkOrder[], goalOrId: string): boolean {
    return orders.some(o => o.id === goalOrId || o.goal?.includes(goalOrId) || o.id.startsWith(goalOrId))
  }
}

export const creationOrderService = new CreationOrderService()
