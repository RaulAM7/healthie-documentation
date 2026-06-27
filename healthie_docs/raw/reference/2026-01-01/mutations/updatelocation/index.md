---
title: updateLocation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatelocation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatelocation/index.md
---

update Location

## Arguments

[`input` ](#argument-input)· [`updateLocationInput` ](/reference/2026-01-01/input-objects/updatelocationinput)· Parameters for updateLocation

## Returns

[`updateLocationPayload`](/reference/2026-01-01/objects/updatelocationpayload)

## Example

```
mutation updateLocation($input: updateLocationInput) {
  updateLocation(input: $input) {
    location
    messages
  }
}
```
