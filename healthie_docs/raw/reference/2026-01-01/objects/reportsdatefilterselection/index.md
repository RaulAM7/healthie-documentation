---
title: ReportsDateFilterSelection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/reportsdatefilterselection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/reportsdatefilterselection/index.md
---

The selected date range for specific report

## Fields

[`appointments` ](#field-appointments)· [`String` ](/reference/2026-01-01/scalars/string)· The selected date range for appointments

[`authorization` ](#field-authorization)· [`String` ](/reference/2026-01-01/scalars/string)· The selected date range for authorizations

[`bank_transfers` ](#field-bank-transfers)· [`String` ](/reference/2026-01-01/scalars/string)· The selected date range for bank transfers

[`client_activity` ](#field-client-activity)· [`String` ](/reference/2026-01-01/scalars/string)· The selected date range for client activities

[`client_blood_sugar_metrics` ](#field-client-blood-sugar-metrics)· [`String` ](/reference/2026-01-01/scalars/string)· The selected date range for client blood sugar metrics

[`client_credits` ](#field-client-credits)· [`String` ](/reference/2026-01-01/scalars/string)· The selected date range for client credits

[`client_list` ](#field-client-list)· [`String` ](/reference/2026-01-01/scalars/string)· The selected date range for clients list

[`client_metrics` ](#field-client-metrics)· [`String` ](/reference/2026-01-01/scalars/string)· The selected date range for client metrics

[`client_status` ](#field-client-status)· [`String` ](/reference/2026-01-01/scalars/string)· The selected date range for client statuses

[`cms_1500s` ](#field-cms-1500s)· [`String` ](/reference/2026-01-01/scalars/string)· The selected date range for cms 1500s

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the selection

[`payments` ](#field-payments)· [`String` ](/reference/2026-01-01/scalars/string)· The selected date range for payments

[`superbills` ](#field-superbills)· [`String` ](/reference/2026-01-01/scalars/string)· The selected date range for superbills

## Used By

[`User.reports_date_filter_selection`](/reference/2026-01-01/objects/user)

## Definition

```
"""
The selected date range for specific report
"""
type ReportsDateFilterSelection {
  """
  The selected date range for appointments
  """
  appointments: String


  """
  The selected date range for authorizations
  """
  authorization: String


  """
  The selected date range for bank transfers
  """
  bank_transfers: String


  """
  The selected date range for client activities
  """
  client_activity: String


  """
  The selected date range for client blood sugar metrics
  """
  client_blood_sugar_metrics: String


  """
  The selected date range for client credits
  """
  client_credits: String


  """
  The selected date range for clients list
  """
  client_list: String


  """
  The selected date range for client metrics
  """
  client_metrics: String


  """
  The selected date range for client statuses
  """
  client_status: String


  """
  The selected date range for cms 1500s
  """
  cms_1500s: String


  """
  The unique identifier of the selection
  """
  id: ID!


  """
  The selected date range for payments
  """
  payments: String


  """
  The selected date range for superbills
  """
  superbills: String
}
```
