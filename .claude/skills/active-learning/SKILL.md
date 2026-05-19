---
name: active-learning
description: >
  Generate active learning notes from wiki pages or document directories —
  structured reading paths using the Feynman technique and critical analysis
  (thesis identification, argument mapping, argument evaluation) that help
  users deeply internalize content through explanation and critical thinking
  rather than passive reading. Use when the user asks to "study",
  "learn", "review", "create study notes", "make a reading guide",
  "help me understand", "quiz me on", "create learning notes",
  "active learning", "reading path", "study plan", "self-test", or
  "learning guide" for any topic covered in a wiki or set of documents.
  Also trigger when the user wants to prepare for a discussion, build
  a mental model of a topic, or says "coach me through" any material.
---

## Active learning workflow

Generate a structured active learning guide from wiki pages or documents. The goal is not summarization — it is to produce a focused set of high-leverage questions that force the reader to identify core claims, analyze supporting arguments, evaluate reasoning, and explain concepts in their own words. These activities produce durable, transferable understanding.

The skill uses two core techniques:
1. **Critical Analysis** — find the thesis, map the arguments, evaluate how well the arguments support the thesis. Not every question needs all three sub-steps — use whichever sub-steps best fit the insight.
2. **Feynman Technique** — explain the concept in your own words as if teaching someone else. Gaps in your explanation reveal gaps in your understanding.

The skill generates **8-10 questions maximum** for multi-document sets, choosing the highest-leverage insights rather than mechanically covering every document. Quality over quantity: one well-crafted question spanning 3 related documents beats 12 rote questions across those same documents.

Use `$ARGUMENTS` as the input path or topic if provided (e.g., `/active-learning wiki/`, `/active-learning wiki/concepts/`, `/active-learning raw/some-document.md`).

### Prerequisites

1. Check that `notes/` exists. If missing, create it.
2. If `$ARGUMENTS` is empty and `wiki/index.md` does not exist (or is empty), suggest the user run `/ingest` on a source document first — there is nothing to study yet.

### Phase 1: Discover & read content

Determine what documents to include based on `$ARGUMENTS`:

**If `$ARGUMENTS` is a file path** — read that single file.

**If `$ARGUMENTS` is a directory path** — list all `.md` files in that directory (and subdirectories). Read each one. Skip `index.md`, `log.md`, and `overview.md` as study content (but read `overview.md` for orientation context if it exists).

**If `$ARGUMENTS` is a topic string** — read `wiki/index.md` and search for pages whose title or description matches the topic. Read the matching pages. If no match, use `AskUserQuestion` to clarify what the user wants to study.

**If `$ARGUMENTS` is empty** — use `AskUserQuestion` to ask what the user wants to study. Options should reflect what is available (list topics from `wiki/index.md` if the wiki exists, or ask for a file/directory path).

For each document, note:
- Whether it has wiki-style frontmatter (with a `type` field) — this determines linking format later
- Its type (concept, technique, entity, synthesis, or flat document)
- Key ideas and how it relates to other documents in the set
- Wikilinks it contains — these reveal prerequisite relationships
- The central thesis and supporting arguments — you will need these to write evaluation criteria
- The most important insight this document contributes to the corpus (may span other documents)

If `wiki/overview.md` exists, read it to understand how the content fits together. This helps identify cross-document insights in Phase 2.

### Phase 2: Assess and focus

This phase determines who the learner is and what to focus on. It uses up to 2 `AskUserQuestion` calls.

#### Step 1 — Ask prior knowledge level

Ask: "How familiar are you with this material?"

Options:
- "New to it" (description: "Start from foundations, provide hints for finding the thesis, simpler evaluation prompts")
- "Know the basics" (description: "No hints, focus on argument quality and gaps in reasoning")
- "Deep background" (description: "Identify implicit theses, unstated assumptions, and conditions under which arguments fail")

These map to beginner / intermediate / advanced calibration for question generation.

#### Step 2 — Extract insights (internal, no user interaction)

After reading all content, identify the most important insights across the corpus for the user's level. An "insight" is one of:
- **A key idea** — a thesis or claim that is central to the topic
- **A tension** — two documents that pull in different directions or make competing claims
- **A distinction** — a boundary between concepts that is easy to confuse (e.g., workflows vs. agents, parallelization vs. orchestrator-workers)
- **A connection** — a non-obvious relationship between ideas across documents

For each insight, note:
- Which documents it draws from (1-3 source documents)
- Which technique best tests understanding of it (Critical Analysis, Feynman, or Synthesis)
- Why it matters for the user's level

Group insights into 3-4 thematic clusters.

