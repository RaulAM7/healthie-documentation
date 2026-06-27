---
title: ConversationMembershipsAllCounts | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/conversationmembershipsallcounts/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/conversationmembershipsallcounts/index.md
---

Counts for all conversation membership tabs (active, scheduled, archived, closed)

## Fields

[`active_count` ](#field-active-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Count of active (non-archived, non-closed) conversation memberships

[`archived_count` ](#field-archived-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Count of archived conversation memberships

[`closed_count` ](#field-closed-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Count of closed conversation memberships

[`scheduled_count` ](#field-scheduled-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Count of scheduled conversation memberships

## Used By

[`Query.conversationMembershipsAllCounts`](/reference/2026-01-01/queries/conversationmembershipsallcounts)

## Definition

```
"""
Counts for all conversation membership tabs (active, scheduled, archived, closed)
"""
type ConversationMembershipsAllCounts {
  """
  Count of active (non-archived, non-closed) conversation memberships
  """
  active_count: Int!


  """
  Count of archived conversation memberships
  """
  archived_count: Int!


  """
  Count of closed conversation memberships
  """
  closed_count: Int!


  """
  Count of scheduled conversation memberships
  """
  scheduled_count: Int!
}
```
