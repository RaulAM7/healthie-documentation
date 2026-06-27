---
title: ClaimLocation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimlocation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimlocation/index.md
---

Frozen location data from a submitted claim snapshot

## Fields

[`city` ](#field-city)· [`String` ](/reference/2026-01-01/scalars/string)· City

[`country` ](#field-country)· [`String` ](/reference/2026-01-01/scalars/string)· Country

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Location ID

[`line1` ](#field-line1)· [`String` ](/reference/2026-01-01/scalars/string)· Street address line 1

[`line2` ](#field-line2)· [`String` ](/reference/2026-01-01/scalars/string)· Street address line 2

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· Location name

[`npi` ](#field-npi)· [`String` ](/reference/2026-01-01/scalars/string)· Location NPI

[`other_id` ](#field-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· Other ID of the location

[`other_id_qualifier` ](#field-other-id-qualifier)· [`String` ](/reference/2026-01-01/scalars/string)· Other ID qualifier of the location

[`place_of_service` ](#field-place-of-service)· [`ClaimPlaceOfService` ](/reference/2026-01-01/objects/claimplaceofservice)· Place of service

[`place_of_service_code` ](#field-place-of-service-code)· [`String` ](/reference/2026-01-01/scalars/string)· Place of service code

[`state` ](#field-state)· [`String` ](/reference/2026-01-01/scalars/string)· State

[`zip` ](#field-zip)· [`String` ](/reference/2026-01-01/scalars/string)· ZIP code

## Used By

[`Claim.service_location`](/reference/2026-01-01/objects/claim)

[`ClaimPatient.location`](/reference/2026-01-01/objects/claimpatient)

[`ClaimPolicy.payer_location`](/reference/2026-01-01/objects/claimpolicy)

[`ClaimPolicyHolder.location`](/reference/2026-01-01/objects/claimpolicyholder)

[`ClaimProvider.location`](/reference/2026-01-01/objects/claimprovider)

[`ClaimReferringPhysician.location`](/reference/2026-01-01/objects/claimreferringphysician)

## Definition

```
"""
Frozen location data from a submitted claim snapshot
"""
type ClaimLocation {
  """
  City
  """
  city: String


  """
  Country
  """
  country: String


  """
  Location ID
  """
  id: ID


  """
  Street address line 1
  """
  line1: String


  """
  Street address line 2
  """
  line2: String


  """
  Location name
  """
  name: String


  """
  Location NPI
  """
  npi: String


  """
  Other ID of the location
  """
  other_id: String


  """
  Other ID qualifier of the location
  """
  other_id_qualifier: String


  """
  Place of service
  """
  place_of_service: ClaimPlaceOfService


  """
  Place of service code
  """
  place_of_service_code: String


  """
  State
  """
  state: String


  """
  ZIP code
  """
  zip: String
}
```
