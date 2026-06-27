---
title: createAutomatedInsuranceBillingSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createautomatedinsurancebillingsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createautomatedinsurancebillingsetting/index.md
---

create automated insurance billing setting

## Arguments

[`input` ](#argument-input)· [`createAutomatedInsuranceBillingSettingInput` ](/reference/2026-01-01/input-objects/createautomatedinsurancebillingsettinginput)· Parameters for createAutomatedInsuranceBillingSetting

## Returns

[`createAutomatedInsuranceBillingSettingPayload`](/reference/2026-01-01/objects/createautomatedinsurancebillingsettingpayload)

## Example

```
mutation createAutomatedInsuranceBillingSetting(
  $input: createAutomatedInsuranceBillingSettingInput
) {
  createAutomatedInsuranceBillingSetting(input: $input) {
    automated_insurance_billing_setting
    messages
  }
}
```
