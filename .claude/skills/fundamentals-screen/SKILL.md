---
name: fundamentals-screen
description: >
  Generate and run a Python fundamentals screen — 4–6 standalone exercises at
  the "fluency + basic design awareness" tier. Above mechanical drills (design
  awareness is evaluated, no time pressure); below LeetCode Easy (no progressive
  requirements, no pattern recognition, no complexity reasoning). Targets companies
  that use a live screen-share fundamentals format (e.g. Axle). Triggers on
  "fundamentals screen", "fluency screen", "Python basics screen", or "Axle-style".
---

# Python Fundamentals Screen

## What This File Is
Generates and runs a set of 4–6 standalone Python exercises that mirror the
fundamentals / fluency screen format observed in real interviews. Each exercise
is Phase 1 only — no search, no optimization, no progressive requirements.
Runs the session itself; does not hand off to interview-coach.

## Tier definition
**Above mechanical drills:** Every exercise has a design question the interviewer
asks. Candidates must articulate *why* they made a choice (mutate vs. fresh dict,
traversal direction, which data structure). Correctness alone is not enough.

**Below LeetCode Easy:** No phase escalation. No naive-vs-optimal gap. No algorithm
selection. All solutions are O(n) or simpler.

---

## Step 1: Select Exercises

Read `screen_metrics.csv` if it exists. For each category compute:

```
weight = (1 / (attempts + 1)) + slow_rate + non_idiomatic_rate
```

where `slow_rate` = fraction of attempts where `secs_to_first_done > 300` and
`non_idiomatic_rate` = fraction where `secs_idiomatic_delta > 0`.

Pick 4–6 highest-weighted categories. Fill slots with no history using
least-attempted first. Never repeat a category in the same session.

### Exercise Categories

**List / sequence**

| ID | What it tests | Design question to ask | Common anti-pattern |
|---|---|---|---|
| `list-filter` | Filter + parameterize | "What changes if the list is empty?" | Hardcoding the condition |
| `dedup-first` | Deduplicate preserving order, keep first | "Why set over checking the output list?" | O(n²) with `if x not in result` |
| `dedup-last` | Deduplicate preserving order, keep last | "How does this differ from keep-first?" | Forgetting to reverse |
| `flatten` | Flatten one level of nesting | "What if a sublist is empty?" | Using `+` in a loop — O(n²) |
| `partition` | Split list into two by predicate | "Tuple or two separate returns — why?" | Mutating the input list |
| `rotate` | Rotate a list left or right by k steps | "In-place or fresh list?" | Off-by-one with modulo; not handling k > len |
| `chunk` | Split list into fixed-size chunks | "What if the list doesn't divide evenly?" | Losing the last partial chunk |
| `interleave` | Interleave two lists element by element | "What if the lists have different lengths?" | Stopping at the shorter list |
| `map-transform` | Apply a parameterized transform to every element | "Lambda vs named function — when does it matter?" | Modifying the input list in place |
| `running-accum` | Running max/min/sum as a new list | "Is there a one-liner approach?" | Off-by-one on initial accumulator value |

**Dict**

| ID | What it tests | Design question to ask | Common anti-pattern |
|---|---|---|---|
| `dict-merge` | Merge two dicts, explicit collision strategy | "Should this mutate either input?" | Mutating `d1` or `d2` in place |
| `dict-invert` | Flip keys and values | "What if two keys share a value?" | Silently overwriting duplicates |
| `group-by` | Group items into dict of lists by a key | "defaultdict or manual check — any preference?" | Forgetting to initialize the list |
| `freq-count` | Count occurrences without Counter | "How would you do this with Counter instead?" | `dict[k] = dict[k] + 1` without `.get()` |
| `dict-filter` | Filter a dict by a value condition | "Mutate or return new dict?" | Mutating while iterating |
| `top-n-by-value` | Return top N keys sorted by value | "What if n > len(dict)?" | Reaching for heapq when `sorted()` is sufficient |
| `nested-get` | Safely access a nested dict key with a fallback | "Missing intermediate key — raise or return default?" | KeyError on missing intermediate key |
| `zip-to-dict` | Zip two lists (keys, values) into a dict | "Different lengths? Repeated keys?" | Silently truncating at the shorter list |

**String**

