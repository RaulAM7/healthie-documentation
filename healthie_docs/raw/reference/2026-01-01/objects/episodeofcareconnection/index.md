---
title: EpisodeOfCareConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/episodeofcareconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/episodeofcareconnection/index.md
---

The connection type for EpisodeOfCare.

## Fields

[`edges` ](#field-edges)· [`[EpisodeOfCareEdge]` ](/reference/2026-01-01/objects/episodeofcareedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[EpisodeOfCare]` ](/reference/2026-01-01/objects/episodeofcare)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.episodesOfCare`](/reference/2026-01-01/queries/episodesofcare)

## Definition

```
"""
The connection type for EpisodeOfCare.
"""
type EpisodeOfCareConnection {
  """
  A list of edges.
  """
  edges: [EpisodeOfCareEdge]


  """
  A list of nodes.
  """
  nodes: [EpisodeOfCare]


  """
  Information to aid in pagination.
  """
  page_info: PageInfo!


  """
  Total count of items.
  """
  total_count: Int!
}
```
