---
title: Wiki Overview
type: overview
created: 2026-05-14
updated: 2026-05-19
---

# Wiki Overview

This wiki captures knowledge about building effective AI agents, drawn primarily from Anthropic's experience working with production deployments across industries.

## Core Framework

The central organizing idea is a **spectrum of agentic complexity**:

1. **Single LLM call** (with retrieval + in-context examples) — sufficient for most applications
2. **Workflows** — predefined orchestration patterns for well-defined tasks
3. **Agents** — autonomous, model-directed systems for open-ended problems

The foundational building block for all of these is the **Augmented LLM**: an LLM enhanced with retrieval, tools, and memory.

## Workflow Patterns

Five composable patterns cover the production workflow design space:

| Pattern | Key Idea | Use When |
|---------|----------|----------|
| Prompt Chaining | Sequential steps with gates | Task decomposes cleanly into fixed subtasks |
| Routing | Classify and dispatch | Distinct categories need different handling |
| Parallelization | Fan-out + aggregate | Independent subtasks or multiple perspectives needed |
| Orchestrator-Workers | Dynamic delegation | Can't predict subtasks in advance |
| Evaluator-Optimizer | Generate + critique loop | Clear criteria and iterative refinement adds value |

## Multi-Agent Orchestration

When a single agent isn't enough, two patterns emerge for coordinating multiple agents:

| Pattern | Topology | Control | Best For |
|---------|----------|---------|----------|
| Manager | Hub-and-spoke | Central manager delegates via tool calls | Synthesizing multi-specialist outputs |
| Decentralized | Peer-to-peer | Agents hand off execution to each other | Triage and domain routing |

The choice depends on whether you need centralized synthesis (manager) or clean domain handoffs (decentralized).

## Safety & Reliability

Two complementary systems keep agents operating within bounds:

- **Guardrails** — Layered automated defenses (relevance classifiers, safety classifiers, PII filters, moderation, tool safeguards, rules-based protections, output validation) that run concurrently with agent execution.
- **Human Intervention** — Graceful escalation when agents exceed failure thresholds or encounter high-risk actions requiring human judgment.

## Design Philosophy

Three principles guide agent construction: **simplicity** (start minimal, earn complexity), **transparency** (show planning steps), and **careful ACI design** (invest in tool interfaces as much as HCI). The Agent-Computer Interface concept — treating tool design with the same rigor as UI design — is a distinctive contribution of this framework.

## Tool Design

Agents interact with external systems through three categories of tools: **Data** (retrieving context), **Action** (changing state), and **Orchestration** (agents serving as tools for other agents). Well-documented, thoroughly tested, reusable tools with standardized definitions are the foundation of reliable agent behavior.
