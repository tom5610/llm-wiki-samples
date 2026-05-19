---
title: Agent Use-Case Selection
type: technique
source: "raw/A practical guide to building agents.md"
created: 2026-05-19
updated: 2026-05-19
---

# Agent Use-Case Selection

## What it is

Agent use-case selection is the process of evaluating whether a workflow is a good candidate for agent-based automation. Not every task benefits from an agent — many workflows are better served by deterministic, rule-based solutions. This technique provides criteria to identify workflows where agents uniquely excel.

## When to use

Use this evaluation framework before committing resources to building an agent. It is especially relevant when:
- Evaluating new automation opportunities
- Deciding between traditional rule-based systems and agent-based approaches
- Prioritizing among multiple potential agent use cases
- Justifying agent investment to stakeholders

## How to implement

### Step 1: Identify candidate workflows

Look for workflows that have previously resisted automation — places where traditional deterministic and rule-based approaches encounter friction.

### Step 2: Evaluate against three criteria

A strong agent candidate exhibits one or more of:

1. **Complex decision-making** — The workflow involves nuanced judgment, exceptions, or context-sensitive decisions that defy simple rules. Example: refund approval in customer service, where each case involves unique circumstances.

2. **Difficult-to-maintain rules** — The existing rule system has become unwieldy, with extensive and intricate rulesets that make updates costly or error-prone. Example: vendor security reviews with hundreds of evolving compliance criteria.

3. **Heavy reliance on unstructured data** — The workflow requires interpreting natural language, extracting meaning from documents, or interacting conversationally. Example: processing home insurance claims from photos, descriptions, and policy documents.

### Step 3: Validate feasibility

Before building, confirm:
- The workflow has clear success criteria (how do you measure "done correctly"?)
- Appropriate [[guardrails|guardrails]] and [[human-intervention|human intervention]] mechanisms can be designed
- The cost-latency-performance tradeoff is acceptable for this use case
- Sufficient training data or examples exist to evaluate agent performance

### Step 4: Consider the alternative

If a workflow doesn't clearly meet the criteria, a deterministic solution likely suffices. The contrast is instructive:

| Approach | Strength | Limitation |
|----------|----------|-----------|
| Rules engine | Predictable, fast, auditable | Rigid; fails on nuance and edge cases |
| Agent | Handles ambiguity, adapts to context | Higher latency, cost, and complexity |

Example: A traditional rules engine for payment fraud works like a checklist, flagging transactions on preset criteria. An LLM agent functions like a seasoned investigator, evaluating context and identifying suspicious activity even when clear-cut rules aren't violated.

## Example

- **Payment fraud analysis** — Agents evaluate context and subtle patterns beyond what preset rules can capture
- **Customer service routing** — Agents understand intent from natural language rather than keyword matching
- **Document processing** — Agents extract structured data from varied, unstructured formats

## Pitfalls

- Building an agent when simple automation would suffice (over-engineering)
- Neglecting to define measurable success criteria before building
- Underestimating the operational overhead of agent monitoring and maintenance
- Assuming agents eliminate the need for human oversight entirely

## See also

- [[agentic-systems|Agentic Systems]]
- [[guardrails|Guardrails]]
- [[human-intervention|Human Intervention]]
- [[agent-design-principles|Agent Design Principles]]
