---
title: uploadBatchToCandidHealth | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/uploadbatchtocandidhealth/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/uploadbatchtocandidhealth/index.md
---

Upload a CMS1500 batch to CandidHealth

## Arguments

[`input` ](#argument-input)· [`uploadBatchToCandidHealthInput` ](/reference/2026-01-01/input-objects/uploadbatchtocandidhealthinput)· Parameters for uploadBatchToCandidHealth

## Returns

[`uploadBatchToCandidHealthPayload`](/reference/2026-01-01/objects/uploadbatchtocandidhealthpayload)

## Example

```
mutation uploadBatchToCandidHealth($input: uploadBatchToCandidHealthInput) {
  uploadBatchToCandidHealth(input: $input) {
    cms1500s
    messages
    success_string
  }
}
```
