---
title: AnnouncementPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/announcementpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/announcementpaginationconnection/index.md
---

The connection type for Announcement.

## Fields

[`edges` ](#field-edges)· [`[AnnouncementEdge]` ](/reference/2026-01-01/objects/announcementedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Announcement]` ](/reference/2026-01-01/objects/announcement)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.announcements`](/reference/2026-01-01/queries/announcements)

## Definition

```
"""
The connection type for Announcement.
"""
type AnnouncementPaginationConnection {
  """
  A list of edges.
  """
  edges: [AnnouncementEdge]


  """
  A list of nodes.
  """
  nodes: [Announcement]


  """
  Information to aid in pagination.
  """
  page_info: PageInfo!


  """
  Total count of items.
  """
  total_count: Int!
}
```
