---
title: Human Intervention
type: concept
source: "raw/A practical guide to building agents.md"
created: 2026-05-19
updated: 2026-05-19
---

# Human Intervention

## Definition

Human intervention is a critical safeguard mechanism that allows an agent to gracefully transfer control to a human operator when it cannot or should not continue autonomously. It bridges the gap between full automation and manual oversight, ensuring user experience is preserved even when the agent reaches its limits.

Human intervention is especially important early in deployment, where it helps identify failures, uncover edge cases, and establish a robust evaluation cycle that improves agent performance over time.

## Principles

1. **Graceful degradation** — Agents should transfer control smoothly rather than failing silently or producing poor outputs. The transition to human handling should feel natural to the end user.
2. **Threshold-driven escalation** — Define explicit, measurable triggers rather than relying on vague "when appropriate" criteria.
3. **Domain-appropriate handoff** — The form of human intervention varies by context: escalating to a human agent in customer service, handing control back to the developer in coding assistants, requesting approval in financial workflows.
4. **Confidence-building** — Start with broader human intervention early in deployment, then narrow triggers as confidence in the agent grows.

## Escalation Triggers

Two primary categories warrant human intervention:

### Exceeding Failure Thresholds

Set limits on agent retries or actions. When the agent exceeds these limits, escalate immediately:
- Fails to understand customer intent after multiple attempts
- Repeated tool call failures
- Circular reasoning or repetitive outputs
- Maximum iteration count reached without progress

### High-Risk Actions

Actions that are sensitive, irreversible, or have high stakes should trigger human oversight until confidence in the agent's reliability grows:
- Canceling user orders
- Authorizing large refunds
- Making payments or financial transfers
- Modifying access permissions
- Actions with legal or compliance implications

## Implications

Human intervention design affects overall system architecture:
- Agents must maintain enough conversational state to provide context when handing off
- The system needs routing infrastructure to connect to human operators
- Monitoring and alerting must detect when escalation thresholds are approached
- Post-escalation analysis feeds back into improving agent instructions and [[guardrails|guardrails]]

## Relationships

Human intervention complements [[guardrails|Guardrails]] — guardrails detect and prevent issues automatically, while human intervention handles cases that exceed automated safety boundaries. The [[agent-design-principles|Agent Design Principles]] identify human-in-the-loop checkpoints as a key mitigation for the autonomous nature of agents. The [[agent-use-case-selection|Agent Use-Case Selection]] technique considers human intervention requirements as part of evaluating agent suitability.

## See also

- [[guardrails|Guardrails]]
- [[agent-design-principles|Agent Design Principles]]
- [[agentic-systems|Agentic Systems]]
- [[agent-use-case-selection|Agent Use-Case Selection]]
