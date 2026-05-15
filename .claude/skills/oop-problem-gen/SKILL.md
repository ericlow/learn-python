---
name: oop-problem-gen
description: >
  Generate an OOP system design interview problem with coaching guide.
  Use when the user wants to practice object-oriented design, low-level
  system design, or class-based coding problems. Triggers on "OOP problem",
  "system design practice", "generate a design problem", or "let's do an
  OOP session". After generating, the interview-coach skill governs the session.
---

# Low-Level System Design Interview Problem Generator

## What This File Is
This file is invoked once per session to generate a problem and coaching guide for that session. It defines how to design requirements, validate difficulty, and structure the coaching guide output.

## What This File Is NOT
- Not a coaching guide — it does not run sessions or coach the candidate
- Not a source of coaching behavior rules — those live in CLAUDE.md and the interview-coach skill
- Not always-on — it is only used when creating a new problem at the start of a session
- Not for algorithmic problems — those use the algo-problem-gen skill
- Not a place for session mechanics (pause/resume, pacing, hint disclosure, rubric scoring protocol) — those live in the interview-coach skill

---

You are an interview problem designer creating coding exercises for Senior Engineering Manager candidates. Your goal is to generate a complete problem and coaching guide for the current session.

---

## Step 1: Gather Domain Context

Ask the user only:

1. **What domain is this for?** (e.g., Sentry/monitoring, banking, logistics, e-commerce)
2. **Any specific twists to include?**
   - JSON input handling
   - Date/time handling
   - Neither

**You (the LLM) must determine:**
- Core entities based on domain knowledge
- A real-world operation involving state management over time
- Appropriate constraints and optimizations that fit the domain

---

## Step 2: Generate the Problem

### Problem Structure Requirements

**Opening Prompt (2-3 sentences only):**
- Vague and open-ended
- Forces candidate to ask clarifying questions
- Does NOT reveal the layered requirements upfront

**Example opening format:**
> "We're going to design a [System] for [Domain]. We need to manage [core entities] as they [operation] throughout the day."

**Hidden Requirements (revealed through discussion):**

| Requirement | Reveal When | Core Principle |
|-------------|-------------|----------------|
| Req 1 | Candidate asks "what operations?" | Establish foundation |
| Req 2 | After Req 1 works | Force meaningful adaptation of foundation |
| Req 3 | After Req 2 works | Force further adaptation; may reveal earlier design choices as limiting |

**Each requirement must:**
- Build on the previous requirement
- Force adaptation of existing code (not just addition)
- Introduce at least one decision point

**Adaptation, not addition:** The key is that Req 2 shouldn't just add something new—it should force changes to what was built in Req 1. Req 3 should compound this further.

**Progressive data structure complexity:** Requirements should escalate the sophistication of data structures needed:
- **Req 1:** Basic types (dicts, lists, simple classes) — establish the foundation
- **Req 2:** Adds indexing, lookup challenges, or new relationships — forces structural adaptation
- **Req 3:** Requires a more sophisticated structure — rewards algorithmic thinking

**Req 3 patterns that force sophisticated structures:**

| Pattern | Data Structure | Example Requirement |
|---------|---------------|---------------------|
| Top K by metric | Heap | "Get top 10 projects by error count" |
| Time-windowed counting | Bucketed storage / sliding window | "Alert if 100 errors in the last hour" |
| Rate limiting | Token bucket / sliding window | "Max 5 alerts per project per hour" |
| Priority ordering | Priority queue | "Process high-severity issues first" |
| Recent N items | Bounded deque | "Show last 50 events for an issue" |
| Range queries | Sorted structure + binary search | "Find all issues with 50-100 errors" |
| Expiration / TTL | Heap by timestamp | "Auto-resolve issues with no events for 24h" |
| Aggregation across dimensions | Multiple indexes | "Get error counts grouped by team AND severity" |

Vary these across problems — don't always use the same pattern.

**Complexity comes from:**
- Multiple entities with relationships AND behavior (not just IDs)
- Business logic with rules to reason about (compatibility, priorities, conditions)
- Requirements that compound and force earlier decisions to be revisited

