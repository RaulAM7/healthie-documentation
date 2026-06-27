---
title: FormHistoryPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/formhistorypaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/formhistorypaginationconnection/index.md
---

The connection type for FormHistory.

## Fields

[`edges` ](#field-edges)· [`[FormHistoryEdge]` ](/reference/2026-01-01/objects/formhistoryedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[FormHistory]` ](/reference/2026-01-01/objects/formhistory)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.formHistories`](/reference/2026-01-01/queries/formhistories)

## Definition

```
"""
The connection type for FormHistory.
"""
type FormHistoryPaginationConnection {
  """
  A list of edges.
  """
  edges: [FormHistoryEdge]


  """
  A list of nodes.
  """
  nodes: [FormHistory]


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
