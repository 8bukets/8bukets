import { z } from 'zod'
import { autonomousFetch, logAutonomousAction } from '@/antigravity/core'

export const NotificationSchema = z.object({
  id: z.string(),
  type: z.enum(['health', 'evolution', 'security', 'scaling']),
  message: z.string(),
  severity: z.enum(['info', 'warning', 'critical']),
  timestamp: z.string()
})

export type Notification = z.infer<typeof NotificationSchema>

const notifications: Notification[] = []

/**
 * Autonomous Notification Service
 * Handles system-wide alerts for cognitive events.
 */
export async function sendNotification(payload: Omit<Notification, 'id' | 'timestamp'>) {







  const newNotification: Notification = {
    ...payload,
    id: Math.random().toString(36).substr(2, 9),
    timestamp: new Date().toISOString()
  }

  notifications.unshift(newNotification)
  if (notifications.length > 20) notifications.pop()

  // Log to the global autonomous buffer
  logAutonomousAction(`[${payload.type.toUpperCase()}] ${payload.message}`, payload.severity === 'critical' ? 'error' : 'info')
  
  return newNotification
}

export async function getNotifications(): Promise<Notification[]> {
  'use cache'
  // Use 'inventory' profile for frequent updates
  return notifications
}

export async function dispatchExecutiveBriefing(summary: string, details?: string) {
  console.log('📢 [Notification] Dispatching executive briefing...')

  const formattedDetails = details ? details.split('\n\n').map(section => {
    if (section.startsWith('---')) {
      return `\n${section.replace(/---/g, '').trim().toUpperCase()}\n${'='.repeat(section.length - 6)}`
    }
    return section
  }).join('\n') : ''

  const fullMessage = details
    ? `🔔 EXECUTIVE BRIEFING\n\nSTATUS: ${summary}\n${formattedDetails}`
    : `🔔 EXECUTIVE BRIEFING: ${summary}`

  const briefing: Notification = {
    id: Math.random().toString(36).substr(2, 9),
    type: 'evolution',
    severity: 'info',
    message: fullMessage,
    timestamp: new Date().toISOString()
  }

  notifications.unshift(briefing)
  logAutonomousAction(`[BRIEFING] ${summary}`, 'info')

  return briefing
}
