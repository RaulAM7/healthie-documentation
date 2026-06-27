---
title: OrganizationCptCodeType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationcptcodetype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationcptcodetype/index.md
---

OrganizationCptCode object

## Fields

[`cpt_code_id` ](#field-cpt-code-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The CPT code id

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · date created

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the join

[`organization_cpt_code_insurance_fees` ](#field-organization-cpt-code-insurance-fees)· [`[OrganizationCptCodeInsuranceFeeType!]` ](/reference/2026-01-01/objects/organizationcptcodeinsurancefeetype)· Returns specific insurance fees associated with organization cpt codes

[`organization_cpt_code_insurance_fees_count` ](#field-organization-cpt-code-insurance-fees-count)· [`String` ](/reference/2026-01-01/scalars/string)· Total insurance fees associated with the organization cpt code

[`organization_id` ](#field-organization-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The organization id

[`price_per_unit` ](#field-price-per-unit)· [`String` ](/reference/2026-01-01/scalars/string)· The price per unit

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · date updated

## Used By

[`Organization.organization_cpt_codes`](/reference/2026-01-01/objects/organization)

[`createOrganizationCptCodePayload.organization_cpt_code`](/reference/2026-01-01/objects/createorganizationcptcodepayload)

[`deleteOrganizationCptCodePayload.organization_cpt_code`](/reference/2026-01-01/objects/deleteorganizationcptcodepayload)

[`updateOrganizationCptCodePayload.organization_cpt_code`](/reference/2026-01-01/objects/updateorganizationcptcodepayload)

[`Query.organizationCptCode`](/reference/2026-01-01/queries/organizationcptcode)

## Definition

```
"""
OrganizationCptCode object
"""
type OrganizationCptCodeType {
  """
  The CPT code id
  """
  cpt_code_id: ID!


  """
  date created
  """
  created_at: ISO8601DateTime!


  """
  The unique identifier of the join
  """
  id: ID!


  """
  Returns specific insurance fees associated with organization cpt codes
  """
  organization_cpt_code_insurance_fees: [OrganizationCptCodeInsuranceFeeType!]


  """
  Total insurance fees associated with the organization cpt code
  """
  organization_cpt_code_insurance_fees_count: String


  """
  The organization id
  """
  organization_id: ID!


  """
  The price per unit
  """
  price_per_unit: String


  """
  date updated
  """
  updated_at: ISO8601DateTime!
}
```
