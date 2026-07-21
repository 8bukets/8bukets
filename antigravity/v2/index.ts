/**
 * Antigravity 2.0 — Public API barrel
 *
 * Import from 'antigravity/v2' to access all 2.0 primitives.
 */

export { Agent, type AgentRole, agent } from './agent';
export { logger } from './logger';
export { loadMemory, saveMemory, recordTask, type AgentMemory } from './memory';
export { runWorkCycle } from './work_cycle';
export { registry } from './service_registry';
export { nexus } from './nexus';
