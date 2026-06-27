---
title: LocationInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/locationinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/locationinput/index.md
---

Payload for a CMS 1500 location

## Fields

[`city` ](#field-city)· [`String` ](/reference/2026-01-01/scalars/string)· The city

[`country` ](#field-country)· [`String` ](/reference/2026-01-01/scalars/string)· The country code

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the location

[`line1` ](#field-line1)· [`String` ](/reference/2026-01-01/scalars/string)· The first line of the address

[`line2` ](#field-line2)· [`String` ](/reference/2026-01-01/scalars/string)· The second line of the address

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The graphql\_name of the location

[`npi` ](#field-npi)· [`String` ](/reference/2026-01-01/scalars/string)· The NPI of the location

[`other_id` ](#field-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· The other ID of the location

[`other_id_qual` ](#field-other-id-qual)· [`String` ](/reference/2026-01-01/scalars/string)· The other ID qual of the location

[`place_of_service_id` ](#field-place-of-service-id)· [`String` ](/reference/2026-01-01/scalars/string)· The place of service ID of the location

[`state` ](#field-state)· [`String` ](/reference/2026-01-01/scalars/string)· The state

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of user who owns the location

[`zip` ](#field-zip)· [`String` ](/reference/2026-01-01/scalars/string)· The zip code

## Used By

[`OrganizationInfoInput.location`](/reference/2026-01-01/input-objects/organizationinfoinput)

[`PatientInput.location`](/reference/2026-01-01/input-objects/patientinput)

[`PolicyInput.holder_location`](/reference/2026-01-01/input-objects/policyinput)

[`PolicyInput.payer_location`](/reference/2026-01-01/input-objects/policyinput)

[`createCms1500Input.service_location`](/reference/2026-01-01/input-objects/createcms1500input)

[`updateCms1500Input.service_location`](/reference/2026-01-01/input-objects/updatecms1500input)

## Definition

```
"""
Payload for a CMS 1500 location
"""
input LocationInput {
  """
  The city
  """
  city: String


  """
  The country code
  """
  country: String


  """
  The ID of the location
  """
  id: ID


  """
  The first line of the address
  """
  line1: String


  """
  The second line of the address
  """
  line2: String


  """
  The graphql_name of the location
  """
  name: String


  """
  The NPI of the location
  """
  npi: String


  """
  The other ID of the location
  """
  other_id: String


  """
  The other ID qual of the location
  """
  other_id_qual: String


  """
  The place of service ID of the location
  """
  place_of_service_id: String


  """
  The state
  """
  state: String


  """
  The ID of user who owns the location
  """
  user_id: String


  """
  The zip code
  """
  zip: String
}
```
