---
title: deleteUniqueDeviceIdentifier | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteuniquedeviceidentifier/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteuniquedeviceidentifier/index.md
---

Delete a UniqueDeviceIdentifier Object

## Arguments

[`input` ](#argument-input)· [`deleteUniqueDeviceIdentifierInput` ](/reference/2026-01-01/input-objects/deleteuniquedeviceidentifierinput)· Parameters for deleteUniqueDeviceIdentifier

## Returns

[`deleteUniqueDeviceIdentifierPayload`](/reference/2026-01-01/objects/deleteuniquedeviceidentifierpayload)

## Example

```
mutation deleteUniqueDeviceIdentifier(
  $input: deleteUniqueDeviceIdentifierInput
) {
  deleteUniqueDeviceIdentifier(input: $input) {
    messages
    unique_device_identifier
  }
}
```
