---
title: deleteAutoTaskGenerator | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteautotaskgenerator/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteautotaskgenerator/index.md
---

Delete auto task generator

## Arguments

[`input` ](#argument-input)· [`deleteAutoTaskGeneratorInput` ](/reference/2026-01-01/input-objects/deleteautotaskgeneratorinput)· Parameters for deleteAutoTaskGenerator

## Returns

[`deleteAutoTaskGeneratorPayload`](/reference/2026-01-01/objects/deleteautotaskgeneratorpayload)

## Example

```
mutation deleteAutoTaskGenerator($input: deleteAutoTaskGeneratorInput) {
  deleteAutoTaskGenerator(input: $input) {
    auto_task_generator
    messages
  }
}
```
