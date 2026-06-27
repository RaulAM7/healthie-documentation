---
title: WithingsConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/withingsconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/withingsconnection/index.md
---

A Withings Connection

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the connections

[`last_sync_date` ](#field-last-sync-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The last time Withings was synced

## Used By

[`User.withings_connection`](/reference/2026-01-01/objects/user)

[`deleteWithingsConnectionPayload.withings_connection`](/reference/2026-01-01/objects/deletewithingsconnectionpayload)

## Definition

```
"""
A Withings Connection
"""
type WithingsConnection {
  """
  The unique identifier of the connections
  """
  id: ID!


  """
  The last time Withings was synced
  """
  last_sync_date: ISO8601DateTime
}
```
