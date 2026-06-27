---
title: updateGeneratedFormAnswerGroupFeedback | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updategeneratedformanswergroupfeedback/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updategeneratedformanswergroupfeedback/index.md
---

Updates feedback for an AI-generated form answer group

## Arguments

[`input` ](#argument-input)· [`updateGeneratedFormAnswerGroupFeedbackInput` ](/reference/2026-01-01/input-objects/updategeneratedformanswergroupfeedbackinput)· Parameters for updateGeneratedFormAnswerGroupFeedback

## Returns

[`updateGeneratedFormAnswerGroupFeedbackPayload`](/reference/2026-01-01/objects/updategeneratedformanswergroupfeedbackpayload)

## Example

```
mutation updateGeneratedFormAnswerGroupFeedback(
  $input: updateGeneratedFormAnswerGroupFeedbackInput
) {
  updateGeneratedFormAnswerGroupFeedback(input: $input) {
    generated_form_answer_group
    messages
  }
}
```
