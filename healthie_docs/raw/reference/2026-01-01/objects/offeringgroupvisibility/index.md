---
title: OfferingGroupVisibility | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringgroupvisibility/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringgroupvisibility/index.md
---

User groups that are specific to this offering will only be visible to clients in these user groups

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the visibility

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· name of the user group

[`offering_id` ](#field-offering-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of related offering

[`user_group_id` ](#field-user-group-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of related user group

## Used By

[`Offering.offering_group_visibilities`](/reference/2026-01-01/objects/offering)

[`OfferingGroupVisibilityEdge.node`](/reference/2026-01-01/objects/offeringgroupvisibilityedge)

[`OfferingGroupVisibilityPaginationConnection.nodes`](/reference/2026-01-01/objects/offeringgroupvisibilitypaginationconnection)

## Definition

```
"""
User groups that are specific to this offering will only be visible to clients in these user groups
"""
type OfferingGroupVisibility {
  """
  The unique identifier of the visibility
  """
  id: ID!


  """
  name of the user group
  """
  name: String


  """
  id of related offering
  """
  offering_id: ID


  """
  id of related user group
  """
  user_group_id: ID
}
```
