---
title: WhitelabelSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/whitelabelsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/whitelabelsetting/index.md
---

Info for Whitelabeling

## Fields

[`amplitude_api_key` ](#field-amplitude-api-key)· [`String` ](/reference/2026-01-01/scalars/string)· Amplitude API Key

[`android_app_link` ](#field-android-app-link)· [`String` ](/reference/2026-01-01/scalars/string)· URL of whitelabeled Android app

[`branded_backend_url` ](#field-branded-backend-url)· [`String` ](/reference/2026-01-01/scalars/string)· The branded URL of the backend (used in certain whitelabel setups)

[`branded_email` ](#field-branded-email)· [`String` ](/reference/2026-01-01/scalars/string)· Branded email of whitelabel

[`branded_favicon_url` ](#field-branded-favicon-url)· [`String` ](/reference/2026-01-01/scalars/string)· Branded favicon url of whitelabel

[`branded_logo_url` ](#field-branded-logo-url)· [`String` ](/reference/2026-01-01/scalars/string)· Branded logo url of whitelabel

[`branded_name` ](#field-branded-name)· [`String` ](/reference/2026-01-01/scalars/string)· Branded name of whitelabel

[`branded_url` ](#field-branded-url)· [`String` ](/reference/2026-01-01/scalars/string)· URL of whitelabel site

[`food_icon_url` ](#field-food-icon-url)· [`String` ](/reference/2026-01-01/scalars/string)· URL of whitelabeled Food icon

[`hide_apple_calendar` ](#field-hide-apple-calendar)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether to hide the Apple Calendar integration

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the setting

[`inactivity_minutes_timeout` ](#field-inactivity-minutes-timeout)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of minutes of allowable inactivity

[`ios_app_link` ](#field-ios-app-link)· [`String` ](/reference/2026-01-01/scalars/string)· URL of whitelabeled iOS app

[`metric_icon_url` ](#field-metric-icon-url)· [`String` ](/reference/2026-01-01/scalars/string)· URL of whitelabeled Metric icon

[`mixpanel_project_token` ](#field-mixpanel-project-token)· [`String` ](/reference/2026-01-01/scalars/string)· Mixpanel Project Token

[`namespace` ](#field-namespace)· [`String` ](/reference/2026-01-01/scalars/string)· The namespace that the whitelabel setting is in.

[`patient_sso_connection` ](#field-patient-sso-connection)· [`SsoConnection` ](/reference/2026-01-01/objects/ssoconnection)· The whitelabel's patient SSO connection

[`patient_sso_connections` ](#field-patient-sso-connections)· [`[SsoConnection!]` ](/reference/2026-01-01/objects/ssoconnection)· The whitelabel's patient SSO connections

[`replacement_words_json` ](#field-replacement-words-json)· [`String` ](/reference/2026-01-01/scalars/string)· JSON hash of whitelabel replacement words

[`selfie_icon_url` ](#field-selfie-icon-url)· [`String` ](/reference/2026-01-01/scalars/string)· URL of whitelabeled Selfie icon

[`staff_sso_connection` ](#field-staff-sso-connection)· [`SsoConnection` ](/reference/2026-01-01/objects/ssoconnection)· The whitelabel's staff SSO connection

[`staff_sso_connections` ](#field-staff-sso-connections)· [`[SsoConnection!]` ](/reference/2026-01-01/objects/ssoconnection)· The whitelabel's staff SSO connections

[`workout_icon_url` ](#field-workout-icon-url)· [`String` ](/reference/2026-01-01/scalars/string)· URL of whitelabeled Workout icon

## Used By

[`Query.whitelabelSetting`](/reference/2026-01-01/queries/whitelabelsetting)

[`signUpPayload.whitelabelSetting`](/reference/2026-01-01/objects/signuppayload)

## Definition

```
"""
Info for Whitelabeling
"""
type WhitelabelSetting {
  """
  Amplitude API Key
  """
  amplitude_api_key(
    """
    The branded URL of the backend (used in certain whitelabel setups)
    """
    branded_url: String
  ): String


  """
  URL of whitelabeled Android app
  """
  android_app_link: String


  """
  The branded URL of the backend (used in certain whitelabel setups)
  """
  branded_backend_url: String


  """
  Branded email of whitelabel
  """
  branded_email: String


  """
  Branded favicon url of whitelabel
  """
  branded_favicon_url: String


  """
  Branded logo url of whitelabel
  """
  branded_logo_url: String


  """
  Branded name of whitelabel
  """
  branded_name: String


  """
  URL of whitelabel site
  """
  branded_url: String


  """
  URL of whitelabeled Food icon
  """
  food_icon_url: String


  """
  Whether to hide the Apple Calendar integration
  """
  hide_apple_calendar: Boolean


  """
  The unique identifier of the setting
  """
  id: ID!


  """
  The number of minutes of allowable inactivity
  """
  inactivity_minutes_timeout: Int


  """
  URL of whitelabeled iOS app
  """
  ios_app_link: String


  """
  URL of whitelabeled Metric icon
  """
  metric_icon_url: String


  """
  Mixpanel Project Token
  """
  mixpanel_project_token(
    """
    The branded URL of the backend (used in certain whitelabel setups)
    """
    branded_url: String
  ): String


  """
  The namespace that the whitelabel setting is in.
  """
  namespace: String


  """
  The whitelabel's patient SSO connection
  """
  patient_sso_connection: SsoConnection


  """
  The whitelabel's patient SSO connections
  """
  patient_sso_connections: [SsoConnection!]


  """
  JSON hash of whitelabel replacement words
  """
  replacement_words_json: String


  """
  URL of whitelabeled Selfie icon
  """
  selfie_icon_url: String


  """
  The whitelabel's staff SSO connection
  """
  staff_sso_connection: SsoConnection


  """
  The whitelabel's staff SSO connections
  """
  staff_sso_connections: [SsoConnection!]


  """
  URL of whitelabeled Workout icon
  """
  workout_icon_url: String
}
```
