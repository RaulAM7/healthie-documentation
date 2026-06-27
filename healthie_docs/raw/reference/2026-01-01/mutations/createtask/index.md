---
title: createTask | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createtask/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createtask/index.md
---

Create a task for provider

## Arguments

[`input` ](#argument-input)· [`createTaskInput` ](/reference/2026-01-01/input-objects/createtaskinput)· Parameters for createTask

## Returns

[`createTaskPayload`](/reference/2026-01-01/objects/createtaskpayload)

## Example

```
mutation createTask($input: createTaskInput) {
  createTask(input: $input) {
    messages
    task
  }
}
```
