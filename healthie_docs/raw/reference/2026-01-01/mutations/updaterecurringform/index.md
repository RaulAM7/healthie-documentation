---
title: updateRecurringForm | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updaterecurringform/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updaterecurringform/index.md
---

update a recurring form

## Arguments

[`input` ](#argument-input)· [`updateRecurringFormInput` ](/reference/2026-01-01/input-objects/updaterecurringforminput)· Parameters for updateRecurringForm

## Returns

[`updateRecurringFormPayload`](/reference/2026-01-01/objects/updaterecurringformpayload)

## Example

```
mutation updateRecurringForm($input: updateRecurringFormInput) {
  updateRecurringForm(input: $input) {
    messages
    recurringForm
  }
}
```
