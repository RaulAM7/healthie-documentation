---
title: ChangeClaimSubmitter | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/changeclaimsubmitter/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/changeclaimsubmitter/index.md
---

Info on connection to Change Health

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the connection

[`is_enabled` ](#field-is-enabled)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if the Change connection is turned by user

## Used By

[`Query.changeClaimSubmitter`](/reference/2026-01-01/queries/changeclaimsubmitter)

## Definition

```
"""
Info on connection to Change Health
"""
type ChangeClaimSubmitter {
  """
  The unique identifier of the connection
  """
  id: ID!


  """
  True if the Change connection is turned by user
  """
  is_enabled: Boolean
}
```
