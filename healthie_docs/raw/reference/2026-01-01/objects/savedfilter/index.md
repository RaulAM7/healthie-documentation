---
title: SavedFilter | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/savedfilter/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/savedfilter/index.md
---

A set of filter options saved for quick loading in the calendar

## Fields

[`filter_data` ](#field-filter-data)· [`JSON!` ](/reference/2026-01-01/scalars/json)· required · JSON-formatted options to use for setting filter

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · Unique ID for this filter

[`name` ](#field-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · Name of the filter

[`organization_id` ](#field-organization-id)· [`String` ](/reference/2026-01-01/scalars/string)· The organization\_id that has access to the filter

[`user_id` ](#field-user-id)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The user that created the filter

[`uuid` ](#field-uuid)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The unique UUID/string of the filter, used for sharing

## Used By

[`Query.savedFilter`](/reference/2026-01-01/queries/savedfilter)

[`SavedFilterEdge.node`](/reference/2026-01-01/objects/savedfilteredge)

[`SavedFilterPaginationConnection.nodes`](/reference/2026-01-01/objects/savedfilterpaginationconnection)

[`createSavedFilterPayload.savedFilter`](/reference/2026-01-01/objects/createsavedfilterpayload)

[`deleteSavedFilterPayload.savedFilter`](/reference/2026-01-01/objects/deletesavedfilterpayload)

[`updateSavedFilterPayload.savedFilter`](/reference/2026-01-01/objects/updatesavedfilterpayload)

## Definition

```
"""
A set of filter options saved for quick loading in the calendar
"""
type SavedFilter {
  """
  JSON-formatted options to use for setting filter
  """
  filter_data: JSON!


  """
  Unique ID for this filter
  """
  id: ID!


  """
  Name of the filter
  """
  name: String!


  """
  The organization_id that has access to the filter
  """
  organization_id: String


  """
  The user that created the filter
  """
  user_id: String!


  """
  The unique UUID/string of the filter, used for sharing
  """
  uuid: String!
}
```
