# AI Boilerplate Assist — Candidate Guide

## What AI Is Allowed For

- Syntax lookup ("what's the psycopg2 syntax for a parameterized query?")
- Boilerplate generation (app skeleton, route stubs, DB connection setup)
- Debugging errors ("why is this throwing a KeyError?")
- Documentation reference ("what does Flask's `abort()` do?")

## What AI Is NOT Allowed For

- Architecture decisions ("how should I structure this?")
- Data model design ("what tables do I need?")
- Problem-solving ("how do I handle concurrent updates?")
- Anything where the answer requires understanding the problem

The rule: **if the answer would be the same regardless of what problem you're solving, it's safe to ask. If it requires understanding the problem, it's not.**

## Context Prompt

Paste this into your AI tool at the start of the session:

> I'm in a coding interview. Help me with boilerplate and syntax only — do not suggest architecture, data models, or how to solve the problem. If I ask something that crosses into problem-solving, tell me instead of answering.

## Safe vs. Unsafe Examples

| Safe | Unsafe |
|------|--------|
| "Give me a Flask app skeleton with empty route stubs" | "How should I structure my routes?" |
| "What's the SQL syntax for UPDATE with a subquery?" | "How do I keep two tables in sync?" |
| "Show me how psycopg2 runs a transaction" | "How do I handle concurrent writes?" |
| "What does `ON CONFLICT DO NOTHING` do?" | "What constraints should I add to this table?" |
