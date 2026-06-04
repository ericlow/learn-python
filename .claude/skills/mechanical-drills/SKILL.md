---
name: mechanical-drills
description: >
  Run timed single-mechanic Python drills to build fluency. Each drill is a
  tiny, fully-specified problem (5–10 lines) with a 3-minute target. Tracks
  results in drill_metrics.csv and weights future sessions toward weak categories.
  Triggers on "mechanical drills", "drill session", "Python drills", or "fluency practice".
---

# Mechanical Drills Skill

## Purpose
Build Python muscle memory through timed, single-mechanic exercises. The problem
is always trivial in scope — the only challenge is writing it correctly and fast.

## Mechanic Categories

| ID | What it tests | In-scope mechanics |
|---|---|---|
| `defaultdict` | Accumulate into defaultdict with various value types | `defaultdict(list)`, `defaultdict(int)`, `defaultdict(set)` |
| `counter` | Frequency counting | `Counter(iterable)`, `most_common(n)`, counter arithmetic |
| `sorting` | Multi-key sort | `sorted()` with `key=lambda`, tuple keys, negation for descending |
| `fstring` | Basic string formatting | `f"{x}"`, `f"{x:.2f}"`, `f"{x} {y}"` — no alignment, no zero-padding |
| `list-comp` | Filter + transform in one pass | Condition in `if` clause, chained method calls, no nested comps |
| `string-ops` | Common string manipulation | `split()`, `join()`, `strip()`, `replace()`, `startswith()` — no `title()`, `zfill()`, or format codes |
| `json` | Basic JSON parsing | `json.loads()`, `json.dumps()`, single-level and one-level nested key access — no serialization edge cases |
| `date` | Basic date handling | `datetime.strptime()` with common formats (`%Y-%m-%d`, `%H:%M`), `timedelta` arithmetic — no `strftime` format trivia |
| `sets` | Set operations | Construction, `union`, `intersection`, `difference`, `in` membership |
| `heapq` | Priority queue patterns | `heappush`, `heappop`, `nlargest`/`nsmallest`, tuple entries for tie-breaking |
| `deque` | Queue and window patterns | `appendleft`, `popleft`, `maxlen`; BFS queue and sliding window |
| `stdin-parse` | Input parsing | `split()`, `strip()`, `int()`/`float()` conversion — basic only |

---

## Session Flow

### Step 1 — Select categories
Read `drill_metrics.csv` (if it exists). For each category compute:

```
weight = (1 / (attempts + 1)) + slow_rate + non_idiomatic_rate
```

where `slow_rate` = fraction of drills where `secs_to_first_done > 300` and
`non_idiomatic_rate` = fraction where `secs_idiomatic_delta > 0`.

Pick the 5 highest-weighted categories. Fill any slots with no history using
the least-attempted categories first.

Tell the user: "Today's categories: X, X, X, X, X. Starting with drill 1/5."

### Step 2 — Per-drill loop (repeat 5 times)

**Present the drill**
- Show category label, problem statement, input/output example, "Target: 5 min"
- Generate `drills/drill_N.py` using the **Write tool** (not `cat` heredoc via Bash — quote chars in `#` comments trigger approval prompts). Read the existing file first if it exists, then overwrite with Write. Keep the expected output comment on a single line to avoid embedded quotes across lines.
- The function must include a docstring with the full problem instructions — do not rely on the chat window. The candidate should be able to read the file and know exactly what to implement without referring back to the conversation.
- Say "Let me know when you're ready to start."

**When user says ready/go/start:**
- Run `date +%s` → record as `t_start`

**While user works**
- Give help if asked. Increment `hints_used` counter each time.
- Help format: show the relevant function signature and a generic example (use `dog`, `cat`, `animal`, `x`, `items` — never names from the drill problem). The example must never be copy-pasteable into the drill — the candidate must adapt it. This forces the learning step.
  - ✅ `sorted(items, key=lambda x: x[1])` where items = [("cat", 3), ("dog", 1)]
  - ❌ `sorted(people, key=lambda x: x[1])` — uses drill variable name, copy-pasteable
- Never provide a working prototype or skeleton. If asked for one, decline.

**When user says done (must say "done" explicitly before checking):**
- Run `date +%s` → `t_first_done` immediately — do not ask if they traced
- Read the `.py` file from `drills/` immediately — do not ask them to paste code
- Run the file and check output against expected

**If correct on first check:**
- Run `date +%s` → `t_logical_correct`
- `secs_bug_fixes = 0`

**If defects found:**
- Give feedback on correctness only (no idiom yet)
- Wait for fix, re-read, re-run — repeat until correct
- Run `date +%s` → `t_logical_correct`

