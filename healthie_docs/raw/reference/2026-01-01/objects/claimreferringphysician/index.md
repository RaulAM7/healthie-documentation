---
title: ClaimReferringPhysician | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimreferringphysician/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimreferringphysician/index.md
---

Frozen referring physician data from a submitted claim snapshot

## Fields

[`accepts_insurance` ](#field-accepts-insurance)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the physician accepts insurance

[`business_name` ](#field-business-name)· [`String` ](/reference/2026-01-01/scalars/string)· Business name

[`email` ](#field-email)· [`String` ](/reference/2026-01-01/scalars/string)· Email

[`fax_number` ](#field-fax-number)· [`String` ](/reference/2026-01-01/scalars/string)· Fax number

[`first_name` ](#field-first-name)· [`String` ](/reference/2026-01-01/scalars/string)· First name

[`full_name` ](#field-full-name)· [`String` ](/reference/2026-01-01/scalars/string)· Full name

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Referring physician ID

[`last_name` ](#field-last-name)· [`String` ](/reference/2026-01-01/scalars/string)· Last name

[`location` ](#field-location)· [`ClaimLocation` ](/reference/2026-01-01/objects/claimlocation)· Location at time of submission

[`notes` ](#field-notes)· [`String` ](/reference/2026-01-01/scalars/string)· Notes

[`npi` ](#field-npi)· [`String` ](/reference/2026-01-01/scalars/string)· National Provider Identifier

[`other_id` ](#field-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· Other ID

[`other_id_qualifier` ](#field-other-id-qualifier)· [`String` ](/reference/2026-01-01/scalars/string)· Other ID qualifier

[`phone_number` ](#field-phone-number)· [`String` ](/reference/2026-01-01/scalars/string)· Phone number

[`speciality` ](#field-speciality)· [`String` ](/reference/2026-01-01/scalars/string)· Speciality

[`website` ](#field-website)· [`String` ](/reference/2026-01-01/scalars/string)· Website

## Used By

[`ClaimReferralInfo.referring_physician`](/reference/2026-01-01/objects/claimreferralinfo)

## Definition

```
"""
Frozen referring physician data from a submitted claim snapshot
"""
type ClaimReferringPhysician {
  """
  Whether the physician accepts insurance
  """
  accepts_insurance: Boolean


  """
  Business name
  """
  business_name: String


  """
  Email
  """
  email: String


  """
  Fax number
  """
  fax_number: String


  """
  First name
  """
  first_name: String


  """
  Full name
  """
  full_name: String


  """
  Referring physician ID
  """
  id: ID


  """
  Last name
  """
  last_name: String


  """
  Location at time of submission
  """
  location: ClaimLocation


  """
  Notes
  """
  notes: String


  """
  National Provider Identifier
  """
  npi: String


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
  Speciality
  """
  speciality: String


  """
  Website
  """
  website: String
}
```
