---
title: ImplantableDevice | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/implantabledevice/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/implantabledevice/index.md
---

An implantable device

## Fields

[`brand_name` ](#field-brand-name)· [`String` ](/reference/2026-01-01/scalars/string)· Brand name of the implantable device.

[`company_name` ](#field-company-name)· [`String` ](/reference/2026-01-01/scalars/string)· Name of the company that manufactures the implantable device.

[`created_at` ](#field-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· A string representation of the date/time when the device record was created in the database.

[`device_id` ](#field-device-id)· [`String` ](/reference/2026-01-01/scalars/string)· A unique identifier assigned to the device.

[`device_id_issuing_agency` ](#field-device-id-issuing-agency)· [`String` ](/reference/2026-01-01/scalars/string)· The agency that issued the device identifier.

[`duns_number` ](#field-duns-number)· [`String` ](/reference/2026-01-01/scalars/string)· Dun & Bradstreet number (DUNS number) is a unique nine-digit identifier for businesses.

[`gmdn_terms` ](#field-gmdn-terms)· [`String` ](/reference/2026-01-01/scalars/string)· Global Medical Device Nomenclature (GMDN) terms, a system of internationally agreed generic descriptors used to identify all medical device products.

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the implantable device type

[`labeled_contains_nrl` ](#field-labeled-contains-nrl)· [`String` ](/reference/2026-01-01/scalars/string)· Whether the device contains natural rubber latex or not.

[`mri_safety_status` ](#field-mri-safety-status)· [`String` ](/reference/2026-01-01/scalars/string)· Status of the device's safety in an MRI environment (e.g., safe, conditional, unsafe).

[`public_device_record_key` ](#field-public-device-record-key)· [`String` ](/reference/2026-01-01/scalars/string)· Key of the device's public record.

[`public_version_date` ](#field-public-version-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date when the public version of the device record was created or updated.

[`public_version_number` ](#field-public-version-number)· [`String` ](/reference/2026-01-01/scalars/string)· Version number of the public device record.

[`public_version_status` ](#field-public-version-status)· [`String` ](/reference/2026-01-01/scalars/string)· Status of the public version of the device record (e.g., active, retired).

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· A string representation of the date/time when the device record was last updated in the database.

[`version_model_number` ](#field-version-model-number)· [`String` ](/reference/2026-01-01/scalars/string)· Version or model number of the device.

## Used By

[`ImplantableDeviceUser.implantable_device`](/reference/2026-01-01/objects/implantabledeviceuser)

## Definition

```
"""
An implantable device
"""
type ImplantableDevice {
  """
  Brand name of the implantable device.
  """
  brand_name: String


  """
  Name of the company that manufactures the implantable device.
  """
  company_name: String


  """
  A string representation of the date/time when the device record was created in the database.
  """
  created_at: ISO8601DateTime


  """
  A unique identifier assigned to the device.
  """
  device_id: String


  """
  The agency that issued the device identifier.
  """
  device_id_issuing_agency: String


  """
  Dun & Bradstreet number (DUNS number) is a unique nine-digit identifier for businesses.
  """
  duns_number: String


  """
  Global Medical Device Nomenclature (GMDN) terms, a system of internationally agreed generic descriptors used to identify all medical device products.
  """
  gmdn_terms: String


  """
  The unique identifier of the implantable device type
  """
  id: ID!


  """
  Whether the device contains natural rubber latex or not.
  """
  labeled_contains_nrl: String


  """
  Status of the device's safety in an MRI environment (e.g., safe, conditional, unsafe).
  """
  mri_safety_status: String


  """
  Key of the device's public record.
  """
  public_device_record_key: String


  """
  Date when the public version of the device record was created or updated.
  """
  public_version_date: ISO8601DateTime


  """
  Version number of the public device record.
  """
  public_version_number: String


  """
  Status of the public version of the device record (e.g., active, retired).
  """
  public_version_status: String


  """
  A string representation of the date/time when the device record was last updated in the database.
  """
  updated_at: ISO8601DateTime


  """
  Version or model number of the device.
  """
  version_model_number: String
}
```
