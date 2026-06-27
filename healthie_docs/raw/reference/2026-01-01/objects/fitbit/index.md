---
title: Fitbit | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/fitbit/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/fitbit/index.md
---

A Fitbit Sync

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the fitbit

[`is_enabled` ](#field-is-enabled)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Checking is active sync in current moment

[`last_sync_date` ](#field-last-sync-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The last time the fitbit was synced

## Used By

[`User.fitbit`](/reference/2026-01-01/objects/user)

[`createFitbitPayload.fitbit`](/reference/2026-01-01/objects/createfitbitpayload)

[`deleteFitbitPayload.fitbit`](/reference/2026-01-01/objects/deletefitbitpayload)

[`updateFitbitPayload.fitbit`](/reference/2026-01-01/objects/updatefitbitpayload)

## Definition

```
"""
A Fitbit Sync
"""
type Fitbit {
  """
  The unique identifier of the fitbit
  """
  id: ID!


  """
  Checking is active sync in current moment
  """
  is_enabled: Boolean!


  """
  The last time the fitbit was synced
  """
  last_sync_date: ISO8601DateTime
}
```
