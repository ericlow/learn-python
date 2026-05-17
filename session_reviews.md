# Session Reviews

Detailed rubric scores and analysis per session. Used to track improvement over time.

**Format change note (effective ~2026-03-23):** Sessions prior to Camera Alert Triage used an open-ended requirements gathering model — candidates discovered the interface through discussion, spending 40–95 min before writing code. Starting with Camera Alert Triage, sessions use an **interface-first format**: skeleton provided upfront, boilerplate skipped, focus on implementation and design decisions. Speed and "time to Req 1" are not comparable across this boundary. pct_teaching, data structures, correctness, and edge case trends are valid across all sessions.

---

## 2026-03-16 — Bowling Alley System

**Problem:** Bowling Alley Management System (new problem, 3 reqs)
**Active Time:** ~123 min (reliable segments); session spread across multiple days due to pauses
**Reqs Completed:** 2.5 / 3

### Rubric Scores

| Dimension | Score | Level |
|-----------|-------|-------|
| Correctness | 2/3 | Hire |
| Code Quality | 2/3 | Hire |
| Data Structures | 1.5/3 | No Hire / Hire |
| Communication | 3/3 | Strong Hire |
| Speed | 1/3 | No Hire |
| **Total** | **9.5/15** | **No Hire (trending Hire)** |

### Dimension Analysis

**Correctness — 2/3 (Hire)**
- ✅ Req 1 fully working: lane check-in/out, heap-based lane selection, shoe inventory
- ✅ Req 2 fully working: shoe rental, inventory validation, return on check-out
- ❌ Req 3 incomplete: `make_reservation` has dead `retval = None` that never updates; `Reservation` missing lane reference; cross-hour conflict detection not implemented

**Code Quality — 2/3 (Hire)**
- ✅ Good helper extraction: `_reserve_lane_shoes_available`, `_reserve_lane_find_lane`, `_reserve_lane_validation`
- ✅ `__repr__` on Party and Lane
- ✅ `__lt__` for heap ordering
- ❌ Req 3 code has `retval = None` that is never set — dead code
- ❌ Some inline logic remains in `reserve_lane`

**Data Structures — 1.5/3 (No Hire / Hire)**
- ✅ Heap for lane selection — correctly chosen and justified
- ✅ Dict for shoe inventory — correct
- ❌ Nested `dict[date, dict[hour, list[Reservation]]]` for reservations — caused cross-hour conflict problem (a 1pm reservation runs to 3pm, conflicting with 2pm slot not captured by hour-only lookup)
- ❌ `Reservation` has no lane reference — made conflict detection impossible to implement correctly
- Note: Recognized complexity was high but chose to push through rather than pivot — that's the key skill gap

**Communication — 3/3 (Strong Hire)**
- ✅ Asked good clarifying questions before coding
- ✅ Reasoned through heap tradeoffs (always-heap vs runtime heap) correctly
- ✅ Justified dict vs list for shoe sizes with clear reasoning
- ✅ Proactively identified when Req 3 was becoming too complex
- ✅ Correctly identified reference equality semantics without prompting

**Speed — 1/3 (No Hire)**
- Req 1: 72 min active (target: 20-25 min)
- Req 2: 34 min active (target: 15-20 min)
- Req 3: not completed
- Primary cause: 30% of session time spent on Python syntax teaching (list comprehension, heapq, __lt__, __repr__, dict.items(), timedelta, forward references)
- Pure coding speed: ~100 lines/hour (target: ~200 lines/hour)

### Key Strengths
- Communication is already Strong Hire — a significant asset for an EM role
- Design instincts are sound for Reqs 1-2
- Good helper method extraction when syntax knowledge wasn't blocking

### Key Improvement Areas
1. **Python syntax fluency** — 30% teaching overhead is the single biggest drag; flashcards required
2. **Req 3 design** — need to practice recognizing when a data structure choice is boxing you in and pivoting early
3. **Pure coding speed** — even with zero teaching interruptions, 2x speed improvement needed

