# Drill Reviews

---

## 2026-03-26 — Session 1

### Drill 1 — sorting

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 729s | < 300s | ❌ |
| secs_bug_fixes | 206s | 0 | ❌ |
| secs_idiomatic_delta | 123s | 0 | ❌ |
| secs_total | 1058s | — | |
| hints_used | 4 | 0 | ❌ |

**Analysis:** Two bugs cost the most time: writing `people[1]` instead of `x[1]` in the lambda (confusing the list with the iteration variable), and using `reverse=True` which flipped both sort fields instead of negating the score. The `key=` keyword syntax also needed a hint. Pattern to internalize: for mixed-direction sorts, always use `(-numeric_field, string_field)` without `reverse=True` — negation gives you descending on one field while leaving others ascending.

**Cross-drill trend:** First drill of session — no trend yet.

### Drill 2 — list-comp

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 632s | < 300s | ❌ |
| secs_bug_fixes | 0s | 0 | ✅ |
| secs_idiomatic_delta | 111s | 0 | ❌ |
| secs_total | 743s | — | |
| hints_used | 3 | 0 | ❌ |

**Analysis:** Logically correct on first check — no bugs. Time lost in the idiom phase: solved it as three chained list comps with intermediate variables, then had to consolidate into one. The pattern to internalize: when filter + transform can be expressed in one pass, write it that way from the start — `[x.strip().title() for x in items if x.strip()[0].lower() in 'aeiou']`. Also called `.strip()` twice; storing it avoids that but a single-pass comp is the idiomatic choice here.

**Cross-drill trend (2 drills):** Both drills slow on `secs_to_first_done` (729s, 632s). Drill 2 improved on bug fixes (206s → 0) and idiomatic delta (123s → 111s). Speed is the consistent gap — mechanics are landing, just not fast yet.

### Drill 4 — heapq

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 407s | < 300s | ❌ |
| secs_bug_fixes | 0s | 0 | ✅ |
| secs_idiomatic_delta | 5s | 0 | ✅ |
| secs_total | 412s | — | |
| hints_used | 0 | 0 | ✅ |

**Analysis:** Clean submit — no bugs, no idiom fix needed, no hints. The negation trick for max-heap (`-score`) came naturally, and the tuple tie-break was applied correctly. Only gap is speed (407s vs 300s target). This is the strongest drill of the session so far.

**Cross-drill trend (3 drills):** Clear improvement trajectory — hints dropping (4 → 3 → 0), bug fixes gone after drill 1, idiomatic delta shrinking (123s → 111s → 0). Speed still lags but drill 4 was 225s faster than drill 1. Heapq pattern is solid; sorting and list-comp need more reps.

### Drill 5 — deque

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 177s | < 300s | ✅ |
| secs_bug_fixes | 0s | 0 | ✅ |
| secs_idiomatic_delta | 0s | 0 | ✅ |
| secs_total | 177s | — | |
| hints_used | 1 | 0 | — |

**Analysis:** First drill to hit the 300s target. Clean submit with no bug fixes and no idiom delta. The one help request (whether oldest element is returned) was a clarification about deque behavior, not a syntax gap. `maxlen=k` pattern landed correctly on first try.

---

## Session 2 — 2026-03-26

### Drill 1 — sorting

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 508s | < 300s | ❌ |
| secs_bug_fixes | 122s | 0 | ❌ |
| secs_idiomatic_delta | 0s | 0 | ✅ |
| secs_total | 859s | — | |
| hints_used | 2 | 0 | ❌ |

**Analysis:** Faster than the session 1 sorting drill (508s vs 729s) and idiom was clean this time. Bug came from returning tuples instead of extracting names — the sort key was correct from the start. Pattern to watch: after building sorted data, always check what the return value actually contains.

**Cross-drill trend:** First drill of session 2 — comparing to session 1: hints down (4→2), idiomatic delta gone (123s→0), bug fix time down (206s→122s). Speed still lagging but improving.

### Drill 2 — list-comp

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 457s | < 300s | ❌ |
| secs_bug_fixes | 0s | 0 | ✅ |
| secs_idiomatic_delta | 126s | 0 | ❌ |
| secs_total | 583s | — | |
| hints_used | 1 | 0 | — |

**Analysis:** Logically correct on first run after catching the `prices = ...` vs `prices.append(...)` bug independently. The hint was about why str vs float error occurred — not syntax, but understanding what the error meant. Idiom delta came from the debug print; the list-comp structure itself was sound. list-comp pattern is landing but debug hygiene is costing time.

