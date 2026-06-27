---
title: SubOrganizationInfoInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/suborganizationinfoinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/suborganizationinfoinput/index.md
---

Payload for a sub-organization

## Fields

[`copy_appointment_settings` ](#field-copy-appointment-settings)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether to copy the appointment settings from the parent organization

[`copy_onboarding_flows` ](#field-copy-onboarding-flows)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether to copy the onboarding flows from the parent organization

[`copy_packages` ](#field-copy-packages)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether to copy the packages from the parent organization

[`copy_programs` ](#field-copy-programs)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether to copy the programs from the parent organization

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the suborganization

[`inherit_appointment_types` ](#field-inherit-appointment-types)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether to inherit appointment types from the parent organization

[`inherit_custom_module_forms` ](#field-inherit-custom-module-forms)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether to inherit custom module forms from the parent organization

[`inherit_stripe_account` ](#field-inherit-stripe-account)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether to inherit the stripe account from the parent organization

[`organization_settings` ](#field-organization-settings)· [`OrganizationSettingsInput` ](/reference/2026-01-01/input-objects/organizationsettingsinput)· Configuration options for the suborganization

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· DEPRECATED: Use primary organization info input instead

deprecated

Use primary organization info input instead

## Used By

[`createOrganizationInput.sub_org_settings`](/reference/2026-01-01/input-objects/createorganizationinput)

## Definition

```
"""
Payload for a sub-organization
"""
input SubOrganizationInfoInput {
  """
  Whether to copy the appointment settings from the parent organization
  """
  copy_appointment_settings: Boolean = true


  """
  Whether to copy the onboarding flows from the parent organization
  """
  copy_onboarding_flows: Boolean = false


  """
  Whether to copy the packages from the parent organization
  """
  copy_packages: Boolean = false


  """
  Whether to copy the programs from the parent organization
  """
  copy_programs: Boolean = false


  """
  The ID of the suborganization
  """
  id: ID


  """
  Whether to inherit appointment types from the parent organization
  """
  inherit_appointment_types: Boolean = true


  """
  Whether to inherit custom module forms from the parent organization
  """
  inherit_custom_module_forms: Boolean = true


  """
  Whether to inherit the stripe account from the parent organization
  """
  inherit_stripe_account: Boolean = true


  """
  Configuration options for the suborganization
  """
  organization_settings: OrganizationSettingsInput


  """
  DEPRECATED: Use primary organization info input instead
  """
  name: String
    @deprecated(reason: "Use primary organization info input instead")
}
```