### Flashcard Topics from This Session
- `heapq` module — `heapify(list)` in-place, `heappop(list)`, min-heap behavior
- `__lt__(self, other)` — required for heapq to sort custom objects
- Forward reference in type hints — `other: "ClassName"`
- `__repr__` vs `__str__` — both use double underscores each side
- `dict.items()` — required for key/value unpacking in for loop
- `dict.get(key, default)` — replaces if/not-in/assign pattern
- `list(source)` — shallow copy
- `datetime.hour` — extract hour from datetime
- `timedelta(hours=N)` — add time to datetime
- Chained comparisons — `a <= b < c` valid in Python
- Don't shadow imports — don't name param `datetime` if you imported `datetime`

---

## 2026-03-22 — Restaurant Kitchen System

**Problem:** Restaurant management system — seating, ordering, kitchen dispatch (OOP, 3 reqs)
**Active Time:** ~190 min estimated (multi-day, many pauses; wall time unreliable)
**Reqs Completed:** 3 / 3

### Rubric Scores

| Dimension | Score | Level |
|-----------|-------|-------|
| Correctness | 2/3 | Hire |
| Code Quality | 2/3 | Hire |
| Data Structures | 2/3 | Hire |
| Communication | 3/3 | Strong Hire |
| Speed | 1/3 | No Hire |
| **Total** | **10/15** | **No Hire (trending Hire)** |

### Dimension Analysis

**Correctness — 2/3 (Hire)**
- ✅ All 3 reqs completed; all drivers passed
- ✅ Capacity guard implemented after driver revealed missing check
- ✅ Null checks consistent throughout (table not found, order not found, invalid types)
- ❌ `unoccupy_table` does not reset `table.order = None` — next party inherits previous bill
- ❌ No smallest-fit table selection (occupies by ID, not by capacity)
- ❌ Missing `get_available_tables()` equivalent

**Code Quality — 2/3 (Hire)**
- ✅ Clean entity separation: OrderItem, Order, Staff, Table, Cook, RMS
- ✅ `__repr__` added to OrderItem
- ✅ `get_available_chef` and `query_cook_load` extracted as helpers
- ✅ `create_menu` extracted
- ❌ `unoccupy_tabe` — typo in method name
- ❌ String literals for status ("Not Started", "In Progress") instead of enum — candidate flagged it but didn't implement
- ❌ Tables/staff stored as lists requiring O(n) lookup despite candidate recognizing dicts are better

**Data Structures — 2/3 (Hire)**
- ✅ Articulated list vs dict tradeoff clearly: O(n) vs O(1), extra find method required
- ✅ Consciously chose linear scan over heap for cook assignment with full reasoning
- ✅ Set for cook.order_items; menu as dict
- ❌ Did not implement dict for tables/staff despite recognizing it was the better choice
- ❌ Capacity check uses total-capacity math rather than per-cook guard in `get_available_chef`

**Communication — 3/3 (Strong Hire)**
- ✅ Extensive clarifying questions before any coding; drove entity modeling discussion
- ✅ Proactively reasoned through heap vs linear scan and articulated the tradeoff correctly
- ✅ Identified array vs dict tradeoff unprompted, with O(n) vs O(1) justification
- ✅ Reasoned through atomic capacity check vs partial assignment — chose simpler invariant
- ✅ Proactively asked "have I made any mistakes before going further?" — rare self-awareness
- ✅ Correctly distinguished ticket lifecycle from order lifecycle, then decided to collapse into OrderItem state

**Speed — 1/3 (No Hire)**
- Requirements gathering alone: ~41 min before first line of code written
- Req 1 active: ~65 min (target: 20-25 min)
- Req 2 active: ~26 min (target: 15-20 min)
- Req 3 active: ~70 min (target: 15-20 min)
- Primary cause: discussion-heavy session, not syntax blocks

### Trend Analysis

- **Score trajectory:** 9.5 → 10 — marginal improvement; still No Hire overall
- **pct_teaching:** 30% → ~5% — dramatic improvement ✅ biggest win this session; almost no Python syntax help needed
- **Speed:** Still No Hire but root cause shifted — no longer blocked by syntax, now blocked by extended requirements discussion (~41 min before coding)
- **Data structures:** Recognizing good choices but not implementing them — same pattern as Bowling Alley (recognized pivot opportunity, chose not to act)
- **Edge cases:** ~13 listed across 3 reqs, 1 missed (cook capacity guard) — improving from prior sessions

