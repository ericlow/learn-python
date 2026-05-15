---
name: db-problem-gen
description: >
  Generate a database coding interview problem. Covers baseline setup, Q&A-based
  schema discovery, schema reveal, DDL execution, and two progressive query/design
  phases drawn from level-appropriate pools. Triggers on "database problem", "SQL
  interview", "db problem", "schema design practice". After generating,
  db-interview-coach governs the session.
---

# Database Interview Problem Generator

## What This File Is
Generates a DB interview problem: domain, baseline, Q&A reveal script, pre-designed
schema, and two phase challenges drawn from level-appropriate pools.

## What This File Is NOT
Not for OOP or algorithmic problems. Session mechanics live in `db-interview-coach`.

---

## Step 1: Gather Context

Ask:
1. **Domain?** (e-commerce, hospital, library, ride-share, event ticketing — or "surprise me")
2. **Level?** junior / mid / senior / staff
3. **Baseline mode?** `practice` (candidate builds it) or `generate` (auto-generate working code)
4. **DDL mode?** `generate` (coach writes DDL after schema reveal) or `coach` (candidate writes, coach guides toward plan)

Language: Python + psycopg2. Do not ask.

---

## Step 2: Note Baseline Mode

The baseline always uses `docs/mosaicapp.md` as the starting point — do not generate baseline code.

**`generate` mode:** The coach copies `docs/mosaicapp.md` to `baseline.py` at session start and runs it. Note this in the overview file so the coach knows what to do.

**`practice` mode:** The candidate builds their baseline pre-session using `docs/mosaicapp.md` as the reference pattern. Note this in the overview file.

---

## Step 3: Q&A Design

Design the full entity/relationship/attribute model, then write a reveal script the coach uses to answer candidate questions during the Q&A phase.

