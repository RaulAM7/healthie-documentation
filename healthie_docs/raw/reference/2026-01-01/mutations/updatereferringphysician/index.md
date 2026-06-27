---
title: updateReferringPhysician | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatereferringphysician/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatereferringphysician/index.md
---

Update Referring Physician

## Arguments

[`input` ](#argument-input)· [`updateReferringPhysicianInput` ](/reference/2026-01-01/input-objects/updatereferringphysicianinput)· Parameters for updateReferringPhysician

## Returns

[`updateReferringPhysicianPayload`](/reference/2026-01-01/objects/updatereferringphysicianpayload)

## Example

```
mutation updateReferringPhysician($input: updateReferringPhysicianInput) {
  updateReferringPhysician(input: $input) {
    messages
    referring_physician
  }
}
```
