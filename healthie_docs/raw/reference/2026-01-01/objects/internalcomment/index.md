---
title: InternalComment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/internalcomment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/internalcomment/index.md
---

An internal comment for tracking work on tasks and other objects

## Fields

[`content` ](#field-content)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The content of this comment

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date on which the comment was created

[`edited` ](#field-edited)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Has the comment been edited since it was first created?

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the internal comment

[`provider` ](#field-provider)· [`User!` ](/reference/2026-01-01/objects/user)· required · Provider who created the comment

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date on which the comment was last updated

## Used By

[`CreateInternalCommentPayload.internal_comment`](/reference/2026-01-01/objects/createinternalcommentpayload)

[`DestroyInternalCommentPayload.internal_comment`](/reference/2026-01-01/objects/destroyinternalcommentpayload)

[`InternalCommentEdge.node`](/reference/2026-01-01/objects/internalcommentedge)

[`InternalCommentPaginationConnection.nodes`](/reference/2026-01-01/objects/internalcommentpaginationconnection)

[`UpdateInternalCommentPayload.internal_comment`](/reference/2026-01-01/objects/updateinternalcommentpayload)

## Definition

```
"""
An internal comment for tracking work on tasks and other objects
"""
type InternalComment {
  """
  The content of this comment
  """
  content: String!


  """
  The date on which the comment was created
  """
  created_at: ISO8601DateTime!


  """
  Has the comment been edited since it was first created?
  """
  edited: Boolean!


  """
  The unique identifier of the internal comment
  """
  id: ID!


  """
  Provider who created the comment
  """
  provider: User!


  """
  The date on which the comment was last updated
  """
  updated_at: ISO8601DateTime!
}
```
