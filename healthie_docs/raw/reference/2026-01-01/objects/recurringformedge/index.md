---
title: RecurringFormEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/recurringformedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/recurringformedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`RecurringForm` ](/reference/2026-01-01/objects/recurringform)· The item at the end of the edge.

## Used By

[`RecurringFormPaginationConnection.edges`](/reference/2026-01-01/objects/recurringformpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type RecurringFormEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: RecurringForm
}
```
