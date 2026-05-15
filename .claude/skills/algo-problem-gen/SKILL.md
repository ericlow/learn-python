---
name: algo-problem-gen
description: >
  Generate an algorithmic coding interview problem with coaching guide.
  Use when the user wants to practice algorithms, data structures, graphs,
  trees, arrays, or string problems. Triggers on "algorithm problem", "algo
  practice", "generate an algo problem", or "let's do an algorithm session".
  After generating, the interview-coach skill governs the session.
---

# Algorithmic Coding Interview Problem Generator

## What This File Is
Generates an algorithmic problem and coaching guide calibrated to the target
difficulty. Problems use real-world framing but are algorithmically-core — the
domain is the wrapper, the algorithm is the challenge.

## What This File Is NOT
- Not for OOP system design — use `applied-oop-problem-gen`
- Not a coaching guide — session mechanics live in `interview-coach`

## Out of scope (never generate)
- Dynamic programming — only appears at Google; not a target company pattern
- Segment trees, Fenwick trees, advanced graph algorithms (Dijkstra, Floyd-Warshall)

---

## Step 1: Gather Context

Ask the user:
1. **Difficulty?** easy / medium / hard (see scale below)
2. **Algorithm category?** or "surprise me"
3. **Framing?** real-world domain, abstract, or no preference

**Difficulty scale:**

| Level | In scope | Excluded |
|-------|----------|----------|
| **Easy** | Hashmap, basic loops, sorting, sliding window, two pointers | Trees, graphs |
| **Medium** | All of Easy + trees, BFS/DFS, prefix sum, trie/tree construction | Topological sort, matrix BFS |
| **Hard** | All of Medium + graphs, topological sort, matrix traversal, heaps, monotonic structures | DP, segment trees |

---

## Step 2: Generate the Problem

Three progressive requirements. Each must force adaptation of existing code, not just
addition of a new function.

- **Req 1:** Brute force acceptable — establish correctness
- **Req 2:** Brute force becomes suboptimal — candidate must recognize the gap
- **Req 3:** Requires the optimal algorithm or data structure for the chosen difficulty

The problem is well-designed if: a meaningful complexity gap exists between naive and
optimal (e.g. O(n²) → O(n log n)), and at least 3 non-obvious edge cases arise from
the domain.

---

## Step 3: Corner Cases

4–6 cases drawn from: empty input, single element, cycles, disconnected components,
negative values, duplicates, boundary conditions. Document each with: which requirement,
scenario, expected behavior, common mistake, test snippet.

---

## Step 4: Coaching Guide

Sections to generate:
- **Issue reference:** per bug or design gap — severity, 3 graduated hints, answer.
  Every corner case from Step 3 must have an entry.
- **Reveal script:** opening brief (1–2 sentences), expected clarifying questions,
  edge case probes per requirement, phase transition prompts.

---

## Step 5: Driver Code + Reference Implementation

Driver: `print()` statements with inline expected output per requirement. Do not reveal
which will fail.

Reference: clean implementation handling all requirements and corner cases. Runnable
Python with test cases.

---

## Step 6: Rubric (scored 1–3, total /15)

Dimensions: Correctness, Code Quality, Data Structures, Communication, Speed.
Fill in problem-specific criteria for the first three before the session.

---

## Algorithm Categories

### Easy
| Category | Algorithm | Example |
|----------|-----------|---------|
| Array | Sliding window | Max sum subarray of size K |
| Array | Two pointers | All pairs summing to target |
| Array | Sorting + scan | Merge overlapping intervals |
| String | Frequency map | Longest substring without repeating chars |
| String | Two pointers | All anagram positions in a string |
| Lookup | Hashmap | Two-sum, group anagrams |
| Multiset | Counter availability check | Can these letters spell this word? — `Counter(word) - Counter(available)` is empty iff all letters are covered |

### Medium
| Category | Algorithm | Example |
|----------|-----------|---------|
| Tree | Recursion | Max depth, lowest common ancestor |
| Tree | BFS level-order | Return values level by level |
| Tree construction | Trie / prefix tree | Build call tree from stack traces |
| Array | Prefix sum | Count subarrays with sum = target |
| Graph | BFS | Shortest path in unweighted graph |
| Graph | DFS | Cycle detection in directed graph |
| Interval | Gaps + cursor sweep | Sort merged periods, sweep with cursor = window_start, emit (cursor, period_start) as gap, advance cursor = max(cursor, end), check trailing gap after loop |

### Hard
| Category | Algorithm | Example |
|----------|-----------|---------|
| Matrix | BFS/DFS on 2D grid | Number of islands |
| Matrix | BFS with state | Shortest path through grid avoiding obstacles |
| Graph | Topological sort (DFS) | Valid task order given dependencies |
| Graph | Topological sort (Kahn's) | Detect cycle + return ordered result |
| Heap | Top-K / K-way merge | K most frequent, merge K sorted lists — heap tuple: `(value, list_idx, elem_idx)` |
| Stack | Monotonic stack | Next greater element |
| Interval | Sweep-line peak overlap | Create `(time, +1/-1)` events for interval starts/ends, sort by `(time, delta)` to process ends before starts at ties, sweep tracking count — finds time ranges of maximum simultaneous overlap |

---

## Phase Behavior Reference

Observed phase progressions from real interviews. Use these to calibrate coaching guides.

| Problem type | Phase 1 | Phase 2 | Phase 3 |
|---|---|---|---|
| Stream aggregation (Everlaw word counter) | Tokenize + count into dict | Retrieve count by word | Top-K by frequency (heap) |
| Tree construction (Sentry stack profiler) *(2 phases — recalled)* | Build tree from all traces: walk each top-down, create nodes on first visit, increment counts | DFS walk to render indented output with ms counts | — |
| Grid traversal (Baton block puzzle) | Single-step move validation | Find all valid moves | Find move sequence that clears most blocks |
| Interval merge + gaps (Verkada motion) | Merge overlapping periods (sort + sweep) | Find uncovered gaps in a monitoring window | Combine K camera lists — flatten + re-merge; sweep-line for peak overlap |
| Multiset availability (TabaPay spell check) *(single-phase)* | Given pool of letters and list of words, return words that can be spelled — key: `Counter(word) - Counter(pool)` empty iff word is spellable | — | — |

---

## Output

Save as **4 files** in `problems/`:
- `problems/YYMMDD-[slug]_overview.md` — problem description, entities, all reqs at a glance, opening prompt, rubric (~100 lines)
- `problems/YYMMDD-[slug]_req1.md` — Req 1 full content: requirement, reveal script, edge case probes, corner cases, decision points, issue reference with hints, reference implementation, driver code, phase evaluation guide (~200 lines)
- `problems/YYMMDD-[slug]_req2.md` — same structure for Req 2 (~200 lines)
- `problems/YYMMDD-[slug]_req3.md` — same structure for Req 3, plus extension questions and common pitfalls (~200 lines)

**Skeleton progression rule:**
- The initial `.py` file (created by the coach at session start) contains only Req 1 function signatures
- Each `req2.md` and `req3.md` must include a `## Skeleton Addition` section near the top with the exact Python snippet the coach will Edit into the `.py` file at phase transition — signatures and `pass` only, no implementation
- New helper functions or updated signatures belong in this section

The `_session_notes.md` file is created at runtime by the coach — do not generate it upfront.

Confirm all 4 files were saved and hand off to `interview-coach`.
