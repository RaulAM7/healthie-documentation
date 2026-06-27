---
title: updateNoteScheduler | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatenotescheduler/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatenotescheduler/index.md
---

Update a Note Scheduler and return NoteSchedulerType

## Arguments

[`input` ](#argument-input)· [`updateNoteSchedulerInput` ](/reference/2026-01-01/input-objects/updatenoteschedulerinput)· Parameters for updateNoteScheduler

## Returns

[`updateNoteSchedulerPayload`](/reference/2026-01-01/objects/updatenoteschedulerpayload)

## Example

```
mutation updateNoteScheduler($input: updateNoteSchedulerInput) {
  updateNoteScheduler(input: $input) {
    messages
    noteScheduler
  }
}
```
