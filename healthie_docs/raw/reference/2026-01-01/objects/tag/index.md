---
title: Tag | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/tag/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/tag/index.md
---

A custom tag that can be applied on a user

## Fields

[`active_users_count` ](#field-active-users-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of active users who have the tag

[`added_by` ](#field-added-by)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the user who created the tag

[`archived_users_count` ](#field-archived-users-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of archived users who have the tag

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time when the tag was created

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the tag

[`name` ](#field-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · A human-readable name of the tag

[`org_members_count` ](#field-org-members-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of org members who have the tag

[`patients_tagged_count` ](#field-patients-tagged-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of patients this tag is applied to

[`providers_tagged_count` ](#field-providers-tagged-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of providers this tag is applied to

[`tagged_users` ](#field-tagged-users)· [`UserConnection` ](/reference/2026-01-01/objects/userconnection)· The array of tagged users

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The last time the tag was updated

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The user who created the tag

## Used By

[`AppliedTag.tag`](/reference/2026-01-01/objects/appliedtag)

[`Organization.tags`](/reference/2026-01-01/objects/organization)

[`TagEdge.node`](/reference/2026-01-01/objects/tagedge)

[`TagPaginationConnection.nodes`](/reference/2026-01-01/objects/tagpaginationconnection)

[`User.active_tags`](/reference/2026-01-01/objects/user)

[`bulkApplyPayload.tags`](/reference/2026-01-01/objects/bulkapplypayload)

[`createTagPayload.tag`](/reference/2026-01-01/objects/createtagpayload)

[`deleteTagPayload.tag`](/reference/2026-01-01/objects/deletetagpayload)

[`removeAppliedTagPayload.tag`](/reference/2026-01-01/objects/removeappliedtagpayload)

[`updateTagPayload.tag`](/reference/2026-01-01/objects/updatetagpayload)

[`Query.tags`](/reference/2026-01-01/queries/tags)

## Definition

```
"""
A custom tag that can be applied on a user
"""
type Tag {
  """
  The number of active users who have the tag
  """
  active_users_count: Int


  """
  The name of the user who created the tag
  """
  added_by: String


  """
  The number of archived users who have the tag
  """
  archived_users_count: Int


  """
  The time when the tag was created
  """
  created_at: ISO8601DateTime!


  """
  The unique identifier of the tag
  """
  id: ID!


  """
  A human-readable name of the tag
  """
  name: String!


  """
  The number of org members who have the tag
  """
  org_members_count: Int


  """
  The number of patients this tag is applied to
  """
  patients_tagged_count: Int


  """
  The number of providers this tag is applied to
  """
  providers_tagged_count: Int


  """
  The array of tagged users
  """
  tagged_users(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int
  ): UserConnection


  """
  The last time the tag was updated
  """
  updated_at: ISO8601DateTime!


  """
  The user who created the tag
  """
  user: User
}
```
