---
title: LabOrderBilling | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/laborderbilling/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/laborderbilling/index.md
---

The entity that will be billed for the lab order

## Used By

[`ELabsSettings.billing_types`](/reference/2026-01-01/objects/elabssettings)

[`SubmissionInput.billing_type`](/reference/2026-01-01/input-objects/submissioninput)

## Definition

```
"""
The entity that will be billed for the lab order
"""
enum LabOrderBilling {
  """
  Bill to patient insurance
  """
  INSURANCE


  """
  Bill to organization
  """
  PROVIDER


  """
  Bill to patient
  """
  PATIENT
}
```
