import { experimental_taintObjectReference } from 'react'
import { autonomousFetch } from '@/antigravity/core'
import { z } from 'zod'

export const UserSchema = z.object({
  id: z.string(),
  name: z.string(),
  email: z.string(),
  token: z.string(),
})

export type User = z.infer<typeof UserSchema>

export async function getUser(id: string): Promise<User> {
  return autonomousFetch(
    UserSchema,
    async () => {
      'use cache'
      // In a real app, fetch from DB
      const user = {
        id,
        name: 'John Doe',
        email: 'john@example.com',
        token: 'secret-session-token'
      }

      // Taint the user object to prevent it from being passed to Client Components
      experimental_taintObjectReference(
        'Do not pass the full user object to the client. It contains sensitive tokens.',
        user
      )

      return user
    },
    {
      tags: [`user-${id}`],
      life: 'minutes'
    }
  )
}

/**
 * Scalable Pattern: Export "Safe" versions of data for Client Components
 */
export function getSafeUser(user: User) {
  return {
    id: user.id,
    name: user.name
  }
}
