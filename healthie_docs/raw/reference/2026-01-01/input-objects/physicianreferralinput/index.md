---
title: PhysicianReferralInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/physicianreferralinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/physicianreferralinput/index.md
---

Payload for a referral

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If the referral should be destroyed

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the referral

[`referral_reason` ](#field-referral-reason)· [`String` ](/reference/2026-01-01/scalars/string)· The reason for the referral

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the user

## Used By

[`createReferringPhysicianInput.referrals`](/reference/2026-01-01/input-objects/createreferringphysicianinput)

[`updateReferringPhysicianInput.referrals`](/reference/2026-01-01/input-objects/updatereferringphysicianinput)

## Definition

```
"""
Payload for a referral
"""
input PhysicianReferralInput {
  """
  If the referral should be destroyed
  """
  _destroy: Boolean


  """
  The ID of the referral
  """
  id: ID


  """
  The reason for the referral
  """
  referral_reason: String


  """
  The ID of the user
  """
  user_id: ID
}
```
