---
title: DexcomConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/dexcomconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/dexcomconnection/index.md
---

A Dexcom Connection

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the connection

[`last_sync_date` ](#field-last-sync-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The last time Dexcom was synced

## Used By

[`User.dexcom_connection`](/reference/2026-01-01/objects/user)

[`deleteDexcomConnectionPayload.dexcom_connection`](/reference/2026-01-01/objects/deletedexcomconnectionpayload)

## Definition

```
"""
A Dexcom Connection
"""
type DexcomConnection {
  """
  The unique identifier of the connection
  """
  id: ID!


  """
  The last time Dexcom was synced
  """
  last_sync_date: ISO8601DateTime
}
```
