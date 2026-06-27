---
title: NotificationEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/notificationedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/notificationedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Notification` ](/reference/2026-01-01/objects/notification)· The item at the end of the edge.

## Used By

[`NotificationPaginationConnection.edges`](/reference/2026-01-01/objects/notificationpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type NotificationEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Notification
}
```
