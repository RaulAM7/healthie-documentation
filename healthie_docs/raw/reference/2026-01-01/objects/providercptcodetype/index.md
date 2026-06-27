---
title: ProviderCptCodeType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/providercptcodetype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/providercptcodetype/index.md
---

ProviderCptCode object

## Fields

[`cpt_code_id` ](#field-cpt-code-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The CPT code ID

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the type

[`price_per_unit` ](#field-price-per-unit)· [`String` ](/reference/2026-01-01/scalars/string)· The price per unit

[`provider_id` ](#field-provider-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The provider ID

## Used By

[`ProviderCptCodeTypeEdge.node`](/reference/2026-01-01/objects/providercptcodetypeedge)

[`ProviderCptCodeTypePaginationConnection.nodes`](/reference/2026-01-01/objects/providercptcodetypepaginationconnection)

[`deleteProviderCptCodePayload.provider_cpt_code`](/reference/2026-01-01/objects/deleteprovidercptcodepayload)

## Definition

```
"""
ProviderCptCode object
"""
type ProviderCptCodeType {
  """
  The CPT code ID
  """
  cpt_code_id: ID!


  """
  The unique identifier of the type
  """
  id: ID!


  """
  The price per unit
  """
  price_per_unit: String


  """
  The provider ID
  """
  provider_id: ID!
}
```
