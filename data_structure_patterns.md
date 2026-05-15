# Data Structure Patterns for Interview Problems

Quick reference for common Req 3 patterns that require sophisticated data structures. Each pattern includes a simple, interview-friendly Python implementation.

---

## 1. Top K by Metric (Heap)

**Problem:** "Get the top 10 projects by error count" where data streams in continuously.

**Approach:** Use Python's `heapq` module. The trick is that `heapq` is a min-heap, so to get top K largest items, you maintain a min-heap of size K. When a new item comes in, compare it to the smallest item in the heap — if it's larger, pop the smallest and push the new one.

**Implementation:** Store projects normally with their counts. When you need top K, build a heap from all projects. For streaming, you can maintain a separate heap that you update on each event.

```python
import heapq

# One-time query approach
def get_top_k(projects, k):
    # heapq.nlargest handles it for you
    return heapq.nlargest(k, projects.values(), key=lambda p: p.error_count)
```

For streaming where you call this frequently, maintain the heap as state and update it on each event with `heappushpop`. The key insight: min-heap of size K gives you top K largest because you're always evicting the smallest of your candidates.

---

## 2. Time-Windowed Counting (Bucketed Storage)

**Problem:** "Alert if an issue gets 100 errors in the last hour."

**Approach:** Divide time into fixed buckets (e.g., one per minute). Store a dict mapping `minute_number -> count`. When an event arrives, increment the current minute's bucket. To query, sum the last 60 buckets.

**Implementation:**

```python
class Issue:
    def __init__(self):
        self.minute_buckets = {}  # minute -> count

    def add_event(self, timestamp):
        minute = int(timestamp) // 60
        self.minute_buckets[minute] = self.minute_buckets.get(minute, 0) + 1

    def count_last_hour(self, now):
        current_minute = int(now) // 60
        return sum(
            self.minute_buckets.get(m, 0)
            for m in range(current_minute - 59, current_minute + 1)
        )
```

Periodically clean old buckets to prevent memory growth. This gives O(1) updates and O(60)=O(1) queries with minute-level granularity — good enough for most alerting use cases.

---

## 3. Rate Limiting (Token Bucket)

**Problem:** "Max 5 alerts per project per hour."

**Approach:** Track when alerts were sent using a list of timestamps. Before sending an alert, check how many were sent in the last hour. If under the limit, allow it and record the timestamp.

**Implementation:**

```python
from collections import deque

class RateLimiter:
    def __init__(self, max_count, window_seconds):
        self.max_count = max_count
        self.window = window_seconds
        self.timestamps = deque()

    def allow(self, now):
        # Remove old timestamps
        cutoff = now - self.window
        while self.timestamps and self.timestamps[0] <= cutoff:
            self.timestamps.popleft()

        # Check limit
        if len(self.timestamps) < self.max_count:
            self.timestamps.append(now)
            return True
        return False
```

Each project gets its own `RateLimiter` instance. The deque stays bounded to `max_count` since old entries expire. Simple to reason about in an interview — just a sliding window of "when did I last do this action?"

---

## 4. Priority Ordering (Priority Queue)

**Problem:** "Process high-severity issues first."

**Approach:** Use a heap where priority determines order. In Python, `heapq` pops the smallest value first, so use negative priority or a tuple `(priority, item)` where lower numbers = higher priority.

**Implementation:**

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0  # tiebreaker for same priority

    def push(self, item, priority):
        # Lower priority number = processed first
        # Counter ensures FIFO for same priority
        heapq.heappush(self.heap, (priority, self.counter, item))
        self.counter += 1

    def pop(self):
        if self.heap:
            priority, _, item = heapq.heappop(self.heap)
            return item
        return None
```

Map severity to priority: `{"critical": 1, "high": 2, "medium": 3, "low": 4}`. The counter acts as a tiebreaker so items with the same priority come out in FIFO order. Push issues as they arrive, pop to process in priority order.

---

## 5. Recent N Items (Bounded Deque)

**Problem:** "Show the last 50 events for an issue."

**Approach:** Use `collections.deque` with a `maxlen` parameter. It automatically evicts the oldest item when you append past the limit. No manual cleanup needed.

**Implementation:**

```python
from collections import deque

class Issue:
    def __init__(self):
        self.recent_events = deque(maxlen=50)
        self.total_count = 0

    def add_event(self, event):
        self.recent_events.append(event)
        self.total_count += 1

    def get_recent(self):
        return list(self.recent_events)
