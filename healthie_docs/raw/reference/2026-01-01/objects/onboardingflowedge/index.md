---
title: OnboardingFlowEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/onboardingflowedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/onboardingflowedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`OnboardingFlow` ](/reference/2026-01-01/objects/onboardingflow)· The item at the end of the edge.

## Used By

[`OnboardingFlowPaginationConnection.edges`](/reference/2026-01-01/objects/onboardingflowpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type OnboardingFlowEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: OnboardingFlow
}
```
