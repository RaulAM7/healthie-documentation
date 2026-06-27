---
title: updateCalendarViewSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecalendarviewsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecalendarviewsetting/index.md
---

Update and return calendar view setting

## Arguments

[`input` ](#argument-input)· [`updateCalendarViewSettingInput` ](/reference/2026-01-01/input-objects/updatecalendarviewsettinginput)· Parameters for updateCalendarViewSetting

## Returns

[`updateCalendarViewSettingPayload`](/reference/2026-01-01/objects/updatecalendarviewsettingpayload)

## Example

```
mutation updateCalendarViewSetting($input: updateCalendarViewSettingInput) {
  updateCalendarViewSetting(input: $input) {
    calendar_view_setting
    messages
  }
}
```
