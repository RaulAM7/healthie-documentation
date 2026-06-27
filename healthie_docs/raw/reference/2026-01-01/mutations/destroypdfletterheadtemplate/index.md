---
title: destroyPdfLetterheadTemplate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/destroypdfletterheadtemplate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/destroypdfletterheadtemplate/index.md
---

Delete \`PdfLetterheadTemplate\`

## Arguments

[`input` ](#argument-input)· [`destroyPdfLetterheadTemplateInput` ](/reference/2026-01-01/input-objects/destroypdfletterheadtemplateinput)· Parameters for destroyPdfLetterheadTemplate

## Returns

[`destroyPdfLetterheadTemplatePayload`](/reference/2026-01-01/objects/destroypdfletterheadtemplatepayload)

## Example

```
mutation destroyPdfLetterheadTemplate(
  $input: destroyPdfLetterheadTemplateInput
) {
  destroyPdfLetterheadTemplate(input: $input) {
    messages
    organization
    pdf_letterhead_template
  }
}
```
