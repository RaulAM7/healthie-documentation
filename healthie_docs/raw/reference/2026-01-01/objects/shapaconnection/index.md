---
title: ShapaConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/shapaconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/shapaconnection/index.md
---

A Shapa Connection

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the connection

[`last_sync_date` ](#field-last-sync-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The last time Shapa was synced

## Used By

[`User.clearstep_connection`](/reference/2026-01-01/objects/user)

[`User.shapa_connection`](/reference/2026-01-01/objects/user)

[`deleteShapaConnectionPayload.shapa_connection`](/reference/2026-01-01/objects/deleteshapaconnectionpayload)

## Definition

```
"""
A Shapa Connection
"""
type ShapaConnection {
  """
  The unique identifier of the connection
  """
  id: ID!


  """
  The last time Shapa was synced
  """
  last_sync_date: ISO8601DateTime
}
```
