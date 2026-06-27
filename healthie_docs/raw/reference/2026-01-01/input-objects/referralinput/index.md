---
title: ReferralInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/referralinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/referralinput/index.md
---

Payload for a referral

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the referral will be deleted

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the referral

[`referring_physician` ](#field-referring-physician)· [`ReferringPhysicianInput` ](/reference/2026-01-01/input-objects/referringphysicianinput)· The referring physician object

[`referring_physician_id` ](#field-referring-physician-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the referring physician

## Used By

[`updateClientInput.referrals`](/reference/2026-01-01/input-objects/updateclientinput)

## Definition

```
"""
Payload for a referral
"""
input ReferralInput {
  """
  If true, the referral will be deleted
  """
  _destroy: Boolean


  """
  The ID of the referral
  """
  id: ID


  """
  The referring physician object
  """
  referring_physician: ReferringPhysicianInput


  """
  The ID of the referring physician
  """
  referring_physician_id: ID
}
```
