---
title: PdfLetterheadTemplatePhoneNumberSource | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/pdfletterheadtemplatephonenumbersource/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/pdfletterheadtemplatephonenumbersource/index.md
---

The source used to populate the phone number shown on the letterhead.

## Used By

[`PdfLetterheadTemplate.phone_number_source`](/reference/2026-01-01/objects/pdfletterheadtemplate)

[`createPdfLetterheadTemplateInput.phone_number_source`](/reference/2026-01-01/input-objects/createpdfletterheadtemplateinput)

[`updatePdfLetterheadTemplateInput.phone_number_source`](/reference/2026-01-01/input-objects/updatepdfletterheadtemplateinput)

## Definition

```
"""
The source used to populate the phone number shown on the letterhead.
"""
enum PdfLetterheadTemplatePhoneNumberSource {
  ORGANIZATION
  CURRENT_USER
  PRIMARY_PROVIDER
  OTHER
}
```
