---
title: AppliedTagPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appliedtagpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appliedtagpaginationconnection/index.md
---

The connection type for AppliedTag.

## Fields

[`edges` ](#field-edges)· [`[AppliedTagEdge]` ](/reference/2026-01-01/objects/appliedtagedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[AppliedTag]` ](/reference/2026-01-01/objects/appliedtag)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.appliedTags`](/reference/2026-01-01/queries/appliedtags)

## Definition

```
"""
The connection type for AppliedTag.
"""
type AppliedTagPaginationConnection {
  """
  A list of edges.
  """
  edges: [AppliedTagEdge]


  """
  A list of nodes.
  """
  nodes: [AppliedTag]


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
