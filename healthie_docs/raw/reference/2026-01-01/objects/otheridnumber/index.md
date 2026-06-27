---
title: OtherIdNumber | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/otheridnumber/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/otheridnumber/index.md
---

Alternative ID numbers for a provider

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the other id number

[`label` ](#field-label)· [`String` ](/reference/2026-01-01/scalars/string)· The label to use for the other id

[`organization` ](#field-organization)· [`Organization` ](/reference/2026-01-01/objects/organization)· The associated organization

[`organization_id` ](#field-organization-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the associated organization

[`other_id` ](#field-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· The other id

[`other_id_qualifier` ](#field-other-id-qualifier)· [`String` ](/reference/2026-01-01/scalars/string)· The other ID qualifier (what type of ID it is)

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The associated user

deprecated

You never need to query the user of the other\_id

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the associated user

## Used By

[`Cms1500.rendering_provider_other_id_object`](/reference/2026-01-01/objects/cms1500)

[`OtherIdNumberEdge.node`](/reference/2026-01-01/objects/otheridnumberedge)

[`OtherIdNumberPaginationConnection.nodes`](/reference/2026-01-01/objects/otheridnumberpaginationconnection)

[`User.other_id_number`](/reference/2026-01-01/objects/user)

[`User.other_id_numbers`](/reference/2026-01-01/objects/user)

[`Query.otherIdNumber`](/reference/2026-01-01/queries/otheridnumber)

## Definition

```
"""
Alternative ID numbers for a provider
"""
type OtherIdNumber {
  """
  The unique identifier of the other id number
  """
  id: ID!


  """
  The label to use for the other id
  """
  label: String


  """
  The associated organization
  """
  organization: Organization


  """
  The ID of the associated organization
  """
  organization_id: String


  """
  The other id
  """
  other_id: String


  """
  The other ID qualifier (what type of ID it is)
  """
  other_id_qualifier: String


  """
  The associated user
  """
  user: User
    @deprecated(reason: "You never need to query the user of the other_id")


  """
  The ID of the associated user
  """
  user_id: String
}
```
