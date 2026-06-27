---
title: AuditEventEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/auditeventedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/auditeventedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`AuditEvent` ](/reference/2026-01-01/objects/auditevent)· The item at the end of the edge.

## Used By

[`AuditEventPaginationConnection.edges`](/reference/2026-01-01/objects/auditeventpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type AuditEventEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: AuditEvent
}
```
