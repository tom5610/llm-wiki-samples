---
title: The Augmented LLM
type: concept
source: "raw/Building Effective AI Agents.md"
created: 2026-05-14
updated: 2026-05-19
---

# The Augmented LLM

## Definition

The augmented LLM is the foundational building block of all agentic systems. It is an LLM enhanced with three key augmentations:

- **Retrieval** — The model generates its own search queries to access external knowledge (RAG, vector databases, document search).
- **Tools** — The model selects and invokes appropriate tools via structured API calls (calculators, code execution, external services).
- **Memory** — The model determines what information to retain across interactions (conversation history, working state, long-term knowledge).

The diagram below shows this architecture: input flows into the LLM, which bidirectionally interacts with retrieval (query/results), tools (call/response), and memory (read/write) before producing output.

![The Augmented LLM — LLM with bidirectional connections to Retrieval, Tools, and Memory](../../raw/assets/d3083d3f40bb2b6f477901cc9a240738d3dd1371-2401x1000.webp)

## Principles

1. **Tailor capabilities to your use case** — Don't add all augmentations by default. Choose the retrieval sources, tools, and memory mechanisms that fit the specific task.
2. **Provide clear interfaces** — Each augmentation should have an easy, well-documented interface for the LLM to use. Poor tool documentation degrades model performance.
3. **Composability** — Every LLM call in a workflow or agent pattern is itself an augmented LLM. The building block is recursive.

## Implications

The Model Context Protocol (MCP) is Anthropic's recommended approach for tool integration, providing a standardized client implementation that connects to a growing ecosystem of third-party tools. This means teams don't need to build custom tool integrations from scratch.

Modern LLMs can actively use these capabilities — they are not passive recipients of context, but active participants that generate queries, select tools, and manage their own memory.

## Relationships

The augmented LLM is the atomic unit that composes into all [[agentic-systems|Agentic Systems]]. Each node in workflow diagrams ([[prompt-chaining|Prompt Chaining]], [[routing|Routing]], etc.) represents one augmented LLM call. The quality of the [[agent-computer-interface|Agent-Computer Interface]] directly determines how effectively the LLM can use its tools.

## See also

- [[agentic-systems|Agentic Systems]]
- [[agent-computer-interface|Agent-Computer Interface]]
- [[tool-taxonomy|Tool Taxonomy]]
- [[prompt-chaining|Prompt Chaining]]
- [[routing|Routing]]
- [[parallelization|Parallelization]]
- [[orchestrator-workers|Orchestrator-Workers]]
- [[evaluator-optimizer|Evaluator-Optimizer]]
