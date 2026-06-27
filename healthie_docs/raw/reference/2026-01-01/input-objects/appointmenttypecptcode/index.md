---
title: AppointmentTypeCptCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/appointmenttypecptcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/appointmenttypecptcode/index.md
---

Payload for a CPT code associated with an appointment type

## Fields

[`cpt_code_id` ](#field-cpt-code-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the CPT code

[`fee_per_unit` ](#field-fee-per-unit)· [`Int` ](/reference/2026-01-01/scalars/int)· Fee (in cents) per unit

[`insurance_billing_enabled` ](#field-insurance-billing-enabled)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· DEPRECATED. Use appointmentType's insurance\_billing\_enabled instead

deprecated

Use appointmentType's insurance\_billing\_enabled instead

[`units` ](#field-units)· [`String` ](/reference/2026-01-01/scalars/string)· The number of units for the CPT code

## Used By

[`createAppointmentTypeInput.appointment_type_cpt_code`](/reference/2026-01-01/input-objects/createappointmenttypeinput)

[`updateAppointmentTypeInput.appointment_type_cpt_code`](/reference/2026-01-01/input-objects/updateappointmenttypeinput)

## Definition

```
"""
Payload for a CPT code associated with an appointment type
"""
input AppointmentTypeCptCode {
  """
  The ID of the CPT code
  """
  cpt_code_id: String


  """
  Fee (in cents) per unit
  """
  fee_per_unit: Int


  """
  DEPRECATED. Use appointmentType's insurance_billing_enabled instead
  """
  insurance_billing_enabled: Boolean
    @deprecated(
      reason: "Use appointmentType's insurance_billing_enabled instead"
    )


  """
  The number of units for the CPT code
  """
  units: String
}
```