#### Step 3 — Ask focus (multi-document sets only)

**Skip this step if the input is a single document or 2-3 documents.** With few documents there aren't enough thematic options to warrant a choice — go directly to Phase 3.

For 4+ documents, present 3-4 thematic focus options via `AskUserQuestion`. Each option promises the same question budget (~8-10 questions), targeting different insight clusters.

Rules for constructing options:
- The first option should always be "Full picture (Recommended)" — covers the most important insights across all thematic clusters
- Other options should represent genuinely distinct focus areas derived from the thematic clusters identified in Step 2
- Each option's description should name the specific topics/ideas it covers and the approximate question count
- The user can always select "Other" to type their own focus

Example for a 10-document agentic systems wiki:
> "I've read all 10 documents. Pick a focus:"
> - "Full picture (Recommended)" — "8-10 questions across the core ideas: the workflow-vs-agent spectrum, pattern selection, and ACI design"
> - "Workflow patterns deep-dive" — "8-10 questions focused on the five patterns, their tradeoffs, and how to choose between them"
> - "Foundations and decision-making" — "8-10 questions on the augmented LLM concept, the agentic systems taxonomy, and the decision framework"

### Phase 3: Design the question plan

Select the 8-10 highest-leverage insights for the chosen focus (or all insights for small document sets). For each insight, choose the question technique and allocate from the question budget.

#### Question budget

| Corpus size | Budget |
|---|---|
| 1 document | Up to 4 questions |
| 2-3 documents | 6-8 questions |
| 4+ documents | 8-10 questions |

Spend questions where the learning value is highest. A single Feynman question that spans 3 related documents can be worth more than 3 separate thesis questions. Not every document needs a dedicated question — some documents serve as context for questions that target other documents.

#### Technique selection per insight

Match the technique to the insight, not to the document:

- **Strong debatable claim** → Critical Analysis. Use whichever sub-steps fit:
  - Thesis + Arguments + Evaluation (full cycle) — when the document has rich, mappable arguments
  - Thesis + Evaluation (skip argument mapping) — when the claim matters but arguments are thin
  - Evaluation only — when the thesis is obvious but its strength relative to alternatives is the real question
- **Key concept, mechanism, or distinction** → Feynman. Name a specific concept and a specific audience.
- **Cross-document connection or tension** → Synthesis. Ask the reader to connect or compare ideas from 2-3 documents.

#### Level calibration

Apply the same calibration as before — level affects question difficulty, not question count:

**Critical Analysis calibration:**
- **Beginner**: Provide a hint about where to look for the thesis. Ask for 2 arguments. Evaluation: "Which argument is most convincing? Why?"
- **Intermediate**: No hints. Ask for 3 arguments. Evaluation: "Rate each argument's strength. Identify gaps."
- **Advanced**: Ask for implicit/unstated thesis too. Ask for 4 arguments including implied ones. Evaluation: "Identify assumptions each argument depends on. Under what conditions does the thesis fail?"

**Feynman calibration:**
- **Beginner**: "Explain [concept] to a friend who has never encountered this topic. Use an analogy if it helps."
- **Intermediate**: "Explain [concept] to a junior colleague. Include why it matters and one common misconception to avoid."
- **Advanced**: "Explain [concept] to a peer in a related field. Highlight what makes this non-obvious and where the boundaries of the concept lie."

#### Structure the question plan

1. Order questions into 2-3 thematic groups. Name each group for the insight cluster it covers, not for document types (e.g., "Core Patterns & When to Choose" not "Techniques").
2. Within each group, order so that prerequisite concepts come first.
3. Reserve the final 1-2 slots for closing exercises:
   - **Final Feynman**: "Explain the entire topic in under 300 words, as if writing an introduction for someone new to it."
   - **Final Evaluation** (if budget allows): "Which thesis is strongest and why? Which argument is weakest? What single piece of evidence would most improve the overall body of work?"

#### Confirm with the user

Present the question plan via `AskUserQuestion`. Show the numbered list of insight targets with their technique and source documents — use the Reading Order Summary format from the output template so the user sees exactly what they'll be asked.

Options:
- "Looks good, generate the guide (Recommended)" (description: "Proceed with this question plan")
- "Adjust" (description: "I want to change the focus, add/remove questions, or shift emphasis")

If the user adjusts, incorporate feedback and re-present. **Do not proceed until the user confirms.**

### Phase 4: Generate learning notes

Read `references/output-template.md` for the exact output structure. Write the learning note to `notes/<topic-slug>-study-guide.md`.

Every question must follow the answer-block format defined in the output template: a unique question ID, the question text, a source reference (which may list multiple documents), an answer block (blockquote lines), and evaluation criteria.

