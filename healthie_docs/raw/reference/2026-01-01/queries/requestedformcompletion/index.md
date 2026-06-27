---
title: requestedFormCompletion | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/requestedformcompletion/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/requestedformcompletion/index.md
---

fetch a requested form completion by id

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`track_opened_event` ](#argument-track-opened-event)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If TRUE, create form history 'opened' event

## Returns

[`RequestedFormCompletion`](/reference/2026-01-01/objects/requestedformcompletion)

## Example

```
query requestedFormCompletion($id: ID, $track_opened_event: Boolean) {
  requestedFormCompletion(id: $id, track_opened_event: $track_opened_event) {
    custom_module_form
    custom_module_form_id
    date_to_show
    form_answer_group
    form_answer_group_id
    id
    item_type
    metadata
    recipient
    recipient_id
    recurring_form
    sender
    sender_id
    status
  }
}
```
