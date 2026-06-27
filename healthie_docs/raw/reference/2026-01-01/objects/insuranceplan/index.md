---
title: InsurancePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/insuranceplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/insuranceplan/index.md
---

An Insurance Plan

## Fields

[`change_healthcare_eligibility_payer_id` ](#field-change-healthcare-eligibility-payer-id)· [`String` ](/reference/2026-01-01/scalars/string)· The Eligibility Payer ID for eligibility requests in Change that this maps to

deprecated

ChangeHealth integration has been discontinued.

[`change_healthcare_payer_id` ](#field-change-healthcare-payer-id)· [`String` ](/reference/2026-01-01/scalars/string)· The Payer ID for claims requests in Change that this maps to

deprecated

ChangeHealth claims integration has been discontinued.

[`default_payer_location` ](#field-default-payer-location)· [`Location` ](/reference/2026-01-01/objects/location)· Location of the first policy associated to the current user and insurance plan

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the plan

[`is_accepted` ](#field-is-accepted)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Insurance Plan marked as accepted

[`is_custom` ](#field-is-custom)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Insurance plan marked as custom

[`is_in_fee_schedules` ](#field-is-in-fee-schedules)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not this insurance plan is associated with fee schedule for the logged in user.

[`metadata` ](#field-metadata)· [`JSON` ](/reference/2026-01-01/scalars/json)· A serialized JSON string of metadata. Maximum character limit of 2,000.

[`name_and_id` ](#field-name-and-id)· [`String` ](/reference/2026-01-01/scalars/string)· A combined string to use for labels

[`payer_id` ](#field-payer-id)· [`String` ](/reference/2026-01-01/scalars/string)· The Payer ID of the insurance plan

[`payer_name` ](#field-payer-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the insurance plan

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· Owner of this insurance plan

deprecated

Insurance Plans do not have an associated user

## Used By

[`AcceptedInsurancePlan.insurance_plan`](/reference/2026-01-01/objects/acceptedinsuranceplan)

[`ClientSource.related_insurance`](/reference/2026-01-01/objects/clientsource)

[`InsurancePlanEdge.node`](/reference/2026-01-01/objects/insuranceplanedge)

[`InsurancePlanPaginationConnection.nodes`](/reference/2026-01-01/objects/insuranceplanpaginationconnection)

[`Organization.insurance_plans_used_by_organization_providers`](/reference/2026-01-01/objects/organization)

[`OrganizationCptCodeInsuranceFeeType.insurance_plan`](/reference/2026-01-01/objects/organizationcptcodeinsurancefeetype)

[`Policy.insurance_plan`](/reference/2026-01-01/objects/policy)

[`createInsurancePlanPayload.insurance_plan`](/reference/2026-01-01/objects/createinsuranceplanpayload)

[`deleteInsurancePlanPayload.insurance_plan`](/reference/2026-01-01/objects/deleteinsuranceplanpayload)

[`updateInsurancePlanPayload.insurance_plan`](/reference/2026-01-01/objects/updateinsuranceplanpayload)

## Definition

```
"""
An Insurance Plan
"""
type InsurancePlan {
  """
  The Eligibility Payer ID for eligibility requests in Change that this maps to
  """
  change_healthcare_eligibility_payer_id: String
    @deprecated(reason: "ChangeHealth integration has been discontinued.")


  """
  The Payer ID for claims requests in Change that this maps to
  """
  change_healthcare_payer_id: String
    @deprecated(
      reason: "ChangeHealth claims integration has been discontinued."
    )


  """
  Location of the first policy associated to the current user and insurance plan
  """
  default_payer_location(
    """
    Array of plan ids
    """
    ids: String
  ): Location


  """
  The unique identifier of the plan
  """
  id: ID!


  """
  Insurance Plan marked as accepted
  """
  is_accepted(
    """
    The known value of is_accepted (from the query argument)
    """
    known_value: Boolean
  ): Boolean


  """
  Insurance plan marked as custom
  """
  is_custom: Boolean


  """
  Whether or not this insurance plan is associated with fee schedule for the logged in user.
  """
  is_in_fee_schedules: Boolean


  """
  A serialized JSON string of metadata. Maximum character limit of 2,000.
  """
  metadata: JSON


  """
  A combined string to use for labels
  """
  name_and_id: String


  """
  The Payer ID of the insurance plan
  """
  payer_id: String


  """
  The name of the insurance plan
  """
  payer_name: String


  """
  Owner of this insurance plan
  """
  user: User
    @deprecated(reason: "Insurance Plans do not have an associated user")
}
```
