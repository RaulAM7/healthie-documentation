---
title: organizationFeeScheduleCptCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/organizationfeeschedulecptcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/organizationfeeschedulecptcode/index.md
---

Fetch CPT code and fee schedule pricing by CPT code ID

## Arguments

[`cpt_code_id` ](#argument-cpt-code-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required

## Returns

[`OrganizationFeeScheduleCptCodeType`](/reference/2026-01-01/objects/organizationfeeschedulecptcodetype)

## Example

```
query organizationFeeScheduleCptCode($cpt_code_id: ID!) {
  organizationFeeScheduleCptCode(cpt_code_id: $cpt_code_id) {
    code
    description
    display_name
    fee_per_unit_cents
    id
  }
}
```