**Reveal script covers:**
- Every entity and its attributes (what exists, what doesn't)
- Every relationship (one-to-many vs many-to-many, FK direction)
- Business rules and constraints
- Boundary behaviors ("can a user have multiple X?", "what happens when Y is deleted?")

The coach answers only from this script. Never volunteers entity names or relationships unprompted.

---

## Step 4: Schema Design

Pre-design the schema the coach reveals after Q&A. Candidate does not design it — it is given.

| Level | Tables | Constraints |
|-------|--------|-------------|
| Junior | 1–2 | PK, NOT NULL, basic types |
| Mid | 2–3 + junction | FK, UNIQUE, CHECK |
| Senior | 3–5 | FK cascades, composite unique, deferred |
| Staff | 4+ with tradeoff | Normalization decision documented, indexes called out |

Include the reference DDL. This is what `coach` mode guides toward and `generate` mode produces directly.

---

## Step 5: Select Phase 2 and Phase 3

Draw one challenge from each pool for the given level. Prefer different `Dim` values between Phase 2 and Phase 3. Never draw the same challenge twice across sessions if avoidable.

**Phase 2 pool**

| Challenge | Lvl | Dim |
|---|---|---|
| CRUD functions + basic filters | J | query |
| ORDER BY + LIMIT (top-N) | J | query |
| Date filtering + IS NULL + COALESCE | J | query |
| Multi-table JOIN | M | query |
| UNION / UNION ALL | M | query |
| GROUP BY + HAVING | M | query |
| Self-join | M | query |
| CASE expressions | M | query |
| Date arithmetic + interval calculations | M | query |
| Multi-step business logic | M | concur |
| Soft delete | M | model |
| Subqueries in WHERE (IN / EXISTS) | M | query |
| Window fn — basic (ROW_NUMBER, RANK) | M | query |
| Greatest-N-per-group | Sr | query |
| Window fn — advanced (LAG/LEAD, running totals) | Sr | query |
| Time-based querying + temporal overlap | Sr | query |
| Correlated subquery + derived table | Sr | query |
| INTERSECT / EXCEPT | Sr | query |
| Audit trail (extend schema) | Sr | model |
| Schema evolution + backfill | Sr | migr |
| Batch ops (execute_values, COPY) | Sr | perf |
| Connection/cursor mgmt + error handling | Sr | backend |
| Denormalized counter sync (atomic SQL vs. locking) | Sr | concur |
| Complex window fn + frame clauses | St | query |
| Query optimization (EXPLAIN ANALYZE) | St | perf |
| Writeable CTEs | St | query |
| JSONB querying + GIN index | St | query |
| Denormalization | St | model |

**Phase 3 pool**

| Challenge | Lvl | Dim |
|---|---|---|
| Basic aggregation (COUNT/SUM/AVG) | J | query |
| Simple JOIN (inner, basic WHERE) | J | query |
| NULL in results (IS NULL, COALESCE) | J | query |
| Upsert (INSERT ON CONFLICT, idempotency) | M | integ |
| DISTINCT ON (Postgres) | M | query |
| INTERSECT / EXCEPT | M | query |
| Pagination — LIMIT/OFFSET | M | query |
| Transaction + race condition (FOR UPDATE) | Sr | concur |
| Cursor/keyset pagination + tradeoffs | Sr | perf |
| Indexing + partial indexes (EXPLAIN) | Sr | perf |
| Exclusion constraints + composite unique | Sr | integ |
| Isolation level reasoning | Sr | concur |
| Debugging: broken query (join explosion, NULL bug, duplicates) | Sr | query |
| Dynamic search / multi-filter (injection-safe) | Sr | integ |
| Full-text search (tsvector, GIN) | Sr | query |
| Recursive CTE | St | query |
| Materialized views | St | perf |
| Concurrency at scale | St | concur |
| Zero-downtime migration (CONCURRENTLY, dual-write) | St | migr |
| Partitioning (range/list/hash) | St | perf |

---

## Step 6: Corner Cases

4–6 cases per phase. Categories: duplicate insert, FK violation, NULL FK, empty result, boundary values, concurrent access (Senior/Staff). Per case: scenario, expected behavior, common mistake, verification SQL.

---

## Step 7: Coaching Guide

- **Q&A reveal script** — answers to every expected candidate question about entities, relationships, attributes
- **Issue reference** — per schema mistake or query bug: severity, 3 graduated hints, answer
- **Phase transition prompts** — what to say at Q&A → schema reveal → DDL → Phase 2 → Phase 3
- **Concurrency probing (any `concur`-dim challenge):** Never accept whichever strategy the candidate reaches for first. Require them to name all three — atomic SQL (`UPDATE SET x = x + 1`), pessimistic lock (`SELECT ... FOR UPDATE`), optimistic lock (version column + retry) — and defend the choice. Ask: "What breaks under concurrent requests?" and "Why not the other two?" Accepting one answer without this reasoning is a coaching failure.

---

## Step 8: Driver CRUD

Per phase: Python snippets using psycopg2 that verify the schema and query functions. Print with expected output. Cover happy path + corner cases. Coach runs these — candidate does not implement them.

---

## Step 9: Rubric (scored 1–3, total /15)

Dimensions: Correctness, Schema Design, SQL Fluency, Communication, Speed.
Fill in problem-specific criteria for first three before session.

---

## Output

Save as **4 files** in `problems/`:
- `YYMMDD-[domain]-db_overview.md` — domain, level, modes, schema, phase picks, rubric (no baseline content — always sourced from docs/mosaicapp.md)
- `YYMMDD-[domain]-db_req1.md` — Q&A reveal script, schema reveal, DDL reference, Phase 1 driver CRUD
- `YYMMDD-[domain]-db_req2.md` — Phase 2 challenge, coaching guide, skeleton additions, driver CRUD
- `YYMMDD-[domain]-db_req3.md` — Phase 3 challenge, coaching guide, extension questions

**Skeleton progression:** req2.md and req3.md each include a `## Skeleton Addition` section with exact SQL stubs and Python signatures the coach adds at phase transition.

The `_session_notes.md` and working files are created at runtime by the coach. Confirm 4 files saved and hand off to `db-interview-coach`.
