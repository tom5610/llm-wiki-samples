---
title: Wiki Log
type: log
created: 2026-05-14
updated: 2026-05-19
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

## [2026-05-19] ingest | A practical guide to building agents

Source: `raw/A practical guide to building agents.md`
Lens: base

**New pages:**
- `wiki/concepts/guardrails.md` — Layered defense mechanism: classifiers, PII filters, tool safeguards, rules-based protections
- `wiki/concepts/human-intervention.md` — Graceful escalation: failure thresholds and high-risk action triggers
- `wiki/concepts/tool-taxonomy.md` — Three-way tool classification: Data, Action, Orchestration
- `wiki/techniques/agent-use-case-selection.md` — Criteria for evaluating agent suitability
- `wiki/techniques/manager-pattern.md` — Central agent delegates to specialized agents via tool calls
- `wiki/techniques/decentralized-pattern.md` — Peer agents hand off execution to each other

**Updated pages:**
- `wiki/concepts/agentic-systems.md` — Added converging definitions section, incremental growth principle, multi-agent pattern references
- `wiki/techniques/orchestrator-workers.md` — Added relationship to multi-agent patterns section, cross-references
- `wiki/synthesis/agent-design-principles.md` — Expanded guardrails section with taxonomy, added human intervention and new pattern links

**Cross-references added:** 42 new wikilinks across 9 pages (6 new + 3 updated), bidirectional
