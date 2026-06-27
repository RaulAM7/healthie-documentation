---
title: minimumOfferingPrice | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/minimumofferingprice/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/minimumofferingprice/index.md
---

## Arguments

[`lab_option_ids` ](#argument-lab-option-ids)· [`[ID]`](/reference/2026-01-01/scalars/id)

[`state` ](#argument-state)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`String`](/reference/2026-01-01/scalars/string)

## Example

```
query minimumOfferingPrice($lab_option_ids: [ID], $state: String) {
  minimumOfferingPrice(lab_option_ids: $lab_option_ids, state: $state)
}
```
