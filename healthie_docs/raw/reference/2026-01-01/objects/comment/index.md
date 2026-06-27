---
title: Comment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/comment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/comment/index.md
---

A comment of an entry

## Fields

[`author` ](#field-author)· [`User` ](/reference/2026-01-01/objects/user)· User who created comment

[`content` ](#field-content)· [`String` ](/reference/2026-01-01/scalars/string)· The content of this comment

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date on which the comment was posted

[`creator` ](#field-creator)· [`User` ](/reference/2026-01-01/objects/user)· User who created comment

[`entry_id` ](#field-entry-id)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the entry associated with the comment

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the comment

[`is_reaction` ](#field-is-reaction)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Indicates when posting an emoji reaction

[`poster` ](#field-poster)· [`User` ](/reference/2026-01-01/objects/user)· User who created comment

[`user_id` ](#field-user-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · the owner of the comment

## Used By

[`CommentEdge.node`](/reference/2026-01-01/objects/commentedge)

[`CommentPaginationConnection.nodes`](/reference/2026-01-01/objects/commentpaginationconnection)

[`Entry.comments`](/reference/2026-01-01/objects/entry)

[`createCommentPayload.comment`](/reference/2026-01-01/objects/createcommentpayload)

[`deleteCommentPayload.comment`](/reference/2026-01-01/objects/deletecommentpayload)

[`Query.comment`](/reference/2026-01-01/queries/comment)

## Definition

```
"""
A comment of an entry
"""
type Comment {
  """
  User who created comment
  """
  author: User


  """
  The content of this comment
  """
  content: String


  """
  The date on which the comment was posted
  """
  created_at: ISO8601DateTime!


  """
  User who created comment
  """
  creator: User


  """
  The id of the entry associated with the comment
  """
  entry_id: String


  """
  The unique identifier of the comment
  """
  id: ID!


  """
  Indicates when posting an emoji reaction
  """
  is_reaction: Boolean!


  """
  User who created comment
  """
  poster: User


  """
  the owner of the comment
  """
  user_id: ID!
}
```
