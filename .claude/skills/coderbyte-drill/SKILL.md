---
name: coderbyte-drill
description: >
  Simulate a CoderByte-style at-home assessment — 2 independent, function-completion
  data-parsing/manipulation problems graded against HIDDEN test cases on exact output.
  Mirrors the real employer take-home format: two independent parse-then-manipulate
  problems using different techniques, self-paced ~45 min, unassisted by default. Tracks
  to coderbyte_metrics.csv. Triggers on "coderbyte drill", "coderbyte sim", "coderbyte
  assessment", or "take-home practice".
---

# CoderByte Drill Skill

## Purpose
Reproduce the CoderByte employer take-home experience, not a generic drill. The
defining traits this skill enforces:

1. **Two independent problems.** They do NOT depend on each other, and the selector
   forces them to use different manipulation techniques — because the real assessment
   uses two uncorrelated problems to get breadth signal. Present both up front (like
   the real platform), let the user work them in either order.
2. **Function-completion format.** Given a stub, make it return the specified output.
3. **Hidden-test grading on exact output.** The user sees ONE sample I/O per problem.
   All other test cases are hidden until graded. Exact match — spacing, case,
   delimiters, types all count.
4. **Unassisted by default.** It's a take-home. No hints unless the user explicitly
   asks; if they do, deliver it but flag `hints_used`.

This is harder and more realistic than combo-drills/fundamentals-screen, which reveal
the tricky case up front. Here the user must anticipate edge cases blind.

---

## Problem Pool

Every problem is one species: **parse a messy input, then manipulate it into exact
output.** There is no "parsing problem" vs "manipulation problem" — both steps are
always present. What varies is the `parse` technique and the `manip` technique, and
which one carries the difficulty. Selection (Step 1) uses those tags to guarantee two
problems that don't feel alike.

`parse`: `delimited` (CSV/kv/lines) · `nested` (brackets/config) · `tokens`
(expression/sequence) · `encoded` (RLE/cipher) · `extract` (freeform, find/match).
`manip`: `group-agg` · `sort-rank` · `merge-reshape` · `window` · `grid` ·
`replay` (stateful) · `count-sum`.

Difficulty is calibrated to the real thing: ~20 min/problem, exact output, 2–3 real
edge cases. No standalone toys — the once-trivial mechanics (RLE, cipher, template)
only appear welded to a manipulation step that makes them fill a slot.

| ID | parse | manip | est_min | Blends |
|---|---|---|---|---|
| `sales-by-region` | delimited | group-agg | 18 | Parse `region,product,amt` lines → totals per region, sorted desc, ties alpha |
| `log-error-summary` | extract | count-sum | 20 | Parse `ts level msg` log lines → count errors per hour → busiest hours |
| `merge-time-ranges` | tokens | merge-reshape | 18 | Parse `HH:MM-HH:MM` strings → merge overlaps → emit merged ranges |
| `score-leaderboard` | delimited | sort-rank | 18 | Parse `name:score` entries → sum per name → top-N with rank, tie by name |
| `config-depth` | nested | count-sum | 20 | Parse nested bracket/config string → report max depth / per-level counts |
| `expr-eval-ltr` | tokens | replay | 20 | Evaluate space-delimited `+ - *` **left-to-right, no precedence** (constrained) |
| `rle-normalize` | encoded | merge-reshape | 15 | Decode an RLE string → re-encode in canonical form (merge adjacent runs) |
| `inventory-replay` | delimited | replay | 20 | Parse `ADD/REMOVE qty item` txns → replay → final stock sorted, reject invalid |
| `matrix-spiral` | delimited | grid | 20 | Parse rows of ints into a grid → output spiral traversal order |
| `csv-quoted-col` | delimited | merge-reshape | 20 | Parse CSV with quoted fields containing commas → extract/join one column |
| `join-orders` | delimited | merge-reshape | 20 | Two record blocks → join on id → combined report, drop unmatched |
| `querystring-norm` | delimited | count-sum | 15 | Parse `k=v&k=v`, repeated keys → normalized, keys sorted, dup policy stated |
| `window-threshold` | tokens | window | 15 | Parse int sequence → first window of size k whose sum exceeds threshold |
| `template-render` | extract | merge-reshape | 15 | Parse `{placeholder}` template + data block → render, handle missing keys |
| `paginate-report` | delimited | merge-reshape | 15 | Parse records → chunk into pages of k → format with page headers + partial last |

---

## Step 1 — Select the two problems

Read `coderbyte_metrics.csv` if it exists. Weight each problem:

```
weight = (1 / (attempts + 1)) + fail_rate_first + slow_rate
```

