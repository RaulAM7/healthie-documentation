---
title: IntegrationOptionType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/integrationoptiontype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/integrationoptiontype/index.md
---

The option of an integration

## Fields

[`button_not_connected` ](#field-button-not-connected)· [`IntegrationButtonConfig`](/reference/2026-01-01/objects/integrationbuttonconfig)

[`disabled_status_name` ](#field-disabled-status-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the status when the option is disabled

[`enable_button_label` ](#field-enable-button-label)· [`String` ](/reference/2026-01-01/scalars/string)· The label of the button to enable the option

[`enable_button_url` ](#field-enable-button-url)· [`String` ](/reference/2026-01-01/scalars/string)· The url of the button to enable the option

[`enabled_status_name` ](#field-enabled-status-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the status when the option is enabled

[`erx_connected_members` ](#field-erx-connected-members)· [`[String!]` ](/reference/2026-01-01/scalars/string)· List of connected members

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the option

[`integration_category_id` ](#field-integration-category-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the category the option belongs to

[`integration_details` ](#field-integration-details)· [`IntegrationDetailsType` ](/reference/2026-01-01/objects/integrationdetailstype)· The details of the option

[`is_active` ](#field-is-active)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the option is active

[`is_pending` ](#field-is-pending)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the option is pending

[`long_description` ](#field-long-description)· [`String` ](/reference/2026-01-01/scalars/string)· The long description of the option

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the option

[`partner_type` ](#field-partner-type)· [`PartnerType` ](/reference/2026-01-01/enums/partnertype)· Partner type options

[`short_description` ](#field-short-description)· [`String` ](/reference/2026-01-01/scalars/string)· The short description of the option

[`type` ](#field-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of the option

## Used By

[`IntegrationCategoryType.options`](/reference/2026-01-01/objects/integrationcategorytype)

## Definition

```
"""
The option of an integration
"""
type IntegrationOptionType {
  button_not_connected: IntegrationButtonConfig


  """
  The name of the status when the option is disabled
  """
  disabled_status_name: String


  """
  The label of the button to enable the option
  """
  enable_button_label: String


  """
  The url of the button to enable the option
  """
  enable_button_url: String


  """
  The name of the status when the option is enabled
  """
  enabled_status_name: String


  """
  List of connected members
  """
  erx_connected_members: [String!]


  """
  The unique identifier of the option
  """
  id: ID!


  """
  The unique identifier of the category the option belongs to
  """
  integration_category_id: ID


  """
  The details of the option
  """
  integration_details: IntegrationDetailsType


  """
  Whether the option is active
  """
  is_active: Boolean


  """
  Whether the option is pending
  """
  is_pending: Boolean


  """
  The long description of the option
  """
  long_description: String


  """
  The name of the option
  """
  name: String


  """
  Partner type options
  """
  partner_type: PartnerType


  """
  The short description of the option
  """
  short_description: String


  """
  The type of the option
  """
  type: String
}
```
