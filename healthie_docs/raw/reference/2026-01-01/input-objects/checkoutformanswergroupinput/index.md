---
title: CheckoutFormAnswerGroupInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/checkoutformanswergroupinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/checkoutformanswergroupinput/index.md
---

Payload for a group of answers

## Fields

[`custom_module_form_id` ](#field-custom-module-form-id)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the custom module form

[`form_answers` ](#field-form-answers)· [`[CheckoutFormAnswerInput]` ](/reference/2026-01-01/input-objects/checkoutformanswerinput)· The list of answers for the form

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of the form answer group

## Used By

[`completeCheckoutInput.form_answer_group`](/reference/2026-01-01/input-objects/completecheckoutinput)

## Definition

```
"""
Payload for a group of answers
"""
input CheckoutFormAnswerGroupInput {
  """
  The id of the custom module form
  """
  custom_module_form_id: String


  """
  The list of answers for the form
  """
  form_answers: [CheckoutFormAnswerInput]


  """
  The id of the form answer group
  """
  id: ID
}
```
