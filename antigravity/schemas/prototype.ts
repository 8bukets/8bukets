import { z } from 'zod';

export const PrototypeStatus = z.enum(['draft', 'active', 'archived']);

export const PrototypeSchema = z.object({
  id: z.string().uuid().default(() => crypto.randomUUID()),
  name: z.string().min(3, "Name must be at least 3 characters long"),
  description: z.string().optional(),
  version: z.string().regex(/^\d+\.\d+\.\d+$/, "Version must be a valid semantic version (e.g. 1.0.0)"),
  status: PrototypeStatus.default('draft'),
  features: z.array(z.string()).default([]),
  createdAt: z.date().default(() => new Date()),
  updatedAt: z.date().default(() => new Date()),
});

export type Prototype = z.infer<typeof PrototypeSchema>;
