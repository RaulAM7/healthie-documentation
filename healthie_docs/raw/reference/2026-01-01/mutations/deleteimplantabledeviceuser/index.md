---
title: deleteImplantableDeviceUser | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteimplantabledeviceuser/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteimplantabledeviceuser/index.md
---

Delete an Implantable Device User association

## Arguments

[`input` ](#argument-input)· [`deleteImplantableDeviceUserInput` ](/reference/2026-01-01/input-objects/deleteimplantabledeviceuserinput)· Parameters for deleteImplantableDeviceUser

## Returns

[`deleteImplantableDeviceUserPayload`](/reference/2026-01-01/objects/deleteimplantabledeviceuserpayload)

## Example

```
mutation deleteImplantableDeviceUser($input: deleteImplantableDeviceUserInput) {
  deleteImplantableDeviceUser(input: $input) {
    implantable_device_user
    messages
  }
}
```
