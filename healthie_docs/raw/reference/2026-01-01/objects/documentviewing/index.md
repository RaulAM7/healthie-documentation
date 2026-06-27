---
title: DocumentViewing | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/documentviewing/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/documentviewing/index.md
---

Information about a document being opened

## Fields

[`document_id` ](#field-document-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the document that was opened

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the viewing

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The user who opened the document

[`user_id` ](#field-user-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the user who opened the document

[`viewed_at` ](#field-viewed-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · When the document was opened

## Used By

[`Document.opens`](/reference/2026-01-01/objects/document)

[`DocumentViewingEdge.node`](/reference/2026-01-01/objects/documentviewingedge)

[`DocumentViewingPaginationConnection.nodes`](/reference/2026-01-01/objects/documentviewingpaginationconnection)

## Definition

```
"""
Information about a document being opened
"""
type DocumentViewing {
  """
  The ID of the document that was opened
  """
  document_id: ID!


  """
  The unique identifier of the viewing
  """
  id: ID!


  """
  The user who opened the document
  """
  user: User


  """
  The ID of the user who opened the document
  """
  user_id: ID!


  """
  When the document was opened
  """
  viewed_at: ISO8601DateTime!
}
```
