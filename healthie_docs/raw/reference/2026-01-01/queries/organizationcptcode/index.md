---
title: organizationCptCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/organizationcptcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/organizationcptcode/index.md
---

Returns organization cpt code object

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`OrganizationCptCodeType`](/reference/2026-01-01/objects/organizationcptcodetype)

## Example

```
query organizationCptCode($id: ID) {
  organizationCptCode(id: $id) {
    cpt_code_id
    created_at
    id
    organization_cpt_code_insurance_fees
    organization_cpt_code_insurance_fees_count
    organization_id
    price_per_unit
    updated_at
  }
}
```
