---
title: UserConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/userconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/userconnection/index.md
---

The connection type for User.

## Fields

[`edges` ](#field-edges)· [`[UserEdge]` ](/reference/2026-01-01/objects/useredge)· A list of edges.

[`nodes` ](#field-nodes)· [`[User]` ](/reference/2026-01-01/objects/user)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Document.shareable_org_members`](/reference/2026-01-01/objects/document)

[`Document.shareable_patients`](/reference/2026-01-01/objects/document)

[`Document.users`](/reference/2026-01-01/objects/document)

[`Folder.shareable_org_members`](/reference/2026-01-01/objects/folder)

[`Folder.shareable_patients`](/reference/2026-01-01/objects/folder)

[`Folder.users`](/reference/2026-01-01/objects/folder)

[`Organization.paginated_users`](/reference/2026-01-01/objects/organization)

[`Organization.providers`](/reference/2026-01-01/objects/organization)

[`Tag.tagged_users`](/reference/2026-01-01/objects/tag)

[`Task.assignees`](/reference/2026-01-01/objects/task)

[`User.active_patients`](/reference/2026-01-01/objects/user)

[`Query.courseGroupClients`](/reference/2026-01-01/queries/coursegroupclients)

[`Query.lastClientActivities`](/reference/2026-01-01/queries/lastclientactivities)

[`Query.organizationMembers`](/reference/2026-01-01/queries/organizationmembers)

[`Query.users`](/reference/2026-01-01/queries/users)

## Definition

```
"""
The connection type for User.
"""
type UserConnection {
  """
  A list of edges.
  """
  edges: [UserEdge]


  """
  A list of nodes.
  """
  nodes: [User]


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
