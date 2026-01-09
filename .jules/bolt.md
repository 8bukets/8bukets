# Bolt Journal

## 2026-01-09 - [Connection Pooling in Agent Systems]
**Learning:** Reusing `aiohttp.ClientSession` across multiple independent agents is critical for performance but requires careful lifecycle management. Implementing a "shared context" pattern where agents check for an existing session before creating a new one allows for connection pooling without breaking encapsulation or requiring major architectural refactors.
**Action:** When designing agent-based systems, inject a shared session/client in the context/config object passed to agents, rather than letting each agent manage its own transport layer.
