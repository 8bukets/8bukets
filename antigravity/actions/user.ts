'use server'

import { updateTag, revalidateTag, refresh } from '@/antigravity/core'

/**
 * Scalable Mutation: 'Read-Your-Writes' consistency
 * updateTag expires and re-executes data fetching in the SAME request.
 */
export async function updateUserName(userId: string, newName: string) {
  // Update the DB (mocked)
  console.log(`Updating user ${userId} to ${newName}`)
  
  // updateTag gives the user an immediate result
  updateTag(`user-${userId}`)
  
  // revalidateTag can still be used for background revalidation
  revalidateTag('user-list', 'max')
}

/**
 * Scalable Global Refresh: 
 */
export async function clearUserSession() {
  // Clear session logic here...
  refresh()
}
