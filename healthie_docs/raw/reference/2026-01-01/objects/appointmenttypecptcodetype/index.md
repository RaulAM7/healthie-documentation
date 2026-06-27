---
title: AppointmentTypeCptCodeType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmenttypecptcodetype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmenttypecptcodetype/index.md
---

AppointmentTypeCptCode object

## Fields

[`appointment_type_id` ](#field-appointment-type-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · Appointment Type ID

[`cpt_code_id` ](#field-cpt-code-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · CPT Code ID

[`fee_per_unit` ](#field-fee-per-unit)· [`Int` ](/reference/2026-01-01/scalars/int)· Fee (in cents) per unit

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the object

[`insurance_billing_enabled` ](#field-insurance-billing-enabled)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· DEPRECATED. Use appointmentType's insurance\_billing\_enabled instead

deprecated

Use appointmentType's insurance\_billing\_enabled instead

[`units` ](#field-units)· [`String` ](/reference/2026-01-01/scalars/string)· Units

## Used By

[`AppointmentType.appointment_type_cpt_code`](/reference/2026-01-01/objects/appointmenttype)

[`createAppointmentTypeCptCodePayload.appointment_type_cpt_code`](/reference/2026-01-01/objects/createappointmenttypecptcodepayload)

[`deleteAppointmentTypeCptCodePayload.appointment_type_cpt_code`](/reference/2026-01-01/objects/deleteappointmenttypecptcodepayload)

[`updateAppointmentTypeCptCodePayload.appointment_type_cpt_code`](/reference/2026-01-01/objects/updateappointmenttypecptcodepayload)

## Definition

```
"""
AppointmentTypeCptCode object
"""
type AppointmentTypeCptCodeType {
  """
  Appointment Type ID
  """
  appointment_type_id: ID!


  """
  CPT Code ID
  """
  cpt_code_id: ID!


  """
  Fee (in cents) per unit
  """
  fee_per_unit: Int


  """
  The unique identifier of the object
  """
  id: ID!


  """
  DEPRECATED. Use appointmentType's insurance_billing_enabled instead
  """
  insurance_billing_enabled: Boolean
    @deprecated(
      reason: "Use appointmentType's insurance_billing_enabled instead"
    )


  """
  Units
  """
  units: String
}
```
