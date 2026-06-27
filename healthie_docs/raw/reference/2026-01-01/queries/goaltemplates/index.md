---
title: goalTemplates | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/goaltemplates/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/goaltemplates/index.md
---

Fetch paginated goal templates collection

## Arguments

[`category` ](#argument-category)· [`String` ](/reference/2026-01-01/scalars/string)· Can be 'personal', 'organizational', or 'default'

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`GoalTemplatePaginationConnection`](/reference/2026-01-01/objects/goaltemplatepaginationconnection)

## Example

```
query goalTemplates(
  $category: String
  $keywords: String
  $user_id: ID
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  goalTemplates(
    category: $category
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
