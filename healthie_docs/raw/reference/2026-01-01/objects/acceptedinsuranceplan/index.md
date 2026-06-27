---
title: AcceptedInsurancePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/acceptedinsuranceplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/acceptedinsuranceplan/index.md
---

Accepted Insurance Plan

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · Unique identifier of the plan

[`insurance_plan` ](#field-insurance-plan)· [`InsurancePlan` ](/reference/2026-01-01/objects/insuranceplan)· Connected ICD Code Object

## Used By

[`AcceptedInsurancePlanConnection.nodes`](/reference/2026-01-01/objects/acceptedinsuranceplanconnection)

[`AcceptedInsurancePlanEdge.node`](/reference/2026-01-01/objects/acceptedinsuranceplanedge)

[`AppointmentSetting.accepted_insurance_plans`](/reference/2026-01-01/objects/appointmentsetting)

[`ProviderAcceptedInsurancePlanType.accepted_insurance_plan`](/reference/2026-01-01/objects/provideracceptedinsuranceplantype)

[`createAcceptedInsurancePlanPayload.accepted_insurance_plans`](/reference/2026-01-01/objects/createacceptedinsuranceplanpayload)

[`deleteAcceptedInsurancePlanPayload.accepted_insurance_plan`](/reference/2026-01-01/objects/deleteacceptedinsuranceplanpayload)

## Definition

```
"""
Accepted Insurance Plan
"""
type AcceptedInsurancePlan {
  """
  Unique identifier of the plan
  """
  id: ID!


  """
  Connected ICD Code Object
  """
  insurance_plan: InsurancePlan
}
```
