---
title: Parallelization
type: technique
source: "raw/Building Effective AI Agents.md"
created: 2026-05-14
updated: 2026-05-14
---

# Parallelization

## What it is

Parallelization runs multiple LLM calls simultaneously and aggregates their outputs programmatically. It manifests in two key variations:

- **Sectioning** — Breaking a task into independent subtasks that run in parallel. Each LLM handles a different aspect of the problem.
- **Voting** — Running the same task multiple times with different prompts or configurations to get diverse outputs, then aggregating for higher confidence.

The architecture fans out input to multiple parallel LLM calls, then combines results through an aggregator.

![Parallelization workflow — input fans out to multiple LLM calls, results merge through an Aggregator](../../raw/assets/406bb032ca007fd1624f261af717d70e6ca86286-2401x1000.webp)

## When to use

Use parallelization when:
- Subtasks are independent and can execute simultaneously (sectioning)
- Multiple perspectives or attempts improve confidence (voting)
- Each consideration benefits from focused LLM attention rather than handling everything in one call
- Speed matters and subtasks don't depend on each other's outputs

## How to implement

**Sectioning:**
1. Identify independent aspects of the task
2. Design focused prompts for each aspect
3. Execute all calls in parallel
4. Aggregate results (concatenation, merge, or synthesis)

**Voting:**
1. Design diverse prompts that approach the same question differently
2. Execute all variations in parallel
3. Apply an aggregation strategy (majority vote, threshold, weighted consensus)

## Example

- **Sectioning**: One model instance processes user queries while another screens for inappropriate content — performs better than having one call handle both
- **Sectioning**: Automated evals where each LLM call evaluates a different quality aspect
- **Voting**: Multiple prompts review code for vulnerabilities, flagging if any find a problem
- **Voting**: Content moderation with multiple prompts evaluating different aspects, using vote thresholds to balance false positives/negatives

## Pitfalls

- Higher cost (N parallel calls vs. 1) — ensure the confidence gain justifies the expense
- Aggregation logic must handle disagreement gracefully
- Not suitable when subtasks depend on each other's outputs (use [[prompt-chaining|Prompt Chaining]] instead)

## See also

- [[agentic-systems|Agentic Systems]]
- [[augmented-llm|The Augmented LLM]]
- [[orchestrator-workers|Orchestrator-Workers]]
- [[evaluator-optimizer|Evaluator-Optimizer]]
- [[prompt-chaining|Prompt Chaining]]
