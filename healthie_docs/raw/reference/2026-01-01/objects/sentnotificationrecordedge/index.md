---
title: SentNotificationRecordEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/sentnotificationrecordedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/sentnotificationrecordedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`SentNotificationRecord` ](/reference/2026-01-01/objects/sentnotificationrecord)· The item at the end of the edge.

## Used By

[`SentNotificationRecordPaginationConnection.edges`](/reference/2026-01-01/objects/sentnotificationrecordpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type SentNotificationRecordEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: SentNotificationRecord
}
```
