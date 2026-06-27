---
title: Human | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/human/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/human/index.md
---

Human object controls authentication for users

## Fields

[`current_user` ](#field-current-user)· [`User` ](/reference/2026-01-01/objects/user)· The current user

[`current_user_id` ](#field-current-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The Id of the human's currently selected user

[`email` ](#field-email)· [`String` ](/reference/2026-01-01/scalars/string)· The email of the human

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the human

[`last_sign_in_at` ](#field-last-sign-in-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· last date the human signed in

## Used By

[`updateHumanPayload.human`](/reference/2026-01-01/objects/updatehumanpayload)

## Definition

```
"""
Human object controls authentication for users
"""
type Human {
  """
  The current user
  """
  current_user: User


  """
  The Id of the human's currently selected user
  """
  current_user_id: ID


  """
  The email of the human
  """
  email: String


  """
  The unique identifier of the human
  """
  id: ID!


  """
  last date the human signed in
  """
  last_sign_in_at: ISO8601DateTime
}
```
