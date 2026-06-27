---
title: ProviderAcceptedInsurancePlanType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/provideracceptedinsuranceplantype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/provideracceptedinsuranceplantype/index.md
---

Insurance plan accepted by a provider

## Fields

[`accepted_insurance_plan` ](#field-accepted-insurance-plan)· [`AcceptedInsurancePlan!` ](/reference/2026-01-01/objects/acceptedinsuranceplan)· required · The accepted insurance plan

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the provider accepted insurance plan

[`organization` ](#field-organization)· [`Organization!` ](/reference/2026-01-01/objects/organization)· required · The associated organization

[`provider` ](#field-provider)· [`User!` ](/reference/2026-01-01/objects/user)· required · The provider assigned to the appointment request, if provided

## Used By

[`ProviderAcceptedInsurancePlanTypeEdge.node`](/reference/2026-01-01/objects/provideracceptedinsuranceplantypeedge)

[`ProviderAcceptedInsurancePlanTypePaginationConnection.nodes`](/reference/2026-01-01/objects/provideracceptedinsuranceplantypepaginationconnection)

[`createProviderAcceptedInsurancePlansPayload.provider_accepted_insurance_plans`](/reference/2026-01-01/objects/createprovideracceptedinsuranceplanspayload)

[`deleteProviderAcceptedInsurancePlanPayload.providerAcceptedInsurancePlan`](/reference/2026-01-01/objects/deleteprovideracceptedinsuranceplanpayload)

[`Query.providerAcceptedInsurancePlan`](/reference/2026-01-01/queries/provideracceptedinsuranceplan)

## Definition

```
"""
Insurance plan accepted by a provider
"""
type ProviderAcceptedInsurancePlanType {
  """
  The accepted insurance plan
  """
  accepted_insurance_plan: AcceptedInsurancePlan!


  """
  The unique identifier of the provider accepted insurance plan
  """
  id: ID!


  """
  The associated organization
  """
  organization: Organization!


  """
  The provider assigned to the appointment request, if provided
  """
  provider: User!
}
```
