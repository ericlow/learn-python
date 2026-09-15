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

## 2026-06-05 — Session (6 drills)

### Session Summary Table

| # | Category | secs_to_first_done | secs_bug_fixes | secs_idiomatic_delta | secs_total | hints | lines | clean_submit |
|---|---|---|---|---|---|---|---|---|
| 1 | heapq | 319s | 0s | 748s | 1067s | 1 | 3 | ❌ |
| 2 | list-comp | 699s | 98s | 44s | 841s | 2 | 1 | ❌ |
| 3 | sets | — | 0s | 77s | 77s | 0 | 2 | ❌ |
| 4 | fstring | 388s | 35s | 0s | 423s | 1 | 1 | ❌ |
| 5 | sorting | 179s | 75s | 64s | 318s | 1 | 2 | ❌ |
| 6 | heapq | 196s | 0s | 0s | 208s | 0 | 3 | ✅ |

**Intra-session trends (session 1):**
- Speed improved across session 1: 319 → 699 → — → 388 → 179. Drill 5 was the fastest.
- Hints flat at 1 per drill except drill 3 (0) and drill 2 (2). No improvement within session.
- No clean submits in session 1: every drill had either a bug or an idiom issue.

**Session 2 (drill 6):**
- heapq: 196s ✅, 0 bugs ✅, 0 idiom delta ✅ — first clean heapq submit ever. Tuple tie-breaking clicked.

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

### Drill 6 — heapq (Session 2)

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 196s | <300s | ✅ |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | 0s | 0s | ✅ |
| hints_used | 0 | 0 | ✅ |
| lines_written | 3 | — | |

**Analysis:** First clean heapq submit. The `heapify` + list comp pop pattern applied immediately. Key insight absorbed: `(cost, name)` tuples let Python handle tie-breaking automatically — no extra code needed.

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
| 06-05 #1 | 319s | 748s |
| 06-05 #2 | **196s** | **0s** |

Best speed ever (196s, under 300s for the first time). First ever 0s idiom delta — the tuple tie-breaking insight (Python tuple comparison is automatic, no extra code needed) clicked in the explanation phase and carried immediately into the next attempt.

