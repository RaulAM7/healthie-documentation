---
title: OrganizationInfo | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationinfo/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationinfo/index.md
---

Specific information for an organization

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The creation date of the organization

[`external_id` ](#field-external-id)· [`String` ](/reference/2026-01-01/scalars/string)· The External ID of the organization

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the organization info

[`id_number_type` ](#field-id-number-type)· [`String` ](/reference/2026-01-01/scalars/string)· The number type ID of the organization

[`location` ](#field-location)· [`Location` ](/reference/2026-01-01/objects/location)· The location of the organization

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the organization

[`npi` ](#field-npi)· [`String` ](/reference/2026-01-01/scalars/string)· The NPI of the organization

[`organization` ](#field-organization)· [`Organization` ](/reference/2026-01-01/objects/organization)· The associated organization

[`other_id` ](#field-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· The other id

[`other_id_qual` ](#field-other-id-qual)· [`String` ](/reference/2026-01-01/scalars/string)· The other ID qualifier (what type of ID it is)

[`phone_number` ](#field-phone-number)· [`String` ](/reference/2026-01-01/scalars/string)· The phone number of the organization

[`primary` ](#field-primary)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Set billing provider as primary

[`tax_id` ](#field-tax-id)· [`String` ](/reference/2026-01-01/scalars/string)· The tax id of the organization

[`tax_id_type` ](#field-tax-id-type)· [`String` ](/reference/2026-01-01/scalars/string)· The tax id type of the organization

## Used By

[`Claim.org_info`](/reference/2026-01-01/objects/claim)

[`Cms1500.org_info`](/reference/2026-01-01/objects/cms1500)

[`Organization.organization_info`](/reference/2026-01-01/objects/organization)

[`OrganizationInfoEdge.node`](/reference/2026-01-01/objects/organizationinfoedge)

[`OrganizationInfoPaginationConnection.nodes`](/reference/2026-01-01/objects/organizationinfopaginationconnection)

[`deleteOrganizationInfoPayload.organizationInfo`](/reference/2026-01-01/objects/deleteorganizationinfopayload)

[`updateOrganizationPayload.updated_organization_info`](/reference/2026-01-01/objects/updateorganizationpayload)

[`Query.organizationInfo`](/reference/2026-01-01/queries/organizationinfo)

## Definition

```
"""
Specific information for an organization
"""
type OrganizationInfo {
  """
  The creation date of the organization
  """
  created_at: ISO8601DateTime!


  """
  The External ID of the organization
  """
  external_id: String


  """
  The unique identifier of the organization info
  """
  id: ID!


  """
  The number type ID of the organization
  """
  id_number_type: String


  """
  The location of the organization
  """
  location: Location


  """
  The name of the organization
  """
  name: String


  """
  The NPI of the organization
  """
  npi: String


  """
  The associated organization
  """
  organization: Organization


  """
  The other id
  """
  other_id: String


  """
  The other ID qualifier (what type of ID it is)
  """
  other_id_qual: String


  """
  The phone number of the organization
  """
  phone_number: String


  """
  Set billing provider as primary
  """
  primary: Boolean


  """
  The tax id of the organization
  """
  tax_id: String


  """
  The tax id type of the organization
  """
  tax_id_type: String
}
```
