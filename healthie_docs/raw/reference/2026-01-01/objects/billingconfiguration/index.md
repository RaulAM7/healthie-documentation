---
title: BillingConfiguration | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/billingconfiguration/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/billingconfiguration/index.md
---

Billing configuration for an organization

## Fields

[`encounters_enabled` ](#field-encounters-enabled)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether patient encounters are the source of truth for billing data for this organization

## Used By

[`Organization.billing_configuration`](/reference/2026-01-01/objects/organization)

## Definition

```
"""
Billing configuration for an organization
"""
type BillingConfiguration {
  """
  Whether patient encounters are the source of truth for billing data for this organization
  """
  encounters_enabled: Boolean!
}
```