**Examples of good vs weak design:**

| Aspect | Weak (Too Easy) | Strong (Challenging) |
|--------|-----------------|----------------------|
| Entities | `project_id` string in a dict | `Project` class with `team`, `error_count`, methods |
| Business logic | `count > threshold` | Size compatibility: small→any, medium→med/large, large→large only |
| Req 2 adaptation | "Add team-level query" (just loop existing data) | "Query by dimension you didn't index" (forces restructure) |
| Algorithm need | Any structure works | Heap required for efficient top-N |
| Relationships | Simple containment (garage has list of spots) | Car ↔ Spot linkage: who owns the reference? Bidirectional or not? |
| State storage | State obviously lives on one entity | "Is spot available?" — flag on spot vs inferred vs central set? |

**Possible twists (vary these across problems):**
- Introducing a new entity that interacts with existing ones
- Changing how state is managed
- Adding validation that ripples through existing code
- Reversing a lookup direction (e.g., "find X by Y" when you only indexed by X)
- Adding a constraint that invalidates a naive approach
- Code reuse opportunity between Req 2 and Req 3
- Time/space tradeoff that becomes apparent in Req 3

Do NOT always use the same twist. Vary the challenges to create different problem shapes.

---

## Step 2a: Validate Problem Difficulty

Before finalizing the problem, apply these tests:

### The Adaptation Test
**Ask:** "If I implement Req 1 the obvious/naive way, will Req 2 force me to change my data structures or approach?"

- ❌ If Req 2 just adds new methods that work with existing structure → too easy
- ✅ If Req 2 requires restructuring, adding indexes, or rethinking storage → good

### The Entity Richness Test
**Ask:** "Do entities have behavior, or are they just IDs in dictionaries?"

- ❌ Entities are just string IDs tracked in dicts/sets → too thin
- ✅ Entities are objects with methods that encapsulate business logic → good

### The Business Logic Test
**Ask:** "Are there non-trivial rules the candidate must reason about?"

- ❌ Simple comparisons like `count > threshold` → too easy
- ✅ Compatibility matrices, priority rules, conditional state transitions → good

### The Algorithm Choice Test
**Ask:** "Is there at least one requirement where data structure choice meaningfully affects performance or complexity?"

- ❌ Any reasonable structure works equally well → too easy
- ✅ Choosing heap vs sort, maintaining indexes vs iterating → good

### The Relationship Modeling Test
**Ask:** "Do entities have non-trivial relationships that the candidate must deliberately model?"

- ❌ Entities are independent or have obvious parent-child containment → too easy
- ✅ Candidate must decide: Does A reference B, does B reference A, or does a third entity manage the relationship? → good

Examples of challenging relationships:
- Many-to-many relationships (which side owns it?)
- Relationships that could be modeled as containment OR reference
- Implicit relationships that need to be made explicit (e.g., a Ticket linking Car ↔ Spot)
- Bidirectional vs unidirectional references (with consistency tradeoffs)

### The State Storage Test
**Ask:** "Is there at least one piece of state where the candidate must decide WHERE it lives?"

- ❌ State obviously belongs on one entity → too easy
- ✅ Candidate must choose between storing state on Entity A, Entity B, or a central manager — with real tradeoffs → good

Examples of state storage decisions:
| State to Track | Option A | Option B | Option C |
|----------------|----------|----------|----------|
| Which car is in which spot | `car.spot_id` | `spot.car` | `garage.car_to_spot` dict |
| Is spot available | `spot.reserved` flag | Infer from `spot.car is None` | `garage.available_spots` set |
| Error count per project | `project.error_count` | `event` list, count at query | `manager.project_counts` dict |

The tradeoffs to discuss: consistency risk, query efficiency, update complexity, single source of truth.

**If any test fails, redesign the requirements before proceeding.**

---

## Step 2b: Define Corner Cases

Every problem MUST include corner cases that test the candidate's thoroughness. Design at least 4-6 corner cases across the requirements.

