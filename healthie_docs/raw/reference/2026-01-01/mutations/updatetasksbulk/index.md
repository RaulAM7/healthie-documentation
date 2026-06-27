---
title: updateTasksBulk | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatetasksbulk/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatetasksbulk/index.md
---

Bulk update multiple tasks with completion status, seen status, and filtering options. Can update all tasks matching filters or specific tasks by ID.

## Arguments

[`input` ](#argument-input)· [`bulkUpdateTasksInput` ](/reference/2026-01-01/input-objects/bulkupdatetasksinput)· Parameters for bulkUpdateTasks

## Returns

[`bulkUpdateTasksPayload`](/reference/2026-01-01/objects/bulkupdatetaskspayload)

## Example

```
mutation updateTasksBulk($input: bulkUpdateTasksInput) {
  updateTasksBulk(input: $input) {
    messages
    tasks
  }
}
```
