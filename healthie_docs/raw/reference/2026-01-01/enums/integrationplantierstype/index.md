---
title: IntegrationPlanTiersType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/integrationplantierstype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/integrationplantierstype/index.md
---

The plan tiers that an integration is available for

## Used By

[`IntegrationDetailsType.available_for`](/reference/2026-01-01/objects/integrationdetailstype)

## Definition

```
"""
The plan tiers that an integration is available for
"""
enum IntegrationPlanTiersType {
  ENTERPRISE
  GROUP
  PLUS
  ESSENTIALS
  CORE
  STARTER
}
```
