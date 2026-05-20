# Building Effective AI Agents — Tutorial Series

A hands-on tutorial series teaching intermediate developers how to build effective AI agents using Claude. Based on [Anthropic's production experience](https://www.anthropic.com/research/building-effective-agents) and the [Claude Cookbooks](https://github.com/anthropics/claude-cookbooks/tree/main/patterns/agents).

## Who This Is For

Developers who are familiar with LLM APIs (making calls, system prompts, structured output) and want to level up to building multi-step, production-grade agent systems.

## Prerequisites

- Python 3.9+
- `pip install anthropic`
- `ANTHROPIC_API_KEY` environment variable set
- Familiarity with Claude's Messages API

## The Complexity Spectrum

Not every application needs an agent. This series teaches you to pick the right level:

![The Augmented LLM — LLM with bidirectional connections to Retrieval, Tools, and Memory](assets/augmented_llm.webp)

```
Single LLM Call → Workflows → Autonomous Agents
(start here)     (5 patterns)   (when needed)
```

---

## Learning Path

### Phase 1: Conceptual Foundation

| Notebook | What You'll Learn |
|----------|-------------------|
| [00_foundations.ipynb](00_foundations.ipynb) | The mental model: augmented LLMs, workflows vs. agents, decision framework, ACI principles, design principles |

### Phase 2: Workflow Patterns (Simple → Complex)

| Notebook | Pattern | Key Idea |
|----------|---------|----------|
| [01_prompt_chaining.ipynb](01_prompt_chaining.ipynb) | Prompt Chaining | Sequential steps with quality gates |
| [02_routing.ipynb](02_routing.ipynb) | Routing | Classify input, dispatch to specialist |
| [03_parallelization.ipynb](03_parallelization.ipynb) | Parallelization | Fan-out for speed and confidence |

### Phase 3: Advanced Workflows

| Notebook | Pattern | Key Idea |
|----------|---------|----------|
| [04_orchestrator_workers.ipynb](04_orchestrator_workers.ipynb) | Orchestrator-Workers | Dynamic task decomposition at runtime |
| [05_evaluator_optimizer.ipynb](05_evaluator_optimizer.ipynb) | Evaluator-Optimizer | Iterative refinement through feedback loops |

### Phase 4: Full Agents

| Notebook | What You'll Build |
|----------|-------------------|
| [06_autonomous_agents.ipynb](06_autonomous_agents.ipynb) | Complete agent loop with tools, guardrails, and production patterns |

---

## Pattern Decision Framework

Use this to pick the right pattern for your task:

| Your Situation | Pattern | Why |
|---------------|---------|-----|
| Task has fixed sequential steps | **Prompt Chaining** | Linear pipeline with verification gates |
| Inputs fall into distinct categories | **Routing** | Classify once, optimize each path |
| Subtasks are independent, speed matters | **Parallelization** | N calls in parallel, aggregate results |
| Can't predict subtasks until you see input | **Orchestrator-Workers** | LLM decides decomposition at runtime |
| Output quality improves with iteration | **Evaluator-Optimizer** | Generate → critique → refine loop |
| Open-ended problem, unpredictable steps | **Autonomous Agent** | LLM + tools + loop until done |

### The Decision Tree

```
Does a single LLM call handle it?
├── YES → Stop. Use a single call.
└── NO → Can you predefine the steps?
    ├── YES → Is it sequential? → Prompt Chaining
    │         Independent? → Parallelization
    │         Different handlers per input type? → Routing
    │         Need iterative improvement? → Evaluator-Optimizer
    └── NO → Need dynamic decomposition? → Orchestrator-Workers
             Need full autonomy? → Autonomous Agent
```

---

## Three Core Principles

From Anthropic's production experience:

1. **Simplicity** — Start with the simplest approach. Only add complexity when measured results justify it.
2. **Transparency** — Show the agent's reasoning at every step. Enable human oversight and debugging.
3. **Careful ACI Design** — Invest in tool interfaces (names, descriptions, error-proofing) as much as prompt engineering.

---

## Shared Utilities

All notebooks import from [util.py](util.py):

- `llm_call(prompt, system_prompt, model)` — Standardized Claude API call
- `extract_xml(text, tag)` — Parse XML-tagged responses from Claude

---

## Architecture Diagrams

The `assets/` folder contains architecture diagrams for each pattern:

| Diagram | Used In |
|---------|---------|
| [augmented_llm.webp](assets/augmented_llm.webp) | Foundations |
| [prompt_chaining.webp](assets/prompt_chaining.webp) | Prompt Chaining |
| [routing.webp](assets/routing.webp) | Routing |
| [parallelization.webp](assets/parallelization.webp) | Parallelization |
| [orchestrator_workers.webp](assets/orchestrator_workers.webp) | Orchestrator-Workers |
| [evaluator_optimizer.webp](assets/evaluator_optimizer.webp) | Evaluator-Optimizer |
| [autonomous_agent_loop.webp](assets/autonomous_agent_loop.webp) | Autonomous Agents |
| [coding_agent_flow.webp](assets/coding_agent_flow.webp) | Autonomous Agents |

---

## Further Reading

- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) — Anthropic's research paper (source material for this tutorial)
- [Claude Cookbooks: Agent Patterns](https://github.com/anthropics/claude-cookbooks/tree/main/patterns/agents) — Original code examples
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) — Standardized tool integration
- [Anthropic API Documentation](https://docs.anthropic.com/) — Claude API reference

---

*This tutorial series was created by synthesizing Anthropic's "Building Effective Agents" research with runnable code from the Claude Cookbooks.*
