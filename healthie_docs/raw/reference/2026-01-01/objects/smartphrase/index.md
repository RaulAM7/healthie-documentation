---
title: SmartPhrase | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/smartphrase/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/smartphrase/index.md
---

A smart phrase object

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The time when the smart phrase was created

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the smart phrase

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the smart phrase

[`phrase` ](#field-phrase)· [`String` ](/reference/2026-01-01/scalars/string)· The content of the smart phrase

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The time when the smart phrase was last updated

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The smart phrase owner

## Used By

[`SmartPhraseEdge.node`](/reference/2026-01-01/objects/smartphraseedge)

[`SmartPhrasePaginationConnection.nodes`](/reference/2026-01-01/objects/smartphrasepaginationconnection)

[`createSmartPhrasePayload.smartPhrase`](/reference/2026-01-01/objects/createsmartphrasepayload)

[`deleteSmartPhrasePayload.smartPhrase`](/reference/2026-01-01/objects/deletesmartphrasepayload)

[`updateSmartPhrasePayload.smartPhrase`](/reference/2026-01-01/objects/updatesmartphrasepayload)

## Definition

```
"""
A smart phrase object
"""
type SmartPhrase {
  """
  The time when the smart phrase was created
  """
  created_at: ISO8601DateTime!


  """
  The unique identifier of the smart phrase
  """
  id: ID!


  """
  The name of the smart phrase
  """
  name: String


  """
  The content of the smart phrase
  """
  phrase: String


  """
  The time when the smart phrase was last updated
  """
  updated_at: ISO8601DateTime


  """
  The smart phrase owner
  """
  user: User
}
```
