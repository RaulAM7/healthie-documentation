---
title: customEmail | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/customemail/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/customemail/index.md
---

Custom Email object

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`CustomEmail`](/reference/2026-01-01/objects/customemail)

## Example

```
query customEmail($id: ID) {
  customEmail(id: $id) {
    created_at
    email_type
    greeting
    id
    message_body
    name
    reactivation_wait_days
    related_object
    subject
    updated_at
    user_id
  }
}
```
