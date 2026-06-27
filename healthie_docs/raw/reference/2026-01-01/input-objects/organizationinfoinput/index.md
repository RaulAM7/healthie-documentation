---
title: OrganizationInfoInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/organizationinfoinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/organizationinfoinput/index.md
---

Payload for adding an organization info

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the organization

[`location` ](#field-location)· [`LocationInput` ](/reference/2026-01-01/input-objects/locationinput)· The location of the organization

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The graphql\_name of the organization

[`npi` ](#field-npi)· [`String` ](/reference/2026-01-01/scalars/string)· The NPI of the organization

[`organization_id` ](#field-organization-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the organization

[`other_id` ](#field-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· The other ID of the organization

[`other_id_qual` ](#field-other-id-qual)· [`String` ](/reference/2026-01-01/scalars/string)· The other ID qual of the organization

[`phone_number` ](#field-phone-number)· [`String` ](/reference/2026-01-01/scalars/string)· The phone number of the organization

[`tax_id` ](#field-tax-id)· [`String` ](/reference/2026-01-01/scalars/string)· The tax ID of the organization

[`tax_id_type` ](#field-tax-id-type)· [`String` ](/reference/2026-01-01/scalars/string)· The tax ID type of the organization

## Used By

[`createCms1500Input.organization_info`](/reference/2026-01-01/input-objects/createcms1500input)

[`updateCms1500Input.organization_info`](/reference/2026-01-01/input-objects/updatecms1500input)

## Definition

```
"""
Payload for adding an organization info
"""
input OrganizationInfoInput {
  """
  The ID of the organization
  """
  id: ID


  """
  The location of the organization
  """
  location: LocationInput


  """
  The graphql_name of the organization
  """
  name: String


  """
  The NPI of the organization
  """
  npi: String


  """
  The ID of the organization
  """
  organization_id: ID


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
  The tax ID of the organization
  """
  tax_id: String


  """
  The tax ID type of the organization
  """
  tax_id_type: String
}
```
