---
title: RecurringFormPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/recurringformpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/recurringformpaginationconnection/index.md
---

The connection type for RecurringForm.

## Fields

[`edges` ](#field-edges)· [`[RecurringFormEdge]` ](/reference/2026-01-01/objects/recurringformedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[RecurringForm]` ](/reference/2026-01-01/objects/recurringform)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.recurringForms`](/reference/2026-01-01/queries/recurringforms)

## Definition

```
"""
The connection type for RecurringForm.
"""
type RecurringFormPaginationConnection {
  """
  A list of edges.
  """
  edges: [RecurringFormEdge]


  """
  A list of nodes.
  """
  nodes: [RecurringForm]


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
