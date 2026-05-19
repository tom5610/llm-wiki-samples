---
title: Routing
type: technique
source: "raw/Building Effective AI Agents.md"
created: 2026-05-14
updated: 2026-05-14
---

# Routing

## What it is

Routing classifies an input and directs it to a specialized follow-up task. This enables separation of concerns — each downstream path can have an optimized prompt, model, or toolset without compromising performance on other input types.

The architecture uses a router LLM that categorizes the input, then dispatches to one of several specialized LLM calls. Only one path executes per input.

![Routing workflow — LLM Call Router dispatches to one of several specialized LLM paths](../../raw/assets/5c0c0e9fe4def0b584c04d37849941da55e5e71c-2401x1000.webp)

## When to use

Use routing when:
- There are distinct categories of input that benefit from different handling
- Classification can be handled accurately (by LLM or traditional classifier)
- Optimizing prompts for one category would hurt performance on another

## How to implement

1. Define your input categories and their distinguishing characteristics
2. Build a classifier (LLM-based or traditional ML) that reliably categorizes inputs
3. Design specialized downstream handlers for each category
4. Route classified inputs to the appropriate handler
5. Optionally include a fallback path for unclassifiable inputs

## Example

- **Customer service**: Route general questions, refund requests, and technical support into different processes with specialized prompts and tools
- **Model selection**: Route easy/common questions to smaller cost-efficient models (e.g., Claude Haiku) and hard/unusual questions to more capable models (e.g., Claude Sonnet)

## Pitfalls

- Classification errors cascade — a misrouted input gets inappropriate handling with no recovery
- Too many routes increase classification difficulty and maintenance burden
- Not appropriate when inputs don't fall into discrete categories (use [[prompt-chaining|Prompt Chaining]] or direct processing instead)

## See also

- [[agentic-systems|Agentic Systems]]
- [[augmented-llm|The Augmented LLM]]
- [[prompt-chaining|Prompt Chaining]]
- [[parallelization|Parallelization]]
- [[orchestrator-workers|Orchestrator-Workers]]
