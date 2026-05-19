---
title: Wiki Log
type: log
created: 2026-05-14
updated: 2026-05-20
---

# Wiki Log

## [2026-05-14] init | Wiki bootstrapped via first ingest

Created directory structure and initial files.

## [2026-05-14] ingest | Building Effective AI Agents

Source: `raw/Building Effective AI Agents.md`
Lens: base

**New pages:**
- `wiki/concepts/agentic-systems.md` — Core taxonomy: workflows vs. agents under the agentic systems umbrella
- `wiki/concepts/augmented-llm.md` — The foundational building block: LLM + retrieval + tools + memory
- `wiki/concepts/agent-computer-interface.md` — Design principles for agent-facing tool interfaces (ACI)
- `wiki/techniques/prompt-chaining.md` — Sequential LLM calls with programmatic gates
- `wiki/techniques/routing.md` — Input classification and dispatch to specialized handlers
- `wiki/techniques/parallelization.md` — Simultaneous execution via sectioning or voting
- `wiki/techniques/orchestrator-workers.md` — Dynamic task delegation with centralized coordination
- `wiki/techniques/evaluator-optimizer.md` — Generator/evaluator feedback loop
- `wiki/synthesis/agent-design-principles.md` — Three core principles: simplicity, transparency, ACI design

**Updated pages:** None (first ingest)

**Cross-references added:** 48 wikilinks across all 9 pages, bidirectional

## [2026-05-20] ingest | Writing Effective Tools for AI Agents—Using AI Agents

Source: `raw/Writing effective tools for AI agents—using AI agents.md`
Lens: base

**New pages:**
- `wiki/techniques/tool-evaluation.md` — Evaluation-driven development loop: prototype, generate tasks, run evals, analyze with agents, iterate
- `wiki/techniques/tool-response-design.md` — Engineering tool responses for effectiveness: format enums, token efficiency, pagination, error messages
- `wiki/concepts/tool-namespacing.md` — How naming conventions (prefix/suffix patterns) help agents disambiguate between many tools
- `wiki/concepts/tool-selection.md` — Choosing which tools to build: affordance mismatch, consolidation, curation over coverage

**Updated pages:**
- `wiki/concepts/agent-computer-interface.md` — Added evaluation-driven improvement section with empirical data (Slack/Asana benchmarks); added cross-references to new pages

**Cross-references added:** 32 wikilinks across new and updated pages, bidirectional
