# Building Effective AI Agents — Wiki

A structured knowledge wiki distilling Anthropic's [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents) article into interlinked, scannable pages optimized for learning and reference.

## Overview

This project transforms a long-form technical article into a cross-referenced Obsidian wiki, then uses that wiki as source material to generate a hands-on tutorial series. It draws from Anthropic's experience with dozens of production agent deployments.

The wiki is organized around a **spectrum of agentic complexity**: from single augmented LLM calls, through predefined workflow patterns, to fully autonomous agents.

## Repository Structure

```
├── wiki/                     # Generated wiki pages (Obsidian vault)
│   ├── index.md              # Directory of all pages
│   ├── overview.md           # High-level framework
│   ├── log.md                # Ingestion changelog
│   ├── concepts/             # Foundational ideas
│   ├── techniques/           # Composable workflow patterns
│   └── synthesis/            # Meta-principles and guidance
├── raw/                      # Source documents (input)
│   ├── Building Effective AI Agents.md
│   └── assets/               # Diagrams and images
├── output/                   # Tutorial notebooks (generated output)
│   ├── 00–06 .ipynb          # Seven hands-on notebooks
│   ├── util.py               # Shared utilities
│   └── assets/               # Architecture diagrams
```

## Prompt on Skill

The tutorial content in the `output/` folder was generated using the following Claude Code prompt:

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

**Output:** [output folder](./output)

## Source

Based on [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents) by Anthropic (2024).
