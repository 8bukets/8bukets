'use client';

import { useCompletion } from '@ai-sdk/react';

export default function AskPage() {
  const { completion, input, handleInputChange, handleSubmit, isLoading } = useCompletion({
    api: '/api/ask',
    initialInput: 'Why is the sky blue?'
  });

  return (
    <div className="flex flex-col w-full max-w-md py-24 mx-auto stretch">
      <h1 className="text-2xl font-bold mb-4">Ask Gemini</h1>

      <div className="whitespace-pre-wrap my-6 border p-4 rounded bg-gray-50 min-h-32 text-black">
        {completion || "Awaiting response..."}
      </div>

      <form onSubmit={handleSubmit} className="flex gap-2">
        <input
          className="fixed bottom-0 w-full max-w-md p-2 mb-8 border border-gray-300 rounded shadow-xl text-black"
          value={input}
          placeholder="Ask a question..."
          onChange={handleInputChange}
          disabled={isLoading}
        />
      </form>
    </div>
  );
}
