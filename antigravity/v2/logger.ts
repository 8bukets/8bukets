/**
 * Antigravity 2.0 — Safe Logger
 *
 * A drop-in console wrapper that is immune to iCloud Drive file-lock
 * collisions (macOS error -11 / EAGAIN).
 *
 * When stdout/stderr are redirected to a file inside iCloud Drive, the OS
 * File Provider may have that file "dataless" (not yet downloaded) and any
 * write to it throws EAGAIN (-11). This logger catches that case so it never
 * crashes the caller.
 */

const LEVEL_ICONS: Record<string, string> = {
  info:  '✅',
  warn:  '⚠️ ',
  error: '❌',
  debug: '🔍',
  phase: '📡',
}

function safeWrite(stream: NodeJS.WriteStream, text: string) {
  try {
    stream.write(text + '\n');
  } catch (_) {
    // Swallow iCloud -11 lock errors — the message is lost but the
    // process continues. This is intentional for 24/7 daemon mode.
  }
}

export const logger = {
  info(msg: string)  { safeWrite(process.stdout, `${LEVEL_ICONS.info}  [AGY] ${msg}`) },
  warn(msg: string)  { safeWrite(process.stderr, `${LEVEL_ICONS.warn} [AGY] ${msg}`) },
  error(msg: string) { safeWrite(process.stderr, `${LEVEL_ICONS.error} [AGY] ${msg}`) },
  debug(msg: string) { safeWrite(process.stdout, `${LEVEL_ICONS.debug} [AGY] ${msg}`) },
  phase(msg: string) { safeWrite(process.stdout, `${LEVEL_ICONS.phase} [AGY] ${msg}`) },
  raw(msg: string)   { safeWrite(process.stdout, msg) },
}
