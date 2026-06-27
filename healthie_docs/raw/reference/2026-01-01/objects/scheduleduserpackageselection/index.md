---
title: ScheduledUserPackageSelection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/scheduleduserpackageselection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/scheduleduserpackageselection/index.md
---

Billing items that are scheduled and will have a user package selection associated with them

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the room

[`offering` ](#field-offering)· [`Offering` ](/reference/2026-01-01/objects/offering)· Related offering

[`recurring_payment` ](#field-recurring-payment)· [`RecurringPayment` ](/reference/2026-01-01/objects/recurringpayment)· Related recurring\_payment

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· Related user

## Used By

[`ScheduledUserPackageSelectionEdge.node`](/reference/2026-01-01/objects/scheduleduserpackageselectionedge)

[`ScheduledUserPackageSelectionPaginationConnection.nodes`](/reference/2026-01-01/objects/scheduleduserpackageselectionpaginationconnection)

## Definition

```
"""
Billing items that are scheduled and will have a user package selection associated with them
"""
type ScheduledUserPackageSelection {
  """
  The unique identifier of the room
  """
  id: ID!


  """
  Related offering
  """
  offering: Offering


  """
  Related recurring_payment
  """
  recurring_payment: RecurringPayment


  """
  Related user
  """
  user: User
}
```
