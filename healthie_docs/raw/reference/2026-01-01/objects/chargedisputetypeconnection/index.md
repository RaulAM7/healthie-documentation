---
title: ChargeDisputeTypeConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/chargedisputetypeconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/chargedisputetypeconnection/index.md
---

The connection type for ChargeDisputeType.

## Fields

[`edges` ](#field-edges)· [`[ChargeDisputeTypeEdge]` ](/reference/2026-01-01/objects/chargedisputetypeedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[ChargeDisputeType]` ](/reference/2026-01-01/objects/chargedisputetype)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.chargeDisputes`](/reference/2026-01-01/queries/chargedisputes)

## Definition

```
"""
The connection type for ChargeDisputeType.
"""
type ChargeDisputeTypeConnection {
  """
  A list of edges.
  """
  edges: [ChargeDisputeTypeEdge]


  """
  A list of nodes.
  """
  nodes: [ChargeDisputeType]


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
