---
title: SsoConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/ssoconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/ssoconnection/index.md
---

Information on an SsoConnection

## Fields

[`allow_jit_provisioning` ](#field-allow-jit-provisioning)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not to allow Just-In-Time provisioning

[`for_user_type` ](#field-for-user-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of user this SSO is for (either patient or staff)

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the SSO connection

[`label` ](#field-label)· [`String` ](/reference/2026-01-01/scalars/string)· The label to display on the sign in button

[`sign_in_url` ](#field-sign-in-url)· [`String` ](/reference/2026-01-01/scalars/string)· The URL to take the user to to sign in via SSO

[`sign_out_url` ](#field-sign-out-url)· [`String` ](/reference/2026-01-01/scalars/string)· The URL to take the user to to sign out via SSO

## Used By

[`WhitelabelSetting.patient_sso_connection`](/reference/2026-01-01/objects/whitelabelsetting)

[`WhitelabelSetting.patient_sso_connections`](/reference/2026-01-01/objects/whitelabelsetting)

[`WhitelabelSetting.staff_sso_connection`](/reference/2026-01-01/objects/whitelabelsetting)

[`WhitelabelSetting.staff_sso_connections`](/reference/2026-01-01/objects/whitelabelsetting)

## Definition

```
"""
Information on an SsoConnection
"""
type SsoConnection {
  """
  Whether or not to allow Just-In-Time provisioning
  """
  allow_jit_provisioning: Boolean


  """
  The type of user this SSO is for (either patient or staff)
  """
  for_user_type: String


  """
  The unique identifier of the SSO connection
  """
  id: ID!


  """
  The label to display on the sign in button
  """
  label: String


  """
  The URL to take the user to to sign in via SSO
  """
  sign_in_url: String


  """
  The URL to take the user to to sign out via SSO
  """
  sign_out_url: String
}
```
