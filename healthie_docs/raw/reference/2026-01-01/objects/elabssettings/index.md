---
title: ELabsSettings | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/elabssettings/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/elabssettings/index.md
---

Organization level settings for E-Labs

## Fields

[`billing_types` ](#field-billing-types)· [`[LabOrderBilling!]` ](/reference/2026-01-01/enums/laborderbilling)· A list of acceptable billing types

[`lab_vendors` ](#field-lab-vendors)· [`[LabOrderLabVendor!]` ](/reference/2026-01-01/enums/laborderlabvendor)· A list of acceptable lab vendors

## Used By

[`Organization.e_labs_settings`](/reference/2026-01-01/objects/organization)

## Definition

```
"""
Organization level settings for E-Labs
"""
type ELabsSettings {
  """
  A list of acceptable billing types
  """
  billing_types: [LabOrderBilling!]


  """
  A list of acceptable lab vendors
  """
  lab_vendors: [LabOrderLabVendor!]
}
```
