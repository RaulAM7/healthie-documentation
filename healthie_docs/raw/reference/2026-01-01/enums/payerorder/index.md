---
title: PayerOrder | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/payerorder/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/payerorder/index.md
---

Whether a claim is primary or secondary

## Used By

[`Claim.payer_order`](/reference/2026-01-01/objects/claim)

## Definition

```
"""
Whether a claim is primary or secondary
"""
enum PayerOrder {
  """
  Primary claim
  """
  PRIMARY


  """
  Secondary claim
  """
  SECONDARY
}
```
