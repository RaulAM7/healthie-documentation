---
title: Referral | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/referral/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/referral/index.md
---

A referral

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · created at

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the referral

[`metadata` ](#field-metadata)· [`String` ](/reference/2026-01-01/scalars/string)· A serialized JSON string of metadata. Maximum character limit of 128,000.

[`referral_reason` ](#field-referral-reason)· [`String` ](/reference/2026-01-01/scalars/string)· The reason the client was referred to the physician

[`referring_physician` ](#field-referring-physician)· [`ReferringPhysician` ](/reference/2026-01-01/objects/referringphysician)· The referring physician

[`referring_physician_id` ](#field-referring-physician-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of the referring physician

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · updated at

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The referred client

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of the referred client

## Used By

[`Policy.referral`](/reference/2026-01-01/objects/policy)

[`ReferringPhysician.referrals`](/reference/2026-01-01/objects/referringphysician)

[`User.referrals`](/reference/2026-01-01/objects/user)

[`createReferralPayload.referral`](/reference/2026-01-01/objects/createreferralpayload)

[`deleteReferralPayload.referral`](/reference/2026-01-01/objects/deletereferralpayload)

[`updateReferralPayload.referral`](/reference/2026-01-01/objects/updatereferralpayload)

[`Query.referral`](/reference/2026-01-01/queries/referral)

## Definition

```
"""
A referral
"""
type Referral {
  """
  created at
  """
  created_at: ISO8601DateTime!


  """
  The unique identifier of the referral
  """
  id: ID!


  """
  A serialized JSON string of metadata. Maximum character limit of 128,000.
  """
  metadata: String


  """
  The reason the client was referred to the physician
  """
  referral_reason: String


  """
  The referring physician
  """
  referring_physician: ReferringPhysician


  """
  id of the referring physician
  """
  referring_physician_id: ID


  """
  updated at
  """
  updated_at: ISO8601DateTime!


  """
  The referred client
  """
  user: User


  """
  id of the referred client
  """
  user_id: ID
}
```
