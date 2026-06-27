---
title: Immunization | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/immunization/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/immunization/index.md
---

User immunization

## Fields

[`additional_notes` ](#field-additional-notes)· [`String` ](/reference/2026-01-01/scalars/string)· Additional notes

[`cvx_code` ](#field-cvx-code)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · The cvx\_code

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the type

[`received_at` ](#field-received-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · Time when the immunization was received

[`status` ](#field-status)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The immunization status

[`user_id` ](#field-user-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The identifier of the user

[`vaccine_name` ](#field-vaccine-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The description of the code

## Used By

[`User.immunizations`](/reference/2026-01-01/objects/user)

[`createImmunizationPayload.immunization`](/reference/2026-01-01/objects/createimmunizationpayload)

[`updateImmunizationPayload.immunization`](/reference/2026-01-01/objects/updateimmunizationpayload)

## Definition

```
"""
User immunization
"""
type Immunization {
  """
  Additional notes
  """
  additional_notes: String


  """
  The cvx_code
  """
  cvx_code: Int!


  """
  The unique identifier of the type
  """
  id: ID!


  """
  Time when the immunization was received
  """
  received_at: ISO8601DateTime!


  """
  The immunization status
  """
  status: String!


  """
  The identifier of the user
  """
  user_id: ID!


  """
  The description of the code
  """
  vaccine_name: String!
}
```