**Cross-drill trend (session 2, 2 drills):** Speed improving vs session 1 (508s→457s). Bug fixes dropped (122s→0). Idiom delta still present both drills. Pattern: logic is getting cleaner, but debug prints are a consistent drag on idiomatic score.

### Drill 3 — sets

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 777s | < 300s | ❌ |
| secs_bug_fixes | 0s | 0 | ✅ |
| secs_idiomatic_delta | 87s | 0 | ❌ |
| secs_total | 864s | — | |
| hints_used | 2 | 0 | — |

**Analysis:** Logically correct on first submit — good. The approach was sound: build a dict of sets, then iteratively intersect. Two help requests: one about the `set.intersection(*iterable)` idiom (correctly flagged as esoteric), one about the iterative approach using `&`. Idiom delta came from minor cleanup (`list()` in sorted, `dict()` vs `{}`). The `defaultdict(set)` pattern would have eliminated the null-check entirely — worth internalizing for next time.

**Cross-drill trend (session 2, 3 drills):** Zero bug fixes across all 3 drills — logic is solid. Speed still slow (457s→777s, going the wrong direction). Idiom delta persistent (126s→87s, slight improvement). The slowdown on drill 3 reflects the problem being genuinely harder, not regression.

### Drill 4 — heapq

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 1047s | < 300s | ❌ |
| secs_bug_fixes | 0s | 0 | ✅ |
| secs_idiomatic_delta | 881s | 0 | ❌ |
| secs_total | 1928s | — | |
| hints_used | 4 | 0 | ❌ |

**Analysis:** Hardest drill of the session. The double-negation bug (storing `-score` then negating again in the key) cost significant time to diagnose. The idiom phase was long — dead import and comment block took multiple rounds to clear. Logic was sound once the sort key was corrected. Key pattern to internalize: store raw values, negate only in the sort key. The set-membership simplification was skipped — the manual loop with `break` is acceptable but verbose.

**Cross-drill trend (session 2, 4 drills):** This drill broke the zero-bug-fix streak on diagnosis time (not logic), and idiom delta spiked. Speed and hint count both regressed vs drill 3. The problem was harder though — heapq + top-N unique scores is multi-step.

### Drill 5 — string-ops

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | N/A | < 300s | — |
| secs_bug_fixes | 0s | 0 | ✅ |
| secs_idiomatic_delta | 0s | 0 | ✅ |
| hints_used | 0 | 0 | ✅ |

**Analysis:** Clean submit — no bugs, no hints, no idiom issues. The strip-all-parts pattern (`[p.strip() for p in parts]`) was a smart choice that handled all whitespace variations in one step. Timing not captured (start not recorded).

---

## Session 2 Summary — 2026-03-26

| # | Category | secs_to_first_done | secs_bug_fixes | secs_idiomatic_delta | secs_total | hints | clean? |
|---|---|---|---|---|---|---|---|
| 1 | sorting | 508s ❌ | 122s ❌ | 0s ✅ | 859s | 2 | ❌ |
| 2 | list-comp | 457s ❌ | 0s ✅ | 126s ❌ | 583s | 1 | ❌ |
| 3 | sets | 777s ❌ | 0s ✅ | 87s ❌ | 864s | 2 | ❌ |
| 4 | heapq | 1047s ❌ | 0s ✅ | 881s ❌ | 1928s | 4 | ❌ |
| 5 | string-ops | N/A | 0s ✅ | 0s ✅ | N/A | 0 | ✅ |

**Trends:**
- Zero bug fixes on 4 of 5 drills — logic is landing clean
- Idiom delta is the main gap: 0s → 126s → 87s → 881s → 0s (heapq was an outlier)
- Hints dropping except on the hardest problem (heapq)
- string-ops was cleanest drill of the session — no help, no issues

---

## Session 1 Summary — 2026-03-26

| # | Category | secs_to_first_done | secs_bug_fixes | secs_idiomatic_delta | secs_total | hints | clean_submit |
|---|---|---|---|---|---|---|---|
| 1 | sorting | 729s ❌ | 206s ❌ | 123s ❌ | 1058s | 4 | ❌ |
| 2 | list-comp | 632s ❌ | 0s ✅ | 111s ❌ | 743s | 3 | ❌ |
| 3 | heapq | 407s ❌ | 0s ✅ | 5s ✅ | 412s | 0 | ✅ |
| 4 | deque | 177s ✅ | 0s ✅ | 0s ✅ | 177s | 1 | ✅ |

