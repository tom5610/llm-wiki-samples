---
title: Tool Namespacing
type: concept
source: "raw/Writing effective tools for AI agents—using AI agents.md"
created: 2026-05-20
updated: 2026-05-20
---

# Tool Namespacing

## Definition

Tool namespacing is the practice of grouping related tools under common naming prefixes or suffixes to help agents delineate boundaries between tools. As agents gain access to dozens of MCP servers and potentially hundreds of tools, namespacing becomes critical for reducing confusion about which tools to use for which tasks.

## Principles

1. **Delineate by service** — Group tools by the system they interact with (e.g., `asana_search`, `jira_search`, `slack_search`).
2. **Delineate by resource** — Within a service, further subdivide by resource type (e.g., `asana_projects_search`, `asana_users_search`).
3. **Prefix vs. suffix matters** — The choice between prefix-based (`asana_search`) and suffix-based (`search_asana`) naming has measurable, non-trivial effects on tool-use evaluation performance. Effects vary by LLM.
4. **Reduce overlap** — When tools overlap in function or have vague purposes, agents get confused about which to use. Clear naming eliminates ambiguity.
5. **Reflect task subdivisions** — Tool names should reflect natural subdivisions of tasks, simultaneously reducing the total tool count and offloading computation from agent context into tool calls.

## Implications

Namespacing interacts with several agent failure modes:

- **Calling the wrong tool** — Clear namespaces help agents distinguish between similar tools across services
- **Wrong parameters** — Service-prefixed tools carry implicit context about expected parameter types
- **Too few tool calls** — Well-named tools make multi-step workflows more obvious
- **Incorrect response processing** — Namespace conventions set expectations about return formats

MCP clients sometimes apply namespacing automatically (e.g., prepending the server name), which provides a baseline level of disambiguation. However, deliberate naming within a server's own tool set still matters.

The optimal naming scheme is empirically determined — there is no universal best practice. The recommendation is to evaluate prefix vs. suffix naming against your specific agent and task distribution.

## Relationships

Tool namespacing is a specific application of [[agent-computer-interface|Agent-Computer Interface]] design principles — it addresses the "document like onboarding a junior developer" and "poka-yoke" principles by making tool selection structurally harder to get wrong. It directly supports the [[tool-taxonomy|Tool Taxonomy]]'s principle of well-documented tools, and impacts the effectiveness of [[tool-evaluation|Tool Evaluation]] results.

## See also

- [[agent-computer-interface|Agent-Computer Interface (ACI)]]
- [[tool-taxonomy|Tool Taxonomy]]
- [[tool-selection|Tool Selection]]
- [[tool-evaluation|Tool Evaluation]]
- [[tool-response-design|Tool Response Design]]
