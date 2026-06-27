---
title: OrganizationCptCodeInsuranceFeeType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationcptcodeinsurancefeetype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationcptcodeinsurancefeetype/index.md
---

OrganizationCptCodeInsuranceFeeType object

## Fields

[`fee_per_unit` ](#field-fee-per-unit)· [`Int` ](/reference/2026-01-01/scalars/int)· Fee (in cents) per unit

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · Unique identifier for the object

[`insurance_plan` ](#field-insurance-plan)· [`InsurancePlan` ](/reference/2026-01-01/objects/insuranceplan)· The insurance plan that is associated with the org cpt code

[`organization_cpt_code_id` ](#field-organization-cpt-code-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID associated with organization cpt code object

## Used By

[`OrganizationCptCodeType.organization_cpt_code_insurance_fees`](/reference/2026-01-01/objects/organizationcptcodetype)

## Definition

```
"""
OrganizationCptCodeInsuranceFeeType object
"""
type OrganizationCptCodeInsuranceFeeType {
  """
  Fee (in cents) per unit
  """
  fee_per_unit: Int


  """
  Unique identifier for the object
  """
  id: ID!


  """
  The insurance plan that is associated with the org cpt code
  """
  insurance_plan: InsurancePlan


  """
  The ID associated with organization cpt code object
  """
  organization_cpt_code_id: ID
}
```
