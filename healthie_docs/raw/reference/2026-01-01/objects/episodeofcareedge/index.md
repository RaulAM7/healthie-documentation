---
title: EpisodeOfCareEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/episodeofcareedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/episodeofcareedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`EpisodeOfCare` ](/reference/2026-01-01/objects/episodeofcare)· The item at the end of the edge.

## Used By

[`EpisodeOfCareConnection.edges`](/reference/2026-01-01/objects/episodeofcareconnection)

## Definition

```
"""
An edge in a connection.
"""
type EpisodeOfCareEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: EpisodeOfCare
}
```
