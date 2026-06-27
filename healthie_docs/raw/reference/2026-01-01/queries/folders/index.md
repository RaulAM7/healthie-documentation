---
title: folders | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/folders/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/folders/index.md
---

Fetch paginated folders collection

## Arguments

[`client_id` ](#argument-client-id)· [`String`](/reference/2026-01-01/scalars/string)

[`consolidated_user_id` ](#argument-consolidated-user-id)· [`String`](/reference/2026-01-01/scalars/string)

[`document_to_move_id` ](#argument-document-to-move-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`filter` ](#argument-filter)· [`String`](/reference/2026-01-01/scalars/string)

[`folder_id` ](#argument-folder-id)· [`String`](/reference/2026-01-01/scalars/string)

[`folder_to_move_id` ](#argument-folder-to-move-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`for_template_use` ](#argument-for-template-use)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`private_user_id` ](#argument-private-user-id)· [`String`](/reference/2026-01-01/scalars/string)

[`provider_id` ](#argument-provider-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`should_paginate` ](#argument-should-paginate)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`FolderOrderKeys`](/reference/2026-01-01/enums/folderorderkeys)

[`viewable_user_id` ](#argument-viewable-user-id)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`FolderPaginationConnection`](/reference/2026-01-01/objects/folderpaginationconnection)

## Example

```
query folders(
  $client_id: String
  $consolidated_user_id: String
  $document_to_move_id: ID
  $filter: String
  $folder_id: String
  $folder_to_move_id: ID
  $for_template_use: Boolean
  $keywords: String
  $private_user_id: String
  $provider_id: ID
  $should_paginate: Boolean
  $sort_by: String
  $order_by: FolderOrderKeys
  $viewable_user_id: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  folders(
    client_id: $client_id
    consolidated_user_id: $consolidated_user_id
    document_to_move_id: $document_to_move_id
    filter: $filter
    folder_id: $folder_id
    folder_to_move_id: $folder_to_move_id
    for_template_use: $for_template_use
    keywords: $keywords
    private_user_id: $private_user_id
    provider_id: $provider_id
    should_paginate: $should_paginate
    sort_by: $sort_by
    order_by: $order_by
    viewable_user_id: $viewable_user_id
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
