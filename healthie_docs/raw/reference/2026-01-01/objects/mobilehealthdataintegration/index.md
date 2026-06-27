---
title: MobileHealthDataIntegration | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/mobilehealthdataintegration/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/mobilehealthdataintegration/index.md
---

Mobile health data integration

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · ID of the integration

[`type` ](#field-type)· [`MobileHealthDataIntegrationType!` ](/reference/2026-01-01/enums/mobilehealthdataintegrationtype)· required · Type of integration

## Used By

[`CreateMobileHealthDataIntegrationPayload.integration`](/reference/2026-01-01/objects/createmobilehealthdataintegrationpayload)

[`DeleteMobileHealthDataIntegrationPayload.integration`](/reference/2026-01-01/objects/deletemobilehealthdataintegrationpayload)

[`User.mobile_health_integrations`](/reference/2026-01-01/objects/user)

## Definition

```
"""
Mobile health data integration
"""
type MobileHealthDataIntegration {
  """
  ID of the integration
  """
  id: ID!


  """
  Type of integration
  """
  type: MobileHealthDataIntegrationType!
}
```
