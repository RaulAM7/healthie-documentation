---
title: deleteOrganizationInfo | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteorganizationinfo/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteorganizationinfo/index.md
---

Destroy an organization info

## Arguments

[`input` ](#argument-input)· [`deleteOrganizationInfoInput` ](/reference/2026-01-01/input-objects/deleteorganizationinfoinput)· Parameters for deleteOrganizationInfo

## Returns

[`deleteOrganizationInfoPayload`](/reference/2026-01-01/objects/deleteorganizationinfopayload)

## Example

```
mutation deleteOrganizationInfo($input: deleteOrganizationInfoInput) {
  deleteOrganizationInfo(input: $input) {
    messages
    organizationInfo
  }
}
```
