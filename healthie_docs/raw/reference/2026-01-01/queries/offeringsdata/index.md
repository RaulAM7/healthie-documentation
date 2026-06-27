---
title: offeringsData | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/offeringsdata/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/offeringsdata/index.md
---

returns metadata about offerings purchased

## Arguments

[`org_level` ](#argument-org-level)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

## Returns

[`[OfferingsDataType!]`](/reference/2026-01-01/objects/offeringsdatatype)

## Example

```
query offeringsData($org_level: Boolean) {
  offeringsData(org_level: $org_level) {
    freq
    month
  }
}
```
