---
title: Shareable | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/unions/shareable/index
  md: https://docs.gethealthie.com/reference/2026-01-01/unions/shareable/index.md
---

Union type representing either a Document or Folder

## Possible types

[`Document`](#field-document)

[`Folder`](#field-folder)

## Used By

[`Mutation.createSharings`](/reference/2026-01-01/mutations/createsharings)

[`Mutation.deleteSharings`](/reference/2026-01-01/mutations/deletesharings)

[`Query.shareable`](/reference/2026-01-01/queries/shareable)

## Definition

```
"""
Union type representing either a Document or Folder
"""
union Shareable = Document | Folder
```
