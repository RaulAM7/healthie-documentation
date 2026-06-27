---
title: announcements | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/announcements/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/announcements/index.md
---

Fetch an array of announcements for a provider

## Arguments

[`exclude_dismissed` ](#argument-exclude-dismissed)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, only show announcements that client has not dismissed

[`keywords` ](#argument-keywords)· [`String` ](/reference/2026-01-01/scalars/string)· Search announcements by name, title and description

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`AnnouncementPaginationConnection`](/reference/2026-01-01/objects/announcementpaginationconnection)

## Example

```
query announcements(
  $exclude_dismissed: Boolean
  $keywords: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  announcements(
    exclude_dismissed: $exclude_dismissed
    keywords: $keywords
    after: $after
    before: $before
    first: $first
    last: $last
  ) {
    edges
    nodes
    page_info
    total_count
  }
}
```
