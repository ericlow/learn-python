---
name: session-review
description: >
  Generate the end-of-session report, score the rubric, analyze trends across
  sessions, and write results to session_metrics.csv and session_reviews.md.
  Use when the candidate finishes a session, says "wrap up", "let's review",
  "how did I do", or "end session". Do not use during the session — this skill
  is only for post-session review and record keeping.
---

# Session Review — Post-Mortem

## Step 0: Load the Rubric

Before scoring anything, read two files for this session (both in the `problems/` directory):
1. **`[problem]_session_notes.md`** — primary source of per-phase observations written during the session
2. **`[problem]_overview.md`** — contains the problem-specific rubric

If `_session_notes.md` does not exist (older session format), fall back to reading the full coaching guide.

The rubric has 5 dimensions scored 1–3:
- **1 = No Hire** — below expectations
- **2 = Hire** — meets expectations
- **3 = Strong Hire** — exceeds expectations

**Correctness, Code Quality, and Data Structures** criteria are problem-specific — use the criteria from the overview file's rubric section.

**Communication and Speed** are standard across all problems:

| Score | Communication | Speed |
|-------|--------------|-------|
| 1 | Silent, jumps to code, no clarifying questions | Doesn't finish Req 2 in 60 min |
| 2 | Asks clarifying questions, explains approach before coding | Finishes all 3 reqs in 60 min |
| 3 | Proactively identifies ambiguity, articulates tradeoffs, flags complexity | Finishes with time for corner cases and complexity discussion |

Score each dimension based on what actually happened in the session, then sum for a total out of 15.

---

## Step 1: Generate the Session Summary

**Active time must be calculated from pause/resume timestamps — never use wall time.**
Wall time is unreliable due to intermittent pauses. Instead:
1. Collect all START, RESUMED, PAUSED, and END timestamps from the session notes and conversation
2. Sum only the active segments: each segment runs from a START or RESUMED timestamp to the next PAUSED or END timestamp
3. Report active time as the sum of those segments

```
Active time calculation example:
  21:45:23 START → 21:45:52 PAUSE  =  0.5 min
  22:06:02 RESUME → 22:09:18 PAUSE =  3.3 min
  22:57:47 RESUME → 23:25:12 PAUSE = 27.4 min
  13:54:10 RESUME → 14:26:36 END   = 32.4 min
  ─────────────────────────────────────────
  Active total:                      63.6 min ≈ 64 min
```

Use this active total (not wall time) in the summary, CSV, and speed assessment.

```
═══════════════════════════════════════
SESSION SUMMARY
═══════════════════════════════════════

Active Time: 52 min (calculated from pause/resume timestamps)

Milestone Breakdown:
├─ Session Start:          10:00:00
├─ Code Runs:              10:08:00  (8 min active)   ✓ Good
├─ Requirements Complete:  10:38:00  (30 min active)  ✓ On pace
├─ Tests Pass:             10:48:00  (10 min active)  ✓ Good
└─ Session End:            10:52:00

Segment Durations (active time only, pauses excluded):
├─ Syntax fixes:           8 min   (Target: <10 min)
├─ Core implementation:    30 min  (Target: 25-35 min)
└─ Testing/refinement:     10 min  (Target: 5-10 min)

Time Breakdown:
├─ pct_coding:      X%  (time actually writing code)
├─ pct_teaching:    X%  (coach explaining Python syntax/APIs)
└─ pct_discussion:  X%  (design, tradeoffs, requirements, meta)
(should sum to 100%; goal: pct_teaching decreases over time)

Rubric Score: X/15
├─ Correctness:       X/3  (No Hire=1, Hire=2, Strong Hire=3)
├─ Code Quality:      X/3
├─ Data Structures:   X/3
├─ Communication:     X/3
└─ Speed:             X/3

Overall Assessment: [No Hire / Hire / Strong Hire]

Edge case tracking:
- Cases listed by candidate before implementation: [list]
- Cases missed (revealed by driver): [list]
- Trend vs prior sessions: [improving / same / regressing]
═══════════════════════════════════════
```

---

## Step 2: Read session_reviews.md and Analyze Trends

Before writing anything, read `session_reviews.md` to understand prior sessions.

Analyze trends across the last 3-5 sessions:

- **Rubric score trajectory** — is the total score improving, flat, or regressing?
- **Speed** — is syntax fix time decreasing? Is core implementation time tightening?
- **pct_teaching** — is the teaching overhead decreasing over time? This is the key leading indicator of Python fluency progress.
- **Data structures** — is the candidate making better structure choices earlier, or still hitting the same patterns?
- **Edge cases** — is the ratio of missed-to-listed edge cases improving?
- **Recurring weaknesses** — are the same improvement areas appearing session after session?

Surface the trend analysis in the detailed write-up below AND present it directly to the candidate in the conversation (not just written to the file). The candidate must see the cross-session table and trend narrative — this is the most important part of the review.

