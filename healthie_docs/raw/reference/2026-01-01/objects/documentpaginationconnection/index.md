---
title: DocumentPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/documentpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/documentpaginationconnection/index.md
---

The connection type for Document.

## Fields

[`edges` ](#field-edges)· [`[DocumentEdge]` ](/reference/2026-01-01/objects/documentedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Document]` ](/reference/2026-01-01/objects/document)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.courseItemDocuments`](/reference/2026-01-01/queries/courseitemdocuments)

[`Query.documents`](/reference/2026-01-01/queries/documents)

## Definition

```
"""
The connection type for Document.
"""
type DocumentPaginationConnection {
  """
  A list of edges.
  """
  edges: [DocumentEdge]


  """
  A list of nodes.
  """
  nodes: [Document]


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
