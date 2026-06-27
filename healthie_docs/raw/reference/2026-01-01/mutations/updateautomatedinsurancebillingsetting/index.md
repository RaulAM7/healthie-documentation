---
title: updateAutomatedInsuranceBillingSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateautomatedinsurancebillingsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateautomatedinsurancebillingsetting/index.md
---

update automated insurance billing setting

## Arguments

[`input` ](#argument-input)· [`updateAutomatedInsuranceBillingSettingInput` ](/reference/2026-01-01/input-objects/updateautomatedinsurancebillingsettinginput)· Parameters for updateAutomatedInsuranceBillingSetting

## Returns

[`updateAutomatedInsuranceBillingSettingPayload`](/reference/2026-01-01/objects/updateautomatedinsurancebillingsettingpayload)

## Example

```
mutation updateAutomatedInsuranceBillingSetting(
  $input: updateAutomatedInsuranceBillingSettingInput
) {
  updateAutomatedInsuranceBillingSetting(input: $input) {
    automated_insurance_billing_setting
    messages
  }
}
```
