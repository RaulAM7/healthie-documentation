---
title: updateTask | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatetask/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatetask/index.md
---

Update a task for provider

## Arguments

[`input` ](#argument-input)· [`updateTaskInput` ](/reference/2026-01-01/input-objects/updatetaskinput)· Parameters for updateTask

## Returns

[`updateTaskPayload`](/reference/2026-01-01/objects/updatetaskpayload)

## Example

```
mutation updateTask($input: updateTaskInput) {
  updateTask(input: $input) {
    messages
    task
  }
}
```
