---
title: FolderPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/folderpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/folderpaginationconnection/index.md
---

The connection type for Folder.

## Fields

[`edges` ](#field-edges)· [`[FolderEdge]` ](/reference/2026-01-01/objects/folderedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Folder]` ](/reference/2026-01-01/objects/folder)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.folders`](/reference/2026-01-01/queries/folders)

## Definition

```
"""
The connection type for Folder.
"""
type FolderPaginationConnection {
  """
  A list of edges.
  """
  edges: [FolderEdge]


  """
  A list of nodes.
  """
  nodes: [Folder]


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
