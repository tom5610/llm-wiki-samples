---
title: Agentic Systems
type: concept
source: "raw/Building Effective AI Agents.md"
created: 2026-05-14
updated: 2026-05-14
---

# Agentic Systems

## Definition

Agentic systems are applications built on large language models (LLMs) that go beyond single-call interactions to accomplish complex tasks through multi-step processes. Anthropic categorizes all such systems under the umbrella of "agentic systems" but draws an important architectural distinction between two sub-types:

- **Workflows**: Systems where LLMs and tools are orchestrated through predefined code paths. The control flow is determined by the developer at design time.
- **Agents**: Systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. The control flow is determined by the model at runtime.

## Principles

1. **Simplicity first** — Start with the simplest solution possible (often a single optimized LLM call with retrieval and in-context examples). Only increase complexity when it demonstrably improves outcomes.
2. **Appropriate complexity** — Workflows offer predictability and consistency for well-defined tasks; agents are better when flexibility and model-driven decision-making are needed at scale.
3. **Cost-performance tradeoff** — Agentic systems trade latency and cost for better task performance. This tradeoff must be consciously evaluated.

## Implications

The workflow-vs-agent distinction shapes architectural decisions:

- If you can enumerate and define all subtasks in advance → use a workflow pattern ([[prompt-chaining|Prompt Chaining]], [[routing|Routing]], [[parallelization|Parallelization]], [[orchestrator-workers|Orchestrator-Workers]], [[evaluator-optimizer|Evaluator-Optimizer]])
- If subtasks are unpredictable and require model-driven adaptation → use an autonomous agent with tool access and environment feedback
- If your task is well-served by a single call with good context → don't build an agentic system at all

## Relationships

The [[augmented-llm|Augmented LLM]] is the foundational building block from which all agentic systems compose. The five workflow patterns represent increasing levels of orchestration complexity. The [[agent-computer-interface|Agent-Computer Interface]] governs how agents interact with their tooling. [[agent-design-principles|Agent Design Principles]] capture the meta-guidelines for building reliable agentic systems.

## See also

- [[augmented-llm|The Augmented LLM]]
- [[prompt-chaining|Prompt Chaining]]
- [[routing|Routing]]
- [[parallelization|Parallelization]]
- [[orchestrator-workers|Orchestrator-Workers]]
- [[evaluator-optimizer|Evaluator-Optimizer]]
- [[agent-computer-interface|Agent-Computer Interface]]
- [[agent-design-principles|Agent Design Principles]]
