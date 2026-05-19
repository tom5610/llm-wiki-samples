---
title: Tool Selection
type: concept
source: "raw/Writing effective tools for AI agents—using AI agents.md"
created: 2026-05-20
updated: 2026-05-20
---

# Tool Selection

## Definition

Tool selection is the principle that more tools don't always lead to better outcomes. Effective tool sets are deliberately chosen to match agent affordances — the distinct ways agents perceive and act on available tools — rather than simply wrapping existing API endpoints. The guiding heuristic: build a few thoughtful tools targeting specific high-impact workflows, then scale up from there.

## Principles

### Affordance mismatch

Agents have fundamentally different affordances than traditional software:

| Agent constraint | Traditional software |
|------------------|---------------------|
| Limited context window | Cheap, abundant memory |
| Sequential token-by-token processing | Efficient iteration over collections |
| Strong at targeted retrieval | Strong at brute-force search |
| Natural language reasoning | Programmatic logic |

A tool that returns ALL contacts for brute-force search may work for traditional software but wastes an agent's limited context. The agent equivalent is `search_contacts` (targeted retrieval) rather than `list_contacts` (brute force).

### Consolidation over thin wrappers

Tools should consolidate multi-step workflows rather than mirror API endpoints one-to-one:

| Instead of | Build |
|------------|-------|
| `list_users` + `list_events` + `create_event` | `schedule_event` (finds availability and schedules) |
| `read_logs` | `search_logs` (returns relevant lines + context) |
| `get_customer_by_id` + `list_transactions` + `list_notes` | `get_customer_context` (compiles all relevant info) |

This reduces both the number of tool calls (fewer round-trips) and the intermediate context consumed (less irrelevant data in the agent's window).

### Distinct purpose

Each tool must have a clear, distinct purpose. Tools should enable agents to subdivide and solve tasks in much the same way a human would, given access to the same underlying resources.

### Fewer is often better

Too many tools or overlapping tools distract agents from efficient strategies. Each additional tool:
- Increases the description text loaded into context
- Creates more selection ambiguity
- Raises the probability of calling the wrong tool
- Reduces the cognitive budget available for reasoning

## Implications

The concept of tool selection reframes tool design as a *curation* problem rather than a *coverage* problem. The question isn't "what can we expose?" but "what should we expose given how agents think?"

Tools designed with agent affordances in mind tend to also be surprisingly intuitive for humans — suggesting that good ACI and good HCI converge at a deeper level.

## Relationships

Tool selection is a design-time complement to [[tool-namespacing|Tool Namespacing]] (which helps at runtime). Both serve the [[agent-computer-interface|Agent-Computer Interface]] goal of making tools intuitive for agents. Selection decisions directly impact what gets measured in [[tool-evaluation|Tool Evaluation]], and the [[tool-taxonomy|Tool Taxonomy]] (Data/Action/Orchestration) provides the categorization framework within which selection operates.

## See also

- [[agent-computer-interface|Agent-Computer Interface (ACI)]]
- [[tool-taxonomy|Tool Taxonomy]]
- [[tool-namespacing|Tool Namespacing]]
- [[tool-evaluation|Tool Evaluation]]
- [[tool-response-design|Tool Response Design]]
- [[augmented-llm|The Augmented LLM]]
