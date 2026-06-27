---
title: NotificationPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/notificationpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/notificationpaginationconnection/index.md
---

The connection type for Notification.

## Fields

[`edges` ](#field-edges)· [`[NotificationEdge]` ](/reference/2026-01-01/objects/notificationedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Notification]` ](/reference/2026-01-01/objects/notification)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.notifications`](/reference/2026-01-01/queries/notifications)

## Definition

```
"""
The connection type for Notification.
"""
type NotificationPaginationConnection {
  """
  A list of edges.
  """
  edges: [NotificationEdge]


  """
  A list of nodes.
  """
  nodes: [Notification]


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
