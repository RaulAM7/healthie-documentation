---
title: ReferringPhysicianInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/referringphysicianinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/referringphysicianinput/index.md
---

Payload for a referring physician

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the referring physician will be deleted

[`email` ](#field-email)· [`String` ](/reference/2026-01-01/scalars/string)· The email of the referring physician

[`fax_number` ](#field-fax-number)· [`String` ](/reference/2026-01-01/scalars/string)· The fax number of the referring physician

[`first_name` ](#field-first-name)· [`String` ](/reference/2026-01-01/scalars/string)· The first name of the referring physician

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the referring physician

[`last_name` ](#field-last-name)· [`String` ](/reference/2026-01-01/scalars/string)· The last name of the referring physician

[`legalname` ](#field-legalname)· [`String` ](/reference/2026-01-01/scalars/string)· The legal name of the referring physician

[`location` ](#field-location)· [`ClientLocationInput` ](/reference/2026-01-01/input-objects/clientlocationinput)· The location of the referring physician

[`npi` ](#field-npi)· [`String` ](/reference/2026-01-01/scalars/string)· The NPI of the referring physician

[`phone_number` ](#field-phone-number)· [`String` ](/reference/2026-01-01/scalars/string)· The phone number of the referring physician

## Used By

[`ReferralInput.referring_physician`](/reference/2026-01-01/input-objects/referralinput)

## Definition

```
"""
Payload for a referring physician
"""
input ReferringPhysicianInput {
  """
  If true, the referring physician will be deleted
  """
  _destroy: Boolean


  """
  The email of the referring physician
  """
  email: String


  """
  The fax number of the referring physician
  """
  fax_number: String


  """
  The first name of the referring physician
  """
  first_name: String


  """
  The ID of the referring physician
  """
  id: ID


  """
  The last name of the referring physician
  """
  last_name: String


  """
  The legal name of the referring physician
  """
  legalname: String


  """
  The location of the referring physician
  """
  location: ClientLocationInput


  """
  The NPI of the referring physician
  """
  npi: String


  """
  The phone number of the referring physician
  """
  phone_number: String
}
```
