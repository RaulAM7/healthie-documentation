---
title: BaseCalendarInterval | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/basecalendarinterval/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/basecalendarinterval/index.md
---

The base minute interval for availability operations

## Used By

[`AppointmentSetting.base_calendar_interval`](/reference/2026-01-01/objects/appointmentsetting)

[`createAppointmentSettingInput.base_calendar_interval`](/reference/2026-01-01/input-objects/createappointmentsettinginput)

[`updateAppointmentSettingInput.base_calendar_interval`](/reference/2026-01-01/input-objects/updateappointmentsettinginput)

## Definition

```
"""
The base minute interval for availability operations
"""
enum BaseCalendarInterval {
  FIVE_MINUTES
  TEN_MINUTES
  FIFTEEN_MINUTES
}
```
