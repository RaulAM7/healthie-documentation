---
title: CustomEmailPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/customemailpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/customemailpaginationconnection/index.md
---

The connection type for CustomEmail.

## Fields

[`edges` ](#field-edges)· [`[CustomEmailEdge]` ](/reference/2026-01-01/objects/customemailedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[CustomEmail]` ](/reference/2026-01-01/objects/customemail)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.courseItemCustomEmails`](/reference/2026-01-01/queries/courseitemcustomemails)

[`Query.customEmails`](/reference/2026-01-01/queries/customemails)

## Definition

```
"""
The connection type for CustomEmail.
"""
type CustomEmailPaginationConnection {
  """
  A list of edges.
  """
  edges: [CustomEmailEdge]


  """
  A list of nodes.
  """
  nodes: [CustomEmail]


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
