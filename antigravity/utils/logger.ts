export const logBuffer: { msg: string; time: string; type: string }[] = []

export function logAutonomousAction(msg: string, type: string = 'info') {
  logBuffer.unshift({ msg, time: new Date().toLocaleTimeString(), type })
  if (logBuffer.length > 50) logBuffer.pop()
}
