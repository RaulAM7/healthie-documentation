---
title: healthAssessments | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/healthassessments/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/healthassessments/index.md
---

Fetch Health Assessments

## Arguments

[`device_token` ](#argument-device-token)· [`String`](/reference/2026-01-01/scalars/string)

[`device_type` ](#argument-device-type)· [`String`](/reference/2026-01-01/scalars/string)

[`email` ](#argument-email)· [`String`](/reference/2026-01-01/scalars/string)

[`run_id` ](#argument-run-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`[HealthAssessment!]`](/reference/2026-01-01/objects/healthassessment)

## Example

```
query healthAssessments(
  $device_token: String
  $device_type: String
  $email: String
  $run_id: ID
  $user_id: ID
) {
  healthAssessments(
    device_token: $device_token
    device_type: $device_type
    email: $email
    run_id: $run_id
    user_id: $user_id
  ) {
    body_report
    created_at
    gender
    health_report
    height
    id
    is_diabetic
    race
    recommendation
    title
  }
}
```
