---
title: Agent-Computer Interface (ACI)
type: concept
source: "raw/Building Effective AI Agents.md"
created: 2026-05-14
updated: 2026-05-20
---

# Agent-Computer Interface (ACI)

## Definition

The Agent-Computer Interface (ACI) is the design of tools, APIs, and interaction surfaces that agents use to accomplish tasks. It is the agent-facing analog of Human-Computer Interaction (HCI) — just as HCI invests heavily in making interfaces intuitive for humans, ACI requires equal investment in making tools intuitive for LLMs.

The core insight: tool design for agents deserves as much engineering effort as UI design for humans. In Anthropic's experience building SWE-bench agents, more time was spent optimizing tools than the overall prompt.

## Principles

1. **Empathize with the model** — Put yourself in the model's position. If a tool's usage isn't obvious from its description and parameters, it won't be obvious to the model either.
2. **Format for LLM strengths** — Choose output formats close to what models see in training data. Avoid formats requiring precise counting (line numbers in diffs) or heavy escaping (code inside JSON).
3. **Give thinking space** — Ensure the format gives the model enough tokens to reason before committing to outputs that constrain later generation.
4. **Poka-yoke (error-proofing)** — Design tool arguments so mistakes are structurally difficult. Example: requiring absolute file paths eliminates relative-path errors when the agent changes directories.
5. **Document like onboarding a junior developer** — Include example usage, edge cases, input format requirements, and clear boundaries from other similar tools.

## Implications

Practical tool format guidelines:
- Prefer whole-file rewrites over diffs (diffs require accurate chunk headers before writing new code)
- Prefer markdown code blocks over JSON-wrapped code (JSON requires escaping newlines and quotes)
- Use clear, descriptive parameter names — especially important when the agent has many similar tools
- Test extensively: run many example inputs to observe model mistakes, then iterate on tool design

The quality of the ACI is a force multiplier: a well-designed tool interface makes every workflow pattern and agent more reliable. Conversely, poor ACI design is a common root cause of agent failures that gets misattributed to model limitations.

## Evaluation-Driven Improvement

ACI quality can be systematically measured and improved through [[tool-evaluation|Tool Evaluation]]. Anthropic's internal data shows that iteratively optimizing tools with Claude Code against held-out test sets yields significant gains over both human-written and initial AI-generated implementations:

- Slack MCP server: 67.4% (human-written) → 80.1% (Claude-optimized)
- Asana MCP server: 79.6% (human-written) → 85.7% (Claude-optimized)

Key levers for ACI improvement include [[tool-selection|Tool Selection]] (choosing which tools to build), [[tool-namespacing|Tool Namespacing]] (naming for disambiguation), and [[tool-response-design|Tool Response Design]] (engineering what tools return). Prompt-engineering tool descriptions — making implicit context explicit, as one would when onboarding a new team member — is among the most effective single interventions. Even small refinements to descriptions yielded dramatic improvements on SWE-bench Verified.

## Relationships

ACI quality directly impacts the effectiveness of the [[augmented-llm|Augmented LLM]] building block. Every workflow pattern ([[prompt-chaining|Prompt Chaining]], [[routing|Routing]], [[parallelization|Parallelization]], [[orchestrator-workers|Orchestrator-Workers]], [[evaluator-optimizer|Evaluator-Optimizer]]) benefits from well-designed tool interfaces. ACI is one of the three [[agent-design-principles|Agent Design Principles]].

## See also

- [[augmented-llm|The Augmented LLM]]
- [[agentic-systems|Agentic Systems]]
- [[agent-design-principles|Agent Design Principles]]
- [[orchestrator-workers|Orchestrator-Workers]]
- [[evaluator-optimizer|Evaluator-Optimizer]]
- [[tool-evaluation|Tool Evaluation]]
- [[tool-selection|Tool Selection]]
- [[tool-namespacing|Tool Namespacing]]
- [[tool-response-design|Tool Response Design]]
- [[tool-taxonomy|Tool Taxonomy]]
