---
title: embedWidgetSteps | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/embedwidgetsteps/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/embedwidgetsteps/index.md
---

fetch embed steps based off of params

## Arguments

[`is_for_web` ](#argument-is-for-web)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`locationString` ](#argument-locationstring)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`[EmbedWidgetStepType!]`](/reference/2026-01-01/objects/embedwidgetsteptype)

## Example

```
query embedWidgetSteps($is_for_web: Boolean, $locationString: String) {
  embedWidgetSteps(is_for_web: $is_for_web, locationString: $locationString) {
    id
    title
  }
}
```
