---
title: FormAnswerGroupUserConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/formanswergroupuserconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/formanswergroupuserconnection/index.md
---

An instance representing connection between a group charting note(form\_answer\_group.appointment.is\_group == true) and a user

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the connection

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The user associated with the connection

## Used By

[`FormAnswerGroup.form_answer_group_users_connections`](/reference/2026-01-01/objects/formanswergroup)

## Definition

```
"""
An instance representing connection between a group charting note(form_answer_group.appointment.is_group == true) and a user
"""
type FormAnswerGroupUserConnection {
  """
  The unique identifier of the connection
  """
  id: ID!


  """
  The user associated with the connection
  """
  user: User
}
```
