---
title: Affiliate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/affiliate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/affiliate/index.md
---

(DEPRECATED - NO LONGER USED) Information on the provider's affiliate abilities

## Fields

[`affiliate_id` ](#field-affiliate-id)· [`String` ](/reference/2026-01-01/scalars/string)· The LeadDyno ID of the affiliate

[`affiliate_url` ](#field-affiliate-url)· [`String` ](/reference/2026-01-01/scalars/string)· The referral URL of the affiliate

[`dashboard_url` ](#field-dashboard-url)· [`String` ](/reference/2026-01-01/scalars/string)· The URL of the affiliate's dashboard

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · Unique identifier of the affiliate

## Used By

[`User.affiliate`](/reference/2026-01-01/objects/user)

## Definition

```
"""
(DEPRECATED - NO LONGER USED) Information on the provider's affiliate abilities
"""
type Affiliate {
  """
  The LeadDyno ID of the affiliate
  """
  affiliate_id: String


  """
  The referral URL of the affiliate
  """
  affiliate_url: String


  """
  The URL of the affiliate's dashboard
  """
  dashboard_url: String


  """
  Unique identifier of the affiliate
  """
  id: ID!
}
```
