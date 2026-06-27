---
title: NotePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/notepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/notepaginationconnection/index.md
---

The connection type for Note.

## Fields

[`edges` ](#field-edges)· [`[NoteEdge]` ](/reference/2026-01-01/objects/noteedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Note]` ](/reference/2026-01-01/objects/note)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.notes`](/reference/2026-01-01/queries/notes)

## Definition

```
"""
The connection type for Note.
"""
type NotePaginationConnection {
  """
  A list of edges.
  """
  edges: [NoteEdge]


  """
  A list of nodes.
  """
  nodes: [Note]


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
