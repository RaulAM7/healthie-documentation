---
title: ProviderCptCodeInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/providercptcodeinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/providercptcodeinput/index.md
---

Properties for creating or updating a ProviderCptCode

## Fields

[`cpt_code_id` ](#field-cpt-code-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The CPT code ID

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the code

[`price_per_unit` ](#field-price-per-unit)· [`String` ](/reference/2026-01-01/scalars/string)· The price per unit of the code

[`provider_id` ](#field-provider-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the provider

## Used By

[`createProviderCptCodesInput.provider_cpt_codes`](/reference/2026-01-01/input-objects/createprovidercptcodesinput)

[`updateProviderCptCodesInput.provider_cpt_codes`](/reference/2026-01-01/input-objects/updateprovidercptcodesinput)

## Definition

```
"""
Properties for creating or updating a ProviderCptCode
"""
input ProviderCptCodeInput {
  """
  The CPT code ID
  """
  cpt_code_id: ID


  """
  The unique identifier of the code
  """
  id: ID


  """
  The price per unit of the code
  """
  price_per_unit: String


  """
  The unique identifier of the provider
  """
  provider_id: ID
}
```
