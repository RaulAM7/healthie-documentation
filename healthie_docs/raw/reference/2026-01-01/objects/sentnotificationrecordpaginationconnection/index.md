---
title: SentNotificationRecordPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/sentnotificationrecordpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/sentnotificationrecordpaginationconnection/index.md
---

The connection type for SentNotificationRecord.

## Fields

[`edges` ](#field-edges)· [`[SentNotificationRecordEdge]` ](/reference/2026-01-01/objects/sentnotificationrecordedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[SentNotificationRecord]` ](/reference/2026-01-01/objects/sentnotificationrecord)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.sentNotificationRecords`](/reference/2026-01-01/queries/sentnotificationrecords)

## Definition

```
"""
The connection type for SentNotificationRecord.
"""
type SentNotificationRecordPaginationConnection {
  """
  A list of edges.
  """
  edges: [SentNotificationRecordEdge]


  """
  A list of nodes.
  """
  nodes: [SentNotificationRecord]


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