```
heapq — secs_to_first_done (target ≤300s, max=1047s)
03-26 #1   ████████░░░░░░░░░░░░  407s ❌
03-26 #2   ████████████████████  1047s ❌
03-27 #1   ██████████░░░░░░░░░░  541s ❌
03-27 #2   ███░░░░░░░░░░░░░░░░░  168s ✅
06-01      ████████░░░░░░░░░░░░  409s ❌
06-05 #1   ██████░░░░░░░░░░░░░░  319s ❌
06-05 #2   ████░░░░░░░░░░░░░░░░  196s ✅

heapq — secs_idiomatic_delta (target =0s, max=881s)
03-26 #1   █░░░░░░░░░░░░░░░░░░░  5s ❌
03-26 #2   ████████████████████  881s ❌
03-27 #1   ███████████░░░░░░░░░  493s ❌
03-27 #2   ███░░░░░░░░░░░░░░░░░  112s ❌
06-01      ██░░░░░░░░░░░░░░░░░░  78s ❌
06-05 #1   █████████████████░░░  748s ❌
06-05 #2   ░░░░░░░░░░░░░░░░░░░░  0s ✅
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


## 2026-07-23

### Drill 1 — heapq

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 483s | < 300s ❌ |
| secs_bug_fixes | 61s | 0s ❌ |
| secs_idiomatic_delta | 0s | 0s ✅ |
| secs_total | 544s | — |
| hints_used | 0 | 0 ✅ |
| lines_written | 7 | — |

Used heapify + heappop loop with inverted tuples for tie-breaking — correct approach. Bug: looped over `len(new_list)` instead of `k`, returning all items. Core mechanic was solid; missed the stopping condition. No hints needed.

**Cross-drill trend (so far):** 1 drill in. Speed still slow for heapq (483s vs 300s target), consistent with history where heapq routinely exceeds 300s.

### Drill 2 — list-comp

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 293s | < 300s ✅ |
| secs_bug_fixes | 0s | 0s ✅ |
| secs_idiomatic_delta | 614s | 0s ❌ |
| secs_total | 907s | — |
| hints_used | 0 | 0 ✅ |
| lines_written | 7 | — |

Fast and correct on first check (for loop). Rewrote as a list comp after the idiom flag — the fix landed correctly but took ~10 min. No bugs, no hints. Consistent pattern: list-comp logic is solid, but the idiomatic form doesn't come first.

**Cross-drill trend:** 2 drills in. Speed improving (483s → 293s). Zero bugs both times. Idiom delta is the persistent gap — 0s on heapq, 614s on list-comp. List-comp idiom delta has been ❌ in every session.

### Drill 3 — sets

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 175s | < 300s ✅ |
| secs_bug_fixes | 36s | 0s ❌ |
| secs_idiomatic_delta | 0s | 0s ✅ |
| secs_total | 211s | — |
| hints_used | 1 | 0 — |
| lines_written | 1 | — |

Needed 1 hint to land on set difference (`-` operator). Missing `sorted()` was the only bug — quick fix. Final solution was a clean one-liner. Speed well under target.

**Cross-drill trend:** 3 drills in. Speed: 483s → 293s → 175s — consistently improving. Idiom: 0s, 614s, 0s — list-comp is the outlier. Bug fixes present on drills 1 and 3 (off-by-one on k, missing sorted). Simple errors, quick fixes.

### Drill 4 — fstring

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 278s | < 300s ✅ |
| secs_bug_fixes | 1586s | 0s ❌ |
| secs_idiomatic_delta | 0s | 0s ✅ |
| secs_total | 1864s | — |
| hints_used | 2 | 0 ❌ |
| lines_written | 1 | — |

Under 300s on first attempt but two bugs required multiple rounds to fix: missing `.strip()` on name and missing `:.2f` on unit price (only applied it to total initially). Both needed hints. Final solution was a clean idiomatic one-liner. The f-string structure itself is solid — the format spec and strip are the recurring gaps.

**Cross-drill trend:** 4 drills in. Speed: 483 → 293 → 175 → 278 — all recent drills under 300s. Bug fixes are the new problem: two drills with substantial fix time (61s heapq, 1586s fstring). Idiom is clean on 3/4 drills.

### Drill 5 — sorting

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 236s | < 300s ✅ |
| secs_bug_fixes | 0s | 0s ✅ |
| secs_idiomatic_delta | 178s | 0s ❌ |
| secs_total | 414s | — |
| hints_used | 1 | 0 — |
| lines_written | 2 | — |

Needed 1 hint for the lambda tuple key. No bugs. Idiom miss: used named variables (dept, yr) in the list comp instead of _ for unused slots. Fixed once flagged. The multi-key negation pattern itself was applied correctly.

**Cross-drill trend (session complete):** Speed: 483 → 293 → 175 → 278 → 236. All but drill 1 under 300s. Bug fixes were the surprise problem today — fstring cost 1586s on two separate correctness issues. Idiom clean on heapq, sets, fstring; list-comp (wrote for loop) and sorting (unused vars) had delta.

---

## Session Summary — 2026-07-23

| # | Category | secs_to_first_done | secs_bug_fixes | secs_idiomatic_delta | secs_total | hints | lines | clean? |
|---|---|---|---|---|---|---|---|---|
| 1 | heapq | 483s ❌ | 61s ❌ | 0s ✅ | 544s | 0 | 7 | ❌ |
| 2 | list-comp | 293s ✅ | 0s ✅ | 614s ❌ | 907s | 0 | 7 | ❌ |
| 3 | sets | 175s ✅ | 36s ❌ | 0s ✅ | 211s | 1 | 1 | ❌ |
| 4 | fstring | 278s ✅ | 1586s ❌ | 0s ✅ | 1864s | 2 | 1 | ❌ |
| 5 | sorting | 236s ✅ | 0s ✅ | 178s ❌ | 414s | 1 | 2 | ❌ |

Sets: best result ever (175s / 0s). Fstring: idiom clean 3rd consecutive session. Heapq: idiom clean 2nd consecutive session. List-comp: speed finally consistent but idiom instinct still not there. Sorting: speed solid, idiom delta crept back in (unused vars).

```
Speed (secs_to_first_done, target ≤300s)

  heapq (max=1047s)
  03-26 #1  ████████░░░░░░░░░░░░  407s ❌
  03-26 #2  ████████████████████  1047s ❌
  03-27 #1  ██████████░░░░░░░░░░  541s ❌
  03-27 #2  ███░░░░░░░░░░░░░░░░░  168s ✅
  06-01     ████████░░░░░░░░░░░░  409s ❌
  06-05 #1  ██████░░░░░░░░░░░░░░  319s ❌
  06-05 #2  ████░░░░░░░░░░░░░░░░  196s ✅
  07-23     █████████░░░░░░░░░░░  483s ❌

  list-comp (max=699s)
  03-26 #1  ███░░░░░░░░░░░░░░░░░  110s ✅
  03-26 #2  ██████████████████░░  632s ❌
  03-26 #3  █████████████░░░░░░░  457s ❌
  03-27 #1  ████████████████░░░░  545s ❌
  03-27 #2  ██████░░░░░░░░░░░░░░  218s ✅
  06-01     ████████░░░░░░░░░░░░  272s ✅
  06-05     ████████████████████  699s ❌
  07-23     ████████░░░░░░░░░░░░  293s ✅

  sets (max=777s)
  03-26 #1  █████████░░░░░░░░░░░  357s ❌
  03-26 #2  ████████████████████  777s ❌
  03-27 #1  █████░░░░░░░░░░░░░░░  189s ✅
  03-27 #2  ███████░░░░░░░░░░░░░  253s ✅
  07-23     █████░░░░░░░░░░░░░░░  175s ✅

  fstring (max=513s)
  03-27 #1  ███████████████░░░░░  373s ❌
  03-27 #2  ███████████░░░░░░░░░  281s ✅
  03-27 #3  ███████░░░░░░░░░░░░░  173s ✅
  06-01     ████████████████████  513s ❌
  06-05     ███████████████░░░░░  388s ❌
  07-23     ███████████░░░░░░░░░  278s ✅

  sorting (max=729s)
  03-26 #1  ███████████░░░░░░░░░  388s ❌
  03-26 #2  ████████████████████  729s ❌
  03-26 #3  ██████████████░░░░░░  508s ❌
  03-27 #2  ██████░░░░░░░░░░░░░░  230s ✅
  06-02     ██████████████░░░░░░  506s ❌
  06-05     █████░░░░░░░░░░░░░░░  179s ✅
  07-23     ██████░░░░░░░░░░░░░░  236s ✅

