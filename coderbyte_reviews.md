# CoderByte Reviews

---

## 2026-09-16 — Session 1

Two independent problems, medium. Combined first-submit accuracy: **5 / 14 hidden
tests (36%)** — the headline number, and the one that matters for a real take-home
where you can't iterate freely. Both problems reached 7/7 after debugging, so the
gap is not "can you solve it" but "can you get it right blind, first try."

### log-error-summary — extract/count-sum

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_submit | 2470s | ≤ 1200s | ❌ |
| hidden_tests_passed_first | 5/7 | 7/7 | ❌ |
| secs_debug | 706s | 0 | ❌ |
| hidden_tests_passed_final | 7/7 | 7/7 | ✅ |
| hints_used | 8 | 0 | ❌ |
| lines_written | 20 | — | |

**Analysis:** Core logic was strong on first submit — correct level-field check (did
not fall for "ERROR" appearing inside a message), correct zero-padding, and a working
ascending tie-order. Two hidden cases failed, both the same root cause: an unguarded
`elements[2]` crashed on **empty input** and on **blank lines** (`"".split(' ',3)`
returns a 1-element list). The first debug attempt over-corrected with
`len(elements) == 3`, which then dropped *every* real ERROR line (a line with a message
splits into 4 parts), regressing to 2/7 — a reminder to trace your own guard against a
real input before trusting it. The 8 hints (split maxsplit, heapq ×3, Counter usage,
`.items()` vs `.values()`, tuple sorting) show the algorithm was there but stdlib
recall was not.

**Pattern to internalize:** Test empty string and blank lines before submitting — they
are the #1 CoderByte trap. And when adding a guard, run one valid input through it
mentally: `== 3` vs `>= 3` is the exact class of off-by-one that flips a pass to a zero.

**Cross-session trend:** First session — no trend yet. Baseline: count-sum first-submit
5/7, heavily hint-assisted.

### paginate-report — delimited/merge-reshape

| Metric | Value | Target | |
|---|---|---|---|
| secs_to_first_submit | 527s | ≤ 900s | ✅ |
| hidden_tests_passed_first | 0/7 | 7/7 | ❌ |
| secs_debug | 364s | 0 | ❌ |
| hidden_tests_passed_final | 7/7 | 7/7 | ✅ |
| hints_used | 0 | 0 | ✅ |
| lines_written | 18 | — | |

**Analysis:** Fast and unassisted to first submit, but scored 0/7 — the classic
exact-output gut-punch. The chunking logic was essentially correct; three formatting
defects sank every case: (1) a **trailing newline** on every output (append-`\n`-as-you-go
without trimming) failed all 7 on its own; (2) the `Page N:` header was emitted before
checking any record existed, so **empty input** produced `"Page 1:\n"` instead of `""`;
(3) header emission was coupled to `count == 0`, so a **blank line** arriving after a
full page fired a spurious empty header and shifted records to the wrong page. All three
fixed cleanly on the next attempt by emitting the leading separator only when
`page > 1` and skipping blank lines before any structure is written.

**Pattern to internalize:** For "format to exact output" problems, separate *extract the
real records* from *format them* — build with `\n` as a separator (or join at the end)
so no trailing newline exists to trim, and never emit structure while walking raw lines
you might skip. Diff your output against the sample byte-for-byte, including the last
character.

**Cross-session trend:** First session — no trend yet. Baseline: merge-reshape
first-submit 0/7 (all format/edge, logic sound).
