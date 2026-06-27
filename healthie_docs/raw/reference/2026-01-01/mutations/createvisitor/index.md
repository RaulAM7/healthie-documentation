---
title: createVisitor | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createvisitor/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createvisitor/index.md
---

Creates a Visitor

## Arguments

[`input` ](#argument-input)· [`createVisitorInput` ](/reference/2026-01-01/input-objects/createvisitorinput)· Parameters for createVisitor

## Returns

[`createVisitorPayload`](/reference/2026-01-01/objects/createvisitorpayload)

## Example

```
mutation createVisitor($input: createVisitorInput) {
  createVisitor(input: $input) {
    messages
    visitor
  }
}
```
