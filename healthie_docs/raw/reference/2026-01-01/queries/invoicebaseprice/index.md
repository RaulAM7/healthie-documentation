---
title: invoiceBasePrice | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/invoicebaseprice/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/invoicebaseprice/index.md
---

get the base price for the invoice based off the associated item

## Arguments

[`cms1500_id` ](#argument-cms1500-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`offering_id` ](#argument-offering-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`String`](/reference/2026-01-01/scalars/string)

## Example

```
query invoiceBasePrice($cms1500_id: ID, $offering_id: ID) {
  invoiceBasePrice(cms1500_id: $cms1500_id, offering_id: $offering_id)
}
```
