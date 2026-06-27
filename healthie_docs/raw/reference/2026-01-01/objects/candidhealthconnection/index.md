---
title: CandidHealthConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/candidhealthconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/candidhealthconnection/index.md
---

Info on connection to Candid Health

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the connection

[`is_enabled` ](#field-is-enabled)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · True if the Candid connection is turned by user

## Used By

[`Query.candidHealthConnection`](/reference/2026-01-01/queries/candidhealthconnection)

## Definition

```
"""
Info on connection to Candid Health
"""
type CandidHealthConnection {
  """
  The unique identifier of the connection
  """
  id: ID!


  """
  True if the Candid connection is turned by user
  """
  is_enabled: Boolean!
}
```
