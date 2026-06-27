---
title: PayoutAccount | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/payoutaccount/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/payoutaccount/index.md
---

A payout account representing a Stripe Connected Account within an organization

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · When the payout account was created

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · Internal ID

[`name` ](#field-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · Display name of the payout account

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · When the payout account was last updated

[`uuid` ](#field-uuid)· [`String!` ](/reference/2026-01-01/scalars/string)· required · UUID used for external references and payout routing

## Used By

[`PayoutAccountEdge.node`](/reference/2026-01-01/objects/payoutaccountedge)

[`PayoutAccountPaginationConnection.nodes`](/reference/2026-01-01/objects/payoutaccountpaginationconnection)

[`Query.payoutAccount`](/reference/2026-01-01/queries/payoutaccount)

## Definition

```
"""
A payout account representing a Stripe Connected Account within an organization
"""
type PayoutAccount {
  """
  When the payout account was created
  """
  created_at: ISO8601DateTime!


  """
  Internal ID
  """
  id: ID!


  """
  Display name of the payout account
  """
  name: String!


  """
  When the payout account was last updated
  """
  updated_at: ISO8601DateTime!


  """
  UUID used for external references and payout routing
  """
  uuid: String!
}
```
