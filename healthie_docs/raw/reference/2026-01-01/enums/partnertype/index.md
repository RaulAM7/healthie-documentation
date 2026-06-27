---
title: PartnerType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/partnertype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/partnertype/index.md
---

Describes who built the product and/or the API integration connecting it to Healthie

## Used By

[`IntegrationOptionType.partner_type`](/reference/2026-01-01/objects/integrationoptiontype)

## Definition

```
"""
Describes who built the product and/or the API integration connecting it to Healthie
"""
enum PartnerType {
  """
  The partner company built both the product and the API integration that connects it to Healthie
  """
  HARBOR_PARTNER


  """
  Healthie built both the product itself and the API integration that connects it to Healthie
  """
  HEALTHIE_APP


  """
  Healthie built the API integration that connects a third-party product to Healthie, but did not build the product itself
  """
  HEALTHIE_INTEGRATION


  """
  The partner built the product; Keragon handles the API communication between it and Healthie
  """
  KERAGON
}
```
