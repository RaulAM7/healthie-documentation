---
title: createUniqueDeviceIdentifier | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createuniquedeviceidentifier/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createuniquedeviceidentifier/index.md
---

Create a UniqueDeviceIdentifier Object

## Arguments

[`input` ](#argument-input)· [`createUniqueDeviceIdentifierInput` ](/reference/2026-01-01/input-objects/createuniquedeviceidentifierinput)· Parameters for createUniqueDeviceIdentifier

## Returns

[`createUniqueDeviceIdentifierPayload`](/reference/2026-01-01/objects/createuniquedeviceidentifierpayload)

## Example

```
mutation createUniqueDeviceIdentifier(
  $input: createUniqueDeviceIdentifierInput
) {
  createUniqueDeviceIdentifier(input: $input) {
    messages
    unique_device_identifier
  }
}
```