**Trends:**
- Speed improving sharply drill-to-drill: 729 → 632 → 407 → 177
- Bug fixes and idiomatic delta gone by drill 3
- Hints dropping: 4 → 3 → 0 → 1 (drill 5 hint was a behavior question, not syntax)
- `sorting` and `list-comp` are the weak categories — both need more reps

---

## 2026-03-27

### Drill 1 — heapq

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 541 | < 300 ❌ |
| secs_bug_fixes | 0 | 0 ✅ |
| secs_idiomatic_delta | 493 | 0 ❌ |
| secs_total | 1034 | — |
| hints_used | 4 | — |
| lines_written | 2 | — |

Speed and idiom both struggled. Used `heapify` before `nsmallest`, not knowing `nsmallest` takes any iterable — this is the same pattern seen in prior heapq drills where idiom delta is large. 4 hints used, mostly around tie-breaking mechanics and `nsmallest` API. Core approach (tuple key for tie-break) was correct once explained.


### Drill 2 — list-comp

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 545 | < 300 ❌ |
| secs_bug_fixes | 0 | 0 ✅ |
| secs_idiomatic_delta | 45 | 0 ❌ |
| secs_total | 590 | — |
| hints_used | 4 | — |
| lines_written | 2 | — |

Needed 4 hints to work through single list-comp mechanics. Solution used two list comprehensions (split-then-filter) instead of one with an inline generator — correct and readable, but not meeting the single-comp spec. User accepted the non-idiomatic form. Speed still over target; the conceptual block on how to access split results without double-splitting added significant time.


**Cross-drill trend (2/5):** Both drills over 300s and both have idiomatic delta — same pattern as prior sessions. No bug fixes needed in either, which is a consistent strength. Hints holding at 4 per drill; the blocks are API knowledge (heapq) and syntax mechanics (list-comp), not logic errors.


### Drill 3 — sets

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 189 | < 300 ✅ |
| secs_bug_fixes | 0 | 0 ✅ |
| secs_idiomatic_delta | 71 | 0 ❌ |
| secs_total | 260 | — |
| hints_used | 0 | — |
| lines_written | 1 | — |

First drill under 300s today. Zero hints, zero bugs. Idiom issues: unnecessary `key=lambda r: r[0]` (sorts by first char only) and `.difference()` instead of `-` operator. Both fixed quickly. Conceptual grasp of sets is solid — the friction is polish, not understanding.

**Cross-drill trend (3/5):** Speed improving — 541 → 545 → 189. Hints dropping — 4 → 4 → 0. Bugs consistently zero. Idiomatic delta persists across all three drills; operator/syntax polish is the remaining gap.


### Drill 4 — sorting

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | N/A | < 300 |
| secs_bug_fixes | 0 | 0 ✅ |
| secs_idiomatic_delta | 0 | 0 ✅ |
| hints_used | 0 | — |
| lines_written | 1 | — |

Clean submission — correct tuple key with negation, list comp for names, no bugs, no idiom issues. Timing unavailable (start not announced). Sorting mechanic is clearly solid.

**Cross-drill trend (4/5):** Zero bugs across all 4 drills. Hints: 4 → 4 → 0 → 0 — strong improvement. Idiomatic delta shrinking: 493 → 45 → 71 → 0. Speed where tracked: 541 → 545 → 189 — drill 3 was a breakout. Sorting and sets are clean; heapq and list-comp remain the weak spots.


### Drill 5 — fstring

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 373 | < 300 ❌ |
| secs_bug_fixes | 0 | 0 ✅ |
| secs_idiomatic_delta | 55 | 0 ❌ |
| secs_total | 428 | — |
| hints_used | 1 | — |
| lines_written | 1 | — |

Needed 1 hint for `.1f` format spec. Solution correct on first try, minor idiom fix (`00.1f` → `.1f`). Speed over target — fstring format spec lookup cost ~1min.

---

## Session 1 Summary (2026-03-27)

| # | Category | secs_to_first_done | secs_bug_fixes | secs_idiomatic_delta | secs_total | hints | clean_submit |
|---|---|---|---|---|---|---|---|
| 1 | heapq | 541 | 0 | 493 | 1034 | 4 | ❌ |
| 2 | list-comp | 545 | 0 | 45 | 590 | 4 | ❌ |
| 3 | sets | 189 | 0 | 71 | 260 | 0 | ❌ |
| 4 | sorting | N/A | 0 | 0 | N/A | 0 | ✅ |
| 5 | fstring | 373 | 0 | 55 | 428 | 1 | ❌ |

