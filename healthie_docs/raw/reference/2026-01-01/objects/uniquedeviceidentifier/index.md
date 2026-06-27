---
title: UniqueDeviceIdentifier | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/uniquedeviceidentifier/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/uniquedeviceidentifier/index.md
---

UniqueDeviceIdentifier object

## Fields

[`assigning_authority` ](#field-assigning-authority)· [`String` ](/reference/2026-01-01/scalars/string)· The assigning authority for the device code

[`device_code` ](#field-device-code)· [`String` ](/reference/2026-01-01/scalars/string)· The device code

[`display_name` ](#field-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· The display name for the device code

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the identifier

[`scoping_entity` ](#field-scoping-entity)· [`String` ](/reference/2026-01-01/scalars/string)· The scoping entity for the device code

[`udi_code` ](#field-udi-code)· [`String` ](/reference/2026-01-01/scalars/string)· The UDI code for the device

## Used By

[`createUniqueDeviceIdentifierPayload.unique_device_identifier`](/reference/2026-01-01/objects/createuniquedeviceidentifierpayload)

[`deleteUniqueDeviceIdentifierPayload.unique_device_identifier`](/reference/2026-01-01/objects/deleteuniquedeviceidentifierpayload)

[`updateUniqueDeviceIdentifierPayload.unique_device_identifier`](/reference/2026-01-01/objects/updateuniquedeviceidentifierpayload)

## Definition

```
"""
UniqueDeviceIdentifier object
"""
type UniqueDeviceIdentifier {
  """
  The assigning authority for the device code
  """
  assigning_authority: String


  """
  The device code
  """
  device_code: String


  """
  The display name for the device code
  """
  display_name: String


  """
  The unique identifier of the identifier
  """
  id: ID!


  """
  The scoping entity for the device code
  """
  scoping_entity: String


  """
  The UDI code for the device
  """
  udi_code: String
}
```
