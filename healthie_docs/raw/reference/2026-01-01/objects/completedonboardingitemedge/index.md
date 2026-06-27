---
title: CompletedOnboardingItemEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/completedonboardingitemedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/completedonboardingitemedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`CompletedOnboardingItem` ](/reference/2026-01-01/objects/completedonboardingitem)· The item at the end of the edge.

## Used By

[`CompletedOnboardingItemPaginationConnection.edges`](/reference/2026-01-01/objects/completedonboardingitempaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type CompletedOnboardingItemEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: CompletedOnboardingItem
}
```
