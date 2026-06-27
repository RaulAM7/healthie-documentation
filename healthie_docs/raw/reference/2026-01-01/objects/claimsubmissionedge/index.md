---
title: ClaimSubmissionEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimsubmissionedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimsubmissionedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`ClaimSubmission` ](/reference/2026-01-01/objects/claimsubmission)· The item at the end of the edge.

## Used By

[`ClaimSubmissionPaginationConnection.edges`](/reference/2026-01-01/objects/claimsubmissionpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type ClaimSubmissionEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: ClaimSubmission
}
```
