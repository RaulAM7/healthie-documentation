---
title: AppointmentBookingWarning | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentbookingwarning/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentbookingwarning/index.md
---

Warnings to show provider before they book

## Fields

[`category` ](#field-category)· [`String` ](/reference/2026-01-01/scalars/string)· Category of warning (e.g no credits)

[`potential_issue_ids` ](#field-potential-issue-ids)· [`[String!]` ](/reference/2026-01-01/scalars/string)· Array of IDs of objects causing booking issues for a given category

[`potential_issues` ](#field-potential-issues)· [`[String!]` ](/reference/2026-01-01/scalars/string)· Array of potential booking issues for a given category

[`subtitle` ](#field-subtitle)· [`String` ](/reference/2026-01-01/scalars/string)· Subtitle describing the category

## Used By

[`Query.appointmentBookingWarnings`](/reference/2026-01-01/queries/appointmentbookingwarnings)

## Definition

```
"""
Warnings to show provider before they book
"""
type AppointmentBookingWarning {
  """
  Category of warning (e.g no credits)
  """
  category: String


  """
  Array of IDs of objects causing booking issues for a given category
  """
  potential_issue_ids: [String!]


  """
  Array of potential booking issues for a given category
  """
  potential_issues: [String!]


  """
  Subtitle describing the category
  """
  subtitle: String
}
```
