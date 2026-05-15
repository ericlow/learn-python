---
name: db-session-review
description: >
  Generate the end-of-session report for a database interview session, score the
  rubric, analyze trends, and write results to db_session_metrics.csv and
  db_session_reviews.md. Use when the candidate finishes a DB session, says
  "wrap up", "how did I do", or "end session" after a database practice session.
  Do not use during the session.
---

# DB Session Review — Post-Mortem

## Step 0: Load the Rubric

Read two files (both in `problems/`):
1. **`[problem]_session_notes.md`** — per-phase observations written during the session
2. **`[problem]_overview.md`** — problem-specific rubric

Rubric: 5 dimensions scored 1–3, total out of 15.

**Correctness, Schema Design, and SQL Fluency** criteria are problem-specific — use the overview file.

**Communication and Speed** are standard:

| Score | Communication | Speed |
|-------|--------------|-------|
| 1 | Silent, no schema questions, jumps to DDL | Doesn't complete Phase 2 in 60 min |
| 2 | Asks clarifying questions, explains schema decisions before writing DDL | Completes all 3 phases in 60 min |
| 3 | Proactively identifies ambiguity, articulates normalization tradeoffs, flags constraint edge cases | Finishes with time for extension discussion |

| Score | Schema Design | SQL Fluency |
|-------|--------------|-------------|
| 1 | Missing FKs, wrong normalization, no constraints | Wrong join type, missing NULL handling, no parameterization |
| 2 | Correct tables and relationships, appropriate FKs | Correct joins, handles NULLs, parameterized queries |
| 3 | Optimal normalization, appropriate indexes and constraints, explains tradeoffs | Elegant queries, correct aggregation/window/transaction logic, articulates tradeoffs |

---

## Step 1: Generate the Session Summary

Active time must be calculated from pause/resume timestamps — never use wall time.

```
═══════════════════════════════════════
DB SESSION SUMMARY
═══════════════════════════════════════

Active Time: N min (calculated from pause/resume timestamps)
Schema Mode: given | discovered

Phase Breakdown:
├─ Session Start:      HH:MM:SS
├─ Phase 1 Complete:   HH:MM:SS  (N min active)  ✓ / ❌
├─ Phase 2 Complete:   HH:MM:SS  (N min active)  ✓ / ❌
├─ Phase 3 Complete:   HH:MM:SS  (N min active)  ✓ / ❌
└─ Session End:        HH:MM:SS

Time Breakdown:
├─ pct_coding:      X%  (writing DDL or Python query functions)
├─ pct_teaching:    X%  (coach explaining SQL syntax or psycopg2)
└─ pct_discussion:  X%  (schema design, tradeoffs, requirements)
(goal: pct_teaching decreases over time)

Rubric Score: X/15
├─ Correctness:     X/3
├─ Schema Design:   X/3
├─ SQL Fluency:     X/3
├─ Communication:   X/3
└─ Speed:           X/3

Overall Assessment: [No Hire / Hire / Strong Hire]

Schema tracking: constraints identified before coding / missed (revealed by driver) / normalization level (appropriate / over / under)
═══════════════════════════════════════
```

---

## Step 2: Read db_session_reviews.md and Analyze Trends

Before writing, read `db_session_reviews.md` to understand prior DB sessions.

Analyze across the last 3–5 sessions:
- **Rubric score trajectory** — improving, flat, or regressing?
- **Schema design** — are schemas getting cleaner? Fewer missing constraints?
- **SQL fluency** — is join reasoning improving? Window functions landing faster?
- **pct_teaching** — is SQL teaching overhead decreasing?
- **Recurring weaknesses** — same constraint missed, same NULL handling error?

---

## Step 3: Write Detailed Analysis to db_session_reviews.md

Append a new entry:

```markdown
## YYYY-MM-DD — [Problem Name]

**Problem:** [Brief description] (Database, [N] phases) | **Domain:** [domain]
**Level:** [junior/mid/senior/staff] | **Baseline:** [practice/generate] | **DDL:** [coach/generate]
**Phase 2:** [challenge] | **Phase 3:** [challenge] | **Active Time:** ~[N] min | **Phases:** [N]/3

### Rubric Scores

| Dimension | Score | Level |
|-----------|-------|-------|
| Correctness | X/3 | [No Hire / Hire / Strong Hire] |
| Schema Design | X/3 | [No Hire / Hire / Strong Hire] |
| SQL Fluency | X/3 | [No Hire / Hire / Strong Hire] |
| Communication | X/3 | [No Hire / Hire / Strong Hire] |
| Speed | X/3 | [No Hire / Hire / Strong Hire] |
| **Total** | **X/15** | **[Overall Assessment]** |

### Dimension Analysis

Per dimension: ✅ what worked, ❌ what didn't. For Speed: time per phase vs target + primary cause of slowness.

### Trend Analysis

- **Score trajectory:** [e.g., first DB session / 9 → X — improving / flat]
- **pct_teaching:** [SQL teaching overhead — decreasing ✅ / not improving ❌]
- **Schema quality:** [constraints improving / same gaps / new gaps]
- **Recurring weakness:** [e.g., "NULL handling in LEFT JOIN — 2nd session in a row"]

### Key Strengths
- [Strength 1]
- [Strength 2]

### Key Improvement Areas
1. **[Area]** — [Specific observation and recommendation]
2. **[Area]** — [Specific observation and recommendation]

### Flashcard Topics from This Session
- [SQL concept] — [what to remember]
- [SQL concept] — [what to remember]

---
```

---

## Step 4: Write to db_session_metrics.csv

Append one row to `db_session_metrics.csv`:

| Field | Value |
|-------|-------|
| `date` | YYYY-MM-DD |
| `problem_name` | Coaching guide filename |
| `domain` | Domain name |
| `level` | junior / mid / senior / staff |
| `baseline_mode` | practice / generate |
| `ddl_mode` | coach / generate |
| `phase2_challenge` | Challenge name drawn from pool |
| `phase3_challenge` | Challenge name drawn from pool |
| `total_minutes` | Active time (sum of active segments) |
| `phase1_minutes` | Active time for Phase 1 |
| `phase2_minutes` | Active time for Phase 2 |
| `phase3_minutes` | Active time for Phase 3 |
| `pct_coding` | % writing DDL or query functions |
| `pct_teaching` | % coach explaining SQL/psycopg2 |
| `pct_discussion` | % design, tradeoffs, requirements |
| `rubric_score` | Total out of 15 |
| `correctness` | 1–3 |
| `schema_design` | 1–3 |
| `sql_fluency` | 1–3 |
| `communication` | 1–3 |
| `speed` | 1–3 |
| `assessment` | No Hire / Hire / Strong Hire |
| `constraints_listed` | Count of constraints identified before coding |
| `constraints_missed` | Count of constraints revealed by driver |

Create the file with a header row if it doesn't exist yet.
