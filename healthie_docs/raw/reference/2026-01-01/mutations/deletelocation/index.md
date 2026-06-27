---
title: deleteLocation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletelocation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletelocation/index.md
---

Destroy a Location

## Arguments

[`input` ](#argument-input)· [`deleteLocationInput` ](/reference/2026-01-01/input-objects/deletelocationinput)· Parameters for deleteLocation

## Returns

[`deleteLocationPayload`](/reference/2026-01-01/objects/deletelocationpayload)

## Example

```
mutation deleteLocation($input: deleteLocationInput) {
  deleteLocation(input: $input) {
    location
    messages
  }
}
```