Zero bugs across all drills. Hints dropped significantly (4→4→0→0→1). Speed only hit target on sets. Idiomatic delta on 4/5 drills — operator/syntax polish is the persistent gap. Sorting was the standout clean submit.

---

## Session 2 (2026-03-27)

### Drill 1 — fstring

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 281 | < 300 ✅ |
| secs_bug_fixes | 0 | 0 ✅ |
| secs_idiomatic_delta | 203 | 0 ❌ |
| secs_total | 484 | — |
| hints_used | 0 | — |
| lines_written | 1 | — |

Under target and zero hints — improvement from session 1 fstring (373s, 1 hint). Correct on first try. Idiom fix: tuple unpacking in `for` clause instead of `r[0]`/`r[1]` indexing. Pattern suggests the format spec itself is internalized but Pythonic destructuring is still not instinctive.

**Cross-drill trend (1/5):** 1 drill in. Speed under 300s ✅, zero bugs ✅, idiom delta persists.

### Drill 2 — heapq

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 168 (pause-adjusted) | < 300 ✅ |
| secs_bug_fixes | 187 (pause-adjusted) | 0 ❌ |
| secs_idiomatic_delta | 112 | 0 ❌ |
| secs_total | 467 | — |
| hints_used | 2 | — |
| lines_written | 2 | — |

Speed was good but tie-break direction tripped it up — used `nlargest` on `(score, uid)` which sorted ties by largest uid first, backwards from spec. Fix required 2 hints to land on negated-score + `nsmallest` pattern. Idiom miss: `heapify` called before `nsmallest`, which is dead code since `nsmallest` operates independently. Core heap mechanic is present but nsmallest/nlargest independence isn't internalized yet.

**Cross-drill trend (2/5):** Both drills under 300s ✅. Bug fixes non-zero this drill (tie-break logic error). Idiom delta persisting across both drills — Pythonic patterns (destructuring, dead-code awareness) are the consistent gap.

### Drill 3 — list-comp

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 218 | < 300 ✅ |
| secs_bug_fixes | 0 | 0 ✅ |
| secs_idiomatic_delta | 283 | 0 ❌ |
| secs_total | 511 | — |
| hints_used | 0 | — |
| lines_written | 2 | — |

Clean first submission, zero hints — strong execution. Idiom time on unnecessary `.lower()` on message (not used in comparison) and discussion about two-pass vs inline split. User's preference for named intermediate is defensible in an interview context. Pattern: correctness is solid, idiom gaps are minor style issues not logic gaps.

**Cross-drill trend (3/5):** All three drills under 300s ✅. Zero bugs on drills 2 and 3. Idiom delta still present but shrinking in severity — these are polish issues, not structural ones.

### Drill 4 — fstring

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 173 | < 300 ✅ |
| secs_bug_fixes | 0 | 0 ✅ |
| secs_idiomatic_delta | 82 | 0 ❌ |
| secs_total | 261 | — |
| hints_used | 0 | — |
| lines_written | 1 | — |

Fast, clean, zero hints. Idiom gap: index access (`item[0]`, `item[1]`, `item[2]`) instead of tuple unpacking in the `for` clause. Fixed quickly once flagged. Consistent pattern — the mechanic is solid but destructuring still isn't the first instinct.

**Cross-drill trend (4/5):** Four drills, all under 300s ✅, zero bugs on last three. Idiom delta narrowing (82s this drill vs 283s last). Tuple unpacking in `for` clauses is the recurring miss.

### Drill 5 — sets

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 253 | < 300 ✅ |
| secs_bug_fixes | 0 | 0 ✅ |
| secs_idiomatic_delta | 40 | 0 ❌ |
| secs_total | 298 | — |
| hints_used | 0 | — |
| lines_written | 3 | — |

Clean first submission, zero hints. Used `.intersection()` instead of `&` operator — the set operator idiom isn't instinctive yet. Fixed immediately once flagged. Correctness approach was solid: normalize both lists first, then intersect.

**Cross-drill trend (5/5):** All five drills under 300s ✅. Zero bugs on drills 2–5. Idiom delta present on every drill but shrinking: 283s → 82s → 40s. Operator idioms (`&` vs `.intersection()`, tuple unpacking) are the consistent gap — mechanics are internalized, Pythonic shortcuts are not.

