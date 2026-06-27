---
title: createAppointmentFormAnswerGroupConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createappointmentformanswergroupconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createappointmentformanswergroupconnection/index.md
---

Create a connection between a form answer group and an appointment.

## Arguments

[`input` ](#argument-input)· [`createAppointmentFormAnswerGroupConnectionInput` ](/reference/2026-01-01/input-objects/createappointmentformanswergroupconnectioninput)· Parameters for createAppointmentFormAnswerGroupConnection

## Returns

[`createAppointmentFormAnswerGroupConnectionPayload`](/reference/2026-01-01/objects/createappointmentformanswergroupconnectionpayload)

## Example

```
mutation createAppointmentFormAnswerGroupConnection(
  $input: createAppointmentFormAnswerGroupConnectionInput
) {
  createAppointmentFormAnswerGroupConnection(input: $input) {
    appointment
    form_answer_group
    messages
  }
}
```
