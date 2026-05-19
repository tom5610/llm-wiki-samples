---
title: Evaluator-Optimizer
type: technique
source: "raw/Building Effective AI Agents.md"
created: 2026-05-14
updated: 2026-05-14
---

# Evaluator-Optimizer

## What it is

In the evaluator-optimizer workflow, one LLM generates a response while another evaluates it and provides feedback in a loop. The generator iterates on its output until the evaluator accepts it. This is analogous to the iterative writing process a human writer uses to produce polished work.

The architecture is a feedback loop: Generator produces a solution → Evaluator assesses it → if rejected, feedback flows back to the Generator → cycle repeats until accepted.

![Evaluator-Optimizer workflow — Generator and Evaluator in a feedback loop until the solution is accepted](../../raw/assets/14f51e6406ccb29e695da48b17017e899a6119c7-2401x1000.webp)

## When to use

Use evaluator-optimizer when:
- You have clear, articulable evaluation criteria
- Iterative refinement provides measurable value over single-shot generation
- LLM responses can be demonstrably improved when given articulated feedback (human or automated)
- The LLM can reliably provide evaluation feedback (not just detect problems, but explain them)

## How to implement

1. Design the generator with a prompt optimized for producing initial solutions
2. Design the evaluator with explicit criteria and a structured feedback format
3. Implement the feedback loop with a maximum iteration limit (to prevent infinite loops)
4. Define acceptance criteria that the evaluator uses to decide when to stop
5. Optionally: feed evaluation history to the generator so it doesn't repeat mistakes

## Example

- **Literary translation**: The translator LLM may miss nuances initially, but an evaluator LLM can identify and articulate specific issues (tone, idiom, cultural context) for iterative improvement
- **Comprehensive research**: Multiple rounds of searching and analysis, where the evaluator decides whether the gathered information is sufficient or further searches are warranted

## Pitfalls

- Without a maximum iteration limit, the loop can cycle indefinitely on subjective criteria
- The evaluator must be at least as capable as the generator at recognizing quality — weak evaluators accept bad output
- Each iteration adds latency and cost; diminishing returns are common after 2-3 rounds
- The generator may "overfit" to evaluator feedback, losing qualities the evaluator doesn't measure

## See also

- [[agentic-systems|Agentic Systems]]
- [[augmented-llm|The Augmented LLM]]
- [[prompt-chaining|Prompt Chaining]]
- [[parallelization|Parallelization]]
- [[orchestrator-workers|Orchestrator-Workers]]
- [[agent-computer-interface|Agent-Computer Interface]]