Idiom delta (target =0s)

  heapq (max=881s)
  03-26 #1  █░░░░░░░░░░░░░░░░░░░  5s ❌
  03-26 #2  ████████████████████  881s ❌
  03-27 #1  ███████████░░░░░░░░░  493s ❌
  03-27 #2  ███░░░░░░░░░░░░░░░░░  112s ❌
  06-01     ██░░░░░░░░░░░░░░░░░░  78s ❌
  06-05 #1  █████████████████░░░  748s ❌
  06-05 #2  ░░░░░░░░░░░░░░░░░░░░  0s ✅
  07-23     ░░░░░░░░░░░░░░░░░░░░  0s ✅

  list-comp (max=614s)
  03-26 #1  ██░░░░░░░░░░░░░░░░░░  76s ❌
  03-26 #2  ████░░░░░░░░░░░░░░░░  111s ❌
  03-26 #3  ████░░░░░░░░░░░░░░░░  126s ❌
  03-27 #1  █░░░░░░░░░░░░░░░░░░░  45s ❌
  03-27 #2  █████████░░░░░░░░░░░  283s ❌
  06-01     ██░░░░░░░░░░░░░░░░░░  75s ❌
  06-05     █░░░░░░░░░░░░░░░░░░░  44s ❌
  07-23     ████████████████████  614s ❌

  sets (max=511s)
  03-26 #1  ░░░░░░░░░░░░░░░░░░░░  0s ✅
  03-26 #2  ███░░░░░░░░░░░░░░░░░  87s ❌
  03-27 #1  ███░░░░░░░░░░░░░░░░░  71s ❌
  03-27 #2  ██░░░░░░░░░░░░░░░░░░  40s ❌
  06-02     ████████████████████  511s ❌
  06-05     ███░░░░░░░░░░░░░░░░░  77s ❌
  07-23     ░░░░░░░░░░░░░░░░░░░░  0s ✅

  fstring (max=203s)
  03-27 #1  █████░░░░░░░░░░░░░░░  55s ❌
  03-27 #2  ████████████████████  203s ❌
  03-27 #3  ████████░░░░░░░░░░░░  82s ❌
  06-01     ░░░░░░░░░░░░░░░░░░░░  0s ✅
  06-05     ░░░░░░░░░░░░░░░░░░░░  0s ✅
  07-23     ░░░░░░░░░░░░░░░░░░░░  0s ✅

  sorting (max=178s)
  03-26 #1  ░░░░░░░░░░░░░░░░░░░░  0s ✅
  03-26 #2  ██████████████░░░░░░  123s ❌
  03-26 #3  ░░░░░░░░░░░░░░░░░░░░  0s ✅
  03-27 #1  ░░░░░░░░░░░░░░░░░░░░  0s ✅
  03-27 #2  ░░░░░░░░░░░░░░░░░░░░  0s ✅
  06-02     ░░░░░░░░░░░░░░░░░░░░  0s ✅
  06-05     ███████░░░░░░░░░░░░░  64s ❌
  07-23     ████████████████████  178s ❌
