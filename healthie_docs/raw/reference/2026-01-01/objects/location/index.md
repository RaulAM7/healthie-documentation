---
title: Location | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/location/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/location/index.md
---

A location

## Fields

[`city` ](#field-city)· [`String` ](/reference/2026-01-01/scalars/string)· The city of the address

[`country` ](#field-country)· [`String` ](/reference/2026-01-01/scalars/string)· The Country Code of the address

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the location

[`line1` ](#field-line1)· [`String` ](/reference/2026-01-01/scalars/string)· The first line of the address

[`line2` ](#field-line2)· [`String` ](/reference/2026-01-01/scalars/string)· The second line of the address

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the location

[`npi` ](#field-npi)· [`String` ](/reference/2026-01-01/scalars/string)· The NPI of the location

[`other_id` ](#field-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· The Other ID of the location

[`other_id_qual` ](#field-other-id-qual)· [`String` ](/reference/2026-01-01/scalars/string)· The Other ID Qualification of the location

[`place_of_service` ](#field-place-of-service)· [`PlaceOfService` ](/reference/2026-01-01/objects/placeofservice)· The place of service associated with this location

[`place_of_service_id` ](#field-place-of-service-id)· [`String` ](/reference/2026-01-01/scalars/string)· The place of service id of the location

[`state` ](#field-state)· [`String` ](/reference/2026-01-01/scalars/string)· The state of the address (Uses the 2 letter abbreviation if in US)

[`to_oneline` ](#field-to-oneline)· [`String` ](/reference/2026-01-01/scalars/string)· The location condensed to a single line

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· Owner of this location

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the user

[`zip` ](#field-zip)· [`String` ](/reference/2026-01-01/scalars/string)· The zip/postal code of the address

## Used By

[`Cms1500.service_location`](/reference/2026-01-01/objects/cms1500)

[`InsurancePlan.default_payer_location`](/reference/2026-01-01/objects/insuranceplan)

[`LocationEdge.node`](/reference/2026-01-01/objects/locationedge)

[`LocationPaginationConnection.nodes`](/reference/2026-01-01/objects/locationpaginationconnection)

[`Organization.location`](/reference/2026-01-01/objects/organization)

[`OrganizationInfo.location`](/reference/2026-01-01/objects/organizationinfo)

[`Policy.holder_location`](/reference/2026-01-01/objects/policy)

[`Policy.payer_location`](/reference/2026-01-01/objects/policy)

[`ReferringPhysician.location`](/reference/2026-01-01/objects/referringphysician)

[`SuperBill.location`](/reference/2026-01-01/objects/superbill)

[`SuperBill.patient_location`](/reference/2026-01-01/objects/superbill)

[`User.location`](/reference/2026-01-01/objects/user)

[`User.locations`](/reference/2026-01-01/objects/user)

[`User.super_bill_location`](/reference/2026-01-01/objects/user)

[`User.super_bill_patient_location`](/reference/2026-01-01/objects/user)

[`createLocationPayload.location`](/reference/2026-01-01/objects/createlocationpayload)

[`deleteLocationPayload.location`](/reference/2026-01-01/objects/deletelocationpayload)

[`updateLocationPayload.location`](/reference/2026-01-01/objects/updatelocationpayload)

[`Query.location`](/reference/2026-01-01/queries/location)

## Definition

```
"""
A location
"""
type Location {
  """
  The city of the address
  """
  city: String


  """
  The Country Code of the address
  """
  country: String


  """
  The unique identifier of the location
  """
  id: ID!


  """
  The first line of the address
  """
  line1: String


  """
  The second line of the address
  """
  line2: String


  """
  The name of the location
  """
  name: String


  """
  The NPI of the location
  """
  npi: String


  """
  The Other ID of the location
  """
  other_id: String


  """
  The Other ID Qualification of the location
  """
  other_id_qual: String


  """
  The place of service associated with this location
  """
  place_of_service: PlaceOfService


  """
  The place of service id of the location
  """
  place_of_service_id: String


  """
  The state of the address (Uses the 2 letter abbreviation if in US)
  """
  state: String


  """
  The location condensed to a single line
  """
  to_oneline: String


  """
  Owner of this location
  """
  user: User


  """
  The ID of the user
  """
  user_id: String


  """
  The zip/postal code of the address
  """
  zip: String
}
```
