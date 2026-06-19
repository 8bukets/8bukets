import { z } from 'zod';
import { logAutonomousAction } from '@/antigravity/core';
export const NotificationSchema = z.object({
    id: z.string(),
    type: z.enum(['health', 'evolution', 'security', 'scaling']),
    message: z.string(),
    severity: z.enum(['info', 'warning', 'critical']),
    timestamp: z.string()
});
const notifications = [];
/**
 * Autonomous Notification Service
 * Handles system-wide alerts for cognitive events.
 */
export async function sendNotification(payload) {
    const newNotification = {
        ...payload,
        id: Math.random().toString(36).substr(2, 9),
        timestamp: new Date().toISOString()
    };
    notifications.unshift(newNotification);
    if (notifications.length > 20)
        notifications.pop();
    // Log to the global autonomous buffer
    logAutonomousAction(`[${payload.type.toUpperCase()}] ${payload.message}`, payload.severity === 'critical' ? 'error' : 'info');
    return newNotification;
}
export async function getNotifications() {
    return notifications;
}
export async function dispatchExecutiveBriefing(title, content) {
    console.log(`[EXECUTIVE BRIEFING] ${title}\n${content}`);
    return await sendNotification({
        type: 'evolution',
        message: title,
        severity: 'info'
    });
}