### Key Strengths
- pct_teaching dropped from 30% to ~5% — Python fluency is genuinely improving
- Communication remains Strong Hire — best asset for an EM candidate
- Completed all 3 reqs for the first time since Banking Transaction System

### Key Improvement Areas
1. **Requirements gathering speed** — 41 min of discussion before coding is too long for a 60-min interview; practice timebox requirements gathering to 10 min max
2. **Implement the better choice** — twice this session you identified the right data structure (dicts, enums) but didn't implement it; practice following through
3. **State cleanup on lifecycle transitions** — `unoccupy_table` not clearing `table.order` is a classic stale-state bug; always ask "what needs to reset when X happens?"

### Flashcard Topics from This Session
- `isinstance(x, int)` / `isinstance(x, (int, float))` — type checking
- Python enums — `from enum import Enum; class Status(Enum): NOT_STARTED = "Not Started"`
- `for i in range(len(my_list))` vs `for item in my_list` — prefer direct iteration
- `not x == y` vs `x != y` — prefer `!=` for clarity

---

## 2026-03-23 — Camera Alert Triage

**Problem:** Camera alert triage system — register cameras, trigger/resolve alerts, cross-camera lookup, hotspot detection (Applied OOP, Light, 3 phases)
**Active Time:** ~64 min (calculated from timestamps and pauses; session spread across 2 days)
**Reqs Completed:** 3 / 3

### Rubric Scores

| Dimension | Score | Level |
|-----------|-------|-------|
| Correctness | 3/3 | Strong Hire |
| Code Quality | 2/3 | Hire |
| Data Structures | 3/3 | Strong Hire |
| Communication | 3/3 | Strong Hire |
| Speed | 3/3 | Strong Hire |
| **Total** | **14/15** | **Strong Hire** |

### Dimension Analysis

**Correctness — 3/3 (Strong Hire)**
- ✅ All 3 phases complete, all drivers pass
- ✅ Phase 1 initial bugs (missing return True, wrong dict subscript, severity=0 allowed) all self-caught and fixed before driver ran
- ✅ Phase 3 return type error (Camera object vs camera_id) self-caught during manual trace
- ✅ Edge cases handled: duplicate camera, global alert_id uniqueness, severity bounds, resolve-resolved, cross-camera resolution guard

**Code Quality — 2/3 (Hire)**
- ✅ Clean structure; Enum for state is a nice touch over plain strings
- ✅ Docstrings present on all methods
- ✅ Consistent return types throughout
- ❌ Redundant duplicate check in trigger_alert — checks both `camera.alerts` and `alert_to_camera` when `alert_to_camera` alone suffices
- ❌ Unnecessary null-guard in `get_alert` — `alert_to_camera` lookup already guarantees alert exists on that camera

**Data Structures — 3/3 (Strong Hire)**
- ✅ Added `alert_to_camera` global secondary index proactively in Phase 1 — the extensibility hinge
- ✅ Phase 2 trivially O(1) as a result; no restructuring needed
- ✅ Articulated the tradeoff unprompted: "more things to track vs faster access"
- ✅ Linear scan + max for Phase 3 — correct and appropriate for light difficulty

**Communication — 3/3 (Strong Hire)**
- ✅ Thorough edge case discussion before coding all three phases
- ✅ Proactively articulated secondary index tradeoff without prompting
- ✅ Initially thought resolve-resolved should be idempotent — accepted correction and incorporated it
- ✅ Asked precise clarifying questions (return type, state values)

**Speed — 3/3 (Strong Hire)**
- Phase 1 active: ~20 min (target: <25 min) ✅
- Phase 2 active: ~2 min — done before driver was even added ✅
- Phase 3 active: ~30 min (target: <15 min) — slightly slow but within acceptable range
- Phase 1+2 combined: ~22 min → Strong Hire threshold (<25 min) ✅
- Note: session spread across 2 days; active time calculated from pause/resume timestamps = 64 min

