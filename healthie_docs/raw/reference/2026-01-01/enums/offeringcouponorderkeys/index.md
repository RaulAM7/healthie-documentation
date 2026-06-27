---
title: OfferingCouponOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/offeringcouponorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/offeringcouponorderkeys/index.md
---

OfferingCoupon sorting enum

## Used By

[`Query.offeringCoupons`](/reference/2026-01-01/queries/offeringcoupons)

## Definition

```
"""
OfferingCoupon sorting enum
"""
enum OfferingCouponOrderKeys {
  CODE_ASC
  CODE_DESC
  TYPE_ASC
  TYPE_DESC
  APPLIES_TO_ASC
  APPLIES_TO_DESC
  AMOUNT_ASC
  AMOUNT_DESC
  EXPIRES_AT_ASC
  EXPIRES_AT_DESC
  TOTAL_USAGE_ASC
  TOTAL_USAGE_DESC
}
```
