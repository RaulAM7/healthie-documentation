---
title: CompletedOnboardingItemPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/completedonboardingitempaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/completedonboardingitempaginationconnection/index.md
---

The connection type for CompletedOnboardingItem.

## Fields

[`edges` ](#field-edges)· [`[CompletedOnboardingItemEdge]` ](/reference/2026-01-01/objects/completedonboardingitemedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[CompletedOnboardingItem]` ](/reference/2026-01-01/objects/completedonboardingitem)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.unassociatedCompletedOnboardingItems`](/reference/2026-01-01/queries/unassociatedcompletedonboardingitems)

## Definition

```
"""
The connection type for CompletedOnboardingItem.
"""
type CompletedOnboardingItemPaginationConnection {
  """
  A list of edges.
  """
  edges: [CompletedOnboardingItemEdge]


  """
  A list of nodes.
  """
  nodes: [CompletedOnboardingItem]


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
