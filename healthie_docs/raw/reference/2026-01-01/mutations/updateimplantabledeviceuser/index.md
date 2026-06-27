---
title: updateImplantableDeviceUser | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateimplantabledeviceuser/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateimplantabledeviceuser/index.md
---

Update Implantable Device User association

## Arguments

[`input` ](#argument-input)· [`updateImplantableDeviceUserInput` ](/reference/2026-01-01/input-objects/updateimplantabledeviceuserinput)· Parameters for updateImplantableDeviceUser

## Returns

[`updateImplantableDeviceUserPayload`](/reference/2026-01-01/objects/updateimplantabledeviceuserpayload)

## Example

```
mutation updateImplantableDeviceUser($input: updateImplantableDeviceUserInput) {
  updateImplantableDeviceUser(input: $input) {
    implantable_device_user
    messages
  }
}
```
