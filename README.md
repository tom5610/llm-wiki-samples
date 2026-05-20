# Building Effective AI Agents — Enhanced Workshop

Use [Claude Code](https://claude.ai/code) to enhance Anthropic's [agent patterns workshop](https://github.com/anthropics/claude-cookbooks/tree/main/patterns/agents) with structured knowledge extracted from a wiki.

## The Idea

Anthropic's [claude-cookbooks](https://github.com/anthropics/claude-cookbooks/tree/main/patterns/agents) provides hands-on notebooks for building AI agents, but the code examples are light on conceptual context — the *why*, *when*, and *trade-offs* behind each pattern. Meanwhile, Anthropic's [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents) article is rich in design guidance but has no runnable code.

This project bridges the gap:

1. **Ingest** the article into a structured wiki (`wiki/`) using the [llm-wiki](https://github.com/tom5610/llm-wiki) plugin — extracting concepts, techniques, decision frameworks, and architecture diagrams.
2. **Enhance** the workshop notebooks by combining the wiki's structured knowledge with the cookbooks' runnable code — using Claude Code to synthesize both sources into enriched tutorials (`output/`).

The result is a tutorial series where each notebook teaches *what* a pattern is, *when* to use it, *why* it works, and *how* to implement it — all in one place.

## Repository Structure

```
├── wiki/                     # Structured knowledge base (Obsidian vault)
│   ├── index.md              # Directory of all pages
│   ├── overview.md           # High-level framework
│   ├── log.md                # Ingestion changelog
│   ├── concepts/             # Foundational ideas (augmented LLM, ACI, agentic systems)
│   ├── techniques/           # Workflow patterns (chaining, routing, parallelization, etc.)
│   └── synthesis/            # Design principles and meta-guidance
├── raw/                      # Source documents (input to wiki)
│   ├── Building Effective AI Agents.md
│   └── assets/               # Diagrams from the article
├── output/                   # Enhanced tutorial notebooks (generated output)
│   ├── 00–06 .ipynb          # Seven hands-on notebooks
│   ├── util.py               # Shared utilities
│   └── assets/               # Architecture diagrams
```

## Prompt

The following Claude Code prompt was used to generate the enhanced tutorials in `output/`:

```
Act as a Agentic AI expert, your mission is to help beginner learn and practice
'building effective AI agents". Execute the below tasks per sub-agent in parallel.
When the agents reply with detailed summary and analysis, then brainstorm with me
to create tutorial content in 'output' folder.

**Tasks**:
    * From 'wiki' folder, extract 'building effective agents' concepts, patterns,
      techniques and insights, including architecture design practices, useful images,
      decision-making framework on when & why.
    * Read [claude-cookbooks-folder](https://github.com/anthropics/claude-cookbooks/tree/main/patterns/agents)
      thoroughly and summarise the key insights on each notebook, python script and
      markdown file.

**Rules of creating tutorial content**
    * Do NOT change existing code and may reuse python script(s), if possible
    * Keep the tutorial folder structure flat
    * Extend notebooks with concepts, patterns, techniques and insights, including
      architecture design practices, useful images, decision-making framework on
      when & why.
    * When all code/notebook creation is done, create a `README.md` to mention the
      purpose and summary for each with inter-connected links.

Last, for any questions, please use `AskUserQuestion` tool to clarify with me.
```

## Output

The generated tutorials live in the [`output/`](./output) folder — seven Jupyter notebooks covering the full spectrum from foundations through autonomous agents, each enriched with conceptual context, architecture diagrams, and decision frameworks drawn from the wiki.

See [`output/README.md`](./output/README.md) for the full learning path and pattern decision guide.

## Source Material

- [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic's design guidance (2024)
- [Claude Cookbooks: Agent Patterns](https://github.com/anthropics/claude-cookbooks/tree/main/patterns/agents) — Runnable code examples
