---
title: UserGroupPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/usergrouppaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/usergrouppaginationconnection/index.md
---

The connection type for UserGroup.

## Fields

[`edges` ](#field-edges)· [`[UserGroupEdge]` ](/reference/2026-01-01/objects/usergroupedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[UserGroup]` ](/reference/2026-01-01/objects/usergroup)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Document.shareable_user_groups`](/reference/2026-01-01/objects/document)

[`Folder.shareable_user_groups`](/reference/2026-01-01/objects/folder)

[`User.user_groups`](/reference/2026-01-01/objects/user)

[`Query.userGroups`](/reference/2026-01-01/queries/usergroups)

## Definition

```
"""
The connection type for UserGroup.
"""
type UserGroupPaginationConnection {
  """
  A list of edges.
  """
  edges: [UserGroupEdge]


  """
  A list of nodes.
  """
  nodes: [UserGroup]


  """
  Information to aid in pagination.
  """
  page_info: PageInfo!


  """
  Total count of items.
  """
  total_count: Int!
}
```
