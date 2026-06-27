---
title: dosespotUserInfo | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/dosespotuserinfo/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/dosespotuserinfo/index.md
---

Fetch User Info on DoseSpot Object

## Arguments

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`DoseSpot`](/reference/2026-01-01/objects/dosespot)

## Example

```
query dosespotUserInfo($user_id: ID) {
  dosespotUserInfo(user_id: $user_id) {
    approved
    clinic_id
    clinic_key
    created_at
    dosespot_user_id
    id
    is_clinic_admin
    notification_count
    prescribing_dosespot_user_id
    registration_status
    updated_at
    user_id
  }
}
```
