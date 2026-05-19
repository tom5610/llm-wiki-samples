---
title: Wiki Index
type: index
created: 2026-05-14
updated: 2026-05-20
---

# Wiki Index

## Entities

## Concepts

### Foundational

- [[agentic-systems|Agentic Systems]] — Taxonomy of LLM-based systems: workflows (predefined paths) vs. agents (dynamic control)
- [[augmented-llm|The Augmented LLM]] — The building block: LLM + retrieval + tools + memory

### Derived

- [[agent-computer-interface|Agent-Computer Interface (ACI)]] — Design principles for tool interfaces that agents interact with
- [[guardrails|Guardrails]] — Layered defense mechanism: classifiers, filters, tool safeguards, and rules-based protections
- [[human-intervention|Human Intervention]] — When and how to transfer control to human operators
- [[tool-taxonomy|Tool Taxonomy]] — Three-way tool classification: Data, Action, Orchestration
- [[tool-selection|Tool Selection]] — Choosing which tools to build: affordances, consolidation, deliberate curation over coverage
- [[tool-namespacing|Tool Namespacing]] — Naming conventions that help agents disambiguate between many tools

## Techniques

- [[prompt-chaining|Prompt Chaining]] — Sequential LLM calls with programmatic gates between steps
- [[routing|Routing]] — Classify input and dispatch to specialized handlers
- [[parallelization|Parallelization]] — Simultaneous LLM calls (sectioning or voting) with aggregation
- [[orchestrator-workers|Orchestrator-Workers]] — Central LLM dynamically delegates to worker LLMs
- [[evaluator-optimizer|Evaluator-Optimizer]] — Generator/evaluator feedback loop until acceptance
- [[agent-use-case-selection|Agent Use-Case Selection]] — Criteria for evaluating agent suitability: complex decisions, brittle rules, unstructured data
- [[manager-pattern|Manager Pattern]] — Central agent delegates to specialized agents via tool calls
- [[decentralized-pattern|Decentralized Pattern]] — Peer agents hand off execution to each other
- [[tool-evaluation|Tool Evaluation]] — Evaluation-driven development loop for measuring and improving agent tool use
- [[tool-response-design|Tool Response Design]] — Engineering tool responses for token efficiency and agent effectiveness

## Synthesis & Comparisons

- [[agent-design-principles|Agent Design Principles]] — Three core principles: simplicity, transparency, careful ACI design