**Corner Case Categories:**

| Category | Examples |
|----------|----------|
| Empty/null inputs | Null entity, empty collection, missing fields |
| Boundary conditions | First item, last item, exactly at limit |
| Duplicate operations | Same action twice, already exists |
| State conflicts | Operating on invalid state, concurrent-like issues |
| Capacity limits | Full, overflow, zero capacity |
| Not found | Lookup for non-existent item |

**Corner Case Documentation Format:**

### Corner Case: [Name]

**Requirement:** [Which requirement this applies to]
**Scenario:** [What the candidate might miss]
**Expected behavior:** [What should happen]
**Common mistake:** [What candidates typically do wrong]

**Test case:**
[Code snippet showing the corner case]

**Hints if missed:** Use progressive hint disclosure per the interview-coach skill.

**The problem should be designed so that:**
- At least 2 corner cases are likely to be missed on first implementation
- Corner cases reveal themselves through testing or coach prompts
- Handling corner cases requires thoughtful code changes, not just adding if-statements

---

## Step 3: Define Decision Points

For each major decision in the problem, document:

### Decision Point: [Name]

**Context:** [When this decision arises]

**Options:**
1. [Option A]
   - Pros: ...
   - Cons: ...
   - Time complexity: O(?)

2. [Option B]
   - Pros: ...
   - Cons: ...
   - Time complexity: O(?)

3. [Option C] (if applicable)
   - Pros: ...
   - Cons: ...
   - Time complexity: O(?)

**Preferred Solution:** [Which option and why]

**What it tests:** [The skill being evaluated]

**Data structures in scope:** Arrays, Queues, Heaps, Maps/Dicts
**Data structures out of scope:** Graphs, Tries

---

## Step 4: Generate the Coaching Guide

Create a complete coaching guide with the following sections. Coaching methodology, emoji formatting, time tracking, and hint disclosure are defined in the interview-coach skill — do not repeat them here.

### 4.6 Issue Reference

For each potential bug or missing implementation, document. Use progressive hint disclosure per the interview-coach skill.

### Issue: [Name]

**Lines:** [X-Y]
**Severity:** Critical / Important / Minor
**Type:** Syntax / Logic / Corner Case / Design

**Hint 1:** [Vague]
**Hint 2:** [More specific]
**Hint 3:** [Very specific]
**Answer:** [Complete solution]

**Corner cases must be included in the issue reference.** For each corner case from Step 2b, create an issue entry here.

### 4.7 Iterative Reveal Script

Document how to reveal requirements based on candidate progress:

#### Opening
> "[1-2 sentence opening prompt]"

Wait for candidate questions. Expected questions:
- "What operations do we need to support?"
- "What does [entity] look like?"
- "How many [entities] are we dealing with?"

#### After Candidate Asks About Operations
Reveal Requirement 1:
> "[Description of basic CRUD operations]"

#### Edge Case Probes (Per Requirement)

Document 3-5 probe questions the coach can use if the candidate's edge case list is incomplete. These are problem-specific — do not repeat generic coaching rules here.

Examples:
- "What if the entity doesn't exist?"
- "What if capacity is already full?"
- "What if the same operation is called twice?"
- "What if the input has zero or negative values?"

#### After Requirement 1 Is Working
Reveal Requirement 2:
> "[Description of constraint to add]"

#### After Requirement 2 Is Working
Reveal Requirement 3:
> "[Description of optimization requirement]"

---

## Step 5: Generate Starter Driver Code

For each requirement, generate driver code to hand to the candidate when they finish that requirement. Format as plain `print(...)` or `assert` statements with inline comments showing expected output. Cover: happy path, edge cases, and corner cases from Step 2b that apply to that requirement.

**Example format:**
```python
# --- Driver: Req 1 ---
system = MySystem()
system.add(...)
print(system.get(...))   # expected output
print(system.get(...))   # None — not found
```

Do NOT reveal which cases will fail. The candidate runs the driver and discovers failures themselves.

---

## Step 6: Generate Reference Implementation

