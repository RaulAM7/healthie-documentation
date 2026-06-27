---
title: AuditEventPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/auditeventpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/auditeventpaginationconnection/index.md
---

The connection type for AuditEvent.

## Fields

[`edges` ](#field-edges)· [`[AuditEventEdge]` ](/reference/2026-01-01/objects/auditeventedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[AuditEvent]` ](/reference/2026-01-01/objects/auditevent)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.auditLog`](/reference/2026-01-01/queries/auditlog)

## Definition

```
"""
The connection type for AuditEvent.
"""
type AuditEventPaginationConnection {
  """
  A list of edges.
  """
  edges: [AuditEventEdge]


  """
  A list of nodes.
  """
  nodes: [AuditEvent]


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
