---
title: whitelabelSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/whitelabelsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/whitelabelsetting/index.md
---

Whitelabel setting to use

## Arguments

[`branded_url` ](#argument-branded-url)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`WhitelabelSetting`](/reference/2026-01-01/objects/whitelabelsetting)

## Example

```
query whitelabelSetting($branded_url: String) {
  whitelabelSetting(branded_url: $branded_url) {
    amplitude_api_key
    android_app_link
    branded_backend_url
    branded_email
    branded_favicon_url
    branded_logo_url
    branded_name
    branded_url
    food_icon_url
    hide_apple_calendar
    id
    inactivity_minutes_timeout
    ios_app_link
    metric_icon_url
    mixpanel_project_token
    namespace
    patient_sso_connection
    patient_sso_connections
    replacement_words_json
    selfie_icon_url
    staff_sso_connection
    staff_sso_connections
    workout_icon_url
  }
}
```
