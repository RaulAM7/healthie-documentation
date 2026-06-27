---
title: createOrAddToWaterIntakeEntry | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createoraddtowaterintakeentry/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createoraddtowaterintakeentry/index.md
---

creates a new entry or add to existing water intake entry for the day

## Arguments

[`input` ](#argument-input)· [`createOrAddToWaterIntakeEntryInput` ](/reference/2026-01-01/input-objects/createoraddtowaterintakeentryinput)· Parameters for createOrAddToWaterIntakeEntry

## Returns

[`createOrAddToWaterIntakeEntryPayload`](/reference/2026-01-01/objects/createoraddtowaterintakeentrypayload)

## Example

```
mutation createOrAddToWaterIntakeEntry(
  $input: createOrAddToWaterIntakeEntryInput
) {
  createOrAddToWaterIntakeEntry(input: $input) {
    entry
    messages
  }
}
```
