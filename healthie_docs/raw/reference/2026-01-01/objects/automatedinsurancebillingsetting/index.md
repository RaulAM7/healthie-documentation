---
title: AutomatedInsuranceBillingSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/automatedinsurancebillingsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/automatedinsurancebillingsetting/index.md
---

Automated Insurance Billing Setting Type

## Fields

[`auto_create_cms1500s` ](#field-auto-create-cms1500s)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, CMS1500s will be created automatically

[`auto_submit_cms1500s` ](#field-auto-submit-cms1500s)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, CMS1500s will be submitted automatically

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the setting

[`insurance_billing_enabled` ](#field-insurance-billing-enabled)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, insurance billing features are enabled for the organization

[`use_cpt_codes_units_and_fees_with_appointment_types` ](#field-use-cpt-codes-units-and-fees-with-appointment-types)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· DEPRECATED. This setting no longer has any effect

## Used By

[`Organization.automated_insurance_billing_setting`](/reference/2026-01-01/objects/organization)

[`createAutomatedInsuranceBillingSettingPayload.automated_insurance_billing_setting`](/reference/2026-01-01/objects/createautomatedinsurancebillingsettingpayload)

[`updateAutomatedInsuranceBillingSettingPayload.automated_insurance_billing_setting`](/reference/2026-01-01/objects/updateautomatedinsurancebillingsettingpayload)

[`Query.automatedInsuranceBillingSetting`](/reference/2026-01-01/queries/automatedinsurancebillingsetting)

## Definition

```
"""
Automated Insurance Billing Setting Type
"""
type AutomatedInsuranceBillingSetting {
  """
  When true, CMS1500s will be created automatically
  """
  auto_create_cms1500s: Boolean


  """
  When true, CMS1500s will be submitted automatically
  """
  auto_submit_cms1500s: Boolean


  """
  The unique identifier of the setting
  """
  id: ID!


  """
  When true, insurance billing features are enabled for the organization
  """
  insurance_billing_enabled: Boolean


  """
  DEPRECATED. This setting no longer has any effect
  """
  use_cpt_codes_units_and_fees_with_appointment_types: Boolean
}
```
