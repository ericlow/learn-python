---
name: combo-drills
description: >
  Run timed multi-mechanic Python combo drills. Each drill chains 2–3 mechanics
  from the mechanical drills pool into a single function (10–20 lines, 6-minute
  target). No design questions, no idiom phase. Builds fluency across mechanic
  boundaries. Tracks to combo_metrics.csv. Triggers on "combo drills", "combo
  drill session", or "chain drills".
---

# Combo Drills Skill

## Purpose
Bridge mechanical drills (single mechanic, 3 min) and fundamentals screen (design
questions). Each problem requires 2–3 mechanics to interact — the output of one
feeds the next. Correctness and speed are the only targets.

---

## Combo Pool

| ID | Mechanics | What it chains |
|---|---|---|
| `lcomp-sort` | list-comp, sorting | Filter via comprehension → sort result by key |
| `lcomp-counter` | list-comp, counter | Filter list → count field frequencies in result |
| `lcomp-fstring` | list-comp, fstring | Filter list → format each item as labeled string |
| `defdict-sort` | defaultdict, sorting | Group into defaultdict → sort each group |
| `defdict-lcomp` | defaultdict, list-comp | Group into defaultdict → filter each group |
| `defdict-counter` | defaultdict, counter | Accumulate groups → count top contributor per group |
| `dictcomp-sort` | dict-comp, sorting | Build dict via comprehension → sort by value |
| `zip-dictcomp` | zip-enumerate, dict-comp | Build mapping from two lists → invert it |
| `zip-sort` | zip-enumerate, sorting | Zip two lists into pairs → sort by a field |
| `strops-counter` | string-ops, counter | Normalize strings → count frequencies |
| `strops-lcomp` | string-ops, list-comp | Clean/parse strings → filter or transform |
| `strops-sort` | string-ops, sorting | Extract field from strings → sort by it |
| `counter-sort` | counter, sorting | Count frequencies → top-N sorted alpha on tie |
| `counter-fstring` | counter, fstring | Count → format leaderboard strings |
| `heapq-counter` | heapq, counter | Count frequencies → find top-N via heap |
| `date-sort` | date, sorting | Parse date strings → sort records chronologically |
| `date-lcomp` | date, list-comp | Parse dates → filter records within a date range |
| `date-fstring` | date, fstring | Parse dates → format as human-readable output |
| `json-lcomp` | json, list-comp | Parse JSON records → filter by a field condition |
| `json-sort` | json, sorting | Parse JSON records → sort by numeric field |
| `json-counter` | json, counter | Parse JSON → count field value frequencies |
| `json-date` | json, date | Parse JSON with date fields → filter by date range |
| `strops-counter-sort` | string-ops, counter, sorting | Normalize → count → return top-N sorted |
| `json-lcomp-sort` | json, list-comp, sorting | Parse JSON → filter by condition → sort result |
| `date-lcomp-sort` | date, list-comp, sorting | Parse dates → filter range → sort chronologically |

---

## Step 1 — Select combos

Read `combo_metrics.csv` if it exists. For each mechanic, aggregate across all
combos that contain it:

```
mechanic_attempts  = rows where mechanic_1, mechanic_2, or mechanic_3 equals this mechanic
mechanic_slow_rate = fraction where secs_to_done > 360
mechanic_bug_rate  = fraction where secs_bug_fixes > 0
mechanic_weight    = (1 / (mechanic_attempts + 1)) + mechanic_slow_rate + mechanic_bug_rate
```

If `combo_metrics.csv` has fewer than 6 rows, also read `drill_metrics.csv` and
add `(slow_rate + non_idiomatic_rate)` per category to the mechanic weight as a
bootstrap signal.

Pick 6 combos that maximize coverage of highest-weighted mechanics. Prefer combos
not seen recently. No combo repeated within the same session.

Tell the user: "Today's combos: [list IDs]. Starting with combo 1/6."

---

## Step 2 — Per-combo loop (repeat 6 times)

**Present the combo**
- Show combo_id, mechanics involved, problem statement, and one input/output example.
- Generate `combos/combo_N.py` using the Write tool (not cat/heredoc).
- Docstring must contain the full problem — candidate must not need to refer to chat.
- Say "Let me know when you're ready to start."

**When user says ready:**
- Run `date +%s` → record as `t_start`

**While user works:**
- Help if asked. Increment `hints_used`. Show relevant signatures with generic
  variable names (`items`, `data`, `records`) — never names from the problem.
  Never provide a working skeleton or prototype.

**When user says done:**
- Run `date +%s` → `t_first_done` immediately
- Read the `.py` file; run against happy path and the tricky case
- If correct: `t_correct = t_first_done`, `secs_bug_fixes = 0`
- If defects: name the specific failure, let them fix, re-run until correct →
  run `date +%s` → `t_correct`

No idiom phase. Logically correct = done.

**Compute:**
- `secs_to_done = t_first_done - t_start`
- `secs_bug_fixes = t_correct - t_first_done`
- `secs_total = t_correct - t_start`

**Report ✅ / ❌ per combo:**
- `secs_to_done` vs 360s target
- `secs_bug_fixes` — goal is 0

**After each combo — immediately append one row to `combo_metrics.csv`.**

---

## Step 3 — Session summary

After all 6 combos, print:

| # | combo_id | secs_to_done | secs_bug_fixes | secs_total | hints | lines |
|---|---|---|---|---|---|---|

**Intra-session trend:** is secs_to_done going down across combos? Are later combos
cleaner on first submission?

**Cross-session trend:** for each mechanic appearing in today's combos, show all
prior combo rows containing that mechanic — full history, not averaged. Call out
which mechanics caused the most bug_fixes today.

Render ASCII bar charts for secs_to_done per combo (mark the 360s target line).

---

## combo_metrics.csv

Path: `/Users/eric/projects/learn-python/combo_metrics.csv`
Columns: `date,combo_id,mechanic_1,mechanic_2,mechanic_3,secs_to_done,secs_bug_fixes,secs_total,hints_used,lines_written`

- `mechanic_3`: empty string for 2-mechanic combos
- `secs_to_done`: start → first done call (target: ≤ 360 — want down)
- `secs_bug_fixes`: first done → logically correct (target: 0)
- `secs_total`: sum of both phases

---

## Drill Generation Rules

- Mechanics must interact: output of one feeds the next — not parallel tasks
- 10–20 lines of solution code; single function; interface fully specified
- Include one tricky detail: empty input, duplicate keys, ties in sort, null JSON field
- Input data must be adversarial: wrong implementations must produce wrong output.
  Sort/filter problems need 4+ output records. Ties must expose a missing tie-break.
  JSON drills must include a null field. Date drills must include a boundary record.
- Generic variable names in examples (`x`, `items`, `data`, `records`)