| ID | What it tests | Design question to ask | Common anti-pattern |
|---|---|---|---|
| `word-freq` | Count word frequencies from a sentence | "Case sensitivity? Strip punctuation?" | Not normalizing case or punctuation |
| `anagram-check` | Check if two strings are anagrams | "sorted() vs Counter — which do you prefer and why?" | Checking length only, missing character-count mismatch |
| `string-compress` | Run-length encoding ("aaabbc" → "3a2b1c") | "What if the input is empty?" | Off-by-one when flushing the final group |
| `string-split-clean` | Split on delimiter, strip whitespace, filter empty tokens | "Return new list or mutate? Double delimiter?" | `"  a  ,  ,  b  "` — empty token from double comma |
| `reverse-words` | Reverse order of words in a sentence | "Preserve extra whitespace or normalize to single spaces?" | `"  hello   world  "` — naive split/join drops spacing |
| `camel-to-snake` | Convert camelCase identifier to snake_case (basic form, no consecutive caps) | "In-place string build or split on uppercase chars?" | `"getUserName"` — must not produce `_get_user_name` with leading underscore |
| `dedupe-chars` | Remove duplicate characters preserving order | "Keep first or last occurrence — does it matter here?" | `"abacbc"` — must preserve first occurrence, not last |
| `truncate-words` | Truncate a string to N chars at a word boundary, append "..." | "Cut mid-word or at word boundary? What if N < 3?" | String exactly N chars — should not append "..." |

**Parameterized number**

| ID | What it tests | Design question to ask | Common anti-pattern |
|---|---|---|---|
| `fizzbuzz-variant` | Multiple parameterized divisibility rules | "How would you make the rules table-driven?" | Hardcoding condition pairs; wrong evaluation order |

---

## Step 2: Generate Each Exercise

For each selected category, write an exercise with:
- A fully-specified problem statement (no design decisions required — interface is given)
- One input/output example that includes a tricky detail (empty input, duplicate keys,
  all-same values, collision on merge, etc.)
- Function signature only — `pass` body

Save to `screens/YYMMDD-ex{N}-{category}.py` using the Write tool. File must contain:
- A docstring with the full problem statement (candidate must be able to read the file
  and know exactly what to implement without referring back to the conversation)
- The function signature + `pass`
- A commented-out driver at the bottom showing expected output for happy path and the
  tricky detail

---

## Step 3: Run the Session

Present exercises one at a time. Do not reveal the full list upfront.
Say: "Today's screen: {N} exercises. Starting with exercise 1."

### Per-exercise flow

1. **Present** the problem statement (paste from the file). Say: "Let me know when
   you're ready to start."

2. **When user says ready:** Run `date +%s` → record as `t_start`.

3. **While candidate codes:** Do not intervene unless asked. If asked for help, give
   one hint — the relevant mechanic only, no solution sketch. Increment hints counter.

4. **When candidate says done:** Run `date +%s` → record as `t_first_done`.
   - Read the `.py` file; run it against happy path and tricky detail
   - If **incorrect**: name the specific failure, let them fix it

5. **When logically correct:** Run `date +%s` → record as `t_correct`.
   - Ask the design question for this category
   - Let them refactor if they want; run `date +%s` → record as `t_idiomatic` when done

6. Say "Moving to exercise {N+1}." No extended feedback mid-session.

Compute per-exercise:
- `secs_to_first_done` = `t_first_done - t_start`
- `secs_bug_fixes` = `t_correct - t_first_done`
- `secs_idiomatic_delta` = `t_idiomatic - t_correct` (0 if no refactor)
- `secs_total` = `t_idiomatic - t_start`

---

## Step 4: End-of-Session Debrief

After all exercises:

1. Print the results table
2. Write all rows to `screen_metrics.csv` (create with header if missing)

### Results table

| # | Category | Time | Bug fixes | Idiomatic | Total | Hints | Lines |
|---|---|---|---|---|---|---|---|

Close with one specific category to prioritize based on today's results.

---

## screen_metrics.csv

Path: `/Users/eric/projects/learn-python/screen_metrics.csv`
Columns: `date,category,secs_to_first_done,secs_bug_fixes,secs_idiomatic_delta,secs_total,hints_used,lines_written`

- `secs_to_first_done`: start → first done call (target: < 300 — want down)
- `secs_bug_fixes`: first done → logically correct (target: 0)
- `secs_idiomatic_delta`: logically correct → idiomatic (target: 0)
- `secs_total`: sum of all three phases
- `hints_used`: integer count
- `lines_written`: non-blank, non-comment lines at point of logical correctness