### Trend Analysis

- **Score trajectory:** 9.5 → 10 → 14 — large jump, but two caveats: (1) this was a **light** difficulty problem; (2) this is the first session using the **interface-first format** (skeleton provided upfront, no requirements gathering phase) — scores are not directly comparable to prior open-ended sessions
- **pct_teaching:** 30% → 5% → ~10% — remains low ✅; asked about enum syntax and collection methods; no blocking syntax gaps; this trend is genuine organic improvement
- **Speed:** Strong Hire rating, but context matters — the format change (skeleton provided, boilerplate skipped) eliminated the 40+ min requirements gathering overhead that penalized prior sessions; Phase 1 in ~20 min is the new baseline for the interface-first format; future sessions should compare against this, not against open-ended sessions
- **Data structures:** First Strong Hire here — proactive secondary index is genuine skill; this result is not explained by the format change
- **Edge cases:** Listed 11 edge cases across 3 phases, missed none from driver — strong improvement from prior sessions; this is organic improvement

### Key Strengths
- Proactive secondary index design is the most important signal — thought ahead instead of reacting
- Self-caught all bugs during manual trace before running driver — good discipline
- Phase 1+2 active time comfortably within Strong Hire threshold

### Key Improvement Areas
1. **Redundant state checks** — in `trigger_alert`, checking both `camera.alerts` and `alert_to_camera` is noise; trust your index as single source of truth
2. **Phase 3 speed** — 30 min for a linear scan + max is longer than needed; practice Phase 3 patterns (max/min with filter) until automatic
3. **Difficulty calibration** — this was a light problem; Verkada's CodeSignal will be medium; next session should stress-test the same skills harder

### Flashcard Topics from This Session
- `sum(1 for x in my_list if condition)` — count items matching a predicate without building a list
- `max(my_list, key=lambda x: x.attr)` — find max by attribute; raises ValueError on empty list
- Trust the global index — if you maintain a secondary index, use it as the single authority; don't double-check with the primary collection

---

## 2026-03-24 — EV Charging Network

**Problem:** EV charging network — validate ports, auto-assign, best-port selection (Applied OOP, Medium, 3 phases)
**Active Time:** ~98 min (Reqs 1-2 timing estimated due to session loss; Req 3 = 57 min from timestamps)
**Reqs Completed:** 3 / 3

### Rubric Scores

| Dimension | Score | Level |
|-----------|-------|-------|
| Correctness | 3/3 | Strong Hire |
| Code Quality | 2/3 | Hire |
| Data Structures | 2/3 | Hire |
| Communication | 2/3 | Hire |
| Speed | 1/3 | No Hire |
| **Total** | **10/15** | **Hire** |

### Dimension Analysis

**Correctness — 3/3 (Strong Hire)**
- ✅ All 3 phases complete, all drivers pass (9 + 6 + 7 cases)
- ✅ Validation order correct in Phase 1; state resets cleanly on end_charge
- ✅ Primary sort (highest power) and tiebreaker (most open ports) both correct in Phase 3
- ✅ State consistent after end_charge → best_charge cycle

**Code Quality — 2/3 (Hire)**
- ✅ Readable guard clauses; early exit break in Phase 3 self-caught and added
- ✅ `__repr__` added proactively for debugging
- ❌ `retval` pattern in start_charge — verbose; direct returns cleaner
- ❌ best_charge inlines state mutation instead of reusing start_charge — minor duplication
- ❌ `required_level <= val` enum comparison bug — needed runtime to surface it; fixed independently after

**Data Structures — 2/3 (Hire)**
- ✅ `cars` set correctly introduced in Phase 1 and maintained through all phases
- ✅ Powerlevels-as-stack (pop from end) — creative and functional approach to highest-first iteration
- ✅ Port.vehicle_id used correctly for per-port state throughout
- ❌ Tiebreaker (available port count) computed inline per station inside the sort loop — O(n²) concern; should pre-aggregate once before the loop (D8)
- ❌ `cars` set loses location info — manageable here since port.vehicle_id tracks location, but a dict would be cleaner

