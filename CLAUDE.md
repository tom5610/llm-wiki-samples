# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **reference sample** demonstrating the [llm-wiki plugin](https://github.com/tom5610/llm-wiki). It shows how to transform raw source documents into a structured, interconnected wiki using Claude Code.

The sample ingests Anthropic's "Building Effective AI Agents" document and produces a multi-page wiki covering agentic system design patterns.

## Plugin Dependency

All wiki operations require the **llm-wiki plugin** to be enabled (configured in `.claude/settings.json`). Use the plugin's skills (`/ingest`, `/query`, `/lint`, `/extract`) to manage wiki content.

## Project Structure

- `raw/` — Source documents (the input). Place new documents here before ingesting.
- `wiki/` — Generated wiki pages (the output). Organized by page type: `concepts/`, `techniques/`, `synthesis/`, `entities/`.
- `.claude/skills/` — Project-specific skills (e.g., `active-learning` for generating study guides).
- `.llm-wiki/` — Plugin configuration (lenses, etc.).

## Wiki Conventions

- All wiki pages use YAML frontmatter with `title`, `type`, and date fields.
- Page types: `index`, `overview`, `log`, `concept`, `technique`, `synthesis`.
- Cross-references use wikilinks: `[[slug|Display Text]]`.
- File naming uses hyphens (e.g., `agent-computer-interface.md`).
- `wiki/log.md` is an append-only audit trail of ingest operations — never overwrite it.