### Drill 6 — sorting

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 230 | < 300 ✅ |
| secs_bug_fixes | 0 | 0 ✅ |
| secs_idiomatic_delta | 0 | 0 ✅ |
| secs_total | 235 | — |
| hints_used | 0 | — |
| lines_written | 2 | — |

Clean sweep — correct, idiomatic, zero hints. Bad coach recommendation (lambda multi-arg unpacking) caused a detour but time not counted against candidate. Lambda index access `(e[1], -e[2], e[0])` is the correct idiomatic pattern for sort keys in Python 3.

**Cross-drill trend (session complete):** All 5 drills under 300s ✅. Zero bugs on 4 of 5. Idiom delta narrowed significantly across session (283s → 0s on final drill). Strong finish.

---

## Session 3 Summary (2026-03-27)

| # | Category | secs_to_first_done | secs_bug_fixes | secs_idiomatic_delta | secs_total | hints | clean_submit |
|---|---|---|---|---|---|---|---|
| 1 | heapq | 168 | 187 | 112 | 467 | 2 | ❌ |
| 2 | list-comp | 218 | 0 | 283 | 511 | 0 | ✅ |
| 3 | fstring | 173 | 0 | 82 | 261 | 0 | ✅ |
| 4 | sets | 253 | 0 | 40 | 298 | 0 | ✅ |
| 5 | sorting | 230 | 0 | 0 | 235 | 0 | ✅ |

**Cross-session comparison (speed / idiom delta per instance):**

**heapq:**
- 03-26: 407s/5s, 1047s/881s
- 03-27 sess 1: 541s/493s
- 03-27 sess 3 (today): **168s/112s** ✅✅ — best result across all instances

**list-comp:**
- 03-26: 110s/76s, 632s/111s, 457s/126s
- 03-27 sess 1: 545s/45s
- 03-27 sess 3 (today): **218s/283s** ✅❌ — speed best ever, idiom worst ever

**fstring:**
- 03-27 sess 1: 373s/55s
- 03-27 sess 2: 281s/203s
- 03-27 sess 3 (today): **173s/82s** ✅✅ — improving on both metrics each session

**sets:**
- 03-26: 357s/0s, 777s/87s
- 03-27 sess 1: 189s/71s
- 03-27 sess 3 (today): **253s/40s** ✅✅ — idiom consistently shrinking

**sorting:**
- 03-26: 388s/0s, 729s/123s, 508s/0s
- 03-27 sess 3 (today): **230s/0s** ✅✅ — first clean idiom result

Speed improved across every category vs all prior instances. list-comp idiom delta regressed sharply (best prior: 45s → 283s today) due to unnecessary `.lower()` on the return value. All other categories improved or held. Sorting and fstring show consistent improvement across every session they've appeared in.

```
Speed (secs_to_first_done, target ≤300s)

  heapq
  03-26 #1   |██████████████░░░░░░░░░░░░░░░░░░░░░░| 407s ❌
  03-26 #2   |████████████████████████████████████| 1047s ❌
  03-27 s1   |███████████████████░░░░░░░░░░░░░░░░░| 541s ❌
  03-27 s3   |██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 168s ✅

  list-comp
  03-26 #1   |██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 110s ✅
  03-26 #2   |████████████████████████████████████| 632s ❌
  03-26 #3   |██████████████████████████░░░░░░░░░░| 457s ❌
  03-27 s1   |███████████████████████████████░░░░░| 545s ❌
  03-27 s3   |████████████░░░░░░░░░░░░░░░░░░░░░░░░| 218s ✅

  fstring
  03-27 s1   |████████████████████████████████████| 373s ❌
  03-27 s2   |███████████████████████████░░░░░░░░░| 281s ✅
  03-27 s3   |█████████████████░░░░░░░░░░░░░░░░░░░| 173s ✅

  sets
  03-26 #1   |█████████████████░░░░░░░░░░░░░░░░░░░| 357s ❌
  03-26 #2   |████████████████████████████████████| 777s ❌
  03-27 s1   |█████████░░░░░░░░░░░░░░░░░░░░░░░░░░░| 189s ✅
  03-27 s3   |████████████░░░░░░░░░░░░░░░░░░░░░░░░| 253s ✅

  sorting
  03-26 #1   |███████████████████░░░░░░░░░░░░░░░░░| 388s ❌
  03-26 #2   |████████████████████████████████████| 729s ❌
  03-26 #3   |█████████████████████████░░░░░░░░░░░| 508s ❌
  03-27 s3   |███████████░░░░░░░░░░░░░░░░░░░░░░░░░| 230s ✅

Idiom delta (secs_idiomatic_delta, target 0s)

  heapq
  03-26 #1   |░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 5s ❌
  03-26 #2   |████████████████████████████████████| 881s ❌
  03-27 s1   |████████████████████░░░░░░░░░░░░░░░░| 493s ❌
  03-27 s3   |█████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 112s ❌

  list-comp
  03-26 #1   |██████████░░░░░░░░░░░░░░░░░░░░░░░░░░| 76s ❌
  03-26 #2   |██████████████░░░░░░░░░░░░░░░░░░░░░░| 111s ❌
  03-26 #3   |████████████████░░░░░░░░░░░░░░░░░░░░| 126s ❌
  03-27 s1   |██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 45s ❌
  03-27 s3   |████████████████████████████████████| 283s ❌

  fstring
  03-27 s1   |██████████░░░░░░░░░░░░░░░░░░░░░░░░░░| 55s ❌
  03-27 s2   |████████████████████████████████████| 203s ❌
  03-27 s3   |███████████████░░░░░░░░░░░░░░░░░░░░░| 82s ❌

  sets
  03-26 #1   |░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 0s ✅
  03-26 #2   |████████████████████████████████████| 87s ❌
  03-27 s1   |█████████████████████████████░░░░░░░| 71s ❌
  03-27 s3   |█████████████████░░░░░░░░░░░░░░░░░░░| 40s ❌

  sorting
  03-26 #1   |░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 0s ✅
  03-26 #2   |████████████████████████████████████| 123s ❌
  03-26 #3   |░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 0s ✅
  03-27 s3   |░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 0s ✅
```


