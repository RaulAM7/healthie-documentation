---
title: exportClientEhi | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/exportclientehi/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/exportclientehi/index.md
---

Export Client EHI data

## Arguments

[`input` ](#argument-input)· [`exportClientEhiInput` ](/reference/2026-01-01/input-objects/exportclientehiinput)· Parameters for exportClientEhi

## Returns

[`exportClientEhiPayload`](/reference/2026-01-01/objects/exportclientehipayload)

## Example

```
mutation exportClientEhi($input: exportClientEhiInput) {
  exportClientEhi(input: $input) {
    messages
    success_string
  }
}
```
