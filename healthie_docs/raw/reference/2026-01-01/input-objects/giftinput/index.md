---
title: GiftInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/giftinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/giftinput/index.md
---

Payload for a gift

## Fields

[`giver_email` ](#field-giver-email)· [`String` ](/reference/2026-01-01/scalars/string)· The email of the giver

[`giver_name` ](#field-giver-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the giver

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the gift

[`message` ](#field-message)· [`String` ](/reference/2026-01-01/scalars/string)· The message assigned to the gift

## Used By

[`completeCheckoutInput.gift`](/reference/2026-01-01/input-objects/completecheckoutinput)

## Definition

```
"""
Payload for a gift
"""
input GiftInput {
  """
  The email of the giver
  """
  giver_email: String


  """
  The name of the giver
  """
  giver_name: String


  """
  The ID of the gift
  """
  id: ID


  """
  The message assigned to the gift
  """
  message: String
}
```
