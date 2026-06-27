---
title: chartingItems | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/chartingitems/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/chartingitems/index.md
---

All items to include in the charting list

## Arguments

[`custom_module_form_id` ](#argument-custom-module-form-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Filter by form template ID.

[`date` ](#argument-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Filter by a specific date. Supersedes \`start\_date\` and \`end\_date\`.

[`document_id` ](#argument-document-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Filter by document ID.

[`filler_id` ](#argument-filler-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Filter by the ID of the provider who filled out the items.

[`form_answer_group_id` ](#argument-form-answer-group-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Filter by form answer group ID.

[`generated_form_answer_group_id` ](#argument-generated-form-answer-group-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Filter by generated form answer group ID.

[`include_docs` ](#argument-include-docs)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether to include documents marked for charting. Defaults to true.

[`include_generated_form_answer_groups` ](#argument-include-generated-form-answer-groups)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether to include generated form answer groups. Defaults to false.

[`keywords` ](#argument-keywords)· [`String` ](/reference/2026-01-01/scalars/string)· Full-text search on form answer group name.

[`name` ](#argument-name)· [`String` ](/reference/2026-01-01/scalars/string)· Filter by name of the form answer group, associated form template, or document.

[`user_id` ](#argument-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the client whose charting items to retrieve.

[`start_date` ](#argument-start-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Start of the date range. Superseded by \`date\`. Defaults to today if \`end\_date\` is provided without a start date.

[`end_date` ](#argument-end-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· End of the date range. Superseded by \`date\`. Defaults to today if \`start\_date\` is provided without an end date.

## Returns

[`[ChartingItemType!]`](/reference/2026-01-01/objects/chartingitemtype)

## Example

```
query chartingItems(
  $custom_module_form_id: ID
  $date: ISO8601DateTime
  $document_id: ID
  $filler_id: ID
  $form_answer_group_id: ID
  $generated_form_answer_group_id: ID
  $include_docs: Boolean
  $include_generated_form_answer_groups: Boolean
  $keywords: String
  $name: String
  $user_id: ID
  $start_date: ISO8601DateTime
  $end_date: ISO8601DateTime
) {
  chartingItems(
    custom_module_form_id: $custom_module_form_id
    date: $date
    document_id: $document_id
    filler_id: $filler_id
    form_answer_group_id: $form_answer_group_id
    generated_form_answer_group_id: $generated_form_answer_group_id
    include_docs: $include_docs
    include_generated_form_answer_groups: $include_generated_form_answer_groups
    keywords: $keywords
    name: $name
    user_id: $user_id
    start_date: $start_date
    end_date: $end_date
  ) {
    created_at
    custom_module_form_name
    document
    filler_id
    form_answer_group
    form_answer_group_id
    generated_form_answer_group
    id
    is_document
    is_generated
    name
    provider_name
    signed
    use_for_charting
    use_for_program
  }
}
```
