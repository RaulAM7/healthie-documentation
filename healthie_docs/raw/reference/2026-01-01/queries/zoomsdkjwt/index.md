---
title: zoomSdkJwt | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/zoomsdkjwt/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/zoomsdkjwt/index.md
---

Generate a JWT to be used in the client-side Zoom SDK. This is just available on production, and requires your account to be approved by Healthie. The JWT is valid for 1 day.

## Arguments

[`mn` ](#argument-mn)· [`String` ](/reference/2026-01-01/scalars/string)· The Zoom meeting or webinar number

[`role` ](#argument-role)· [`String` ](/reference/2026-01-01/scalars/string)· The user role. 0 to specify participant, 1 to specify host

## Returns

[`String`](/reference/2026-01-01/scalars/string)

## Example

```
query zoomSdkJwt($mn: String, $role: String) {
  zoomSdkJwt(mn: $mn, role: $role)
}
```