```

## 2026-07-24

### Drill 1 — list-comp

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 190s | ≤300s ✅ |
| secs_bug_fixes | 0s | 0s ✅ |
| secs_idiomatic_delta | 0s | 0s ✅ |
| secs_total | 190s | |
| hints_used | 0 | |
| lines_written | 1 | |

Clean, fast, idiomatic on first submission. Used a single list comprehension with inline split and filter — exactly the right pattern. Contrast with last session (614s idiomatic delta) where the idiom phase broke down; today was a complete reversal.

**Cross-drill trend (after 1/5):** Strong start — 0 hints, 0 bug fixes, under the 300s target.

### Drill 2 — heapq

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 295s | ≤300s ✅ |
| secs_bug_fixes | 0s | 0s ✅ |
| secs_idiomatic_delta | 0s | 0s ✅ |
| secs_total | 295s | |
| hints_used | 0 | |
| lines_written | 9 | |

Correct on first check, 295s — just inside the target. Correctly structured the heap tuple as (priority, created_at, name) for natural sort ordering. heapify + heappop is a solid pattern; nsmallest would have been slightly more concise but equally valid.

**Cross-drill trend (after 2/5):** 2 for 2 — clean submissions, no hints, both under 300s. Strong session so far.

### Drill 3 — fstring

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 295s | ≤300s ✅ |
| secs_bug_fixes | 31s | 0s ❌ |
| secs_idiomatic_delta | 124s | 0s ❌ |
| secs_total | 450s | |
| hints_used | 1 | |
| lines_written | 5 | |

Used hyphen instead of em dash (copy detail) and initially reached for range(len()) instead of enumerate — needed a hint and two correction rounds. The f-string formatting itself (:.2f) was correct. Key takeaway: enumerate is the default when you need index + value.

**Cross-drill trend (after 3/5):** First blemishes of the session — bug fix time and idiom delta both non-zero. Drills 1-2 were clean; drill 3 shows enumerate isn't automatic yet.

### Drill 4 — sets

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 114s | ≤300s ✅ |
| secs_bug_fixes | 90s | 0s ❌ |
| secs_idiomatic_delta | 0s | 0s ✅ |
| secs_total | 204s | |
| hints_used | 0 | |
| lines_written | 2 | |

Set intersection was immediate and correct. Bugs were output-shape errors: converted to int instead of keeping strings, and forgot to sort. No hints needed; idiom was clean once correct. Key watch: track return type through the whole expression.

**Cross-drill trend (after 4/5):** secs_bug_fixes is the theme today — drills 3 and 4 both had non-zero fix time. Speed and idioms are otherwise solid.

### Drill 5 — json

| Metric | Value | Target |
|---|---|---|
| secs_to_first_done | 403s | ≤300s ❌ |
| secs_bug_fixes | 0s | 0s ✅ |
| secs_idiomatic_delta | 108s | 0s ❌ |
| secs_total | 511s | |
| hints_used | 3 | |
| lines_written | 3 | |

First json drill — needed hints for json.loads, None (not Null), and tuple syntax in list comp. Logic was sound once the mechanics were in place; no bugs after the hints. Key things to memorize: json.loads() to parse, null→None, and sorted(key=lambda) for sorting dicts.

**Cross-drill trend (after 5/5):** Session ended on a harder note — json was new territory and it showed (3 hints). Drills 1-2 were the cleanest. Bug fixes and idiom deltas crept in on drills 3-5.

---

## Session Summary — 2026-07-24

| # | Category | secs_to_first_done | secs_bug_fixes | secs_idiomatic_delta | secs_total | hints | lines | clean_submit |
|---|---|---|---|---|---|---|---|---|
| 1 | list-comp | 190s | 0s | 0s | 190s | 0 | 1 | ✅ |
| 2 | heapq | 295s | 0s | 0s | 295s | 0 | 9 | ✅ |
| 3 | fstring | 295s | 31s | 124s | 450s | 1 | 5 | ❌ |
| 4 | sets | 114s | 90s | 0s | 204s | 0 | 2 | ❌ |
| 5 | json | 403s | 0s | 108s | 511s | 3 | 3 | ❌ |

Intra-session: clean starts (drills 1-2), degraded on drills 3-5. Hints 0,0,1,0,3 — json was unfamiliar territory.

### Cross-session ASCII charts

**list-comp speed (max=699s)**
```
03-26 #1  ███░░░░░░░░░░░░░░░░░  110s ✅
03-26 #2  ██████████████████░░  632s ❌
03-26 #3  █████████████░░░░░░░  457s ❌
03-27 #1  ████████████████░░░░  545s ❌
03-27 #2  ██████░░░░░░░░░░░░░░  218s ✅
06-01     ████████░░░░░░░░░░░░  272s ✅
06-05     ████████████████████  699s ❌
07-23     ████████░░░░░░░░░░░░  293s ✅
07-24     █████░░░░░░░░░░░░░░░  190s ✅
```

**list-comp idiom delta (max=614s)**
```
03-26 #1  ██░░░░░░░░░░░░░░░░░░   76s ❌
03-26 #2  ████░░░░░░░░░░░░░░░░  111s ❌
03-26 #3  ████░░░░░░░░░░░░░░░░  126s ❌
03-27 #1  █░░░░░░░░░░░░░░░░░░░   45s ❌
03-27 #2  █████████░░░░░░░░░░░  283s ❌
06-01     ██░░░░░░░░░░░░░░░░░░   75s ❌
06-05     █░░░░░░░░░░░░░░░░░░░   44s ❌
07-23     ████████████████████  614s ❌
07-24     ░░░░░░░░░░░░░░░░░░░░    0s ✅
```

**heapq speed (max=1047s)**
```
03-26 #1  ████████░░░░░░░░░░░░  407s ❌
03-26 #2  ████████████████████  1047s ❌
03-27 #1  ██████████░░░░░░░░░░  541s ❌
03-27 #2  ███░░░░░░░░░░░░░░░░░  168s ✅
06-01     ████████░░░░░░░░░░░░  409s ❌
06-05 #1  ██████░░░░░░░░░░░░░░  319s ❌
06-05 #2  ████░░░░░░░░░░░░░░░░  196s ✅
07-23     █████████░░░░░░░░░░░  483s ❌
07-24     █████░░░░░░░░░░░░░░░  295s ✅
```

**heapq idiom delta (max=881s)**
```
03-26 #1  ░░░░░░░░░░░░░░░░░░░░    5s ❌
03-26 #2  ████████████████████  881s ❌
03-27 #1  ███████████░░░░░░░░░  493s ❌
03-27 #2  ██░░░░░░░░░░░░░░░░░░  112s ❌
06-01     ██░░░░░░░░░░░░░░░░░░   78s ❌
06-05 #1  █████████████████░░░  748s ❌
06-05 #2  ░░░░░░░░░░░░░░░░░░░░    0s ✅
07-23     ░░░░░░░░░░░░░░░░░░░░    0s ✅
07-24     ░░░░░░░░░░░░░░░░░░░░    0s ✅
```

**fstring speed (max=513s)**
```
03-27 #1  ██████████████░░░░░░  373s ❌
03-27 #2  ███████████░░░░░░░░░  281s ✅
03-27 #3  ██████░░░░░░░░░░░░░░  173s ✅
06-01     ████████████████████  513s ❌
06-05     ███████████████░░░░░  388s ❌
07-23     ██████████░░░░░░░░░░  278s ✅
07-24     ███████████░░░░░░░░░  295s ✅
```

**fstring idiom delta (max=203s)**
```
03-27 #1  █████░░░░░░░░░░░░░░░   55s ❌
03-27 #2  ████████████████████  203s ❌
03-27 #3  ████████░░░░░░░░░░░░   82s ❌
06-01     ░░░░░░░░░░░░░░░░░░░░    0s ✅
06-05     ░░░░░░░░░░░░░░░░░░░░    0s ✅
07-23     ░░░░░░░░░░░░░░░░░░░░    0s ✅
07-24     ████████████░░░░░░░░  124s ❌
```

**sets speed (max=777s)**
```
03-26 #1  █████████░░░░░░░░░░░  357s ❌
03-26 #2  ████████████████████  777s ❌
03-27 #1  ████░░░░░░░░░░░░░░░░  189s ✅
03-27 #2  ██████░░░░░░░░░░░░░░  253s ✅
07-23     ████░░░░░░░░░░░░░░░░  175s ✅
07-24     ███░░░░░░░░░░░░░░░░░  114s ✅
```

**sets idiom delta (max=511s)**
```
03-26 #1  ░░░░░░░░░░░░░░░░░░░░    0s ✅
03-26 #2  ███░░░░░░░░░░░░░░░░░   87s ❌
03-27 #1  ██░░░░░░░░░░░░░░░░░░   71s ❌
03-27 #2  █░░░░░░░░░░░░░░░░░░░   40s ❌
06-02     ████████████████████  511s ❌
06-05     ███░░░░░░░░░░░░░░░░░   77s ❌
07-23     ░░░░░░░░░░░░░░░░░░░░    0s ✅
07-24     ░░░░░░░░░░░░░░░░░░░░    0s ✅
```

**json** — first appearance: 403s / 0s bugs / 108s idiom delta / 3 hints

### Callouts
- list-comp idiom: first ever 0s after 8 attempts — breakthrough
- heapq idiom: 3 consecutive 0s — solidified
- fstring idiom: regression after 3 clean sessions — enumerate gap
- json: baseline set, mechanics to memorize: json.loads(), None check, sorted(key=lambda)
- Recurring: output shape bugs — read the return type before writing the list comp

---

## 2026-07-26 — Session

### Drill 1 — json

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 635s | ≤300s | ❌ |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | 1384s | 0s | ❌ |
| secs_total | 2019s | — | |
| hints | 4 | — | |
| lines | 4 | — | |

Key errors: used `json.load` instead of `json.loads`; `sorted()` result not assigned; `datetime.fromisoformat` not used in sort key initially. Idiom delta inflated by interruption — not a true measurement.

### Drill 2 — heapq

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 332s | ≤300s | ❌ |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | 182s | 0s | ❌ |
| secs_total | 514s | — | |
| hints | 0 | — | |
| lines | 2 | — | |

Correct on first check. Got the negation pattern right immediately. Idiom delta: started with heappush+nsmallest mix, refactored to clean nsmallest one-liner after discussion. Asked good conceptual question about nlargest — understood why string negation makes it awkward.

### Drill 3 — list-comp

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 125s | ≤300s | ✅ |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | 213s | 0s | ❌ |
| secs_total | 338s | — | |
| hints | 1 | — | |
| lines | 1 | — | |

Fast and correct. Double-split was the idiom gap — learned maxsplit=1 during session and applied it, but didn't eliminate the double call. Generator unpacking pattern still unfamiliar.

### Drill 4 — fstring

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 177s | ≤300s | ✅ |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | 0s | 0s | ✅ |
| secs_total | 177s | — | |
| hints | 0 | — | |
| lines | 1 | — | |

Clean submit. Inline arithmetic inside f-string with format spec — no intermediate variables needed.

### Drill 5 — sets

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 158s | ≤300s | ✅ |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | 0s | 0s | ✅ |
| secs_total | 158s | — | |
| hints | 0 | — | |
| lines | 2 | — | |

Clean submit. Set difference then filter — correct pattern. Minor: redundant list brackets inside sorted().

### Drill 6 — sorting

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 220s | ≤300s | ✅ |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | 0s | 0s | ✅ |
| secs_total | 220s | — | |
| hints | 1 | — | |
| lines | 1 | — | |

Clean submit. Got tuple key with negation right. Syntax error on first attempt (positional lambda instead of key=) — needed reminder about keyword argument.

---

### Session Summary (6 drills completed)

| # | Category | secs_to_correct | secs_idiomatic_delta | secs_total | hints | lines | clean_submit |
|---|---|---|---|---|---|---|---|
| 1 | json | 635 | 1384* | 2019 | 4 | 4 | ✅ |
| 2 | heapq | 332 | 182 | 514 | 0 | 2 | ✅ |
| 3 | list-comp | 125 | 213 | 338 | 1 | 1 | ✅ |
| 4 | fstring | 177 | 0 | 177 | 0 | 1 | ✅ |
| 5 | sets | 158 | 0 | 158 | 0 | 2 | ✅ |
| 6 | sorting | 220 | 0 | 220 | 1 | 1 | ✅ |

*json idiom delta inflated by interruption.

Intra-session: speed settled 125–220 after drill 1 stumble. 6/6 clean submits. Last 3 drills: idiom delta = 0.

Cross-session priorities: json (slow+hinting), heapq (idiom regression), list-comp (double-split).

---

## 2026-07-27 — Session

### Drill 1 — sorting

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 267s | ≤300s | ✅ |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | 0s | 0s | ✅ |
| secs_total | 267s | — | |
| hints | 0 | — | |
| lines | 1 | — | |

Clean submit.

### Drill 2 — sorting

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 565s | ≤300s | ❌ |
| secs_bug_fixes | 480s | 0s | ❌ |
| secs_idiomatic_delta | 0s | 0s | ✅ |
| secs_total | 1045s | — | |
| hints | 0 | — | |
| lines | 1 | — | |

Slow start and correctness bugs on a sorting drill — the extra time was spent fixing a logic error, not learning. Sorting regressions after clean runs are often output-shape errors (wrong structure returned).

### Drill 3 — sorting

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 241s | ≤300s | ✅ |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | 0s | 0s | ✅ |
| secs_total | 241s | — | |
| hints | 0 | — | |
| lines | 2 | — | |

Clean submit. Multi-key sort with negation and tiebreaker — correct pattern, no hesitation.

### Drill 4 — sorting

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 312s | ≤300s | ❌ |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | 35s | 0s | ❌ |
| secs_total | 347s | — | |
| hints | 0 | — | |
| lines | 3 | — | |

Just over the speed target. Correct on first check. Idiom gap: wrote `not bool(runner["dnf"])` — `bool()` is redundant on an actual bool, `not runner["dnf"]` is the clean form.

### Drill 5 — sorting

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 257s | ≤300s | ✅ |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | 0s | 0s | ✅ |
| secs_total | 257s | — | |
| hints | 0 | — | |
| lines | 2 | — | |

Clean submit. Multi-key ascending sort — straightforward tuple key, no hesitation.

### Drill 6 — sorting

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 224s | ≤300s | ✅ |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | 0s | 0s | ✅ |
| secs_total | 224s | — | |
| hints | 0 | — | |
| lines | 2 | — | |

Clean submit. Filter-in-list-comp with negation in sort key — correct pattern applied without hesitation.

### Drill 7 — sorting

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 133s | ≤300s | ✅ |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | 0s | 0s | ✅ |
| secs_total | 133s | — | |
| hints | 0 | — | |
| lines | 2 | — | |

Clean submit. Three-key sort with negation on float — fastest drill of the session so far.

### Drill 8 — sorting

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 209s | ≤300s | ✅ |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | 0s | 0s | ✅ |
| secs_total | 209s | — | |
| hints | 0 | — | |
| lines | 2 | — | |

Clean submit. Filter in list comp, negation in sort key — pattern fully automatic now.

### Drill 9 — sorting

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 141s | ≤300s | ✅ |
| secs_bug_fixes | 0s | 0s | ✅ |
| secs_idiomatic_delta | 0s | 0s | ✅ |
| secs_total | 141s | — | |
| hints | 0 | — | |
| lines | 2 | — | |

Clean submit. Three-key sort with mixed directions. Timer adjusted for pause.

### Drill 10 — sorting

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_done | 103s | ≤300s | ✅ |
| secs_bug_fixes | 10s | 0s | ❌ |
| secs_idiomatic_delta | 0s | 0s | ✅ |
| secs_total | 113s | — | |
| hints | 0 | — | |
| lines | 2 | — | |

Fastest drill of the session. Missed the `total >= 100` filter on first submit — fixed in ~10s once spotted. Bug was an omission (forgot the filter), not a logic error.

---

### Session Summary (10 drills completed)

| # | secs_to_first_done | secs_bug_fixes | secs_idiomatic_delta | secs_total | hints | lines | clean_submit |
|---|---|---|---|---|---|---|---|
| 1 | 267s | 0 | 0 | 267s | 0 | 1 | ✅ |
| 2 | 565s | 480 | 0 | 1045s | 0 | 1 | ❌ |
| 3 | 241s | 0 | 0 | 241s | 0 | 2 | ✅ |
| 4 | 312s | 0 | 35 | 347s | 0 | 3 | ✅ |
| 5 | 257s | 0 | 0 | 257s | 0 | 2 | ✅ |
| 6 | 224s | 0 | 0 | 224s | 0 | 2 | ✅ |
| 7 | 133s | 0 | 0 | 133s | 0 | 2 | ✅ |
| 8 | 209s | 0 | 0 | 209s | 0 | 2 | ✅ |
| 9 | 141s | 0 | 0 | 141s | 0 | 2 | ✅ |
| 10 | 103s | 10 | 0 | 113s | 0 | 2 | ❌ |

Intra-session: speed trend strongly downward after drill 2 stumble — last 5 drills averaged 165s. Idiom delta appeared only once (drill 4, minor). 0 hints across all 10. Two non-clean submits: drill 2 (logic bug) and drill 10 (filter omission).

Cross-session: sorting speed has converged from ~540s avg (March) to sub-200s by end of today. Idiom gaps rare and shrinking. Main remaining risk: filter omissions when spec combines filter + sort — read the full spec before writing.
