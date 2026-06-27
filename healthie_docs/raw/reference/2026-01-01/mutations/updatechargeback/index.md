---
title: updateChargeBack | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatechargeback/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatechargeback/index.md
---

Update ChargeBack

## Arguments

[`input` ](#argument-input)· [`updateChargeBackInput` ](/reference/2026-01-01/input-objects/updatechargebackinput)· Parameters for updateChargeBack

## Returns

[`updateChargeBackPayload`](/reference/2026-01-01/objects/updatechargebackpayload)

## Example

```
mutation updateChargeBack($input: updateChargeBackInput) {
  updateChargeBack(input: $input) {
    charge_back
    messages
  }
}
```
