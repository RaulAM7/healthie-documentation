---
title: addPharmacy | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/addpharmacy/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/addpharmacy/index.md
---

Add a pharmacy to the user

## Arguments

[`input` ](#argument-input)· [`addPharmacyInput` ](/reference/2026-01-01/input-objects/addpharmacyinput)· Parameters for addPharmacy

## Returns

[`addPharmacyPayload`](/reference/2026-01-01/objects/addpharmacypayload)

## Example

```
mutation addPharmacy($input: addPharmacyInput) {
  addPharmacy(input: $input) {
    messages
    pharmacy
  }
}
```
