---
title: PreferredMedicalCodePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/preferredmedicalcodepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/preferredmedicalcodepaginationconnection/index.md
---

The connection type for PreferredMedicalCode.

## Fields

[`edges` ](#field-edges)· [`[PreferredMedicalCodeEdge]` ](/reference/2026-01-01/objects/preferredmedicalcodeedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[PreferredMedicalCode]` ](/reference/2026-01-01/objects/preferredmedicalcode)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.preferred_medical_codes`](/reference/2026-01-01/queries/preferred-medical-codes)

## Definition

```
"""
The connection type for PreferredMedicalCode.
"""
type PreferredMedicalCodePaginationConnection {
  """
  A list of edges.
  """
  edges: [PreferredMedicalCodeEdge]


  """
  A list of nodes.
  """
  nodes: [PreferredMedicalCode]


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
