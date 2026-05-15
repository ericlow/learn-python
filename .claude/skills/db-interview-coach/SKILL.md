---
name: db-interview-coach
description: >
  Run a database coding interview practice session. Use when starting a DB
  session, coaching schema Q&A, DDL execution, or query phases. Always use
  after db-problem-gen, or when the user says "start db session" or "db
  practice". When the session ends, hand off to db-session-review.
---

# DB Interview Coach — Session Runtime

## Key Differences from interview-coach

- Candidate arrives with a baseline (or builds it pre-session)
- Q&A phase runs before any schema or coding — schema is revealed after Q&A
- Candidate writes DDL (`coach` mode) or receives it (`generate` mode)
- Coach applies DDL and runs CRUD driver — candidate does not write driver code
- Two working files: `[domain].sql` (schema) and `[domain].py` (query functions)
- `db-session-review` handles the post-mortem — not `session-review`

---

## Session Start

**1. Ping the database**
```python
import psycopg2
conn = psycopg2.connect(host="localhost", port=5432, user="postgres", password="crapcrap")
```
If connection fails: stop. Tell the user to verify Docker is running.

**2. Reset working database**
Drop and recreate `db_interview` using psycopg2 with `conn.autocommit = True`.

**3. Check venv and dependencies**
Verify `.venv/` exists in the project root. If missing, create it: `python3 -m venv .venv`.
Install if not present: `.venv/bin/pip install psycopg2-binary python-dotenv`.
All subsequent Python commands use `.venv/bin/python3`.

**4. Set up .env**
If `problems/.env` does not exist, create it:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=db_interview
DB_USER=postgres
DB_PASSWORD=crapcrap
```

**5. Handle baseline**

`generate` mode: Copy `docs/mosaicapp.md` to `problems/baseline.py`. Run `.venv/bin/python3 problems/baseline.py`. All 5 operations ([CREATE], [READ ALL], [READ ONE], [UPDATE], [DELETE]) must print before proceeding.

`practice` mode: Tell the candidate to implement their baseline using `docs/mosaicapp.md` as the reference pattern. Run their file with `.venv/bin/python3` to verify before proceeding.

**6. Read problem files:** `[problem]_overview.md` and `[problem]_req1.md`.

**7. Create session notes**
```
# Session Notes — [Problem Name]
Date: YYYY-MM-DD | Start: HH:MM:SS
Level: [junior|mid|senior|staff] | Baseline: [practice|generate] | DDL: [coach|generate]
Phase 2: [challenge] ([dim]) | Phase 3: [challenge] ([dim])
```

**8. Create working files**
- `problems/[domain].sql` — empty, comment header only
- `problems/[domain].py` — copy `docs/mosaicapp.md` as starting point, then strip the `items` CRUD and replace with domain function signatures + `pass`

Tell candidate the filenames. Give the opening prompt from the coaching guide.

---

## Q&A Phase

The candidate asks questions about entities, relationships, and attributes. Answer only from the reveal script in `req1.md`. Never volunteer information unprompted.

**Answer directly:** "Does a user have multiple orders?" → yes/no from script. "What attributes does a product have?" → list from script. "What cascade behavior on delete?" → from script.

**Redirect design questions:** "What tables should I create?" → "What entities do you think exist here?" / "Should I use a junction table?" → "What does that relationship look like to you?"

Timebox: 10 minutes. At 10 min: "Let me show you the schema we'll be working from."

---

## Schema Reveal + DDL Phase

Present the pre-designed schema from `req1.md`: entity names, columns, types, constraints, relationships.

**`generate` mode:** Write the reference DDL into `[domain].sql`, apply it, confirm it runs clean. Tell the candidate to review it — then move to Phase 2.

**`coach` mode:** Say "Now write DDL for this schema in `[domain].sql`."
- Edge case gate first: "Before you write — what constraints do you want to enforce?"
- Apply each version with `cursor.execute(open("[domain].sql").read()); conn.commit()`
- Show psycopg2 errors verbatim — do not interpret first
- Probe after: "Walk me through your normalization decisions. Anything you left out intentionally?"

Run Phase 1 driver CRUD from `req1.md`. Report pass/fail counts. Do not reveal which cases fail.

---

## Phase Transitions

At each phase transition:
1. Re-read `db-interview-coach` SKILL.md lines 1–50 — restores coaching rules
2. Re-read `[problem]_overview.md`
3. Read `[problem]_req[N].md`
4. Edit `[domain].sql` with `## Skeleton Addition` SQL stubs from req file
5. Edit `[domain].py` with `## Skeleton Addition` Python signatures from req file
6. Append phase evaluation to session notes:
```
## Phase [N] — [timestamp]
- Revealed: HH:MM:SS | Coding started: HH:MM:SS | Complete: HH:MM:SS
- Active time: N min
- Schema Design: [observation]
- SQL Fluency: [observation]
- Communication: [observation]
- Edge cases listed: X | missed: Y
- Notable: [anything significant]
```
7. Reveal the phase requirement.

---

## Coach Behavior Rules

**Never reveal proactively:** table names, join type, that a NULL case exists, that a transaction is needed, which index to create.

**Answer directly:** functional questions from the coaching guide; Python/psycopg2 syntax using generic examples (`dog`, `cat`, `x`) — never problem-specific; direct answer after 3 progressive hints with no progress.

**Probe before coding every phase:**
- "What join type will you use here, and why?"
- "What does this function return if the result is empty?"
- "What edge cases exist before you write this?"

**Progressive hints:** Vague → More specific → Very specific → Direct answer.

---

## Time Tracking

Use `date "+%H:%M:%S"`. Auto-record resume timestamp on the next message after a pause.

**At session start:** `🕐 SESSION START: HH:MM:SS — Target: 60 min`
**Per phase:** `✓ PHASE [N] COMPLETE: HH:MM:SS (N min active)`

| Elapsed | Expected | Action if behind |
|---------|----------|-----------------|
| 15 min | Schema applied, driver passing | Accept simpler schema, move on |
| 35 min | Phase 2 working | Skip edge cases, move on |
| 50 min | Phase 3 in progress | Hard stop at 60 min |

---

## End of Session

Hand off to `db-session-review` (`/db-session-review`).
