---
title: AppliedTag | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appliedtag/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appliedtag/index.md
---

A tag applied to a user

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time the tag was applied

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the applied tag

[`tag` ](#field-tag)· [`Tag` ](/reference/2026-01-01/objects/tag)· The tag applied

[`tag_id` ](#field-tag-id)· [`String` ](/reference/2026-01-01/scalars/string)· The unique identifier of the tag

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time the applied tag was last updated

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The tagged user

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the tagged user

## Used By

[`AppliedTagEdge.node`](/reference/2026-01-01/objects/appliedtagedge)

[`AppliedTagPaginationConnection.nodes`](/reference/2026-01-01/objects/appliedtagpaginationconnection)

[`Query.appliedTag`](/reference/2026-01-01/queries/appliedtag)

## Definition

```
"""
A tag applied to a user
"""
type AppliedTag {
  """
  The time the tag was applied
  """
  created_at: ISO8601DateTime!


  """
  The unique identifier of the applied tag
  """
  id: ID!


  """
  The tag applied
  """
  tag: Tag


  """
  The unique identifier of the tag
  """
  tag_id: String


  """
  The time the applied tag was last updated
  """
  updated_at: ISO8601DateTime!


  """
  The tagged user
  """
  user: User


  """
  The ID of the tagged user
  """
  user_id: String
}
```
