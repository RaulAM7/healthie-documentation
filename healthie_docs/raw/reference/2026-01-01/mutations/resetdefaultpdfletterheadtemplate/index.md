---
title: resetDefaultPdfLetterheadTemplate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/resetdefaultpdfletterheadtemplate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/resetdefaultpdfletterheadtemplate/index.md
---

Set system default \`PdfLetterheadTemplate\` for current\_user's organization

## Arguments

[`input` ](#argument-input)· [`resetDefaultPdfLetterheadTemplateInput` ](/reference/2026-01-01/input-objects/resetdefaultpdfletterheadtemplateinput)· Parameters for resetDefaultPdfLetterheadTemplate

## Returns

[`resetDefaultPdfLetterheadTemplatePayload`](/reference/2026-01-01/objects/resetdefaultpdfletterheadtemplatepayload)

## Example

```
mutation resetDefaultPdfLetterheadTemplate(
  $input: resetDefaultPdfLetterheadTemplateInput
) {
  resetDefaultPdfLetterheadTemplate(input: $input) {
    messages
    organization
  }
}
```