---

## 2026-06-01 — Session (partial, 1 drill)

### Drill 1 — heapq

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 409s | < 300s | ❌ |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | — | 0s | (session ended before idiom phase) |
| hints_used | 2 | 0 | ❌ |
| lines_written | 8 | — | |

**Analysis:** Correct on first run — push-all-then-pop-k approach with negated tuple keys worked. Two hints used: one for the min-heap/negation pattern, one for tuple tie-break ordering. Speed at 409s was over target; the design discussion before starting (heappush vs convenience functions) ate into the clock. Idiom note pending for next session: `for i in range(3)` should use `_` for the unused loop variable.

---

## 2026-06-05 — Session (5 drills)

### Session Summary Table

| # | Category | secs_to_first_done | secs_bug_fixes | secs_idiomatic_delta | secs_total | hints | lines | clean_submit |
|---|---|---|---|---|---|---|---|---|
| 1 | heapq | 319s | 0s | 748s | 1067s | 1 | 3 | ❌ |
| 2 | list-comp | 699s | 98s | 44s | 841s | 2 | 1 | ❌ |
| 3 | sets | — | 0s | 77s | 77s | 0 | 2 | ❌ |
| 4 | fstring | 388s | 35s | 0s | 423s | 1 | 1 | ❌ |
| 5 | sorting | 179s | 75s | 64s | 318s | 1 | 2 | ❌ |

**Intra-session trends:**
- Speed improved across the session: 319 → 699 → — → 388 → 179. Drill 5 was the fastest.
- Hints flat at 1 per drill except drill 3 (0) and drill 2 (2). No improvement within session.
- No clean submits: every drill had either a bug or an idiom issue.

---

### Drill 1 — heapq

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 319s | <300s | ❌ |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | 748s | 0s | ❌ |
| hints_used | 1 | 0 | ❌ |
| lines_written | 3 | — | |

**Analysis:** Correct on first run. The large idiom delta came from starting with `heapify + nsmallest` together (redundant) and using a for-loop instead of a list comprehension with index access — two separate fixes needed. The core insight (negate scores, use tuples for tie-breaking) was solid.

---

### Drill 2 — list-comp

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 699s | <300s | ❌ |
| secs_bug_fixes | 98s | 0s | ❌ |
| secs_idiomatic_delta | 44s | 0s | ❌ |
| hints_used | 2 | 0 | ❌ |
| lines_written | 1 | — | |

**Analysis:** Slowest drill of the session. Initial strategy was wrong — tried to split all lines into words and filter numeric words, losing line context. Once redirected to filter at the line level (startswith), the implementation was quick. The `.upper()` bug (case-insensitive match) cost 98s of bug fixes.

---

### Drill 3 — sets

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | — | <300s | — |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | 77s | 0s | ❌ |
| hints_used | 0 | 0 | ✅ |
| lines_written | 2 | — | |

