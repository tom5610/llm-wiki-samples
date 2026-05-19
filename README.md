# Building Effective AI Agents — Wiki

A structured knowledge wiki distilling Anthropic's [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents) article into interlinked, scannable pages optimized for learning and reference.

## Overview

This project transforms a long-form technical article into a cross-referenced Obsidian wiki. The source material draws from Anthropic's experience with dozens of production agent deployments to provide practical guidance on building reliable agentic systems.

The wiki is organized around a **spectrum of agentic complexity**: from single augmented LLM calls, through predefined workflow patterns, to fully autonomous agents.

## Repository Structure

```
├── wiki/
│   ├── index.md              # Directory of all pages
│   ├── overview.md           # High-level framework
│   ├── log.md                # Ingestion changelog
│   ├── concepts/             # Foundational ideas
│   ├── techniques/           # Composable workflow patterns
│   └── synthesis/            # Meta-principles and guidance
├── raw/
│   ├── Building Effective AI Agents.md   # Original source
│   └── assets/                           # Diagrams and images
```

## Wiki Contents

### Concepts

| Page | Description |
|------|-------------|
| Agentic Systems | Taxonomy of LLM-based systems: workflows (predefined paths) vs. agents (dynamic control) |
| The Augmented LLM | The foundational building block: LLM + retrieval + tools + memory |
| Agent-Computer Interface (ACI) | Design principles for tool interfaces that agents interact with |

### Techniques

| Pattern | Key Idea |
|---------|----------|
| Prompt Chaining | Sequential LLM calls with programmatic gates between steps |
| Routing | Classify input and dispatch to specialized handlers |
| Parallelization | Simultaneous LLM calls (sectioning or voting) with aggregation |
| Orchestrator-Workers | Central LLM dynamically delegates to worker LLMs |
| Evaluator-Optimizer | Generator/evaluator feedback loop until acceptance |

### Synthesis

| Page | Description |
|------|-------------|
| Agent Design Principles | Three core principles: simplicity, transparency, careful ACI design |

## Usage

**As an Obsidian vault:** Open this directory in [Obsidian](https://obsidian.md/) to get full wikilink navigation, graph view, and backlinks across all 9 pages and 48 cross-references.

**As plain markdown:** Browse the `wiki/` directory directly — all pages are standard markdown with `[[wikilink]]` syntax for cross-references.

## Source

Based on [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents) by Anthropic (2024).
