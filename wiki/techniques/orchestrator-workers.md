---
title: Orchestrator-Workers
type: technique
source: "raw/Building Effective AI Agents.md"
created: 2026-05-14
updated: 2026-05-19
---

# Orchestrator-Workers

## What it is

In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results. Unlike [[parallelization|Parallelization]] where subtasks are predefined, the orchestrator determines subtasks at runtime based on the specific input.

The architecture has an orchestrator LLM that analyzes the input, spawns worker LLM calls as needed (the number and nature are dynamic), then a synthesizer combines all worker outputs into the final result.

![Orchestrator-Workers workflow — Orchestrator dynamically delegates to worker LLM calls, Synthesizer combines results](../../raw/assets/8985fc683fae4780fb34eab1365ab78c7e51bc8e-2401x1000.webp)

## When to use

Use orchestrator-workers when:
- You cannot predict the subtasks needed in advance
- The number and nature of subtasks depend on the specific input
- The task is complex enough to benefit from delegation but too variable for fixed parallel paths
- You need flexible decomposition with centralized coordination

## How to implement

1. Design the orchestrator prompt to analyze inputs and produce a decomposition plan
2. Define the worker interface — what inputs workers accept and what outputs they return
3. Implement dynamic worker spawning based on the orchestrator's plan
4. Build a synthesizer that combines heterogeneous worker outputs into a coherent result
5. Include error handling for workers that fail or produce unexpected outputs

## Example

- **Coding products**: Making complex changes to multiple files — the orchestrator determines which files need changes and what kind of change each needs, then delegates to specialized workers
- **Multi-source research**: Gathering and analyzing information from multiple sources — the orchestrator identifies relevant sources and delegates extraction to workers

## Pitfalls

- The orchestrator's decomposition quality is the ceiling on output quality
- Higher latency than fixed [[parallelization|Parallelization]] due to the planning step
- Worker outputs may be inconsistent or contradictory, requiring robust synthesis logic
- More expensive: orchestrator + N workers + synthesizer = at minimum N+2 LLM calls

## Relationship to Multi-Agent Patterns

This technique describes dynamic decomposition within a workflow. When the workers become full agents (with their own tools, instructions, and state), the pattern evolves into multi-agent orchestration:
- The [[manager-pattern|Manager Pattern]] is closely related — it uses a central agent that delegates to specialized agents via tool calls. The distinction: orchestrator-workers emphasizes *dynamic task decomposition*, while the manager pattern emphasizes *pre-defined specialist selection*.
- The [[decentralized-pattern|Decentralized Pattern]] takes a different approach entirely — peer agents hand off execution without centralized control.

## See also

- [[agentic-systems|Agentic Systems]]
- [[augmented-llm|The Augmented LLM]]
- [[parallelization|Parallelization]]
- [[evaluator-optimizer|Evaluator-Optimizer]]
- [[prompt-chaining|Prompt Chaining]]
- [[agent-computer-interface|Agent-Computer Interface]]
- [[manager-pattern|Manager Pattern]]
- [[decentralized-pattern|Decentralized Pattern]]
