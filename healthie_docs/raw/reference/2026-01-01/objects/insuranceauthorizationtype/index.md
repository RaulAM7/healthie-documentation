---
title: InsuranceAuthorizationType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/insuranceauthorizationtype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/insuranceauthorizationtype/index.md
---

An insurance authorization

## Fields

[`authorization_number` ](#field-authorization-number)· [`String` ](/reference/2026-01-01/scalars/string)· The authorization number

[`chart_info` ](#field-chart-info)· [`InsuranceAuthorizationChartType` ](/reference/2026-01-01/objects/insuranceauthorizationcharttype)· Chart info for the insurance authorization

[`end_on` ](#field-end-on)· [`String` ](/reference/2026-01-01/scalars/string)· The day that visits authorized by the insurance company have no effect

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the authorization

[`start_on` ](#field-start-on)· [`String` ](/reference/2026-01-01/scalars/string)· The day that visits authorized by the insurance company take effect

[`unit_type` ](#field-unit-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of units (visits, units, hours)

[`units_authorized` ](#field-units-authorized)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of units authorized by the insurance company

[`units_left` ](#field-units-left)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of units left

[`units_limit_per_visit` ](#field-units-limit-per-visit)· [`String` ](/reference/2026-01-01/scalars/string)· Most units/hours allowed per visit

[`units_used` ](#field-units-used)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of units used by the client

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Most recent date authorization was updated

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the user for whom the authorization was created

[`visits_authorized` ](#field-visits-authorized)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of units authorized by the insurance company

[`visits_left` ](#field-visits-left)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of units left

[`visits_used` ](#field-visits-used)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of units used by the client

## Used By

[`Policy.insurance_authorization`](/reference/2026-01-01/objects/policy)

[`User.insurance_authorization`](/reference/2026-01-01/objects/user)

[`createInsuranceAuthorizationPayload.insuranceAuthorization`](/reference/2026-01-01/objects/createinsuranceauthorizationpayload)

[`deleteInsuranceAuthorizationPayload.insuranceAuthorization`](/reference/2026-01-01/objects/deleteinsuranceauthorizationpayload)

[`updateInsuranceAuthorizationPayload.insuranceAuthorization`](/reference/2026-01-01/objects/updateinsuranceauthorizationpayload)

[`Query.insuranceAuthorization`](/reference/2026-01-01/queries/insuranceauthorization)

## Definition

```
"""
An insurance authorization
"""
type InsuranceAuthorizationType {
  """
  The authorization number
  """
  authorization_number: String


  """
  Chart info for the insurance authorization
  """
  chart_info: InsuranceAuthorizationChartType


  """
  The day that visits authorized by the insurance company have no effect
  """
  end_on: String


  """
  The unique identifier of the authorization
  """
  id: ID!


  """
  The day that visits authorized by the insurance company take effect
  """
  start_on: String


  """
  The type of units (visits, units, hours)
  """
  unit_type: String


  """
  The amount of units authorized by the insurance company
  """
  units_authorized: String


  """
  The amount of units left
  """
  units_left: String


  """
  Most units/hours allowed per visit
  """
  units_limit_per_visit: String


  """
  The amount of units used by the client
  """
  units_used: String


  """
  Most recent date authorization was updated
  """
  updated_at: ISO8601DateTime


  """
  The ID of the user for whom the authorization was created
  """
  user_id: ID


  """
  The amount of units authorized by the insurance company
  """
  visits_authorized: String


  """
  The amount of units left
  """
  visits_left: String


  """
  The amount of units used by the client
  """
  visits_used: String
}
```
