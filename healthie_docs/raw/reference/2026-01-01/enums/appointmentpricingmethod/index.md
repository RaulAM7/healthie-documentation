---
title: AppointmentPricingMethod | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/appointmentpricingmethod/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/appointmentpricingmethod/index.md
---

Available pricing methods for appointments

## Used By

[`Appointment.effective_pricing_method`](/reference/2026-01-01/objects/appointment)

## Definition

```
"""
Available pricing methods for appointments
"""
enum AppointmentPricingMethod {
  """
  Copay pricing method
  """
  COPAY


  """
  Coinsurance pricing method
  """
  COINSURANCE


  """
  Deductible pricing method
  """
  DEDUCTIBLE


  """
  Appointment type client pricing method
  """
  APPOINTMENT_TYPE_CLIENT


  """
  Appointment type provider pricing method
  """
  APPOINTMENT_TYPE_PROVIDER


  """
  Appointment type default pricing method
  """
  APPOINTMENT_TYPE_DEFAULT
}
```
