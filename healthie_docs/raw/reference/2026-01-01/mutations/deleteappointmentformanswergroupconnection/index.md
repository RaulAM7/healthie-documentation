---
title: deleteAppointmentFormAnswerGroupConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteappointmentformanswergroupconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteappointmentformanswergroupconnection/index.md
---

Remove a form\_answer\_groups connection to an appointment

## Arguments

[`input` ](#argument-input)· [`deleteAppointmentFormAnswerGroupConnectionInput` ](/reference/2026-01-01/input-objects/deleteappointmentformanswergroupconnectioninput)· Parameters for deleteAppointmentFormAnswerGroupConnection

## Returns

[`deleteAppointmentFormAnswerGroupConnectionPayload`](/reference/2026-01-01/objects/deleteappointmentformanswergroupconnectionpayload)

## Example

```
mutation deleteAppointmentFormAnswerGroupConnection(
  $input: deleteAppointmentFormAnswerGroupConnectionInput
) {
  deleteAppointmentFormAnswerGroupConnection(input: $input) {
    form_answer_group
    messages
  }
}
```
