---
title: OfferingOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/offeringorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/offeringorderkeys/index.md
---

Offering sorting enum

## Used By

[`Query.offerings`](/reference/2026-01-01/queries/offerings)

## Definition

```
"""
Offering sorting enum
"""
enum OfferingOrderKeys {
  SET_ORDER
  PRICE_ASC
  PRICE_DESC
  NAME_ASC
  NAME_DESC


  """
  Sort by billing items count descending
  """
  BEST_SELLER
}
```
