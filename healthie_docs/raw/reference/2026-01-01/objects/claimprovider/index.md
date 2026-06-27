---
title: ClaimProvider | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimprovider/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimprovider/index.md
---

Frozen provider data from a submitted claim snapshot

## Fields

[`first_name` ](#field-first-name)· [`String` ](/reference/2026-01-01/scalars/string)· First name

[`full_legal_name` ](#field-full-legal-name)· [`String` ](/reference/2026-01-01/scalars/string)· Full legal name

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Provider ID

[`last_name` ](#field-last-name)· [`String` ](/reference/2026-01-01/scalars/string)· Last name

[`location` ](#field-location)· [`ClaimLocation` ](/reference/2026-01-01/objects/claimlocation)· Address at time of submission

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· Provider or organization name

[`npi` ](#field-npi)· [`String` ](/reference/2026-01-01/scalars/string)· National Provider Identifier

[`organization_name` ](#field-organization-name)· [`String` ](/reference/2026-01-01/scalars/string)· Organization name

[`other_id` ](#field-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· Other ID

[`other_id_qualifier` ](#field-other-id-qualifier)· [`String` ](/reference/2026-01-01/scalars/string)· Other ID qualifier

[`phone_number` ](#field-phone-number)· [`String` ](/reference/2026-01-01/scalars/string)· Phone number

[`primary` ](#field-primary)· [`String` ](/reference/2026-01-01/scalars/string)· Primary contact name

[`qualifications` ](#field-qualifications)· [`String` ](/reference/2026-01-01/scalars/string)· Provider qualifications

[`rendering_provider_other_id_number` ](#field-rendering-provider-other-id-number)· [`ClaimOtherIdNumber` ](/reference/2026-01-01/objects/claimotheridnumber)· Claim-specific other ID number

[`tax_id` ](#field-tax-id)· [`String` ](/reference/2026-01-01/scalars/string)· Tax ID

[`taxonomy_code` ](#field-taxonomy-code)· [`String` ](/reference/2026-01-01/scalars/string)· Taxonomy code

## Used By

[`Claim.billing_provider`](/reference/2026-01-01/objects/claim)

[`Claim.referring_provider`](/reference/2026-01-01/objects/claim)

[`Claim.rendering_provider`](/reference/2026-01-01/objects/claim)

## Definition

```
"""
Frozen provider data from a submitted claim snapshot
"""
type ClaimProvider {
  """
  First name
  """
  first_name: String


  """
  Full legal name
  """
  full_legal_name: String


  """
  Provider ID
  """
  id: ID


  """
  Last name
  """
  last_name: String


  """
  Address at time of submission
  """
  location: ClaimLocation


  """
  Provider or organization name
  """
  name: String


  """
  National Provider Identifier
  """
  npi: String


  """
  Organization name
  """
  organization_name: String


  """
  Other ID
  """
  other_id: String


  """
  Other ID qualifier
  """
  other_id_qualifier: String


  """
  Phone number
  """
  phone_number: String


  """
  Primary contact name
  """
  primary: String


  """
  Provider qualifications
  """
  qualifications: String


  """
  Claim-specific other ID number
  """
  rendering_provider_other_id_number: ClaimOtherIdNumber


  """
  Tax ID
  """
  tax_id: String


  """
  Taxonomy code
  """
  taxonomy_code: String
}
```
