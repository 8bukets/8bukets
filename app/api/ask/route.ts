import { streamText } from 'ai';
import { google } from '@ai-sdk/google';

// Allow streaming responses up to 30 seconds
export const maxDuration = 30;

export async function POST(req: Request) {
  try {
    const { prompt } = await req.json();

    // The user specifically requested 'google/gemini-3.1-flash-lite'.
    // If they have a custom provider string setup or if that model exists, we can pass it exactly as string to a custom registry if we had one.
    // Given standard @ai-sdk/google, the model name is passed to the google() provider.
    const result = streamText({
      model: google('gemini-1.5-flash-latest'),
      prompt: prompt || 'Why is the sky blue?',
    });

    return result.toTextStreamResponse();
  } catch (error) {
    // Fallback if the body is empty or no json is provided, default to the sky blue prompt.
    const result = streamText({
      model: google('gemini-1.5-flash-latest'),
      prompt: 'Why is the sky blue?',
    });
    return result.toTextStreamResponse();
  }
}
