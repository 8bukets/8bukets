'use client'

import { Check } from 'lucide-react'

const tiers = [
  {
    name: 'Free Tier',
    id: 'tier-free',
    href: '#',
    priceMonthly: '$0',
    description: 'Basic health monitoring and manual agent tracking.',
    features: ['Dashboard Access', 'System Health Monitoring', 'View Cognitive Stream Logs'],
    featured: false,
    cta: 'Get started for free',
  },
  {
    name: 'Pro API Access',
    id: 'tier-pro',
    href: '/api/checkout?price=price_pro', // We'll handle this in the next step
    priceMonthly: '$49',
    description: 'Full access to the AI/Dev Intelligence Platform API.',
    features: [
      'Real-time AI Model Updates',
      'Proprietary SEO Metrics API',
      'Webhooks for Scraper Output',
      'Daily "Factory" Insights',
    ],
    featured: true,
    cta: 'Subscribe to Pro',
  },
  {
    name: 'Enterprise AaaS',
    id: 'tier-enterprise',
    href: '/api/checkout?price=price_enterprise',
    priceMonthly: '$999',
    description: 'Dedicated Agent-as-a-Service Factory for your organization.',
    features: [
      'Custom DAG Orchestrator UI',
      'Isolated Docker Tenant Swarm',
      'Unlimited Data Ingestion',
      'Priority SLA & Support',
    ],
    featured: false,
    cta: 'Contact Sales',
  },
]

export default function PricingPage() {
  return (
    <div className="bg-white dark:bg-zinc-950 py-24 sm:py-32 flex-1">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto max-w-4xl text-center">
          <h2 className="text-base/7 font-semibold text-green-600 dark:text-green-400">Pricing</h2>
          <p className="mt-2 text-balance text-5xl font-semibold tracking-tight text-zinc-900 dark:text-white sm:text-6xl">
            Pricing that scales with your intelligence needs
          </p>
        </div>
        <p className="mx-auto mt-6 max-w-2xl text-pretty text-center text-lg font-medium text-zinc-600 dark:text-zinc-400 sm:text-xl/8">
          Choose an affordable plan that&apos;s packed with the best features for monitoring, integrating, and deploying autonomous agents.
        </p>
        <div className="isolate mx-auto mt-16 grid max-w-md grid-cols-1 gap-y-8 sm:mt-20 lg:mx-0 lg:max-w-none lg:grid-cols-3 lg:gap-x-8 lg:gap-y-0">
          {tiers.map((tier) => (
            <div
              key={tier.id}
              className={`rounded-3xl p-8 ring-1 ring-zinc-200 dark:ring-zinc-800 ${
                tier.featured ? 'bg-zinc-900 text-white ring-zinc-900 shadow-2xl dark:bg-zinc-800' : 'bg-white text-zinc-900 dark:bg-zinc-900 dark:text-zinc-300'
              } flex flex-col justify-between`}
            >
              <div>
                <h3
                  id={tier.id}
                  className={`text-lg/8 font-semibold ${
                    tier.featured ? 'text-white' : 'text-zinc-900 dark:text-white'
                  }`}
                >
                  {tier.name}
                </h3>
                <p className={`mt-4 text-sm/6 ${tier.featured ? 'text-zinc-300' : 'text-zinc-600 dark:text-zinc-400'}`}>
                  {tier.description}
                </p>
                <p className="mt-6 flex items-baseline gap-x-1">
                  <span
                    className={`text-4xl font-semibold tracking-tight ${
                      tier.featured ? 'text-white' : 'text-zinc-900 dark:text-white'
                    }`}
                  >
                    {tier.priceMonthly}
                  </span>
                  <span className={`text-sm/6 font-semibold ${tier.featured ? 'text-zinc-300' : 'text-zinc-600 dark:text-zinc-400'}`}>
                    /month
                  </span>
                </p>
                <ul
                  role="list"
                  className={`mt-8 space-y-3 text-sm/6 ${
                    tier.featured ? 'text-zinc-300' : 'text-zinc-600 dark:text-zinc-400'
                  }`}
                >
                  {tier.features.map((feature) => (
                    <li key={feature} className="flex gap-x-3">
                      <Check
                        aria-hidden="true"
                        className={`h-6 w-5 flex-none ${tier.featured ? 'text-green-400' : 'text-green-600 dark:text-green-500'}`}
                      />
                      {feature}
                    </li>
                  ))}
                </ul>
              </div>
              <a
                href={tier.href}
                aria-describedby={tier.id}
                className={`mt-8 block rounded-md px-3 py-2 text-center text-sm/6 font-semibold focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 ${
                  tier.featured
                    ? 'bg-green-500 text-white shadow-sm hover:bg-green-400 focus-visible:outline-green-500'
                    : 'text-green-600 ring-1 ring-inset ring-green-200 hover:ring-green-300 dark:text-green-400 dark:ring-green-800 dark:hover:ring-green-700'
                }`}
              >
                {tier.cta}
              </a>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
