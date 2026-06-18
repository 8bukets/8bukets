# Agent Architecture Blueprint

## 1. Agent - Behavior Logic (Logika ponašanja)
The "brain workflow" where the agent decides:
* What to do
* In what order
* Whether to use a tool
* Whether to iterate
* Whether to fix an error

## 2. Harness - Execution/Runtime Layer
The "operating environment" that:
* Calls tools
* Executes commands
* Manages memory
* Provides context to the model
* Controls the loop
* Manages retries
* Sandboxes the system
* Tracks task state

## 3. Tooling Layer
Concrete capability adapters with deep integration to:
* Terminal
* Git
* File system
* Test runners
* Package managers
* Editors
* Shell

## 4. Context Engineering
The "secret sauce" where the system decides:
* Which files to load
* What to summarize
* What to discard
* How to package the repo
* How to compress history
* What to show to the model
This layer determines whether "AI understands the project" or "AI is lost".

## 5. Prompt Orchestration
Multi-layered prompt systems including:
* System prompts
* Hidden chain structures
* Task decomposition prompts
* Reflection prompts
* Self-check prompts

## 6. Autonomy Loop
The core execution cycle that heavily determines agent quality:
* Analyze -> Make change -> Run -> See error -> Fix -> Retry -> Validate -> Continue

## 7. Repo Indexing / Retrieval System
Sophisticated system to determine what to open vs. ignore:
* Semantic search
* Dependency graph
* File relevance ranking
* Retrieval pipeline

## 8. Diff / Edit Engine
Crucial engine for safely modifying code (generating code != safely editing existing repo):
* Patching mechanisms
* Diff merging
* Corruption avoidance
* Formatting preservation
* Partial edits

## 9. Verification Layer
Crucial for preventing "confident hallucinations". System checks if:
* Build passes
* Tests pass
* Lint passes
* Runtime errors exist

## 10. Memory System
Allows long-term operation without context loss:
* Session memory
* Task memory
* Repo memory
* Preference memory

## 11. Safety / Permission System
Essential for autonomous agents. Decides:
* What the agent is allowed to execute
* When it must ask the user
* What is dangerous
* What is read-only

## 12. UX Layer
Determines perception of quality. A good UX ensures:
* Output looks meaningful
* Agent explains its actions
* Flow feels natural
* Terminal UX is well-designed

## Summary of Layers
* Model
* Agent Logic
* Harness/Runtime
* Tooling
* Context System
* Retrieval Engine
* Prompting Architecture
* Autonomy Engine
* Verification System
* Memory
* Permissions
* UX
