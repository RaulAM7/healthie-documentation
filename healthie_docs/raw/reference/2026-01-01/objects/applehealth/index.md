---
title: AppleHealth | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/applehealth/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/applehealth/index.md
---

An Apple Health Sync

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the apple health

[`last_sync_date` ](#field-last-sync-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The last time the apple health was synced

## Used By

[`User.apple_health`](/reference/2026-01-01/objects/user)

[`createAppleHealthPayload.apple_health`](/reference/2026-01-01/objects/createapplehealthpayload)

[`deleteAppleHealthPayload.apple_health`](/reference/2026-01-01/objects/deleteapplehealthpayload)

[`updateAppleHealthPayload.apple_health`](/reference/2026-01-01/objects/updateapplehealthpayload)

## Definition

```
"""
An Apple Health Sync
"""
type AppleHealth {
  """
  The unique identifier of the apple health
  """
  id: ID!


  """
  The last time the apple health was synced
  """
  last_sync_date: ISO8601DateTime
}
```
