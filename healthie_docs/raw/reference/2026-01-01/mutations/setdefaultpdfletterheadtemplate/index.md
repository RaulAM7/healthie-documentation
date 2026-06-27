---
title: setDefaultPdfLetterheadTemplate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/setdefaultpdfletterheadtemplate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/setdefaultpdfletterheadtemplate/index.md
---

Set \`PdfLetterheadTemplate\` default for the org

## Arguments

[`input` ](#argument-input)· [`setDefaultPdfLetterheadTemplateInput` ](/reference/2026-01-01/input-objects/setdefaultpdfletterheadtemplateinput)· Parameters for setDefaultPdfLetterheadTemplate

## Returns

[`setDefaultPdfLetterheadTemplatePayload`](/reference/2026-01-01/objects/setdefaultpdfletterheadtemplatepayload)

## Example

```
mutation setDefaultPdfLetterheadTemplate(
  $input: setDefaultPdfLetterheadTemplateInput
) {
  setDefaultPdfLetterheadTemplate(input: $input) {
    messages
    organization
    pdf_letterhead_template
  }
}
```