**Communication — 2/3 (Hire)**
- ✅ Edge cases listed before coding all phases; none missed in Phase 3
- ✅ Asked clarifying question on primary sort criterion early
- ✅ Considered and articulated multiple design approaches
- ❌ Initially proposed sorting by available ports as the primary criterion (wrong); needed concrete counterexample before self-correcting
- ❌ Did not proactively flag the O(n²) tiebreaker concern before coding

**Speed — 1/3 (No Hire)**
- Req 1 active: ~26 min (target: <25 min) — borderline
- Req 2 active: ~15 min estimated (target: <15 min) — borderline
- Req 3 active: ~57 min (target: <15 min) — well over
- Total: ~98 min vs 45 min Hire threshold
- Primary cause: Req 3 design exploration (~19 min) before settling on approach; primary/tiebreaker ordering confusion required probing to resolve

### Trend Analysis

- **Score trajectory:** 9.5 → 10 → 14 (light) → 10 (medium) — the 14 was on a light problem; 10 on medium is consistent with the earlier 9.5/10 pattern; medium difficulty is the right stress test going forward
- **pct_teaching:** 30% → 5% → 10% → ~5% — consistently low ✅; Python fluency is no longer a drag
- **Speed:** Req 3 design exploration is the new bottleneck; not Python syntax — it's design confidence under time pressure; the primary/tiebreaker confusion cost ~19 min
- **Data structures:** Pre-aggregation optimization (D8) missed — same pattern as Restaurant Kitchen (recognized better choice exists, implemented the simpler one)
- **Edge cases:** 0 missed across all 3 phases — best result to date ✅; organic improvement continuing

### Key Strengths
- Zero edge cases missed across all 3 phases — strongest edge case performance to date
- Design confusion self-resolved after probing with a concrete example — good reasoning when grounded
- Python fluency is no longer a blocker; pct_teaching holding at ~5%

### Key Improvement Areas
1. **State the sort criteria explicitly before proposing an approach** — when a problem has two sort keys, name them in priority order before designing; avoids costly design detours
2. **Pre-aggregate before sorting** — any time you compute a derived value inside a loop used for sorting, ask "can I compute this once?"; this is the D8 pattern
3. **Req 3 speed** — 57 min on Phase 3 is 4x the target; practice multi-key sort problems until the pattern (collect candidates → pre-aggregate tiebreaker → sort with tuple key) is automatic

### Flashcard Topics from This Session
- `list.pop()` — removes and returns last element; use a list as a stack with `append` + `pop`
- Multi-key sort with tuple key — `sorted(items, key=lambda x: (-x.primary, -x.secondary))` — negate for descending
- Pre-aggregate before sorting — compute derived values into a dict once, then reference in sort key; avoids O(n²)
- Enum comparison requires `.value` — `PowerLevel.L2 <= PowerLevel.DCFC` fails; use `.value` on both sides

---

## 2026-05-15 — Fitness Activity Window Analyzer

**Problem:** Sliding window step counter — max window, best window with index, min days to reach target (Algorithmic, 3 reqs)
**Active Time:** ~85 min estimated (multi-day session; Req 1 ~20 min, Req 2 ~30 min, Req 3 ~35 min active)
**Reqs Completed:** 3 / 3

### Rubric Scores

| Dimension | Score | Level |
|-----------|-------|-------|
| Correctness | 3/3 | Strong Hire |
| Code Quality | 2/3 | Hire |
| Data Structures | 3/3 | Strong Hire |
| Communication | 3/3 | Strong Hire |
| Speed | 2/3 | Hire |
| **Total** | **13/15** | **Strong Hire** |

### Dimension Analysis

**Correctness — 3/3 (Strong Hire)**
- ✅ All 3 reqs complete; all driver cases pass
- ✅ Req 1: all 7 cases passed; sliding window with running sum correct first pass
- ✅ Req 2: all 7 cases passed; tie-breaking (`>` not `>=`) and index formula correct
- ✅ Req 3: 7/8 passed first run; missing `target <= 0` guard added after single prompt
- ✅ Self-caught double-add bug in Req 1 after guided trace; self-found overwrite bug in Req 3 through trace

