---
title: GoogleFit | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/googlefit/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/googlefit/index.md
---

A GoogleFit Sync

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the Google fit

[`last_sync_date` ](#field-last-sync-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The last time the apple health was synced

## Used By

[`User.google_fit`](/reference/2026-01-01/objects/user)

[`createGoogleFitPayload.google_fit`](/reference/2026-01-01/objects/creategooglefitpayload)

[`deleteGoogleFitPayload.google_fit`](/reference/2026-01-01/objects/deletegooglefitpayload)

[`updateGoogleFitPayload.google_fit`](/reference/2026-01-01/objects/updategooglefitpayload)

## Definition

```
"""
A GoogleFit Sync
"""
type GoogleFit {
  """
  The unique identifier of the Google fit
  """
  id: ID!


  """
  The last time the apple health was synced
  """
  last_sync_date: ISO8601DateTime
}
```
