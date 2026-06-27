---
title: IntegrationButtonConfig | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/integrationbuttonconfig/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/integrationbuttonconfig/index.md
---

Configuration for the button when the integration is not connected

## Fields

[`href` ](#field-href)· [`String`](/reference/2026-01-01/scalars/string)

[`payload` ](#field-payload)· [`JSON`](/reference/2026-01-01/scalars/json)

[`text` ](#field-text)· [`String!` ](/reference/2026-01-01/scalars/string)· required

## Used By

[`IntegrationOptionType.button_not_connected`](/reference/2026-01-01/objects/integrationoptiontype)

## Definition

```
"""
Configuration for the button when the integration is not connected
"""
type IntegrationButtonConfig {
  href: String
  payload: JSON
  text: String!
}
```
