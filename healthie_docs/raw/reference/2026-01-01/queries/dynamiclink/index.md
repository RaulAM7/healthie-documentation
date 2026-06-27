---
title: dynamicLink | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/dynamiclink/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/dynamiclink/index.md
---

Fetch a link from Fullscript to create a treatment plan for a given user

## Arguments

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`entrypoint` ](#argument-entrypoint)· [`FullscriptEntrypoint` ](/reference/2026-01-01/enums/fullscriptentrypoint)· Fullscript page to open via generated redirect link

## Returns

[`String`](/reference/2026-01-01/scalars/string)

## Example

```
query dynamicLink($user_id: ID, $entrypoint: FullscriptEntrypoint) {
  dynamicLink(user_id: $user_id, entrypoint: $entrypoint)
}
```
