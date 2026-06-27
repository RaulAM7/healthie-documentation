---
title: OrganizationCptCodeInsuranceFeesInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/organizationcptcodeinsurancefeesinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/organizationcptcodeinsurancefeesinput/index.md
---

Payload for Insurance Fees Inputs for Org Cpt Code

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, this object will be deleted

[`fee_per_unit` ](#field-fee-per-unit)· [`Int` ](/reference/2026-01-01/scalars/int)· Fee (in cents) per unit

[`insurance_plan_id` ](#field-insurance-plan-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The insurance plan associated with the cpt code object

[`organization_cpt_code_id` ](#field-organization-cpt-code-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID associated with organization cpt code object

## Used By

[`createOrganizationCptCodeInput.organization_cpt_code_insurance_fees`](/reference/2026-01-01/input-objects/createorganizationcptcodeinput)

[`updateOrganizationCptCodeInput.organization_cpt_code_insurance_fees`](/reference/2026-01-01/input-objects/updateorganizationcptcodeinput)

## Definition

```
"""
Payload for Insurance Fees Inputs for Org Cpt Code
"""
input OrganizationCptCodeInsuranceFeesInput {
  """
  If true, this object will be deleted
  """
  _destroy: Boolean


  """
  Fee (in cents) per unit
  """
  fee_per_unit: Int


  """
  The insurance plan associated with the cpt code object
  """
  insurance_plan_id: ID


  """
  The ID associated with organization cpt code object
  """
  organization_cpt_code_id: ID
}
```
