# Learning Note Output Template

Use this template when generating the learning note file in Phase 4. Replace all `{{placeholders}}` with content derived from the source documents and learner profile.

## Frontmatter

```yaml
---
title: "Active Learning Guide: {{Topic Name}}"
type: learning-note
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
sources:
  - {{page-slug-1}}
  - {{page-slug-2}}
learner-profile:
  level: {{beginner | intermediate | advanced}}
  focus: {{focus label chosen by user, e.g. "Full picture" or "Workflow patterns deep-dive"}}
question-budget: {{N}}
---
```

## Opening block

```markdown
# Active Learning Guide: {{Topic Name}}

> **Your goal:** Deeply understand this material through critical analysis and self-explanation
> **Estimated time:** {{N}} minutes
> **Documents covered:** {{count}}
> **Total questions:** {{N}}
>
> **How to use this guide:**
> 1. Read each document when prompted
> 2. Answer each question in the blockquote answer space provided
> 3. Do not look back at the source while answering — gaps in your answer reveal gaps in understanding
> 4. After answering, check your response against the evaluation criteria below each question
>
> **How to evaluate:**
> - Self-assess using the criteria after each question
> - Or share this completed file — the question IDs, source references, and criteria make external evaluation straightforward
```

## Question format

Every question in the guide MUST follow this exact format. The format is designed so that answers can be evaluated — by the reader or by an external reviewer — against specific criteria.

```markdown
#### Q{{group}}.{{number}} — {{question-type}}

**Read:** {{document link(s) — list what to read before answering this question}}

**Source:** {{document link(s) this question draws from — may list multiple}}

> {{The question text. Be specific. For thesis questions, ask for the thesis.
> For argument questions, ask for N arguments. For evaluation questions,
> specify what dimension to evaluate on. For Feynman questions, name the
> audience and the concept. For synthesis questions, name the specific
> ideas to connect.}}

**Your answer:**

> {{leave 4-6 blank lines for the reader to write}}
>
>
>
>
>

**Evaluation criteria:**

- [ ] {{Criterion 1 — a concrete, checkable statement about what a good answer includes}}
- [ ] {{Criterion 2}}
- [ ] {{Criterion 3}}
```

### Question type labels

Use these labels in the `{{question-type}}` slot:

- `Thesis` — thesis identification questions
- `Arguments` — argument mapping questions
- `Evaluation` — argument evaluation questions
- `Feynman` — explain-in-your-own-words questions
- `Synthesis` — cross-document or cross-group connection questions

### Multi-source questions

A question can reference multiple documents. When it does:

- **Read** lists the documents the reader should read (or re-read) before answering, in prerequisite order
- **Source** lists all documents the question draws from

Example:
```markdown
**Read:** [[routing|Routing]], [[parallelization|Parallelization]], [[orchestrator-workers|Orchestrator-Workers]]

**Source:** [[routing|Routing]], [[parallelization|Parallelization]], [[orchestrator-workers|Orchestrator-Workers]]
```

### Writing evaluation criteria

Criteria must be specific and binary — a reader (or evaluator) can check "yes" or "no" for each one. Examples:

Good criteria:
- "Names the central claim in one sentence (not a topic, a claim)"
- "Identifies at least 2 distinct supporting arguments"
- "Each argument is stated as a complete sentence, not a keyword"
- "Explanation avoids jargon from the source document"
- "Explanation includes an analogy or concrete example"
- "Identifies at least one gap or unstated assumption"
- "Rates each argument with a strength judgment and a reason"
- "Names a specific scenario where the distinction matters"
- "Contrasts both concepts without conflating them"

Bad criteria (too vague — do not use):
- "Demonstrates understanding"
- "Good explanation"
- "Covers the key points"
- "Shows critical thinking"

## Group structure

Organize questions into 2-3 thematic groups. Name each group for the insight cluster it covers, not for document types. Each group contains the questions that target insights in that cluster.

```markdown
---

## {{Group Name}}

> Read the referenced documents for each question below. Answer each question
> before moving to the next.

#### Q1.1 — Feynman

**Read:** {{document link}}

**Source:** {{document link}}

> {{Specific Feynman prompt — names audience and concept}}

**Your answer:**

>
>
>
>
>

**Evaluation criteria:**

- [ ] Explanation is in the reader's own words (not copied phrases from source)
- [ ] Explanation would make sense to the named audience without additional reading
- [ ] {{Specific criterion}}
- [ ] {{Specific criterion}}
```

Repeat for each question in the group. Questions within a group should be ordered so that prerequisite concepts come first.

## Final synthesis (after all groups)

Reserve the last 1-2 questions for closing exercises:

```markdown
---

## Final Synthesis

#### QF.1 — Feynman

**Source:** all documents

> Explain the entire topic covered in this guide in under 300 words, as if
> writing an introduction for someone new to it. Cover the key theses,
> how they connect, and why they matter.

**Your answer:**

>
>
>
>
>
>
>
>
>
>
>
>

**Evaluation criteria:**

- [ ] Under 300 words
- [ ] Names or paraphrases at least {{N}} of the key theses identified in the guide
- [ ] States at least one connection between theses (not just a list)
- [ ] A newcomer could read this and understand why the topic matters
- [ ] Written in the reader's own words
```

If the question budget allows a second closing question:

```markdown
#### QF.2 — Evaluation

**Source:** all documents

> Looking across all the documents you studied: which thesis is strongest
> and why? Which argument across the entire guide is weakest? What single
> piece of evidence or reasoning, if added, would most improve the overall
> body of work?

**Your answer:**

>
>
>
>
>
>
>
>

**Evaluation criteria:**

- [ ] Names a specific thesis as strongest with a reason tied to its arguments
- [ ] Names a specific argument as weakest with a reason
- [ ] Proposes a concrete addition (not vague — names what evidence and where it would strengthen the reasoning)
- [ ] All three judgments reference material from the guide, not generic statements
```

## Reading order summary (closing section)

Show the question plan as a compact overview:

```markdown
---

## Reading Order Summary

    {{Group 1 Name}}
      Q1 — Feynman: {{insight description}} (source-slug)
      Q2 — Thesis: {{insight description}} (source-slug)
      Q3 — Evaluation: {{insight description}} (source-slug-1, source-slug-2)

    {{Group 2 Name}}
      Q4 — Feynman: {{insight description}} (multiple sources)
      Q5 — Synthesis: {{insight description}} (source-slug-1, source-slug-2)

    Final
      QF.1 — Feynman: explain the whole topic (all)
      QF.2 — Evaluation: strongest/weakest across all (all)

    Total: {{N}} questions | ~{{M}} min
```

## Self-evaluation summary (append at end of file)

After all content, include a scoring summary the reader can fill in after completing the guide:

```markdown
---

## Self-Evaluation Summary

| Question | Criteria met | Out of | Notes |
|----------|-------------|--------|-------|
| Q1.1     |             | {{N}}  |       |
| Q1.2     |             | {{N}}  |       |
| ...      |             |        |       |
| QF.1     |             | {{N}}  |       |
| **Total**| **—**       | **{{N}}** | |

**Areas to revisit:**

**Strongest understanding:**
```

## Single-document handling

For a single document, generate up to 4 questions using the standard technique selection: typically one Critical Analysis cycle (thesis, arguments, evaluation) plus one Feynman explanation. Use the same question format and evaluation criteria structure. Skip thematic grouping — just list questions sequentially as Q1 through Q4.
