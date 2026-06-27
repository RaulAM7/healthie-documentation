---
title: InsuranceAuthorizationInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/insuranceauthorizationinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/insuranceauthorizationinput/index.md
---

Payload for an insurance authorization

## Fields

[`authorization_number` ](#field-authorization-number)· [`String` ](/reference/2026-01-01/scalars/string)· The authorization number

[`end_on` ](#field-end-on)· [`String` ](/reference/2026-01-01/scalars/string)· The end date of the authorization

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the insurance authorization

[`start_on` ](#field-start-on)· [`String` ](/reference/2026-01-01/scalars/string)· The start date of the authorization

[`unit_type` ](#field-unit-type)· [`String` ](/reference/2026-01-01/scalars/string)· The unit type

[`units_authorized` ](#field-units-authorized)· [`String` ](/reference/2026-01-01/scalars/string)· The number of authorized units

[`units_limit_per_visit` ](#field-units-limit-per-visit)· [`String` ](/reference/2026-01-01/scalars/string)· The unit limit per visit

[`units_used` ](#field-units-used)· [`String` ](/reference/2026-01-01/scalars/string)· The number of used units

[`visits_authorized` ](#field-visits-authorized)· [`String` ](/reference/2026-01-01/scalars/string)· The number of authorized visits

[`visits_used` ](#field-visits-used)· [`String` ](/reference/2026-01-01/scalars/string)· The number of used visits

## Used By

[`updatePolicyMutationInput.insurance_authorization`](/reference/2026-01-01/input-objects/updatepolicymutationinput)

## Definition

```
"""
Payload for an insurance authorization
"""
input InsuranceAuthorizationInput {
  """
  The authorization number
  """
  authorization_number: String


  """
  The end date of the authorization
  """
  end_on: String


  """
  The ID of the insurance authorization
  """
  id: ID


  """
  The start date of the authorization
  """
  start_on: String


  """
  The unit type
  """
  unit_type: String


  """
  The number of authorized units
  """
  units_authorized: String


  """
  The unit limit per visit
  """
  units_limit_per_visit: String


  """
  The number of used units
  """
  units_used: String


  """
  The number of authorized visits
  """
  visits_authorized: String


  """
  The number of used visits
  """
  visits_used: String
}
```
