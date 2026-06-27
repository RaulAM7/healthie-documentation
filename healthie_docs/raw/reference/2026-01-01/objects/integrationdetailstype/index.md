---
title: IntegrationDetailsType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/integrationdetailstype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/integrationdetailstype/index.md
---

Parsed integration details extracted from long\_description

## Fields

[`available_for` ](#field-available-for)· [`[IntegrationPlanTiersType!]` ](/reference/2026-01-01/enums/integrationplantierstype)· Plan tiers the integration is available for

[`extra_info` ](#field-extra-info)· [`String` ](/reference/2026-01-01/scalars/string)· Any additional information below the long description

[`fee` ](#field-fee)· [`String` ](/reference/2026-01-01/scalars/string)· The integration fee description

[`formatted_description` ](#field-formatted-description)· [`String` ](/reference/2026-01-01/scalars/string)· The cleaned long description with tags removed

deprecated

This field is being deprecated in favor of structured jsonb data in integration\_option

[`is_setup_required` ](#field-is-setup-required)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the integration needs to be setup for the user or if automatically is enabled

## Used By

[`IntegrationOptionType.integration_details`](/reference/2026-01-01/objects/integrationoptiontype)

## Definition

```
"""
Parsed integration details extracted from long_description
"""
type IntegrationDetailsType {
  """
  Plan tiers the integration is available for
  """
  available_for: [IntegrationPlanTiersType!]


  """
  Any additional information below the long description
  """
  extra_info: String


  """
  The integration fee description
  """
  fee: String


  """
  The cleaned long description with tags removed
  """
  formatted_description: String
    @deprecated(
      reason: "This field is being deprecated in favor of structured jsonb data in integration_option"
    )


  """
  Whether the integration needs to be setup for the user or if automatically is enabled
  """
  is_setup_required: Boolean
}
```
