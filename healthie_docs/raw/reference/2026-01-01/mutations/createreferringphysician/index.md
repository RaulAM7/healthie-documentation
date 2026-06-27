---
title: createReferringPhysician | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createreferringphysician/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createreferringphysician/index.md
---

Create new Referring Physician

## Arguments

[`input` ](#argument-input)· [`createReferringPhysicianInput` ](/reference/2026-01-01/input-objects/createreferringphysicianinput)· Parameters for createReferringPhysician

## Returns

[`createReferringPhysicianPayload`](/reference/2026-01-01/objects/createreferringphysicianpayload)

## Example

```
mutation createReferringPhysician($input: createReferringPhysicianInput) {
  createReferringPhysician(input: $input) {
    duplicated_physician
    messages
    referring_physician
  }
}
```