**Analysis:** No start signal so speed not measured, but user noted it took about 1 minute — consistent with the logic being clear. Zero hints, zero bugs. Only issue was `set([...])` wrapping a list comprehension instead of using a set comprehension directly.

---

### Drill 4 — fstring

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 388s | <300s | ❌ |
| secs_bug_fixes | 35s | 0s | ❌ |
| secs_idiomatic_delta | 0s | 0s | ✅ |
| hints_used | 1 | 0 | ❌ |
| lines_written | 1 | — | |

**Analysis:** Needed a hint for `:.2f` colon syntax. Two small bugs: missing `$` and a trailing space. Once fixed, the fstring structure was fully idiomatic — second consecutive session with clean idiom on fstring.

---

### Drill 5 — sorting

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 179s | <300s | ✅ |
| secs_bug_fixes | 75s | 0s | ❌ |
| secs_idiomatic_delta | 64s | 0s | ❌ |
| hints_used | 1 | 0 | ❌ |
| lines_written | 2 | — | |

**Analysis:** Fastest first-done of the session and fastest sorting speed ever (179s). Needed one hint for the lambda tuple syntax. Bug was returning full tuples instead of extracting IDs — a quick fix once flagged. Idiom issue was using `id` as a variable name (shadows Python builtin).

---

### Cross-Session Trend Breakdown

#### heapq

| Instance | secs_to_first_done | secs_idiomatic_delta |
|---|---|---|
| 03-26 #1 | 407s | 5s |
| 03-26 #2 | 1047s | 881s |
| 03-27 #1 | 541s | 493s |
| 03-27 #2 | 168s | 112s |
| 06-01    | 409s | 78s |
| 06-05    | 319s | **748s** |

Speed is improving (319 is 2nd best). Idiom delta regressed sharply — the heapify+nsmallest anti-pattern was new and took long to unpack. Core tuple/negation pattern is solid; the idiom delta is about knowing which heapq functions compose well.

```
heapq — secs_to_first_done (target ≤300s, max=1047s)
03-26 #1  ████████░░░░░░░░░░░░  407s ❌
03-26 #2  ████████████████████  1047s ❌
03-27 #1  ██████████░░░░░░░░░░  541s ❌
03-27 #2  ███░░░░░░░░░░░░░░░░░  168s ✅
06-01     ████████░░░░░░░░░░░░  409s ❌
06-05     ██████░░░░░░░░░░░░░░  319s ❌

heapq — secs_idiomatic_delta (target =0s, max=881s)
03-26 #1  █░░░░░░░░░░░░░░░░░░░  5s ❌
03-26 #2  ████████████████████  881s ❌
03-27 #1  ███████████░░░░░░░░░  493s ❌
03-27 #2  ███░░░░░░░░░░░░░░░░░  112s ❌
06-01     ██░░░░░░░░░░░░░░░░░░  78s ❌
06-05     █████████████████░░░  748s ❌
```

#### list-comp

| Instance | secs_to_first_done | secs_idiomatic_delta |
|---|---|---|
| 03-26 #1 | 110s | 76s |
| 03-26 #2 | 632s | 111s |
| 03-26 #3 | 457s | 126s |
| 03-27 #1 | 545s | 45s |
| 03-27 #2 | 218s | 283s |
| 06-01    | 272s | 75s |
| 06-05    | **699s** | 44s |

Speed regressed (slowest ever) due to wrong initial strategy. Idiom delta is near best (44s). The idiom pattern is getting cleaner; strategy selection is the remaining gap.

```
list-comp — secs_to_first_done (target ≤300s, max=699s)
03-26 #1  ███░░░░░░░░░░░░░░░░░  110s ✅
03-26 #2  ██████████████████░░  632s ❌
03-26 #3  █████████████░░░░░░░  457s ❌
03-27 #1  ████████████████░░░░  545s ❌
03-27 #2  ██████░░░░░░░░░░░░░░  218s ✅
06-01     ████████░░░░░░░░░░░░  272s ✅
06-05     ████████████████████  699s ❌

list-comp — secs_idiomatic_delta (target =0s, max=283s)
03-26 #1  █████░░░░░░░░░░░░░░░  76s ❌
03-26 #2  ████████░░░░░░░░░░░░  111s ❌
03-26 #3  █████████░░░░░░░░░░░  126s ❌
03-27 #1  ███░░░░░░░░░░░░░░░░░  45s ❌
03-27 #2  ████████████████████  283s ❌
06-01     █████░░░░░░░░░░░░░░░  75s ❌
06-05     ███░░░░░░░░░░░░░░░░░  44s ❌
```

