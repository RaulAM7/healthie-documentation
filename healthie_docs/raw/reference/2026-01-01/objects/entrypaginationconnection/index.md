---
title: EntryPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/entrypaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/entrypaginationconnection/index.md
---

The connection type for Entry.

## Fields

[`edges` ](#field-edges)· [`[EntryEdge]` ](/reference/2026-01-01/objects/entryedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Entry]` ](/reference/2026-01-01/objects/entry)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.entries`](/reference/2026-01-01/queries/entries)

## Definition

```
"""
The connection type for Entry.
"""
type EntryPaginationConnection {
  """
  A list of edges.
  """
  edges: [EntryEdge]


  """
  A list of nodes.
  """
  nodes: [Entry]


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
