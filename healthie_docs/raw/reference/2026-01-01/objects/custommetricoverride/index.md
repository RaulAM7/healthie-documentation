---
title: CustomMetricOverride | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/custommetricoverride/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/custommetricoverride/index.md
---

A custom metric for a user

## Fields

[`custom_metric` ](#field-custom-metric)· [`CustomMetric` ](/reference/2026-01-01/objects/custommetric)· custom metric

[`custom_metric_id` ](#field-custom-metric-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of the custom metric

[`feature_toggle_id` ](#field-feature-toggle-id)· [`Int` ](/reference/2026-01-01/scalars/int)· feature toggle id this custom metric belongs to

[`form_id` ](#field-form-id)· [`String` ](/reference/2026-01-01/scalars/string)· id form helper. Equivalent to the \`id\` field

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the override. Returns 0 for objects that exist only in memory and have not yet been saved to preserve non-nullability

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the custom metric

[`show` ](#field-show)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · if yes, show the custom metric

[`show_client` ](#field-show-client)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · if yes, show the custom metric to the client

[`track` ](#field-track)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· if yes, track the custom metric

[`user_id` ](#field-user-id)· [`Int` ](/reference/2026-01-01/scalars/int)· user id this custom metric belongs to

## Used By

[`FeatureToggle.initial_custom_metric_overrides`](/reference/2026-01-01/objects/featuretoggle)

## Definition

```
"""
A custom metric for a user
"""
type CustomMetricOverride {
  """
  custom metric
  """
  custom_metric: CustomMetric


  """
  id of the custom metric
  """
  custom_metric_id: ID


  """
  feature toggle id this custom metric belongs to
  """
  feature_toggle_id: Int


  """
  id form helper. Equivalent to the `id` field
  """
  form_id: String


  """
  The unique identifier of the override. Returns 0 for objects that exist only in memory and have not yet been saved to preserve non-nullability
  """
  id: ID!


  """
  The name of the custom metric
  """
  name: String


  """
  if yes, show the custom metric
  """
  show: Boolean!


  """
  if yes, show the custom metric to the client
  """
  show_client: Boolean!


  """
  if yes, track the custom metric
  """
  track: Boolean


  """
  user id this custom metric belongs to
  """
  user_id: Int
}
```
