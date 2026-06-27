---
title: ClaimSubmissionPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimsubmissionpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimsubmissionpaginationconnection/index.md
---

The connection type for ClaimSubmission.

## Fields

[`edges` ](#field-edges)· [`[ClaimSubmissionEdge]` ](/reference/2026-01-01/objects/claimsubmissionedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[ClaimSubmission]` ](/reference/2026-01-01/objects/claimsubmission)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Claim.claim_submissions`](/reference/2026-01-01/objects/claim)

## Definition

```
"""
The connection type for ClaimSubmission.
"""
type ClaimSubmissionPaginationConnection {
  """
  A list of edges.
  """
  edges: [ClaimSubmissionEdge]


  """
  A list of nodes.
  """
  nodes: [ClaimSubmission]


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
