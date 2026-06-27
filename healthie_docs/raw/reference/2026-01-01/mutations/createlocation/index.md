---
title: createLocation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createlocation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createlocation/index.md
---

create Location

## Arguments

[`input` ](#argument-input)· [`createLocationInput` ](/reference/2026-01-01/input-objects/createlocationinput)· Parameters for createLocation

## Returns

[`createLocationPayload`](/reference/2026-01-01/objects/createlocationpayload)

## Example

```
mutation createLocation($input: createLocationInput) {
  createLocation(input: $input) {
    location
    messages
  }
}
```
