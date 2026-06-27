---
title: updateAutoTaskGenerator | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateautotaskgenerator/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateautotaskgenerator/index.md
---

Update auto task generator

## Arguments

[`input` ](#argument-input)· [`updateAutoTaskGeneratorInput` ](/reference/2026-01-01/input-objects/updateautotaskgeneratorinput)· Parameters for updateAutoTaskGenerator

## Returns

[`updateAutoTaskGeneratorPayload`](/reference/2026-01-01/objects/updateautotaskgeneratorpayload)

## Example

```
mutation updateAutoTaskGenerator($input: updateAutoTaskGeneratorInput) {
  updateAutoTaskGenerator(input: $input) {
    auto_task_generator
    messages
  }
}
```