```

This is the simplest pattern — Python's deque handles everything. You get O(1) append, automatic eviction, and O(N) retrieval where N is bounded at 50. Keep a separate `total_count` if you need the all-time count since the deque only holds recent items.

---

## 6. Range Queries (Sorted List + Binary Search)

**Problem:** "Find all issues with error counts between 50 and 100."

**Approach:** Maintain a sorted list of `(count, issue_id)` tuples. Use `bisect` module to find the start and end positions of your range in O(log N), then slice.

**Implementation:**

```python
import bisect

class IssueIndex:
    def __init__(self):
        self.sorted_by_count = []  # [(count, issue_id), ...]

    def update(self, issue_id, old_count, new_count):
        # Remove old entry
        if old_count is not None:
            self.sorted_by_count.remove((old_count, issue_id))
        # Insert new entry in sorted position
        bisect.insort(self.sorted_by_count, (new_count, issue_id))

    def query_range(self, min_count, max_count):
        left = bisect.bisect_left(self.sorted_by_count, (min_count,))
        right = bisect.bisect_right(self.sorted_by_count, (max_count + 1,))
        return [issue_id for count, issue_id in self.sorted_by_count[left:right]]
```

The tradeoff: O(N) updates (remove is linear) but O(log N + K) queries where K is result size. For interview, mention that a more sophisticated structure (like a balanced BST) would give O(log N) updates too.

---

## 7. Expiration / TTL (Heap by Timestamp)

**Problem:** "Auto-resolve issues with no events for 24 hours."

**Approach:** Maintain a min-heap ordered by `last_event_time`. The issue that's been quiet longest is at the top. Periodically pop and resolve any issues whose last event is older than 24 hours.

**Implementation:**

```python
import heapq

class ExpirationTracker:
    def __init__(self, ttl_seconds):
        self.ttl = ttl_seconds
        self.heap = []  # (last_event_time, issue_id)
        self.last_event = {}  # issue_id -> last_event_time

    def touch(self, issue_id, timestamp):
        # Record latest timestamp (heap may have stale entries)
        self.last_event[issue_id] = timestamp
        heapq.heappush(self.heap, (timestamp, issue_id))

    def get_expired(self, now):
        expired = []
        cutoff = now - self.ttl
        while self.heap and self.heap[0][0] <= cutoff:
            ts, issue_id = heapq.heappop(self.heap)
            # Check if this is still the latest (not stale)
            if self.last_event.get(issue_id) == ts:
                expired.append(issue_id)
                del self.last_event[issue_id]
        return expired
```

The trick is handling updates — when an issue gets a new event, you push a new entry but don't remove the old one. On expiration check, verify the timestamp matches the current `last_event` to filter stale entries.

---

## 8. Aggregation Across Dimensions (Multiple Indexes)

**Problem:** "Get error counts grouped by team AND severity."

**Approach:** Maintain multiple dictionaries that index the same data differently. Update all indexes when data changes. Trade memory for query speed.

**Implementation:**

```python
class AggregationIndex:
    def __init__(self):
        self.by_team = {}           # team -> count
        self.by_severity = {}       # severity -> count
        self.by_team_severity = {}  # (team, severity) -> count

    def record_event(self, team, severity):
        # Update all indexes
        self.by_team[team] = self.by_team.get(team, 0) + 1
        self.by_severity[severity] = self.by_severity.get(severity, 0) + 1

        key = (team, severity)
        self.by_team_severity[key] = self.by_team_severity.get(key, 0) + 1

    def get_by_team(self, team):
        return self.by_team.get(team, 0)

    def get_by_team_and_severity(self, team, severity):
        return self.by_team_severity.get((team, severity), 0)
```

Each index is O(1) lookup. The tradeoff is memory (storing redundant data) and write complexity (must update all indexes consistently). In interview, mention this is a classic "write-time indexing vs query-time computation" tradeoff.

---

## Quick Reference: When to Use What

| Need | Data Structure | Time Complexity |
|------|---------------|-----------------|
| Top K of N items | Heap | O(N log K) build, O(log K) update |
| Count in time window | Bucketed dict | O(1) update, O(bucket count) query |
| Rate limiting | Deque of timestamps | O(1) amortized |
| Process by priority | Heap with priority tuple | O(log N) push/pop |
| Last N items | Bounded deque | O(1) append, O(N) retrieve |
| Range queries | Sorted list + bisect | O(N) update, O(log N + K) query |
| TTL / expiration | Heap by timestamp | O(log N) touch, O(K log N) expire K items |
| Multi-dimension aggregation | Multiple dicts | O(index count) update, O(1) query |
