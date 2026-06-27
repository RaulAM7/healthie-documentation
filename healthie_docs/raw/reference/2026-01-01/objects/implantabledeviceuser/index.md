---
title: ImplantableDeviceUser | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/implantabledeviceuser/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/implantabledeviceuser/index.md
---

An Implantable Device User

## Fields

[`active` ](#field-active)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· A boolean value representing if the Implantable Device is currently active.

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Unique identifier for the Implantable Device User connection record.

[`implantable_device` ](#field-implantable-device)· [`ImplantableDevice` ](/reference/2026-01-01/objects/implantabledevice)· Details of the Implantable Device.

[`implantable_device_id` ](#field-implantable-device-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Unique identifier for the associated Implantable Device record.

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· User provided name for the Implantable Device.

[`udi` ](#field-udi)· [`String` ](/reference/2026-01-01/scalars/string)· Recorded UDI for this associated Implantable Device User record.

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· User associated with the Implantable Device, including all User details.

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Unique identifier for the associated User record.

## Used By

[`User.implantable_devices_users`](/reference/2026-01-01/objects/user)

[`createImplantableDeviceUserPayload.implantable_device_user`](/reference/2026-01-01/objects/createimplantabledeviceuserpayload)

[`deleteImplantableDeviceUserPayload.implantable_device_user`](/reference/2026-01-01/objects/deleteimplantabledeviceuserpayload)

[`updateImplantableDeviceUserPayload.implantable_device_user`](/reference/2026-01-01/objects/updateimplantabledeviceuserpayload)

## Definition

```
"""
An Implantable Device User
"""
type ImplantableDeviceUser {
  """
  A boolean value representing if the Implantable Device is currently active.
  """
  active: Boolean


  """
  Unique identifier for the Implantable Device User connection record.
  """
  id: ID


  """
  Details of the Implantable Device.
  """
  implantable_device: ImplantableDevice


  """
  Unique identifier for the associated Implantable Device record.
  """
  implantable_device_id: ID


  """
  User provided name for the Implantable Device.
  """
  name: String


  """
  Recorded UDI for this associated Implantable Device User record.
  """
  udi: String


  """
  User associated with the Implantable Device, including all User details.
  """
  user: User


  """
  Unique identifier for the associated User record.
  """
  user_id: ID
}
```
