---
title: createImplantableDeviceUser | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createimplantabledeviceuser/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createimplantabledeviceuser/index.md
---

Create Implantable Device User association

## Arguments

[`input` ](#argument-input)· [`createImplantableDeviceUserInput` ](/reference/2026-01-01/input-objects/createimplantabledeviceuserinput)· Parameters for createImplantableDeviceUser

## Returns

[`createImplantableDeviceUserPayload`](/reference/2026-01-01/objects/createimplantabledeviceuserpayload)

## Example

```
mutation createImplantableDeviceUser($input: createImplantableDeviceUserInput) {
  createImplantableDeviceUser(input: $input) {
    implantable_device_user
    messages
  }
}
```
