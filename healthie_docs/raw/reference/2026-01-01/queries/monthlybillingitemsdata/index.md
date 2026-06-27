---
title: monthlyBillingItemsData | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/monthlybillingitemsdata/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/monthlybillingitemsdata/index.md
---

returns metadata about monthly payments

## Arguments

[`gross` ](#argument-gross)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`org_level` ](#argument-org-level)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

## Returns

[`[MonthlyBillingItemsDataType!]`](/reference/2026-01-01/objects/monthlybillingitemsdatatype)

## Example

```
query monthlyBillingItemsData($gross: Boolean, $org_level: Boolean) {
  monthlyBillingItemsData(gross: $gross, org_level: $org_level) {
    amount
    month
  }
}
```
