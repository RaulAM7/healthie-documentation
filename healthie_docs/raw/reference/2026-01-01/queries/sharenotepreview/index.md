---
title: shareNotePreview | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/sharenotepreview/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/sharenotepreview/index.md
---

A HTML string of charting note answers

## Arguments

[`answers` ](#argument-answers)· [`String`](/reference/2026-01-01/scalars/string)

[`form_answer_group_id` ](#argument-form-answer-group-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`letterhead` ](#argument-letterhead)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`pdf_letterhead_template_id` ](#argument-pdf-letterhead-template-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`include_header_on_every_page` ](#argument-include-header-on-every-page)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`String`](/reference/2026-01-01/scalars/string)

## Example

```
query shareNotePreview(
  $answers: String
  $form_answer_group_id: ID
  $letterhead: Boolean
  $pdf_letterhead_template_id: ID
  $include_header_on_every_page: Boolean
  $user_id: ID
) {
  shareNotePreview(
    answers: $answers
    form_answer_group_id: $form_answer_group_id
    letterhead: $letterhead
    pdf_letterhead_template_id: $pdf_letterhead_template_id
    include_header_on_every_page: $include_header_on_every_page
    user_id: $user_id
  )
}
```
