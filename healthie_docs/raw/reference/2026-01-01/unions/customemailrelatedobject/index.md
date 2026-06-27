---
title: CustomEmailRelatedObject | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/unions/customemailrelatedobject/index
  md: https://docs.gethealthie.com/reference/2026-01-01/unions/customemailrelatedobject/index.md
---

CustomEmail related\_object union

## Possible types

[`AppointmentType`](#field-appointmenttype)

[`Course`](#field-course)

[`Offering`](#field-offering)

## Used By

[`CustomEmail.related_object`](/reference/2026-01-01/objects/customemail)

## Definition

```
"""
CustomEmail related_object union
"""
union CustomEmailRelatedObject = AppointmentType | Course | Offering
```
