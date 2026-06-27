---
title: FormAnswerGroupEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/formanswergroupedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/formanswergroupedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`FormAnswerGroup` ](/reference/2026-01-01/objects/formanswergroup)· The item at the end of the edge.

## Used By

[`FormAnswerGroupPaginationConnection.edges`](/reference/2026-01-01/objects/formanswergrouppaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type FormAnswerGroupEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: FormAnswerGroup
}
```