**Present ALL of the following to the candidate in the conversation — every item, every session:**
1. **Cross-session rubric table** — Date | Problem | Type | Score | Correctness | Data Structs | Communication | Speed | pct_teaching
2. **Time breakdown trend table** — Date | Problem | pct_coding | pct_teaching | pct_discussion | Score — this shows progress on Python fluency and time allocation
3. **Written trend narrative** — score trajectory, pct_teaching, data structures, speed, edge cases
4. **Full dimension-by-dimension analysis** (✅/❌ per dimension) — not just the summary box
5. **Key strengths** — what went well this session
6. **Key improvement areas** with specific recommendations
7. **Flashcard topics** from this session

The candidate must see all of this. Do not summarize or omit — progress data (positive or negative) is what the candidate is here for.

---

## Step 3: Write Detailed Analysis to session_reviews.md

Append a new entry to `session_reviews.md` following this exact format:

```markdown
## YYYY-MM-DD — [Problem Name]

**Problem:** [Brief description] ([OOP / Algorithmic], [N] reqs)
**Active Time:** ~[N] min
**Reqs Completed:** [N] / [N]

### Rubric Scores

| Dimension | Score | Level |
|-----------|-------|-------|
| Correctness | X/3 | [No Hire / Hire / Strong Hire] |
| Code Quality | X/3 | [No Hire / Hire / Strong Hire] |
| Data Structures | X/3 | [No Hire / Hire / Strong Hire] |
| Communication | X/3 | [No Hire / Hire / Strong Hire] |
| Speed | X/3 | [No Hire / Hire / Strong Hire] |
| **Total** | **X/15** | **[Overall Assessment]** |

### Dimension Analysis

**Correctness — X/3 ([Level])**
- ✅ [What worked]
- ❌ [What didn't]

**Code Quality — X/3 ([Level])**
- ✅ [What worked]
- ❌ [What didn't]

**Data Structures — X/3 ([Level])**
- ✅ [What worked]
- ❌ [What didn't]

**Communication — X/3 ([Level])**
- ✅ [What worked]
- ❌ [What didn't]

**Speed — X/3 ([Level])**
- [Time per req vs target]
- [Primary cause of slowness if behind]

### Trend Analysis

- **Score trajectory:** [e.g., 9.5 → 11 → X — improving / flat / regressing]
- **pct_teaching:** [e.g., 30% → 22% → X% — teaching overhead decreasing ✅ / not improving ❌]
- **Speed:** [e.g., syntax fix time trending down / same pattern as last session]
- **Recurring weakness:** [e.g., "Data structures: 3rd session in a row with a structure pivot needed in Req 3"]
- **Edge cases:** [e.g., "Listed 2, missed 1 — same as last session; not yet improving"]

### Key Strengths
- [Strength 1]
- [Strength 2]

### Key Improvement Areas
1. **[Area]** — [Specific observation and recommendation]
2. **[Area]** — [Specific observation and recommendation]

### Flashcard Topics from This Session
- [Python concept] — [what to remember]
- [Python concept] — [what to remember]

---
```

---

## Step 4: Write to session_metrics.csv

Append one row to `session_metrics.csv` with these fields:

| Field | Value |
|-------|-------|
| `date` | Today's date (YYYY-MM-DD) |
| `problem_type` | `OOP` or `Algorithmic` |
| `problem_name` | Name of the coaching guide file |
| `total_minutes` | Active time in minutes (sum of active segments from pause/resume timestamps — not wall time) |
| `syntax_fix_minutes` | Start → Code Runs |
| `core_impl_minutes` | Code Runs → Requirements Complete |
| `test_minutes` | Requirements Complete → Session End |
| `pct_coding` | % of active time writing code |
| `pct_teaching` | % of active time on Python syntax/APIs |
| `pct_discussion` | % of active time on design/tradeoffs |
| `rubric_score` | Total out of 15 |
| `correctness` | 1–3 |
| `code_quality` | 1–3 |
| `data_structures` | 1–3 |
| `communication` | 1–3 |
| `speed` | 1–3 |
| `assessment` | `No Hire`, `Hire`, or `Strong Hire` |
| `edge_cases_listed` | Count of edge cases candidate listed before implementation |
| `edge_cases_missed` | Count of edge cases revealed by driver that candidate missed |

Create the file with a header row if it doesn't exist yet.

---

## Step 5: Git Workflow

1. **Update session notes** — append Req N evaluation to `[problem]_session_notes.md` before committing
2. **Commit on the session branch** — stage `solution.py` and `problems/` and commit with message: `"Session: [Problem Name] — all N reqs complete"`
3. **Switch to main** — `git checkout main`
4. **Write review files** — append to `session_reviews.md` and `session_metrics.csv` on main
5. **Commit on main** — stage and commit the review files with message: `"Add session review and metrics for [Problem Name]"`
