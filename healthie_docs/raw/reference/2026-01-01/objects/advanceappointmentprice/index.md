---
title: AdvanceAppointmentPrice | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/advanceappointmentprice/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/advanceappointmentprice/index.md
---

Specific appointment price object for provider/client

## Fields

[`appointment_type_id` ](#field-appointment-type-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Appointment type ID this appointment price is associated with.

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the price

[`price` ](#field-price)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The advance price for this appointment type

[`user_id` ](#field-user-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · User ID this appointment price is associated with.

## Used By

[`AdvanceAppointmentPriceEdge.node`](/reference/2026-01-01/objects/advanceappointmentpriceedge)

[`AdvanceAppointmentPricePaginationConnection.nodes`](/reference/2026-01-01/objects/advanceappointmentpricepaginationconnection)

[`User.advance_appointment_prices`](/reference/2026-01-01/objects/user)

[`updateUserAppointmentPricingPayload.advance_appointment_prices`](/reference/2026-01-01/objects/updateuserappointmentpricingpayload)

## Definition

```
"""
Specific appointment price object for provider/client
"""
type AdvanceAppointmentPrice {
  """
  Appointment type ID this appointment price is associated with.
  """
  appointment_type_id: ID


  """
  The unique identifier of the price
  """
  id: ID!


  """
  The advance price for this appointment type
  """
  price: String!


  """
  User ID this appointment price is associated with.
  """
  user_id: ID!
}
```