**Code Quality — 2/3 (Hire)**
- ✅ Clean variable names throughout (`total`, `max_total`, `min_days`, `L`, `R`)
- ✅ Adapted Req 1 code cleanly for Req 2 — didn't rewrite; restored Req 1 return type correctly
- ✅ Guard clause structure consistent across all three functions
- ❌ Req 3 had redundant `min_days` tracking in two places — candidate noticed but didn't refactor before finishing
- ❌ `L < R` condition in Req 3 while loop is more restrictive than needed (works but non-idiomatic)

**Data Structures — 3/3 (Strong Hire)**
- ✅ Proposed sliding window with running sum independently at Req 1 — no prompting required; explicitly reasoned through queue vs running sum tradeoff
- ✅ Correctly identified variable-width two-pointer at Req 3 immediately — no fixed-window confusion whatsoever
- ✅ Two-pointer structure (expand R, shrink L) stated clearly before coding

**Communication — 3/3 (Strong Hire)**
- ✅ Proactively discussed queue vs running sum at Req 1 before being asked
- ✅ Reasoned through `(0, 0)` ambiguity at Req 2 — arrived at `(-1, 0)` independently after probe
- ✅ Identified tie-breaking requirement (`>` not `>=`) without prompting
- ✅ Asked for a concrete example before coding Req 3 — good instinct; prompted the "include example in reveal" improvement
- ✅ Walked through approach clearly before every implementation
- ❌ Complexity answer needed prompting — said O(n²) before being led back to O(n)

**Speed — 2/3 (Hire)**
- Req 1 active: ~20 min ✅ (on pace)
- Req 2 active: ~30 min estimated ✅ (reasonable)
- Req 3 active: ~35 min estimated ✅ (on pace for medium)
- Total active: ~85 min — Hire threshold; all 3 reqs complete
- Multi-day session with significant pauses; active time estimates are rough

### Trend Analysis

- **Score trajectory:** 9.5 → 10 → 14 (light OOP) → 10 (medium OOP) → **13 (medium Algo)** — first algorithmic session in this format; 13/15 is the strongest result on a non-light problem; strong signal
- **pct_teaching:** 30% → 5% → 10% → 5% → ~2% — effectively zero this session; no Python syntax help needed at all ✅ this trend is now fully established
- **Speed:** All 3 reqs completed in ~85 min active — Hire on speed; not yet Strong Hire, but the multi-day pause structure makes this hard to assess; active time per req is reasonable
- **Data structures:** Strong Hire for the first time on an algorithmic session — independently proposed sliding window and two-pointer; this is a meaningful signal, not a format artifact
- **Edge cases:** Listed ~6 edge cases across 3 reqs; missed `target <= 0` return value (needed prompt); improving trend continues but still 1 miss per session

### Key Strengths
- First truly independent sliding window identification — no complexity probe needed to get to O(n)
- Immediately pivoted to variable-width window at Req 3 with correct structure; no false starts
- Python fluency is no longer discussed — pct_teaching ~2%; no syntax blocks anywhere

### Key Improvement Areas
1. **Complexity articulation** — correct O(n) intuition but couldn't defend it; practice the "each element added once, removed once → O(n)" explanation until automatic
2. **Code cleanup under time pressure** — noticed the redundant `min_days` tracking but didn't refactor; practice identifying and fixing structural issues before moving on
3. **Edge case depth on Req 3** — `target <= 0` was discussed explicitly before coding but guard was still missed; close the loop between discussion and implementation

### Flashcard Topics from This Session
- Two-pointer active time argument — each element is added once and removed at most once → O(n) total, not O(n²)
- Variable-width sliding window pattern — expand R until condition met, shrink L while condition holds, record inside the while loop before advancing L
- Sentinel disambiguation — if `(0, 0)` is a valid result, `(-1, 0)` is the correct invalid sentinel; index -1 can never be a valid start

---
