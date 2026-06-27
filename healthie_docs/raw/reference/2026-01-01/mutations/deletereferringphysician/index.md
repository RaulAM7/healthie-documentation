---
title: deleteReferringPhysician | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletereferringphysician/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletereferringphysician/index.md
---

Delete referring physician

## Arguments

[`input` ](#argument-input)· [`deleteReferringPhysicianInput` ](/reference/2026-01-01/input-objects/deletereferringphysicianinput)· Parameters for deleteReferringPhysician

## Returns

[`deleteReferringPhysicianPayload`](/reference/2026-01-01/objects/deletereferringphysicianpayload)

## Example

```
mutation deleteReferringPhysician($input: deleteReferringPhysicianInput) {
  deleteReferringPhysician(input: $input) {
    messages
    referringPhysician
  }
}
```