**Idiom phase (always runs after correct):**
- If idiomatic: `t_idiomatic = t_logical_correct`, `secs_idiomatic_delta = 0`
- If not: show idiomatic version, wait for fix, re-read, re-run
- Run `date +%s` → `t_idiomatic`

**Compute metrics:**
- `secs_to_first_done = t_first_done - t_start`
- `secs_bug_fixes = t_logical_correct - t_first_done`
- `secs_idiomatic_delta = t_idiomatic - t_logical_correct`
- `secs_total = t_idiomatic - t_start`

**Report each drill with ✅ or ❌:**
- **secs_to_first_done** vs 300s target (5 min)
- **secs_bug_fixes** — goal is 0
- **secs_idiomatic_delta** — goal is 0

**After each drill — immediately write:**
1. Append one row to `drill_metrics.csv` (create with header if missing)
2. Update `drill_reviews.md` (create if missing) — one entry per calendar day:
   - Check if the last entry in `drill_reviews.md` is dated today
   - If yes: update that entry in place — add the new drill's metrics table and replace the analysis with a consolidated view across all drills done today
   - If no: append a new dated section
   - Each day's entry includes: per-drill metrics tables + 2–3 sentence analysis per drill + a running cross-drill trend updated after each drill

### Step 3 — Session summary

After all 5 drills, print a table:

| # | Category | secs_to_correct | secs_idiomatic_delta | secs_total | hints | lines | clean_submit |
|---|---|---|---|---|---|---|---|

Call out intra-session trends:
- Is `secs_to_correct` going down across drills?
- Is `hints_used` going down?
- Are later drills cleaner on first submission?

Then compare current session vs past sessions using `drill_metrics.csv`:
- For each category drilled today, list every prior instance with its `secs_to_first_done` and `secs_idiomatic_delta`, then today's values — show the full trend, not a collapsed average
- Call out categories that improved, regressed, or are new this session
- Note any cross-session patterns (e.g. idiom delta consistently high, specific categories always slow)
- Render ASCII bar charts for speed and idiom delta — one row per historical instance, bars scaled to the max value in that category, ✅/❌ against targets (speed ≤300s, idiom = 0s)

**Immediately write** the full session summary table, cross-session trend breakdown, and ASCII bar charts to today's entry in `drill_reviews.md` — do not wait for user confirmation.

---

## drill_metrics.csv

Path: `/Users/eric/projects/learn-python/drill_metrics.csv`
Columns: `date,category,secs_to_first_done,secs_bug_fixes,secs_idiomatic_delta,secs_total,hints_used,lines_written`

- `date`: YYYY-MM-DD
- `secs_to_first_done`: start → first done+traced (target: < 300 — want down)
- `secs_bug_fixes`: first done → logically correct (target: 0 — want to go to zero)
- `secs_idiomatic_delta`: logically correct → idiomatic complete (target: 0 — want to go to zero)
- `secs_total`: sum of all three phases
- `hints_used`: integer count of hints requested (want down)
- `lines_written`: non-blank, non-comment lines at point of logical correctness

---

## Drill Generation Rules

- **Interview relevance**: every mechanic used in a drill must be something a candidate is expected to know without looking up docs. If the solution hinges on knowing an obscure method name, a specific format code, or a rarely-used parameter, replace it with a more common mechanic. When in doubt, ask: "would a strong candidate be embarrassed not to know this?" If no, it's trivia — cut it.
- Solvable in 5–10 lines of Python
- Interface fully specified — no design decisions required
- Include at least one tricky detail (whitespace in input, ambiguous date format, nested JSON key)
- Use generic variable names in examples (`x`, `items`, `data`, `records`)
- Each drill in a session must use a different input shape to prevent pattern matching
- **Input data must be adversarial**: A common failure mode is sample data that produces the correct output even with wrong code — skipping a required operation (e.g. strip, int cast, tie-break) accidentally gives the right answer because the data doesn't exercise that path. Every required operation must have at least one input that fails without it. This includes output cardinality: if the problem requires sorting, filtering, or set operations, the expected output must have enough records (4+) that accidentally correct results are impossible — a single-element output cannot validate a sort, and a small output cannot validate a filter.
  - Sorting: include ties that expose missing tie-break; include values where lexicographic ≠ numeric order (e.g. "9" vs "88")
  - Filter: include items that pass a naive check but should be excluded, and vice versa
  - String ops: include leading/trailing whitespace that changes the effective first character; include mixed case that breaks a lowercase-only check
  - Before finalizing input data, mentally run the 2–3 most likely wrong implementations and confirm each produces wrong output
