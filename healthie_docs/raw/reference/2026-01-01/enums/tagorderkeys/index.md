---
title: TagOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/tagorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/tagorderkeys/index.md
---

Tag sorting enum

## Used By

[`Query.tags`](/reference/2026-01-01/queries/tags)

[`Query.tagsPaginated`](/reference/2026-01-01/queries/tagspaginated)

## Definition

```
"""
Tag sorting enum
"""
enum TagOrderKeys {
  NAME_ASC
  NAME_DESC


  """
  Sort by amount of patients applied to this Tag descending
  """
  ACTIVE_USERS_DESC


  """
  Sort by amount of patients applied to this Tag ascending
  """
  ACTIVE_USERS_ASC


  """
  Sort by the first name of the user who added the Tag descending
  """
  ADDED_BY_DESC


  """
  Sort by the first name of the user who added the Tag ascending
  """
  ADDED_BY_ASC


  """
  Sort by amount of organization members applied to this Tag ascending
  """
  ORG_MEMBERS_ASC


  """
  Sort by amount of organization members applied to this Tag descending
  """
  ORG_MEMBERS_DESC
}
```
