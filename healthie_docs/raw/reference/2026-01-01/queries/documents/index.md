---
title: documents | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/documents/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/documents/index.md
---

Fetch paginated documents collection

## Arguments

[`consolidated_user_id` ](#argument-consolidated-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of a patient or client whose documents a provider wants to view.

[`file_type` ](#argument-file-type)· [`String` ](/reference/2026-01-01/scalars/string)· Filters documents by file type (e.g. "all", "other").

[`file_types` ](#argument-file-types)· [`[String]` ](/reference/2026-01-01/scalars/string)· (DEPRECATED)

[`filter` ](#argument-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Filters documents by sharing status. Accepted values: "all", "shared", "private".

[`folder_id` ](#argument-folder-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the folder to fetch documents from.

[`for_template_use` ](#argument-for-template-use)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, returns only provider-level documents with no associated patient or client, for use in templates.

[`keywords` ](#argument-keywords)· [`String` ](/reference/2026-01-01/scalars/string)· Search term to filter documents by name.

[`private_user_id` ](#argument-private-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the user whose private documents to fetch.

[`provider_id` ](#argument-provider-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the provider whose documents to fetch. Defaults to the current user.

[`viewable_user_id` ](#argument-viewable-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of a viewable user whose documents to fetch.

[`sort_by` ](#argument-sort-by)· [`String` ](/reference/2026-01-01/scalars/string)· Deprecated.

[`order_by` ](#argument-order-by)· [`DocumentOrderKeys` ](/reference/2026-01-01/enums/documentorderkeys)· Sort order key for the returned documents.

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`DocumentPaginationConnection`](/reference/2026-01-01/objects/documentpaginationconnection)

## Example

```
query documents(
  $consolidated_user_id: String
  $file_type: String
  $file_types: [String]
  $filter: String
  $folder_id: String
  $for_template_use: Boolean
  $keywords: String
  $private_user_id: String
  $provider_id: ID
  $viewable_user_id: String
  $sort_by: String
  $order_by: DocumentOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  documents(
    consolidated_user_id: $consolidated_user_id
    file_type: $file_type
    file_types: $file_types
    filter: $filter
    folder_id: $folder_id
    for_template_use: $for_template_use
    keywords: $keywords
    private_user_id: $private_user_id
    provider_id: $provider_id
    viewable_user_id: $viewable_user_id
    sort_by: $sort_by
    order_by: $order_by
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
