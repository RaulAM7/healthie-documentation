---
title: AppointmentDataType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentdatatype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentdatatype/index.md
---

Appointment Data

## Fields

[`freq` ](#field-freq)· [`AppointmentFrequencyDataType` ](/reference/2026-01-01/objects/appointmentfrequencydatatype)· Appointment Frequency

[`month` ](#field-month)· [`String` ](/reference/2026-01-01/scalars/string)· Appointment Month

## Used By

[`Query.appointmentFrequencyData`](/reference/2026-01-01/queries/appointmentfrequencydata)

## Definition

```
"""
Appointment Data
"""
type AppointmentDataType {
  """
  Appointment Frequency
  """
  freq: AppointmentFrequencyDataType


  """
  Appointment Month
  """
  month: String
}
```
