export type EventType =
  | 'h' // Handshake / Metadata
  | 'r' // Reasoning / Thought process tokens
  | 'a' // Agent response tokens (User-facing)
  | 'c' // Tool Call initialization
  | 'i' // Tool Invoke payload/arguments delta
  | 'e' // Error envelope
  | 'x';// Execution control (EOF, termination)

export interface FastAgentFrame {
  i: string;          // Interaction ID (UUID / compact base64 hash)
  s: number;          // Sequence number (for ordering validation over UDP/WebSockets)
  t: EventType;       // Event type flag (1 byte for rapid switch/case routing)
  d: string | object; // Delta payload (string token or partial JSON object)
  ts: number;         // Unix timestamp in milliseconds for latency tracking
  m?: {               // Optional ephemeral metadata (only sent in 'h' or 'x' frames)
    ttft?: number;    // Time to first token
    tokens?: number;  // Token counts
    model?: string;   // Model routing info
  };
}
