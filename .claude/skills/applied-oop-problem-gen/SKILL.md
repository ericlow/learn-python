---
name: applied-oop-problem-gen
description: >
  Generate an applied OOP coding interview problem grounded in real-world systems.
  Use when the user wants to practice OOP problems that follow the pattern observed
  in real interviews: interface given upfront, progressive requirements, extensibility
  as the core challenge. Distinct from oop-problem-gen which targets FAANG-style
  open-ended system design. Triggers on "applied OOP", "systems problem", or when
  the user wants a problem modeled after real interview patterns.
---

# Applied OOP Interview Problem Generator

## What This File Is
Generates a coding problem where the interface is provided upfront and requirements
escalate across three phases: direct operation → automate the search → optimize with
a metric. The central challenge is extensibility — writing Phase 1 in a way that
Phase 2 does not require a rewrite.

## What This File Is NOT
- Not for open-ended system design where the candidate discovers entities through
  questions — that is `oop-problem-gen`
- Not for abstract algorithmic problems — that is `algo-problem-gen`
- Not a coaching guide — session mechanics live in the `interview-coach` skill

---

## Step 1: Gather Context

Ask the user:
1. **What domain?** (e.g., banking, parking, logistics, library, hospital, ride-share — or "surprise me")
2. **Difficulty?** easy / medium / hard

Language is always Python — do not ask.

**Difficulty scale:**

| Level | Phase 3 ceiling | Phase 2 data structure |
|-------|----------------|----------------------|
| **Easy** | Linear scan + `min()`/`max()` | Dict or list — obvious choice |
| **Medium** | Multiple sort criteria or pre-filter before comparing | Candidate must choose between dict and secondary index |
| **Hard** | Phase 3 introduces an algorithmic element — BFS for shortest path, heap for top-K — layered on top of the OOP design | Secondary index design is non-obvious; state location decision is contested |

At **hard** level, the OOP design remains the core test but Phase 3 requires
the candidate to recognize that an algorithm (not just a `min()` call) is the right tool.
This is the Sentry pattern — parking garage with distance optimization maps to BFS on a
grid if spots have positional layout.

---

## Step 2: Generate the Problem

### Interface first
Provide a class skeleton — signatures and `pass` only, no implementation. The skeleton
communicates the domain. The candidate implements against it. The skeleton must
pre-decide the primary data structure — the candidate should never have to choose it
in Phase 1. If the skeleton leaves that choice open, redesign it.

### Phase structure

| Phase | What changes | Time |
|-------|-------------|------|
| Phase 1 | Caller provides all addressing — validate and mutate | 10–15 min |
| Phase 2 | Caller no longer provides the address — find it | 15–20 min |
| Phase 3 | Add a metric — optimize the search | 10–15 min |

**Phase 1:** No search, no optimization. Validate inputs, mutate state, return a result.
Validation order: existence → state → business rule.

**Phase 2:** Caller stops providing the address. Candidate must find it. This is where
data structure choice first becomes meaningful. Key question: "Given X, quickly find Y?"
→ dict. Scan with filter → list + loop.

**Phase 3:** Find not just *any* valid result, but the *best* one by a metric.
At easy/medium: linear scan + `min()`/`max()` with key, multiple sort criteria, or a
pre-filter that eliminates candidates before comparing.
At hard: heaps, sliding window, or BFS are in scope when the metric requires it.

---

## Step 2a: Extensibility Test

**Ask:** "If a candidate implements Phase 1 the naive way, does Phase 2 require a
structural rewrite or just an extension?"

- ❌ Phase 2 works regardless of how Phase 1 was done → too easy, redesign
- ✅ Naive Phase 1 (hardcoded address, wrong state location, no secondary lookup) breaks under Phase 2 → good

Secondary tests: Is there a state-location decision? At least one non-trivial business rule?
Is the Phase 3 metric clear and domain-meaningful?

---

## Step 2b: Corner Cases

Define 4–6 corner cases drawn from the domain. Categories to cover: duplicate operations,
invalid addressing, self-referential, capacity/empty, null fields, boundary.

For each: phase it applies to, scenario, expected behavior, common mistake, test snippet.

---

## Step 3: Decision Points

Document 2–4 points where the candidate makes a meaningful choice. For each: the options,
pros/cons, preferred solution, what it tests. Focus on: primary collection (dict vs list),
secondary lookup (when to introduce), state location (entity vs manager vs inferred),
return type consistency.

---

## Step 4: Coaching Guide

**Issue reference:** For each potential bug or design failure — phase, severity
(Critical/Important/Minor), type (Logic/Corner Case/Design/State), three graduated hints,
and the answer. Every corner case from Step 2b must have an issue entry.

**Reveal script:** Opening brief (1–2 sentences). List 2–3 expected clarifying questions
— factual only (return values, boundary behavior, input guarantees). No design questions;
the skeleton already answers those. Edge case gate before each phase (candidate lists
edge cases before coding). Phase transition prompts for Phase 2 and Phase 3.

---

## Step 5: Driver Code

Per phase: `print()` statements with inline expected output. Cover happy path, edge cases,
and corner cases. Do not reveal which will fail.

---

## Step 6: Reference Implementation

Starter file: skeleton only. Reference implementation: all three phases, all corner cases,
clean methods, state in the right place, runnable Python with test cases.

---

## Step 7: Common Pitfalls

List 5–6 domain-specific pitfalls: hardcoding address in Phase 1, state on wrong class,
inconsistent return types, missing secondary lookup, wrong validation order, plus one
domain-specific entry.

---

## Step 8: Rubric

Scored 1–3 per dimension, total out of 15. Dimensions: Correctness, Code Quality,
Data Structures, Communication, Speed. Fill in problem-specific criteria for the first
three before the session begins.

---

## Output

Save as **4 files** in `problems/`:
- `problems/YYMMDD-[domain]-applied-oop_overview.md` — problem description, entities, all phases at a glance, opening prompt, rubric (~100 lines)
- `problems/YYMMDD-[domain]-applied-oop_req1.md` — Phase 1 full content: requirement, reveal script, edge case probes, corner cases, decision points, issue reference with hints, reference implementation, driver code, phase evaluation guide (~200 lines)
- `problems/YYMMDD-[domain]-applied-oop_req2.md` — same structure for Phase 2 (~200 lines)
- `problems/YYMMDD-[domain]-applied-oop_req3.md` — same structure for Phase 3, plus extension questions and common pitfalls (~200 lines)

**Skeleton progression rule:**
- The initial `.py` file (created by the coach at session start) contains only Phase 1 classes and method signatures
- Each `req2.md` and `req3.md` must include a `## Skeleton Addition` section near the top with the exact Python snippet the coach will Edit into the `.py` file at phase transition — signatures and `pass` only, no implementation
- New classes, helper stubs (rare), or new method signatures (common) belong in this section

The `_session_notes.md` file is created at runtime by the coach — do not generate it upfront.

Confirm all 4 files were saved and hand off to `interview-coach`.
