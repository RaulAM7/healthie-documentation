---
title: ClaimPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimpaginationconnection/index.md
---

The connection type for Claim.

## Fields

[`edges` ](#field-edges)· [`[ClaimEdge]` ](/reference/2026-01-01/objects/claimedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Claim]` ](/reference/2026-01-01/objects/claim)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Claim.correction_claims`](/reference/2026-01-01/objects/claim)

## Definition

```
"""
The connection type for Claim.
"""
type ClaimPaginationConnection {
  """
  A list of edges.
  """
  edges: [ClaimEdge]


  """
  A list of nodes.
  """
  nodes: [Claim]


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
