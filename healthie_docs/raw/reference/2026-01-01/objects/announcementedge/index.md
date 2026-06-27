---
title: AnnouncementEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/announcementedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/announcementedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Announcement` ](/reference/2026-01-01/objects/announcement)· The item at the end of the edge.

## Used By

[`AnnouncementPaginationConnection.edges`](/reference/2026-01-01/objects/announcementpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type AnnouncementEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Announcement
}
```
