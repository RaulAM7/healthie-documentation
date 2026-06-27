---
title: CustomMetricInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/custommetricinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/custommetricinput/index.md
---

Payload for a custom metric

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not to destroy the custom metric

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of the custom metric

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The graphql\_name of the custom metric

[`show` ](#field-show)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not to show the custom metric

[`show_client` ](#field-show-client)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not to show the custom metric to the client

[`track` ](#field-track)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not to track the custom metric

[`custom_module_form_id` ](#field-custom-module-form-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of an autoscored custom module form

## Used By

[`createFeatureToggleInput.custom_metrics`](/reference/2026-01-01/input-objects/createfeaturetoggleinput)

[`updateFeatureToggleInput.custom_metrics`](/reference/2026-01-01/input-objects/updatefeaturetoggleinput)

## Definition

```
"""
Payload for a custom metric
"""
input CustomMetricInput {
  """
  Whether or not to destroy the custom metric
  """
  _destroy: Boolean


  """
  The id of the custom metric
  """
  id: ID


  """
  The graphql_name of the custom metric
  """
  name: String


  """
  Whether or not to show the custom metric
  """
  show: Boolean


  """
  Whether or not to show the custom metric to the client
  """
  show_client: Boolean


  """
  Whether or not to track the custom metric
  """
  track: Boolean


  """
  The ID of an autoscored custom module form
  """
  custom_module_form_id: ID
}
```
