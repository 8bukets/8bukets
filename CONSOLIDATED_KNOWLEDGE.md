# Consolidated Knowledge Base

**Last Sync (Python):** 2026-06-13T20:45:00Z

## 🤖 AI Agents Knowledge (Latest)
See `data/knowledge/ai_agents_knowledge.md` for full details on Google AI Agents.

**System Version:** 1

## 🧩 Strategic Identity & Unified Model
# Glossary

## Compile

To compile means to gather information from various sources and arrange it into a structured format, such as a report, list, book, or file. In computing, it refers to translating human-readable source code into machine-readable, executable instructions.

### Key Definitions of Compile

- **Gathering Information**: To collect and put together data, facts, or documents (e.g., to compile a report or compile a list).
- **Creating Works**: To produce a book, anthology, or database from various materials.
- **Computing**: To convert high-level programming code (like C++ or Java) into machine code, allowing a computer to execute the program.

## LLM Architecture & Strategy (Ingested 2026-06-16T13:06:27.517Z)

### Core Architecture: The Transformer
- **Mechanism**: Self-Attention (Scaled Dot-Product).
- **Equation**: Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V.
- **Trend**: Hybrid Architectures (Transformer + Mamba/SSM) are emerging for better efficiency.

### Processing & Tokenization
- **Mapping**: Vocabulary IDs mapped to high-dimensional embeddings.
- **Optimization**: Vocabulary pruning and dynamic embedding resizing to reduce memory footprint.

### Training & Alignment
- **Pre-training**: Unsupervised next-token prediction on terabytes of raw data.
- **Alignment**: SFT (Supervised Fine-Tuning) and RLHF (Reinforcement Learning from Human Feedback).
- **Emerging**: DPO (Direct Preference Optimization) as a simpler alternative to RLHF.

### Agentic Workflows & Frontiers
- **Context Window**: Expanding towards 10M+ tokens using FlashAttention and RoPE.
- **Agentic AI**: Moving from single-turn chat to multi-step reasoning, tool use, and self-correction.
- **Reasoning Models**: Implementation of chain-of-thought (CoT) and search-based reasoning (e.g., Gemini 2.0 Thinking).

### Strategic Insights
- **Cost vs Performance**: Tiered model selection (Premium vs Standard vs Budget) based on task complexity.
- **Smaller, Smarter**: The shift towards high-performance small models (1B-7B) matching previous generation large models.