where `fail_rate_first` = fraction of attempts where `hidden_tests_passed_first <
hidden_tests_total`, and `slow_rate` = fraction where `secs_to_first_submit > est_min*60`.

Pick **two problems that use different `manip` techniques** (and ideally different
`parse` techniques) whose `est_min` sum to **38–46** — this makes the session load
match a real ~45-min take-home instead of two toys or two monsters. Among valid pairs,
maximize combined weight. Never repeat a problem seen in the last 3 sessions. Default
difficulty **medium** (ask only if the user wants light/challenging).

Tell the user: "CoderByte drill: 2 problems, ~{sum est_min} min target, 3-hour cap.
Graded on hidden tests. P1 = {parse}/{manip}, P2 = {parse}/{manip}. Independent."

---

## Step 2 — Generate both problems

For each problem, using the Write tool:
- Write `coderbyte/problem_{N}.py` — overwrite any existing file (no dated names).
- File contains: a docstring with the FULL spec (user must not need the chat), the
  function stub with `pass`, and exactly ONE commented sample input→output.
- Do NOT put edge cases or the hidden tests in the file. The sample must look benign;
  the hidden tests are where the edge cases live.

Design the **hidden test set** (hold it yourself — do not write it to a file the user
edits): 5–8 cases per problem covering empty input, single element, ties, boundaries,
duplicates, and one "exact-format" trap (trailing space, capitalization, int vs str).
Record `hidden_tests_total` per problem. Adversarial rule: a plausible-but-wrong
solution must fail at least 2 hidden cases.

---

## Step 3 — Run the session

Present both problem statements (paste both files). Say: "Both problems are yours.
Tell me which you're starting and say 'ready'."

### Per-problem flow
1. **On "ready":** run `date +%s` → `t_start`.
2. **While working:** stay silent. If the user asks for help, give one targeted hint
   and increment `hints_used` (flag that this wouldn't be available on the real thing).
3. **On "submit"/"done":** run `date +%s` → `t_first_submit`. Read `problem_{N}.py`,
   run their function against the FULL hidden set via a temporary harness (write it to
   `coderbyte/.grade_{N}.py`, run, delete).
   - Report `X / total passed`.
   - For each FAIL, reveal the **input only** (and the actual output they produced) —
     NOT the expected output. Mirror CoderByte: you learn a case failed, you reason why.
   - Record `hidden_tests_passed_first`.
4. **Iterate:** let them fix and re-submit until all pass, OR they say "reveal" (then
   show expected outputs and stop). Run `date +%s` → `t_final` at all-pass or reveal.
   Record `hidden_tests_passed_final`.
5. Move to the other problem.

Compute per problem:
- `secs_to_first_submit = t_first_submit - t_start`
- `secs_debug = t_final - t_first_submit`
- `secs_total = t_final - t_start`

---

## Step 4 — Debrief & record

After both problems, print the session table:

| # | problem_id | parse/manip | 1st submit | 1st pass | final pass | debug | total | hints | lines |
|---|---|---|---|---|---|---|---|---|---|

**First-submit pass rate is the headline** — on a real take-home you can't iterate
freely, so call it out. Then persist BOTH artifacts:
- Append one row per problem to `coderbyte_metrics.csv`.
- Append a dated narrative block per problem to `coderbyte_reviews.md` (schema below).

---

## coderbyte_metrics.csv

Path: `/Users/eric/projects/learn-python/coderbyte_metrics.csv`
Columns: `date,problem_id,parse,manip,difficulty,est_min,secs_to_first_submit,hidden_tests_total,hidden_tests_passed_first,secs_debug,hidden_tests_passed_final,secs_total,hints_used,lines_written`

- `parse` / `manip`: the technique tags from the pool table
- `secs_to_first_submit`: start → first submit (target: ≤ `est_min`*60 — want down)
- `hidden_tests_passed_first`: the realism metric — want this == `hidden_tests_total`
- `secs_debug`: first submit → all-pass/reveal
- `lines_written`: non-blank, non-comment lines at final

---

## coderbyte_reviews.md

Path: `/Users/eric/projects/learn-python/coderbyte_reviews.md`
Narrative history, mirroring `drill_reviews.md`. Per session add a
`## YYYY-MM-DD — Session N` header, then per problem a
`### {problem_id} — {parse}/{manip}` block with:
- The metrics table with ✅/❌ vs targets (1st submit ≤ `est_min`*60; 1st pass == total; debug 0; hints 0).
- **Analysis:** which hidden cases failed and the root-cause bug or wrong assumption.
- **Pattern to internalize:** the edge-case habit that would have caught it.
- **Cross-session trend:** for this `manip` technique, is first-submit accuracy improving, and which edge-case types (empty / ties / exact-format) keep biting?
