---
title: PdfLetterheadTemplateTeamMemberNameSource | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/pdfletterheadtemplateteammembernamesource/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/pdfletterheadtemplateteammembernamesource/index.md
---

The source used to populate the team member name shown on the letterhead.

## Used By

[`PdfLetterheadTemplate.team_member_name_source`](/reference/2026-01-01/objects/pdfletterheadtemplate)

[`createPdfLetterheadTemplateInput.team_member_name_source`](/reference/2026-01-01/input-objects/createpdfletterheadtemplateinput)

[`updatePdfLetterheadTemplateInput.team_member_name_source`](/reference/2026-01-01/input-objects/updatepdfletterheadtemplateinput)

## Definition

```
"""
The source used to populate the team member name shown on the letterhead.
"""
enum PdfLetterheadTemplateTeamMemberNameSource {
  CURRENT_USER
  PRIMARY_PROVIDER
}
```
