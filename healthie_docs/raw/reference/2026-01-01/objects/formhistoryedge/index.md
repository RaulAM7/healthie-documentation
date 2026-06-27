---
title: FormHistoryEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/formhistoryedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/formhistoryedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`FormHistory` ](/reference/2026-01-01/objects/formhistory)· The item at the end of the edge.

## Used By

[`FormHistoryPaginationConnection.edges`](/reference/2026-01-01/objects/formhistorypaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type FormHistoryEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: FormHistory
}
```
