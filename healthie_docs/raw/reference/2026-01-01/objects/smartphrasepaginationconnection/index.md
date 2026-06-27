---
title: SmartPhrasePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/smartphrasepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/smartphrasepaginationconnection/index.md
---

The connection type for SmartPhrase.

## Fields

[`edges` ](#field-edges)· [`[SmartPhraseEdge]` ](/reference/2026-01-01/objects/smartphraseedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[SmartPhrase]` ](/reference/2026-01-01/objects/smartphrase)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.smartPhrases`](/reference/2026-01-01/queries/smartphrases)

## Definition

```
"""
The connection type for SmartPhrase.
"""
type SmartPhrasePaginationConnection {
  """
  A list of edges.
  """
  edges: [SmartPhraseEdge]


  """
  A list of nodes.
  """
  nodes: [SmartPhrase]


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
