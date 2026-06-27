---
title: DsiComment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/dsicomment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/dsicomment/index.md
---

An allergy/sensitivity/preference for a client

## Fields

[`content` ](#field-content)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The content of the comment

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the comment

[`intervention_type` ](#field-intervention-type)· [`InterventionType!` ](/reference/2026-01-01/enums/interventiontype)· required · The type of intervention

[`organization_id` ](#field-organization-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The organization that the comment belongs to

## Used By

[`Query.dsiComment`](/reference/2026-01-01/queries/dsicomment)

[`createDsiCommentPayload.dsi_comment`](/reference/2026-01-01/objects/createdsicommentpayload)

[`updateDsiCommentPayload.dsi_comment`](/reference/2026-01-01/objects/updatedsicommentpayload)

## Definition

```
"""
An allergy/sensitivity/preference for a client
"""
type DsiComment {
  """
  The content of the comment
  """
  content: String!


  """
  The unique identifier of the comment
  """
  id: ID!


  """
  The type of intervention
  """
  intervention_type: InterventionType!


  """
  The organization that the comment belongs to
  """
  organization_id: ID!
}
```
