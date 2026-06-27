---
title: CustomMetricOverridesInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/custommetricoverridesinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/custommetricoverridesinput/index.md
---

Payload for overriding a custom metric

## Fields

[`custom_metric_id` ](#field-custom-metric-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the custom metric

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the custom metric override

[`show` ](#field-show)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not to show the custom metric

[`show_client` ](#field-show-client)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not to show the custom metric to the client

## Used By

[`createFeatureToggleInput.custom_metric_overrides`](/reference/2026-01-01/input-objects/createfeaturetoggleinput)

[`updateFeatureToggleInput.custom_metric_overrides`](/reference/2026-01-01/input-objects/updatefeaturetoggleinput)

## Definition

```
"""
Payload for overriding a custom metric
"""
input CustomMetricOverridesInput {
  """
  The ID of the custom metric
  """
  custom_metric_id: ID


  """
  The ID of the custom metric override
  """
  id: ID


  """
  Whether or not to show the custom metric
  """
  show: Boolean


  """
  Whether or not to show the custom metric to the client
  """
  show_client: Boolean
}
```
