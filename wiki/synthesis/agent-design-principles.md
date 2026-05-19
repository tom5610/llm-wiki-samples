---
title: Agent Design Principles
type: synthesis
source: "raw/Building Effective AI Agents.md"
created: 2026-05-14
updated: 2026-05-14
---

# Agent Design Principles

This page synthesizes the three core principles Anthropic recommends for building effective AI agents, along with the broader philosophical stance on complexity that underpins them.

## The Simplicity Imperative

The overarching philosophy: success in the LLM space isn't about building the most sophisticated system — it's about building the *right* system for your needs. The recommended progression is:

1. Start with simple prompts
2. Optimize them with comprehensive evaluation
3. Add multi-step [[agentic-systems|agentic systems]] only when simpler solutions fall short

This is not mere conservatism. Agentic systems trade latency, cost, and debuggability for task performance. Each layer of complexity must demonstrably earn its place.

## Three Core Principles

### 1. Simplicity

Maintain simplicity in your agent's design. The most successful production implementations use simple, composable patterns rather than complex frameworks or specialized libraries. Many patterns can be implemented in a few lines of code using LLM APIs directly.

Implications:
- Prefer direct API usage over heavy frameworks
- If using a framework, understand what's under the hood (incorrect assumptions are a common error source)
- Don't add orchestration layers unless single-call approaches have been tried and measured

### 2. Transparency

Prioritize transparency by explicitly showing the agent's planning steps. Agents operate autonomously, which creates risk of compounding errors. Making the reasoning visible enables:

- Human oversight at checkpoints
- Debugging when things go wrong
- Trust-building with users who need to understand agent behavior
- Early termination when the agent goes off-track

The autonomous agent architecture shows this: agents can pause for human feedback at checkpoints or when encountering blockers.

![Autonomous agent loop — LLM Call cycles between Action and Feedback from Environment, with Human oversight and Stop conditions](../../raw/assets/58d9f10c985c4eb5d53798dea315f7bb5ab6249e-2401x1000.webp)

### 3. Careful ACI Design

Carefully craft your [[agent-computer-interface|Agent-Computer Interface]] through thorough tool documentation and testing. The interface between agent and tools is where most reliability issues originate. Invest in:

- Testing tool usage with many example inputs
- Iterating on tool descriptions and parameter design
- Error-proofing (poka-yoke) tool arguments
- Choosing formats that play to LLM strengths

![High-level coding agent flow — Human queries Interface, LLM clarifies task, searches files, writes code in test loop until passing](../../raw/assets/4b9a1f4eb63d5962a6e1746ac26bbc857cf3474f-2400x1666.webp)

## When Agents Are Appropriate

Agents suit open-ended problems where:
- The required number of steps is unpredictable
- You cannot hardcode a fixed path
- The LLM must operate for many turns
- You have sufficient trust in the model's decision-making
- The environment provides ground truth feedback at each step (tool results, test outcomes)

Two validated production domains:
- **Customer support** — Natural conversation flow + tool access + measurable success criteria
- **Coding agents** — Verifiable outputs (tests) + structured problem space + iterative feedback loops

## Guardrails

The autonomous nature of agents means higher costs and potential for compounding errors. Mitigations:
- Extensive testing in sandboxed environments
- Maximum iteration limits (stopping conditions)
- Human-in-the-loop checkpoints for high-stakes decisions
- Clear success criteria to know when to stop

## See also

- [[agentic-systems|Agentic Systems]]
- [[augmented-llm|The Augmented LLM]]
- [[agent-computer-interface|Agent-Computer Interface]]
- [[prompt-chaining|Prompt Chaining]]
- [[orchestrator-workers|Orchestrator-Workers]]
- [[evaluator-optimizer|Evaluator-Optimizer]]
