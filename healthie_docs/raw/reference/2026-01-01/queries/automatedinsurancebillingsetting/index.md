---
title: automatedInsuranceBillingSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/automatedinsurancebillingsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/automatedinsurancebillingsetting/index.md
---

fetch the automated insurance billing setting

## Arguments

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`AutomatedInsuranceBillingSetting`](/reference/2026-01-01/objects/automatedinsurancebillingsetting)

## Example

```
query automatedInsuranceBillingSetting($user_id: ID) {
  automatedInsuranceBillingSetting(user_id: $user_id) {
    auto_create_cms1500s
    auto_submit_cms1500s
    id
    insurance_billing_enabled
    use_cpt_codes_units_and_fees_with_appointment_types
  }
}
```
