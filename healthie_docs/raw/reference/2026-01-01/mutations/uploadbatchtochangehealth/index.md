---
title: uploadBatchToChangeHealth | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/uploadbatchtochangehealth/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/uploadbatchtochangehealth/index.md
---

deprecated ChangeHealth claims integration has been discontinued.

Upload a CMS1500 batch to ChangeHealth

## Arguments

[`input` ](#argument-input)· [`uploadBatchToChangeHealthInput` ](/reference/2026-01-01/input-objects/uploadbatchtochangehealthinput)· Parameters for uploadBatchToChangeHealth

## Returns

[`uploadBatchToChangeHealthPayload`](/reference/2026-01-01/objects/uploadbatchtochangehealthpayload)

## Example

```
mutation uploadBatchToChangeHealth($input: uploadBatchToChangeHealthInput) {
  uploadBatchToChangeHealth(input: $input) {
    cms1500s
    messages
    success_string
  }
}
```
