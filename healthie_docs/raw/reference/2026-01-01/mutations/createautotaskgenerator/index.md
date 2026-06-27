---
title: createAutoTaskGenerator | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createautotaskgenerator/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createautotaskgenerator/index.md
---

Create auto task generator

## Arguments

[`input` ](#argument-input)· [`createAutoTaskGeneratorInput` ](/reference/2026-01-01/input-objects/createautotaskgeneratorinput)· Parameters for createAutoTaskGenerator

## Returns

[`createAutoTaskGeneratorPayload`](/reference/2026-01-01/objects/createautotaskgeneratorpayload)

## Example

```
mutation createAutoTaskGenerator($input: createAutoTaskGeneratorInput) {
  createAutoTaskGenerator(input: $input) {
    auto_task_generator
    messages
  }
}
```
