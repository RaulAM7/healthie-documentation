---
title: updateOrganizationUiConfiguration | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateorganizationuiconfiguration/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateorganizationuiconfiguration/index.md
---

## Arguments

[`input` ](#argument-input)· [`UpdateUiConfigurationInput` ](/reference/2026-01-01/input-objects/updateuiconfigurationinput)· Parameters for UpdateUiConfiguration

## Returns

[`UpdateUiConfigurationPayload`](/reference/2026-01-01/objects/updateuiconfigurationpayload)

## Example

```
mutation updateOrganizationUiConfiguration($input: UpdateUiConfigurationInput) {
  updateOrganizationUiConfiguration(input: $input) {
    messages
    organization
  }
}
```
