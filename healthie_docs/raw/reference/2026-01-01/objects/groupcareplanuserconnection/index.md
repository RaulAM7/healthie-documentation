---
title: GroupCarePlanUserConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/groupcareplanuserconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/groupcareplanuserconnection/index.md
---

A connection between a user and a care plan

## Fields

[`active` ](#field-active)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · The care plan active status

[`care_plan_id` ](#field-care-plan-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the care plan

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the join

[`user_group_id` ](#field-user-group-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the user\_group

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the client

## Used By

[`removeUserFromGroupCarePlanPayload.groupCarePlanUserConnection`](/reference/2026-01-01/objects/removeuserfromgroupcareplanpayload)

## Definition

```
"""
A connection between a user and a care plan
"""
type GroupCarePlanUserConnection {
  """
  The care plan active status
  """
  active: Boolean!


  """
  The ID of the care plan
  """
  care_plan_id: ID


  """
  The unique identifier of the join
  """
  id: ID!


  """
  The ID of the user_group
  """
  user_group_id: ID


  """
  The ID of the client
  """
  user_id: ID
}
```
