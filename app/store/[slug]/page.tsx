export const unstable_instant = { prefetch: 'static' }

import { Suspense } from 'react'
import { PageProps, resolve } from '@/antigravity/core'

// Mock fetching function
async function getProduct(slug: string) {
  // [Evolution] TODO: Add autonomous error handling (try/catch)
  // [Evolution] TODO: Add autonomous error handling (try/catch)
  'use cache'
  // In a real app, this would fetch from a database or API
  return {
    slug,
    name: `Product ${slug.charAt(0).toUpperCase() + slug.slice(1)}`,
    price: Math.floor(Math.random() * 100) + 50,
    description: "This is a great product that demonstrates 'use cache' and instant navigation."
  }
}

async function getInventory(slug: string) {
  // Uncached, will stream
  await new Promise(res => setTimeout(res, 1000)) // Artificial delay
  return {
    count: Math.floor(Math.random() * 20)
  }
}

export default async function StorePage({
  params,
}: PageProps<{ slug: string }>) {
  return (
    <div className="flex flex-col p-8 gap-8">
      <Suspense fallback={<ProductSkeleton />}>
        {resolve(params).then(({ slug }) => (
          <ProductDetails slug={slug} />
        ))}
      </Suspense>
      
      <Suspense fallback={<InventorySkeleton />}>
        <Inventory params={params} />
      </Suspense>
    </div>
  )
}

async function ProductDetails({ slug }: { slug: string }) {
  const product = await getProduct(slug)
  return (
    <div className="flex flex-col gap-4">
      <h1 className="text-4xl font-bold">{product.name}</h1>
      <p className="text-2xl text-zinc-600">${product.price}</p>
      <p className="max-w-prose">{product.description}</p>
    </div>
  )
}

async function Inventory({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params
  const inventory = await getInventory(slug)
  return (
    <div className="p-4 bg-zinc-100 dark:bg-zinc-800 rounded-lg">
      <p className="font-semibold">{inventory.count} items in stock</p>
      <p className="text-sm text-zinc-500 italic">(Fetched live from inventory system)</p>
    </div>
  )
}

function ProductSkeleton() {
  return (
    <div className="flex flex-col gap-4 animate-pulse">
      <div className="h-10 w-64 bg-zinc-200 dark:bg-zinc-700 rounded" />
      <div className="h-8 w-24 bg-zinc-200 dark:bg-zinc-700 rounded" />
      <div className="h-20 w-full bg-zinc-200 dark:bg-zinc-700 rounded" />
    </div>
  )
}

function InventorySkeleton() {
  return (
    <div className="h-20 w-full bg-zinc-100 dark:bg-zinc-800 rounded-lg animate-pulse" />
  )
}
