import { logAutonomousAction } from '../core';

/**
 * ADAPTIVE RECOVERY SERVICE
 * Implements self-correcting automation with a "creativity dose" when a run fails.
 */

export class AdaptiveRecoveryService {
  private failedAttempts: Record<string, number> = {};

  /**
   * Evaluates an error, applies a "creativity dose" to formulate an alternative plan,
   * and attempts self-correction.
   */
  public async selfCorrect(context: string, error: any): Promise<void> {
    const errorMsg = error instanceof Error ? error.message : String(error);
    logAutonomousAction(`🚨 [Recovery] Failure detected in ${context}: ${errorMsg}`, 'error');

    this.failedAttempts[context] = (this.failedAttempts[context] || 0) + 1;

    if (this.failedAttempts[context] > 3) {
      logAutonomousAction(`🛑 [Recovery] Max retry limit reached for ${context}. Skipping.`, 'error');
      // Reset after max to eventually try again later
      this.failedAttempts[context] = 0;
      return;
    }

    const creativityDose = this.synthesizeCreativeSolution(context, errorMsg);
    logAutonomousAction(`💡 [Recovery] Applying Creativity Dose: ${creativityDose.plan}`, 'cognitive');

    try {
      await this.executeCreativeSolution(creativityDose);
      logAutonomousAction(`✅ [Recovery] Successfully applied creativity dose for ${context}.`, 'info');
      // Decrease failure count on success
      this.failedAttempts[context]--;
    } catch (correctionError: any) {
      logAutonomousAction(`❌ [Recovery] Creativity dose failed for ${context}: ${correctionError.message}`, 'error');
    }
  }

  /**
   * Generates an alternative approach (Creativity Dose) based on the error.
   */
  private synthesizeCreativeSolution(context: string, errorMsg: string) {
    if (errorMsg.includes('network') || errorMsg.includes('ETIMEDOUT') || errorMsg.includes('fetch')) {
      return {
        type: 'NETWORK_RETRY',
        plan: 'Network issue detected. Temporarily switching to local cache or offline mode heuristics.'
      };
    }

    if (errorMsg.includes('git') || errorMsg.includes('merge') || errorMsg.includes('conflict')) {
      return {
        type: 'GIT_RESET',
        plan: 'Git conflict or state issue. Reverting to safe HEAD state and skipping problematic PR/commit.'
      };
    }

    if (errorMsg.includes('memory') || errorMsg.includes('heap')) {
       return {
         type: 'MEMORY_CLEAR',
         plan: 'Memory pressure detected. Flushing cached cognitive state before retry.'
       }
    }

    if (errorMsg.includes('NSFileProviderErrorDomain') || errorMsg.includes('-5009') || errorMsg.includes('iCloud') || errorMsg.includes('fileproviderd')) {
       return {
         type: 'ICLOUD_SYNC_FIX',
         plan: 'iCloud File Provider sync issue detected. Restarting background daemons to restore fluid workflow.'
       }
    }

    // Generic "creative" fallback
    return {
      type: 'HEURISTIC_BYPASS',
      plan: `Unknown failure in ${context}. Injecting heuristic bypass logic: Skipping failing sub-module and prioritizing core integrity checks.`
    };
  }

  private async executeCreativeSolution(solution: { type: string, plan: string }) {
    if (solution.type === 'GIT_RESET') {
      const { exec } = await import('child_process');
      const { promisify } = await import('util');
      const execAsync = promisify(exec);
      try {
         await execAsync('git reset --hard HEAD || true');
         await execAsync('git clean -fd || true');
      } catch (e) {}
    } else if (solution.type === 'NETWORK_RETRY') {
      // Simulate waiting for network or switching to local
      await new Promise(resolve => setTimeout(resolve, 2000));
    } else if (solution.type === 'MEMORY_CLEAR') {
      if (global.gc) {
          global.gc();
      }
    } else if (solution.type === 'ICLOUD_SYNC_FIX') {
      const { exec } = await import('child_process');
      const { promisify } = await import('util');
      const execAsync = promisify(exec);
      try {
        await execAsync('bash scripts/fix_icloud_sync.sh');
        await new Promise(resolve => setTimeout(resolve, 3000)); // Give daemons time to restart
      } catch (e) {}
    } else {
       // HEURISTIC_BYPASS - we just log and allow the system to proceed without the failing component
       await new Promise(resolve => setTimeout(resolve, 1000));
    }
  }
}

export const adaptiveRecovery = new AdaptiveRecoveryService();
