---
title: bulkDeleteTasks | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkdeletetasks/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkdeletetasks/index.md
---

Delete tasks

## Arguments

[`input` ](#argument-input)· [`bulkDeleteTasksInput` ](/reference/2026-01-01/input-objects/bulkdeletetasksinput)· Parameters for bulkDeleteTasks

## Returns

[`bulkDeleteTasksPayload`](/reference/2026-01-01/objects/bulkdeletetaskspayload)

## Example

```
mutation bulkDeleteTasks($input: bulkDeleteTasksInput) {
  bulkDeleteTasks(input: $input) {
    messages
    tasks
  }
}
```
