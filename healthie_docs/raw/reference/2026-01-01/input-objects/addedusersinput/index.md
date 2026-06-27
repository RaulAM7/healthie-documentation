---
title: AddedUsersInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/addedusersinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/addedusersinput/index.md
---

Payload for added user as a label-value pair

## Fields

[`label` ](#field-label)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The label for the user

[`value` ](#field-value)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The labeled value

## Used By

[`createConversationInput.added_users`](/reference/2026-01-01/input-objects/createconversationinput)

## Definition

```
"""
Payload for added user as a label-value pair
"""
input AddedUsersInput {
  """
  The label for the user
  """
  label: String!


  """
  The labeled value
  """
  value: ID!
}
```
