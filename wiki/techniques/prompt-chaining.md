---
title: Prompt Chaining
type: technique
source: "raw/Building Effective AI Agents.md"
created: 2026-05-14
updated: 2026-05-14
---

# Prompt Chaining

## What it is

Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. Programmatic checks ("gates") can be inserted between steps to verify intermediate outputs before proceeding.

The flow is linear: Input → LLM Call 1 → Gate (pass/fail) → LLM Call 2 → LLM Call 3 → Output. If a gate fails, the process exits early rather than propagating errors.

![Prompt chaining workflow — sequential LLM calls with a gate check between steps](../../raw/assets/7418719e3dab222dccb379b8879e1dc08ad34c78-2401x1000.webp)

## When to use

Use prompt chaining when:
- The task can be cleanly decomposed into fixed, sequential subtasks
- You want to trade latency for higher accuracy by making each individual LLM call simpler
- You need programmatic verification between steps

## How to implement

1. Identify natural decomposition boundaries in your task
2. Design each step as a focused, single-purpose LLM call
3. Define gate conditions between steps (format validation, content checks, safety filters)
4. Chain outputs → inputs through the sequence
5. Handle gate failures with early exits or fallback paths

## Example

- **Marketing copy pipeline**: Generate marketing copy → Translate into target language
- **Document authoring**: Write outline → Validate outline meets criteria → Write full document from outline

## Pitfalls

- Over-decomposition increases latency without proportional accuracy gains
- Gates that are too strict cause unnecessary failures; too lenient defeats their purpose
- Not suitable when subtask boundaries are unclear or task-dependent (use [[orchestrator-workers|Orchestrator-Workers]] instead)

## See also

- [[agentic-systems|Agentic Systems]]
- [[augmented-llm|The Augmented LLM]]
- [[routing|Routing]]
- [[evaluator-optimizer|Evaluator-Optimizer]]
- [[parallelization|Parallelization]]
