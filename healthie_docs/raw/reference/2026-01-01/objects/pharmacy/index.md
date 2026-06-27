---
title: Pharmacy | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/pharmacy/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/pharmacy/index.md
---

A pharmacy generated from Dosespot

## Fields

[`city` ](#field-city)· [`String` ](/reference/2026-01-01/scalars/string)· The city of the address

[`fax_number` ](#field-fax-number)· [`String` ](/reference/2026-01-01/scalars/string)· The fax number of the pharmacy

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the pharmacy

[`latitude` ](#field-latitude)· [`Float` ](/reference/2026-01-01/scalars/float)· latitude coordinate of the pharmacy

[`line1` ](#field-line1)· [`String` ](/reference/2026-01-01/scalars/string)· The first line of the address

[`line2` ](#field-line2)· [`String` ](/reference/2026-01-01/scalars/string)· The second line of the address

[`longitude` ](#field-longitude)· [`Float` ](/reference/2026-01-01/scalars/float)· longitude coordinate of the pharmacy

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the pharmacy

[`ncpdpid` ](#field-ncpdpid)· [`ID` ](/reference/2026-01-01/scalars/id)· The NCPDP ID of the pharmacy

[`phone_number` ](#field-phone-number)· [`String` ](/reference/2026-01-01/scalars/string)· The phone number of the pharmacy

[`service_level` ](#field-service-level)· [`[String!]` ](/reference/2026-01-01/scalars/string)· The service level of the pharmacy

[`specialties` ](#field-specialties)· [`[String!]` ](/reference/2026-01-01/scalars/string)· The specialties of the pharmacy

[`state` ](#field-state)· [`String` ](/reference/2026-01-01/scalars/string)· The state of the address (Uses the 2 letter abbreviation if in US)

[`zip` ](#field-zip)· [`String` ](/reference/2026-01-01/scalars/string)· The zip/postal code of the address

## Used By

[`PharmacyEdge.node`](/reference/2026-01-01/objects/pharmacyedge)

[`PharmacyPaginationConnection.nodes`](/reference/2026-01-01/objects/pharmacypaginationconnection)

[`Prescription.pharmacy`](/reference/2026-01-01/objects/prescription)

[`User.default_pharmacy`](/reference/2026-01-01/objects/user)

[`addPharmacyPayload.pharmacy`](/reference/2026-01-01/objects/addpharmacypayload)

[`Query.pharamcy`](/reference/2026-01-01/queries/pharamcy)

[`Query.pharmacy`](/reference/2026-01-01/queries/pharmacy)

## Definition

```
"""
A pharmacy generated from Dosespot
"""
type Pharmacy {
  """
  The city of the address
  """
  city: String


  """
  The fax number of the pharmacy
  """
  fax_number: String


  """
  The unique identifier of the pharmacy
  """
  id: ID!


  """
  latitude coordinate of the pharmacy
  """
  latitude: Float


  """
  The first line of the address
  """
  line1: String


  """
  The second line of the address
  """
  line2: String


  """
  longitude coordinate of the pharmacy
  """
  longitude: Float


  """
  The name of the pharmacy
  """
  name: String


  """
  The NCPDP ID of the pharmacy
  """
  ncpdpid: ID


  """
  The phone number of the pharmacy
  """
  phone_number: String


  """
  The service level of the pharmacy
  """
  service_level: [String!]


  """
  The specialties of the pharmacy
  """
  specialties: [String!]


  """
  The state of the address (Uses the 2 letter abbreviation if in US)
  """
  state: String


  """
  The zip/postal code of the address
  """
  zip: String
}
```
