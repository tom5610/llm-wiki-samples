---
title: Tool Taxonomy
type: concept
source: "raw/A practical guide to building agents.md"
created: 2026-05-19
updated: 2026-05-19
---

# Tool Taxonomy

## Definition

The tool taxonomy is a three-way classification of capabilities that agents use to interact with external systems. Tools extend an agent beyond pure reasoning into the realm of action, giving it access to context, the ability to change state, and the means to coordinate with other agents.

## The Three Categories

| Type | Purpose | Examples |
|------|---------|----------|
| **Data tools** | Retrieve context and information needed for workflow execution | Query databases, read PDFs, search the web, access CRMs |
| **Action tools** | Interact with systems to make changes — add, update, or send | Send emails/texts, update CRM records, hand off tickets to humans |
| **Orchestration tools** | Agents themselves serving as tools for other agents | Refund agent, research agent, writing agent |

### Data Tools

Data tools provide the agent with the information it needs to make decisions. They are read-oriented and typically low-risk:
- Querying transaction databases
- Reading documents
- Searching knowledge bases
- Fetching user profiles from CRMs

### Action Tools

Action tools allow the agent to change state in external systems. They range in risk from low (sending a notification) to high (authorizing a payment):
- Sending communications (emails, messages)
- Updating records
- Creating new entries
- Triggering external workflows

### Orchestration Tools

In multi-agent systems, agents can serve as tools for other agents. This is the foundation of the [[manager-pattern|Manager Pattern]], where a central agent invokes specialized agents as callable functions.

## Principles

1. **Standardized definitions** — Each tool should have a consistent interface definition, enabling flexible many-to-many relationships between tools and agents.
2. **Well-documented** — Tool descriptions, parameter names, and return types should be clear enough for the LLM to select and use correctly.
3. **Thoroughly tested** — Tools should be tested independently to isolate failures from agent logic.
4. **Reusable** — Design tools for reuse across agents to improve discoverability, simplify version management, and prevent redundant definitions.
5. **Scale-aware** — As the number of required tools grows, consider splitting responsibilities across multiple agents rather than overloading a single agent with too many tools.

## Legacy System Access

For systems without APIs, agents can rely on computer-use models to interact directly through web and application UIs — just as a human would. This extends the tool concept beyond traditional API integrations to any interactive interface.

## Relationships

The tool taxonomy refines the [[augmented-llm|Augmented LLM]] concept by categorizing the "tools" component into distinct functional roles. It connects directly to [[agent-computer-interface|Agent-Computer Interface]] design, which governs how tools are documented and presented to agents. The orchestration category is the mechanism underlying both the [[manager-pattern|Manager Pattern]] and [[decentralized-pattern|Decentralized Pattern]].

## See also

- [[augmented-llm|The Augmented LLM]]
- [[agent-computer-interface|Agent-Computer Interface]]
- [[manager-pattern|Manager Pattern]]
- [[decentralized-pattern|Decentralized Pattern]]
- [[guardrails|Guardrails]]
