---
title: ProfessionsInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/professionsinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/professionsinput/index.md
---

Payload for a profession

## Fields

[`profession` ](#field-profession)· [`String` ](/reference/2026-01-01/scalars/string)· The graphql\_name of the profession

[`profession_category` ](#field-profession-category)· [`String` ](/reference/2026-01-01/scalars/string)· The category of the profession

## Used By

[`bulkCreateOrganizationMembershipsInput.professions`](/reference/2026-01-01/input-objects/bulkcreateorganizationmembershipsinput)

[`createOrganizationMembershipInput.professions`](/reference/2026-01-01/input-objects/createorganizationmembershipinput)

[`updateOrganizationMembershipInput.professions`](/reference/2026-01-01/input-objects/updateorganizationmembershipinput)

## Definition

```
"""
Payload for a profession
"""
input ProfessionsInput {
  """
  The graphql_name of the profession
  """
  profession: String


  """
  The category of the profession
  """
  profession_category: String
}
```
