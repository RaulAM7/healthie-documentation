---
title: SpecialtiesInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/specialtiesinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/specialtiesinput/index.md
---

The properties of the specialty

## Fields

[`specialty` ](#field-specialty)· [`String` ](/reference/2026-01-01/scalars/string)· The graphql\_name of the specialty

[`specialty_category` ](#field-specialty-category)· [`String` ](/reference/2026-01-01/scalars/string)· The category of the specialty

## Used By

[`bulkCreateOrganizationMembershipsInput.specialties`](/reference/2026-01-01/input-objects/bulkcreateorganizationmembershipsinput)

[`createOrganizationMembershipInput.specialties`](/reference/2026-01-01/input-objects/createorganizationmembershipinput)

[`updateOrganizationMembershipInput.specialties`](/reference/2026-01-01/input-objects/updateorganizationmembershipinput)

## Definition

```
"""
The properties of the specialty
"""
input SpecialtiesInput {
  """
  The graphql_name of the specialty
  """
  specialty: String


  """
  The category of the specialty
  """
  specialty_category: String
}
```
