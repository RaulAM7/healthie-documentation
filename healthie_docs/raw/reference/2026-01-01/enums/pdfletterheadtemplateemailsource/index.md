---
title: PdfLetterheadTemplateEmailSource | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/pdfletterheadtemplateemailsource/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/pdfletterheadtemplateemailsource/index.md
---

The source used to populate the email address shown on the letterhead.

## Used By

[`PdfLetterheadTemplate.email_source`](/reference/2026-01-01/objects/pdfletterheadtemplate)

[`createPdfLetterheadTemplateInput.email_source`](/reference/2026-01-01/input-objects/createpdfletterheadtemplateinput)

[`updatePdfLetterheadTemplateInput.email_source`](/reference/2026-01-01/input-objects/updatepdfletterheadtemplateinput)

## Definition

```
"""
The source used to populate the email address shown on the letterhead.
"""
enum PdfLetterheadTemplateEmailSource {
  ORGANIZATION
  CURRENT_USER
  PRIMARY_PROVIDER
  OTHER
}
```
