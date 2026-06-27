---
title: AppointmentPricingInfoType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentpricinginfotype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentpricinginfotype/index.md
---

Appointment pricing info

## Fields

[`cpt_code` ](#field-cpt-code)· [`CptCode` ](/reference/2026-01-01/objects/cptcode)· The CPT Code

[`cpt_code_id` ](#field-cpt-code-id)· [`String` ](/reference/2026-01-01/scalars/string)· CPT Code ID

[`insurance_billing_method` ](#field-insurance-billing-method)· [`String` ](/reference/2026-01-01/scalars/string)· The insurance billing method for this appointment

[`price` ](#field-price)· [`String` ](/reference/2026-01-01/scalars/string)· The price

[`units` ](#field-units)· [`String` ](/reference/2026-01-01/scalars/string)· The units of the price

## Used By

[`Appointment.pricing_info`](/reference/2026-01-01/objects/appointment)

[`AppointmentType.pricing_info`](/reference/2026-01-01/objects/appointmenttype)

## Definition

```
"""
Appointment pricing info
"""
type AppointmentPricingInfoType {
  """
  The CPT Code
  """
  cpt_code: CptCode


  """
  CPT Code ID
  """
  cpt_code_id: String


  """
  The insurance billing method for this appointment
  """
  insurance_billing_method: String


  """
  The price
  """
  price: String


  """
  The units of the price
  """
  units: String
}
```