#### sets

| Instance | secs_to_first_done | secs_idiomatic_delta |
|---|---|---|
| 03-26 #1 | 357s | 0s |
| 03-26 #2 | 777s | 87s |
| 03-27 #1 | 189s | 71s |
| 03-27 #2 | 253s | 40s |
| 06-02    | — | 511s |
| 06-05    | — | **77s** |

Idiom delta recovered strongly from 511s (06-02) to 77s. The `set([...])` habit is persisting but shrinking. Speed not measured in last two sessions.

```
sets — secs_to_first_done (target ≤300s, max=777s) [entries with data only]
03-26 #1  █████████░░░░░░░░░░░  357s ❌
03-26 #2  ████████████████████  777s ❌
03-27 #1  █████░░░░░░░░░░░░░░░  189s ✅
03-27 #2  ███████░░░░░░░░░░░░░  253s ✅

sets — secs_idiomatic_delta (target =0s, max=511s)
03-26 #1  ░░░░░░░░░░░░░░░░░░░░  0s ✅
03-26 #2  ███░░░░░░░░░░░░░░░░░  87s ❌
03-27 #1  ███░░░░░░░░░░░░░░░░░  71s ❌
03-27 #2  ██░░░░░░░░░░░░░░░░░░  40s ❌
06-02     ████████████████████  511s ❌
06-05     ███░░░░░░░░░░░░░░░░░  77s ❌
```

#### fstring

| Instance | secs_to_first_done | secs_idiomatic_delta |
|---|---|---|
| 03-27 #1 | 373s | 55s |
| 03-27 #2 | 281s | 203s |
| 03-27 #3 | 173s | 82s |
| 06-01    | 513s | 0s |
| 06-05    | 388s | 0s |

Two consecutive clean idiom phases — the fstring pattern is internalised. Speed is inconsistent; the `:.2f` hint cost time today.

```
fstring — secs_to_first_done (target ≤300s, max=513s)
03-27 #1  ███████████████░░░░░  373s ❌
03-27 #2  ███████████░░░░░░░░░  281s ✅
03-27 #3  ███████░░░░░░░░░░░░░  173s ✅
06-01     ████████████████████  513s ❌
06-05     ███████████████░░░░░  388s ❌

fstring — secs_idiomatic_delta (target =0s, max=203s)
03-27 #1  █████░░░░░░░░░░░░░░░  55s ❌
03-27 #2  ████████████████████  203s ❌
03-27 #3  ████████░░░░░░░░░░░░  82s ❌
06-01     ░░░░░░░░░░░░░░░░░░░░  0s ✅
06-05     ░░░░░░░░░░░░░░░░░░░░  0s ✅
```

#### sorting

| Instance | secs_to_first_done | secs_idiomatic_delta |
|---|---|---|
| 03-26 #1 | 388s | 0s |
| 03-26 #2 | 729s | 123s |
| 03-26 #3 | 508s | 0s |
| 03-27 #1 | — | 0s |
| 03-27 #2 | 230s | 0s |
| 06-02    | 506s | 0s |
| 06-05    | **179s** | 64s |

Speed is a clear personal best (179s). Idiom delta regressed after a streak of 0s — the `id` builtin shadowing issue. The multi-key negation pattern is well-internalised; variable naming is the new gap.

```
sorting — secs_to_first_done (target ≤300s, max=729s)
03-26 #1  ███████████░░░░░░░░░  388s ❌
03-26 #2  ████████████████████  729s ❌
03-26 #3  ██████████████░░░░░░  508s ❌
03-27 #2  ██████░░░░░░░░░░░░░░  230s ✅
06-02     ██████████████░░░░░░  506s ❌
06-05     █████░░░░░░░░░░░░░░░  179s ✅

sorting — secs_idiomatic_delta (target =0s, max=123s)
03-26 #1  ░░░░░░░░░░░░░░░░░░░░  0s ✅
03-26 #2  ████████████████████  123s ❌
03-26 #3  ░░░░░░░░░░░░░░░░░░░░  0s ✅
03-27 #1  ░░░░░░░░░░░░░░░░░░░░  0s ✅
03-27 #2  ░░░░░░░░░░░░░░░░░░░░  0s ✅
06-02     ░░░░░░░░░░░░░░░░░░░░  0s ✅
06-05     ██████████░░░░░░░░░░  64s ❌
```

