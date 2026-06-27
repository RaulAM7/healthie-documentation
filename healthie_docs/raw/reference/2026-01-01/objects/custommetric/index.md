---
title: CustomMetric | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/custommetric/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/custommetric/index.md
---

A custom metric for a user

## Fields

[`custom_module_form` ](#field-custom-module-form)· [`CustomModuleForm` ](/reference/2026-01-01/objects/custommoduleform)· The associated autoscored custom module form

[`custom_module_form_id` ](#field-custom-module-form-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the autoscored custom module form

[`feature_toggle_id` ](#field-feature-toggle-id)· [`Int` ](/reference/2026-01-01/scalars/int)· feature toggle id this custom metric belongs to

[`high_warning_threshold` ](#field-high-warning-threshold)· [`Int` ](/reference/2026-01-01/scalars/int)· The high end of the normal range

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the metric

[`low_warning_threshold` ](#field-low-warning-threshold)· [`Int` ](/reference/2026-01-01/scalars/int)· The low end of the normal range

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the custom metric

[`should_show` ](#field-should-show)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· if yes, should show based on if there is custom metric override

[`should_show_client` ](#field-should-show-client)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· if yes, should show the client based on if there is a custom metric override

[`show` ](#field-show)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · if yes, show the custom metric

[`show_client` ](#field-show-client)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · if yes, show the custom metric to client

[`track` ](#field-track)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · if yes, track the custom metric

[`user_id` ](#field-user-id)· [`Int` ](/reference/2026-01-01/scalars/int)· user id this custom metric belongs to

## Used By

[`CustomMetricOverride.custom_metric`](/reference/2026-01-01/objects/custommetricoverride)

[`FeatureToggle.custom_metrics`](/reference/2026-01-01/objects/featuretoggle)

[`FeatureToggle.metric_category_objects`](/reference/2026-01-01/objects/featuretoggle)

[`User.custom_metrics`](/reference/2026-01-01/objects/user)

## Definition

```
"""
A custom metric for a user
"""
type CustomMetric {
  """
  The associated autoscored custom module form
  """
  custom_module_form: CustomModuleForm


  """
  The ID of the autoscored custom module form
  """
  custom_module_form_id: ID


  """
  feature toggle id this custom metric belongs to
  """
  feature_toggle_id: Int


  """
  The high end of the normal range
  """
  high_warning_threshold: Int


  """
  The unique identifier of the metric
  """
  id: ID!


  """
  The low end of the normal range
  """
  low_warning_threshold: Int


  """
  The name of the custom metric
  """
  name: String


  """
  if yes, should show based on if there is custom metric override
  """
  should_show: Boolean


  """
  if yes, should show the client based on if there is a custom metric override
  """
  should_show_client: Boolean


  """
  if yes, show the custom metric
  """
  show: Boolean!


  """
  if yes, show the custom metric to client
  """
  show_client: Boolean!


  """
  if yes, track the custom metric
  """
  track: Boolean!


  """
  user id this custom metric belongs to
  """
  user_id: Int
}
```
