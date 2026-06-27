---
title: ContactTypeOverride | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/contacttypeoverride/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/contacttypeoverride/index.md
---

Payload for overriding a contact type

## Fields

[`show` ](#field-show)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether to show this contact type

## Used By

[`updateAppointmentTypeInput.contact_type_override_in_person`](/reference/2026-01-01/input-objects/updateappointmenttypeinput)

[`updateAppointmentTypeInput.contact_type_override_phone_call`](/reference/2026-01-01/input-objects/updateappointmenttypeinput)

[`updateAppointmentTypeInput.contact_type_override_video_chat`](/reference/2026-01-01/input-objects/updateappointmenttypeinput)

## Definition

```
"""
Payload for overriding a contact type
"""
input ContactTypeOverride {
  """
  Whether to show this contact type
  """
  show: Boolean!
}
```
