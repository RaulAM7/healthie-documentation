---
title: locations | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/locations/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/locations/index.md
---

Get locations for a given user (or current user)

## Arguments

[`has_name` ](#argument-has-name)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Pass in true to get service facilities for CMS 1500

[`has_service_facilities` ](#argument-has-service-facilities)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Pass in true to get service facilities for CMS 1500

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`user_id` ](#argument-user-id)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`LocationPaginationConnection`](/reference/2026-01-01/objects/locationpaginationconnection)

## Example

```
query locations(
  $has_name: Boolean
  $has_service_facilities: Boolean
  $keywords: String
  $user_id: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  locations(
    has_name: $has_name
    has_service_facilities: $has_service_facilities
    keywords: $keywords
    user_id: $user_id
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
