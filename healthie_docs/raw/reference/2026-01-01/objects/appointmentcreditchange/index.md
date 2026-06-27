---
title: AppointmentCreditChange | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentcreditchange/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentcreditchange/index.md
---

An object containing appointment type credit change event

## Fields

[`appointment` ](#field-appointment)· [`Appointment` ](/reference/2026-01-01/objects/appointment)· The appointment related to credit change event

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time when credit change event was created

[`credit_change_event` ](#field-credit-change-event)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The event which caused credit change

[`credit_change_event_type` ](#field-credit-change-event-type)· [`String` ](/reference/2026-01-01/scalars/string)· The specific action which caused credit change

[`credit_quantity` ](#field-credit-quantity)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · The amount of credits after specific event

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the credit change

[`initiator` ](#field-initiator)· [`User` ](/reference/2026-01-01/objects/user)· The user who triggered credit change

[`offering` ](#field-offering)· [`Offering` ](/reference/2026-01-01/objects/offering)· The offering related to credit change event

## Used By

[`AppointmentCreditChangeEdge.node`](/reference/2026-01-01/objects/appointmentcreditchangeedge)

[`AppointmentCreditChangePaginationConnection.nodes`](/reference/2026-01-01/objects/appointmentcreditchangepaginationconnection)

## Definition

```
"""
An object containing appointment type credit change event
"""
type AppointmentCreditChange {
  """
  The appointment related to credit change event
  """
  appointment: Appointment


  """
  The time when credit change event was created
  """
  created_at: ISO8601DateTime!


  """
  The event which caused credit change
  """
  credit_change_event: String!


  """
  The specific action which caused credit change
  """
  credit_change_event_type: String


  """
  The amount of credits after specific event
  """
  credit_quantity: Int!


  """
  The unique identifier of the credit change
  """
  id: ID!


  """
  The user who triggered credit change
  """
  initiator: User


  """
  The offering related to credit change event
  """
  offering: Offering
}
```
