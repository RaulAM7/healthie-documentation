---
title: ClaimMdMessage | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimmdmessage/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimmdmessage/index.md
---

A message from ClaimMD

## Fields

[`fields` ](#field-fields)· [`[String!]!` ](/reference/2026-01-01/scalars/string)· required · The fields involved in the message

[`message` ](#field-message)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The message content

[`status` ](#field-status)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The status of the message

## Used By

[`Claim.claim_md_rejection_messages`](/reference/2026-01-01/objects/claim)

[`Cms1500.claim_md_rejection_messages`](/reference/2026-01-01/objects/cms1500)

## Definition

```
"""
A message from ClaimMD
"""
type ClaimMdMessage {
  """
  The fields involved in the message
  """
  fields: [String!]!


  """
  The message content
  """
  message: String!


  """
  The status of the message
  """
  status: String!
}
```
