---
title: availableItemTypes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/availableitemtypes/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/availableitemtypes/index.md
---

Fetch available item types (for use in onboarding items)

## Arguments

[`onboarding_flow_id` ](#argument-onboarding-flow-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`String`](/reference/2026-01-01/scalars/string)

## Example

```
query availableItemTypes($onboarding_flow_id: ID) {
  availableItemTypes(onboarding_flow_id: $onboarding_flow_id)
}
```
