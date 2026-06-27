---
title: newOrganizationSupportPriceString | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/neworganizationsupportpricestring/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/neworganizationsupportpricestring/index.md
---

String containing info for the user about the org upgrade price when adding a new support user

## Arguments

[`new_support_num` ](#argument-new-support-num)· [`Int`](/reference/2026-01-01/scalars/int)

## Returns

[`[String]`](/reference/2026-01-01/scalars/string)

## Example

```
query newOrganizationSupportPriceString($new_support_num: Int) {
  newOrganizationSupportPriceString(new_support_num: $new_support_num)
}
```
