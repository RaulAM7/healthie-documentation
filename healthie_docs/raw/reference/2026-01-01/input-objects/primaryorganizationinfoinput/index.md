---
title: PrimaryOrganizationInfoInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/primaryorganizationinfoinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/primaryorganizationinfoinput/index.md
---

Payload for a primary organization

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the organization will be deleted

[`external_id` ](#field-external-id)· [`String` ](/reference/2026-01-01/scalars/string)· The external ID of the organization

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the organization

[`id_number_type` ](#field-id-number-type)· [`String` ](/reference/2026-01-01/scalars/string)· The ID number type of the organization

[`location` ](#field-location)· [`OrgLocationInput` ](/reference/2026-01-01/input-objects/orglocationinput)· The location of the organization

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The graphql\_name of the organization

[`npi` ](#field-npi)· [`String` ](/reference/2026-01-01/scalars/string)· The NPI of the organization

[`other_id` ](#field-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· The other ID of the organization

[`other_id_qual` ](#field-other-id-qual)· [`String` ](/reference/2026-01-01/scalars/string)· The other ID qual of the organization

[`phone_number` ](#field-phone-number)· [`String` ](/reference/2026-01-01/scalars/string)· The phone number of the organization

[`primary` ](#field-primary)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the organization is primary

[`tax_id` ](#field-tax-id)· [`String` ](/reference/2026-01-01/scalars/string)· The tax ID of the organization

[`tax_id_type` ](#field-tax-id-type)· [`String` ](/reference/2026-01-01/scalars/string)· The tax ID type of the organization

## Used By

[`createOrganizationInput.organization_info`](/reference/2026-01-01/input-objects/createorganizationinput)

[`updateOrganizationInput.organization_info`](/reference/2026-01-01/input-objects/updateorganizationinput)

## Definition

```
"""
Payload for a primary organization
"""
input PrimaryOrganizationInfoInput {
  """
  If true, the organization will be deleted
  """
  _destroy: Boolean


  """
  The external ID of the organization
  """
  external_id: String


  """
  The ID of the organization
  """
  id: ID


  """
  The ID number type of the organization
  """
  id_number_type: String


  """
  The location of the organization
  """
  location: OrgLocationInput


  """
  The graphql_name of the organization
  """
  name: String


  """
  The NPI of the organization
  """
  npi: String


  """
  The other ID of the organization
  """
  other_id: String


  """
  The other ID qual of the organization
  """
  other_id_qual: String


  """
  The phone number of the organization
  """
  phone_number: String


  """
  Whether the organization is primary
  """
  primary: Boolean


  """
  The tax ID of the organization
  """
  tax_id: String


  """
  The tax ID type of the organization
  """
  tax_id_type: String
}
```
