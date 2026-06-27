---
title: Problem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/problem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/problem/index.md
---

Base class for types

## Fields

[`code` ](#field-code)· [`String` ](/reference/2026-01-01/scalars/string)· Code of the problem

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · Self-descriptive

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· Name of the problem

[`requires_consolidation` ](#field-requires-consolidation)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, this object must be consolidated as part of a CCDA Ingest

## Used By

[`User.problems`](/reference/2026-01-01/objects/user)

## Definition

```
"""
Base class for types
"""
type Problem {
  """
  Code of the problem
  """
  code: String


  """
  Self-descriptive
  """
  id: ID!


  """
  Name of the problem
  """
  name: String


  """
  When true, this object must be consolidated as part of a CCDA Ingest
  """
  requires_consolidation: Boolean
}
```
