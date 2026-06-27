---
title: PatientLocationInputs | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/patientlocationinputs/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/patientlocationinputs/index.md
---

A location of a patient

## Fields

[`city` ](#field-city)· [`String` ](/reference/2026-01-01/scalars/string)· The city

[`country` ](#field-country)· [`String` ](/reference/2026-01-01/scalars/string)· The country code

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the location

[`line1` ](#field-line1)· [`String` ](/reference/2026-01-01/scalars/string)· The first line of the address

[`line2` ](#field-line2)· [`String` ](/reference/2026-01-01/scalars/string)· The second line of the address

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The graphql\_name of the location

[`state` ](#field-state)· [`String` ](/reference/2026-01-01/scalars/string)· The state

[`zip` ](#field-zip)· [`String` ](/reference/2026-01-01/scalars/string)· The zip code

## Used By

[`createSuperBillInput.patient_location`](/reference/2026-01-01/input-objects/createsuperbillinput)

[`updateSuperBillInput.patient_location`](/reference/2026-01-01/input-objects/updatesuperbillinput)

## Definition

```
"""
A location of a patient
"""
input PatientLocationInputs {
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
  The state
  """
  state: String


  """
  The zip code
  """
  zip: String
}
```
