---
title: deleteTask | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletetask/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletetask/index.md
---

Destroy a task

## Arguments

[`input` ](#argument-input)· [`deleteTaskInput` ](/reference/2026-01-01/input-objects/deletetaskinput)· Parameters for deleteTask

## Returns

[`deleteTaskPayload`](/reference/2026-01-01/objects/deletetaskpayload)

## Example

```
mutation deleteTask($input: deleteTaskInput) {
  deleteTask(input: $input) {
    messages
    task
  }
}
```