**Starter Code:** Blank file only. No pre-existing classes, methods, or implementations. Candidate discovers everything through requirements gathering.

Provide one working reference implementation at **Target level** only:
- All requirements implemented
- Clean code structure with helper methods extracted
- No duplication
- Handles core corner cases
- Complete, runnable Python code with test cases

Do NOT generate minimum or stretch implementations. Instead, document what distinguishes each level in the rubric (Step 8).

---

## Step 6: Common Pitfalls

List domain-specific pitfalls:

1. **[Pitfall]** - [Why it happens] - [How to avoid]
2. **[Pitfall]** - [Why it happens] - [How to avoid]

---

## Step 7: Extension Questions

Provide 4-6 follow-up questions interviewers might ask:

1. **"How would you handle [extension]?"**
   - Key considerations: ...
   - Possible approaches: ...

2. **"What's the time complexity of [operation]?"**
   - Answer: O(?)
   - Explanation: ...

---

## Step 8: Generate Rubric

Create a scoring rubric for this specific problem. Each dimension is scored 1-3:
- **1 = No Hire** — below expectations
- **2 = Hire** — meets expectations
- **3 = Strong Hire** — exceeds expectations

Total score out of 15. Record in `session_metrics.csv` as `rubric_score`.

## Rubric

| Dimension | 1 — No Hire | 2 — Hire | 3 — Strong Hire |
|-----------|-------------|----------|-----------------|
| **Correctness** | [problem-specific criteria] | [problem-specific criteria] | [problem-specific criteria] |
| **Code Quality** | [problem-specific criteria] | [problem-specific criteria] | [problem-specific criteria] |
| **Data Structures** | [problem-specific criteria] | [problem-specific criteria] | [problem-specific criteria] |
| **Communication** | Silent, jumps to code, no clarifying questions | Asks clarifying questions, explains approach before coding | Proactively identifies ambiguity, articulates tradeoffs, flags complexity |
| **Speed** | Doesn't finish Req 2 in 60 min | Finishes all 3 reqs in 60 min | Finishes with time for corner cases and discussion |

**Correctness, Code Quality, and Data Structures criteria must be problem-specific.**
Communication and Speed criteria are standard across all problems.

---

## Output Format

Save as **4 files** in `problems/`:

- **`problems/[name]_overview.md`** (~100 lines) — problem description, core entities and relationships, all 3 reqs at a glance (1–2 lines each), how reqs build on each other, pre-loaded data, opening prompt, rubric
- **`problems/[name]_req1.md`** (~200 lines) — Req 1 requirement (full method signatures, pre-loaded data), reveal script + edge case probes for Req 1, corner cases for Req 1, decision points for Req 1, issue reference with progressive hints for Req 1, reference implementation for Req 1 classes/methods, Req 1 driver code, phase evaluation guide
- **`problems/[name]_req2.md`** (~200 lines) — same structure for Req 2
- **`problems/[name]_req3.md`** (~200 lines) — same structure for Req 3, plus extension questions and common pitfalls for all reqs

**Skeleton progression rule:**
- The initial `.py` file (created by the coach at session start) contains only Req 1 classes and method signatures
- Each `req2.md` and `req3.md` must include a `## Skeleton Addition` section near the top with the exact Python snippet the coach will Edit into the `.py` file at phase transition — signatures and `pass` only, no implementation
- New classes, helper stubs (rare), or new method signatures (common) belong in this section

The `_session_notes.md` file is created at runtime by the coach — do not generate it upfront.

After saving all 4 files, confirm they were saved and hand off to the interview-coach skill for session execution.

---

## Example Domain Applications

| Domain | Core Entity | Operation | Possible Twist |
|--------|-------------|-----------|----------------|
| Sentry | Error events | Grouping/routing alerts | JSON event parsing |
| Banking | Transactions | Processing/fraud detection | Date handling |
| Logistics | Shipments | Routing/tracking | Time windows |
| E-commerce | Orders | Inventory/fulfillment | JSON cart data |
| Parking | Vehicles/Spots | Parking/retrieval | Distance optimization |
