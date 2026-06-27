---
title: DoseSpot | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/dosespot/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/dosespot/index.md
---

Only available to Internal Healthie Users -- Roles assigned to a given User

## Fields

[`approved` ](#field-approved)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · State of account being approved

[`clinic_id` ](#field-clinic-id)· [`String` ](/reference/2026-01-01/scalars/string)· User's Clinic ID

[`clinic_key` ](#field-clinic-key)· [`String` ](/reference/2026-01-01/scalars/string)· User's Clinic Key

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · Date the object was created

[`dosespot_user_id` ](#field-dosespot-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· User ID associated with DoseSpot

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the type

[`is_clinic_admin` ](#field-is-clinic-admin)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· This user is a clinic admin in dosespot

[`notification_count` ](#field-notification-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Number of notifications on dosespot the User has

[`prescribing_dosespot_user_id` ](#field-prescribing-dosespot-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· ID of the user prescribing the dosespot

[`registration_status` ](#field-registration-status)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The dosespot status

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · Date the object was last updated

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· User ID associated with the dosespot object in Healthie

## Used By

[`Query.dosespotUserInfo`](/reference/2026-01-01/queries/dosespotuserinfo)

[`createDosespotClinicianPayload.dosespot_user`](/reference/2026-01-01/objects/createdosespotclinicianpayload)

## Definition

```
"""
Only available to Internal Healthie Users -- Roles assigned to a given User
"""
type DoseSpot {
  """
  State of account being approved
  """
  approved: Boolean!


  """
  User's Clinic ID
  """
  clinic_id: String


  """
  User's Clinic Key
  """
  clinic_key: String


  """
  Date the object was created
  """
  created_at: ISO8601DateTime!


  """
  User ID associated with DoseSpot
  """
  dosespot_user_id: String


  """
  The unique identifier of the type
  """
  id: ID!


  """
  This user is a clinic admin in dosespot
  """
  is_clinic_admin: Boolean


  """
  Number of notifications on dosespot the User has
  """
  notification_count: Int!


  """
  ID of the user prescribing the dosespot
  """
  prescribing_dosespot_user_id: String


  """
  The dosespot status
  """
  registration_status: Boolean


  """
  Date the object was last updated
  """
  updated_at: ISO8601DateTime!


  """
  User ID associated with the dosespot object in Healthie
  """
  user_id: String
}
```
