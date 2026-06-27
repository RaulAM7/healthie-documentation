---
title: colorCodeOptions | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/colorcodeoptions/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/colorcodeoptions/index.md
---

Color Code Options for a given category

## Arguments

[`appointment_setting_id` ](#argument-appointment-setting-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`color_code_by` ](#argument-color-code-by)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`[ColorCodeOption!]`](/reference/2026-01-01/objects/colorcodeoption)

## Example

```
query colorCodeOptions($appointment_setting_id: ID, $color_code_by: String) {
  colorCodeOptions(
    appointment_setting_id: $appointment_setting_id
    color_code_by: $color_code_by
  ) {
    label
    value
  }
}
```
