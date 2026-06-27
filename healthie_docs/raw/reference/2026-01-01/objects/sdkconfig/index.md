---
title: SDKConfig | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/sdkconfig/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/sdkconfig/index.md
---

Configuration for the SDK

## Fields

[`stripe_publishable_key` ](#field-stripe-publishable-key)· [`String!` ](/reference/2026-01-01/scalars/string)· required · Stripe's publishable key

## Used By

[`Query.sdkConfig`](/reference/2026-01-01/queries/sdkconfig)

## Definition

```
"""
Configuration for the SDK
"""
type SDKConfig {
  """
  Stripe's publishable key
  """
  stripe_publishable_key: String!
}
```
