---
title: canCapOfferingPurchases | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/cancapofferingpurchases/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/cancapofferingpurchases/index.md
---

Check if the user has access to the package buy limit feature

## Arguments

[`token` ](#argument-token)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`Boolean`](/reference/2026-01-01/scalars/boolean)

## Example

```
query canCapOfferingPurchases($token: String) {
  canCapOfferingPurchases(token: $token)
}
```
