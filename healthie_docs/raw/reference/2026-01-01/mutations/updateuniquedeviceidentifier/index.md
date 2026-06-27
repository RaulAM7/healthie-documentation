---
title: updateUniqueDeviceIdentifier | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateuniquedeviceidentifier/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateuniquedeviceidentifier/index.md
---

Update a UniqueDeviceIdentifier Object

## Arguments

[`input` ](#argument-input)· [`updateUniqueDeviceIdentifierInput` ](/reference/2026-01-01/input-objects/updateuniquedeviceidentifierinput)· Parameters for updateUniqueDeviceIdentifier

## Returns

[`updateUniqueDeviceIdentifierPayload`](/reference/2026-01-01/objects/updateuniquedeviceidentifierpayload)

## Example

```
mutation updateUniqueDeviceIdentifier(
  $input: updateUniqueDeviceIdentifierInput
) {
  updateUniqueDeviceIdentifier(input: $input) {
    messages
    unique_device_identifier
  }
}
```
