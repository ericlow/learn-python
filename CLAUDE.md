# Interview Coaching Framework

## What This File Is
Routing and formatting rules that apply to every interaction. Session mechanics, coaching behavior, time tracking, and problem generation are in skills — not here.

---

## Problem Type Selection

At the start of each session, check `session_metrics.csv` and recommend the underrepresented problem type:
- If recent sessions are mostly OOP → recommend algorithmic
- If recent sessions are mostly algorithmic → recommend OOP
- If balanced → your choice

Use the `oop-problem-gen` skill for open-ended OOP system design problems (FAANG-style).
Use the `applied-oop-problem-gen` skill for applied OOP problems (interface given upfront, extensibility as the core challenge).
Use the `algo-problem-gen` skill for algorithmic problems.
Use the `interview-coach` skill to run the session after a problem is generated.
Use the `db-problem-gen` skill for database interview problems (schema design, SQL, psycopg2).
Use the `db-interview-coach` skill to run a DB session after `db-problem-gen` finishes.

The user always has final say and can override the recommendation.

## Difficulty

Both `algo-problem-gen` and `applied-oop-problem-gen` accept a difficulty: **light / medium / challenging**.
`db-problem-gen` accepts a difficulty: **easy / medium / hard**.
Ask if the user has not specified. Default to medium if no preference given.

DP is never in scope — it is a Google-specific pattern and not a target for these sessions.
Challenging problems may include trees, graphs, BFS/DFS, heaps, and topological sort.

---

## Routing Process Changes

When the user requests a change to the coaching process, think critically before writing it down:

1. **Does it govern how sessions are run?** → `interview-coach` (OOP/algo) or `db-interview-coach` (DB)
2. **Does it govern how problems are designed?** → relevant problem generator skill(s)
3. **Does it apply to all OOP and algorithmic types?** → all OOP/algo generator skills
4. **Does it apply to DB sessions only?** → `db-problem-gen` and/or `db-interview-coach`
5. **Does it apply only to one OOP style?** → `oop-problem-gen` (open-ended) or `applied-oop-problem-gen` (interface-first), not both
6. **Is it already covered elsewhere?** → update existing entry, don't duplicate

---

## Available Slash Commands
On every conversation start, list these skills
- `/oop-problem-gen` — generate an open-ended OOP system design problem (FAANG-style)
- `/applied-oop-problem-gen` — generate an applied OOP problem with interface given upfront (matches real interview patterns)
- `/algo-problem-gen` — generate an algorithmic coding problem
- `/interview-coach` — run a practice session (also auto-invoked after OOP/algo generator finishes)
- `/session-review` — end-of-session report, rubric scoring, and write results to session_metrics.csv
- `/db-problem-gen` — generate a database interview problem (schema design, SQL, psycopg2)
- `/db-interview-coach` — run a database practice session (also auto-invoked after db-problem-gen finishes)
- `/db-session-review` — end-of-DB-session report, rubric scoring, and write results to db_session_metrics.csv
- `/mechanical-drills` — timed single-mechanic Python drills to build fluency (tracks to drill_metrics.csv)
- `/combo-drills` — timed 2–3 mechanic combo drills; chains mechanics from the drill pool (tracks to combo_metrics.csv)
- `/fundamentals-screen` — 4–6 standalone exercises at the fluency + design awareness tier; mirrors real fundamentals screens (tracks to screen_metrics.csv)
- `/coderbyte-drill` — CoderByte take-home sim; 2 independent data-parsing problems graded on hidden tests, exact output (tracks to coderbyte_metrics.csv)

---

## Response Formatting

- Start every response with 10 fire emojis so the user can easily spot the start of the response
- Only use ✅ and ❌ emojis otherwise in responses

---

## Session Git Workflow

Each session runs on its own branch: `session/[slug]` (e.g., `session/260515-fitness-activity`).
The coach creates and checks out this branch at session start, and returns to `main` after session-review.

---

## File Size Limits

On every conversation start, run these checks using bash `wc -l` — do NOT read the files into memory:

```bash
wc -l CLAUDE.md .claude/skills/*/SKILL.md
```

Limits:
- `CLAUDE.md` — 100 lines max
- Any `SKILL.md` — 175 lines max

If any file exceeds its limit, warn immediately before doing anything else:
> "⚠️ [filename] is N lines — over the [limit]-line limit. Suggest trimming before this session."

Do not block the session on this warning — just surface it once at the top.