#### Writing questions

For each question in the confirmed plan:

1. **Write the Read directive** — list which document(s) to read before answering. For multi-source questions, list them in prerequisite order.
2. **Write the question** — be specific. Thesis questions ask for the thesis. Argument questions ask for N arguments. Evaluation questions specify what dimension to evaluate. Feynman questions name a specific audience and a specific concept. Synthesis questions name the specific ideas to connect.
3. **Write evaluation criteria** — 3-4 binary, checkable criteria per question. Each criterion must be specific enough that two independent evaluators would mostly agree on whether an answer meets it.

#### Quality checks

- Every question must require the reader to analyze, judge, or produce — never just recall or copy.
- Feynman prompts must name a specific audience and a specific concept. "Explain this" is never acceptable.
- Evaluation criteria must be concrete. "Demonstrates understanding" is forbidden. Use checks like "names at least 2 supporting arguments" or "explanation uses no jargon from the source."
- If a document has no clear thesis (glossaries, reference tables), replace thesis identification with: "What is the organizing principle of this document?" and replace argument mapping with: "What are the key categories or distinctions it establishes?"
- Reference images in Feynman prompts when they convey important structural information (diagrams, flowcharts). Ask the reader to redraw or describe the diagram from memory.

### Phase 5: File & report

1. Write the learning note to `notes/<topic-slug>-study-guide.md`.

2. **If the source content is from the wiki** (pages with wiki frontmatter), append to `wiki/log.md`:
   ```
   ## [YYYY-MM-DD] active-learning | {{Topic Name}}

   **Learning note created:** `notes/{{filename}}.md`
   **Pages covered:** {{list of page slugs}}
   **Learner profile:** {{level}} / {{focus}}
   ```

3. **Do not update `wiki/index.md`** — learning notes are personal study artifacts, not canonical wiki pages.

4. Report to the user:
   - What was created (filename, location)
   - Number of questions generated and estimated study time
   - How to use the guide: read each document when prompted, then answer the questions in the blockquote sections
   - How to evaluate: self-assess using the inline criteria, or share the completed file for external evaluation

## Linking conventions

- **Wiki source content**: Use `[[slug|Display Text]]` wikilinks in the learning note to reference source pages. This keeps the learning note navigable in Obsidian.
- **Flat document source content**: Use relative markdown links `[Display Text](../relative/path.md)` since wikilinks would not resolve.
- **Mixed content**: If some sources are wiki and some are flat, use the appropriate link format for each.

## Edge cases

- **Single short document** (<500 words): Produce a mini guide — one critical analysis cycle (thesis, arguments, evaluation), one Feynman explanation. Up to 4 questions total. Do not pad artificially.
- **Single document** (500+ words): Up to 4 questions using the standard technique selection. Skip the focus question (Phase 2 Step 3).
- **2-3 documents**: 6-8 questions. Skip the focus question. Go directly to question plan confirmation.
- **4+ documents**: 8-10 questions. Include the focus question.
- **Non-English content**: Generate the learning note in the same language as the source documents.
- **Documents with no clear thesis**: Replace thesis identification with "What is the organizing principle?" and argument mapping with "What are the key categories or distinctions?" Adapt evaluation accordingly.
- **Documents with images**: Reference images in Feynman prompts when they convey important structural information. Ask the reader to redraw or describe the diagram from memory.

## Guidelines

- This skill is **read-only on the wiki**. Learning notes are written to `notes/`, not into the wiki. The only wiki write is appending to `wiki/log.md`. Never modify wiki pages, `index.md`, or `overview.md`.
- The purpose is active learning through critical thinking and explanation, not summarization. Every question should require the reader to analyze, judge, or produce — never just recall or copy.
- **Quality over quantity**: a well-crafted question spanning 3 related documents beats separate questions for each. Each question should target a specific, testable understanding. Not every document needs its own question.
- Evaluation criteria must be specific enough that two independent evaluators would mostly agree on whether an answer meets them. Avoid vague criteria like "demonstrates understanding." Prefer concrete checks like "names at least 2 supporting arguments" or "explanation uses no jargon from the source."
- Feynman prompts must name a specific audience and a specific concept. "Explain this" is never acceptable — always "Explain [specific concept] to [specific audience]."
- Adapt to the actual content. If a document has a clear thesis-argument structure, lean into critical analysis. If it's more conceptual or definitional, lean into Feynman explanation. Match the technique to the insight, not to a rigid template.
- **Respect the question budget.** Do not exceed 10 questions for any corpus. The constraint forces selectivity — which insights truly matter most?
