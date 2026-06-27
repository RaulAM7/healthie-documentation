---
title: MonthlyBillingItemsDataType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/monthlybillingitemsdatatype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/monthlybillingitemsdatatype/index.md
---

Monthly billing items data

## Fields

[`amount` ](#field-amount)· [`Int` ](/reference/2026-01-01/scalars/int)· Amount of monthly billing items

[`month` ](#field-month)· [`String` ](/reference/2026-01-01/scalars/string)· Month the data relates to

## Used By

[`Query.monthlyBillingItemsData`](/reference/2026-01-01/queries/monthlybillingitemsdata)

## Definition

```
"""
Monthly billing items data
"""
type MonthlyBillingItemsDataType {
  """
  Amount of monthly billing items
  """
  amount: Int


  """
  Month the data relates to
  """
  month: String
}
```
