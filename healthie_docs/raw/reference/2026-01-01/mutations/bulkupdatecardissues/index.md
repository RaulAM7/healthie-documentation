---
title: bulkUpdateCardIssues | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkupdatecardissues/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkupdatecardissues/index.md
---

Update unseen card issues on a provider

## Arguments

[`input` ](#argument-input)· [`bulkUpdateCardIssuesInput` ](/reference/2026-01-01/input-objects/bulkupdatecardissuesinput)· Parameters for bulkUpdateCardIssues

## Returns

[`bulkUpdateCardIssuesPayload`](/reference/2026-01-01/objects/bulkupdatecardissuespayload)

## Example

```
mutation bulkUpdateCardIssues($input: bulkUpdateCardIssuesInput) {
  bulkUpdateCardIssues(input: $input) {
    card_issues
    messages
  }
}
```
