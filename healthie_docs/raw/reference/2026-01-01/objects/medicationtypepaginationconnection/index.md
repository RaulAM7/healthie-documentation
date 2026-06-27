---
title: MedicationTypePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/medicationtypepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/medicationtypepaginationconnection/index.md
---

The connection type for MedicationType.

## Fields

[`edges` ](#field-edges)· [`[MedicationTypeEdge]` ](/reference/2026-01-01/objects/medicationtypeedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[MedicationType]` ](/reference/2026-01-01/objects/medicationtype)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.medications`](/reference/2026-01-01/queries/medications)

## Definition

```
"""
The connection type for MedicationType.
"""
type MedicationTypePaginationConnection {
  """
  A list of edges.
  """
  edges: [MedicationTypeEdge]


  """
  A list of nodes.
  """
  nodes: [MedicationType]


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
