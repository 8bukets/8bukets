import { NextRequest, NextResponse } from 'next/server'
import Stripe from 'stripe'

// In a real environment, you must set STRIPE_SECRET_KEY in your .env
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY || 'sk_test_mock', {
  apiVersion: '2026-04-22.dahlia', // Latest stable Stripe API version (per type definitions in installed version)
})

export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams
  const priceId = searchParams.get('price')

  if (!priceId) {
    return NextResponse.json({ error: 'Price ID is required' }, { status: 400 })
  }

  try {
    const baseUrl = process.env.NEXT_PUBLIC_SITE_URL || request.nextUrl.origin

    // Create Checkout Sessions from body params.
    const session = await stripe.checkout.sessions.create({
      line_items: [
        {
          // Provide the exact Price ID (for example, pr_1234) of the product you want to sell
          price: priceId,
          quantity: 1,
        },
      ],
      mode: 'subscription',
      success_url: `${baseUrl}/?success=true&session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${baseUrl}/pricing?canceled=true`,
    })

    if (session.url) {
      return NextResponse.redirect(session.url, 303)
    } else {
       return NextResponse.json({ error: 'Failed to create checkout session' }, { status: 500 })
    }
  } catch (err: unknown) {
    console.error('Stripe error:', err)
    // If we're using a mock key, just redirect to success to simulate it for now
    if (process.env.STRIPE_SECRET_KEY === undefined) {
         const baseUrl = process.env.NEXT_PUBLIC_SITE_URL || request.nextUrl.origin
         return NextResponse.redirect(`${baseUrl}/?success=true&mock=true`, 303)
    }

    if (err instanceof Error) {
        // Stripe errors typically carry a statusCode property.
        const statusCode = (err as unknown as { statusCode?: number }).statusCode || 500;
        return NextResponse.json(
        { error: err.message },
        { status: statusCode }
        )
    }

    return NextResponse.json({ error: 'Unknown error occurred' }, { status: 500 })
  }
}
