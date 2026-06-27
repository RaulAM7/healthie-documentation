---
title: uploadBatchToOfficeally | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/uploadbatchtoofficeally/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/uploadbatchtoofficeally/index.md
---

Upload a CMS1500 batch to OfficeAlly

## Arguments

[`input` ](#argument-input)· [`uploadBatchToOfficeallyInput` ](/reference/2026-01-01/input-objects/uploadbatchtoofficeallyinput)· Parameters for uploadBatchToOfficeally

## Returns

[`uploadBatchToOfficeallyPayload`](/reference/2026-01-01/objects/uploadbatchtoofficeallypayload)

## Example

```
mutation uploadBatchToOfficeally($input: uploadBatchToOfficeallyInput) {
  uploadBatchToOfficeally(input: $input) {
    cms1500s
    messages
    success_string
  }
}
```
