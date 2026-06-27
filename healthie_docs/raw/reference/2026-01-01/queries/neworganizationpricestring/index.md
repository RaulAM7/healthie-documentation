---
title: newOrganizationPriceString | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/neworganizationpricestring/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/neworganizationpricestring/index.md
---

String containing info for the user about the org upgrade price

## Arguments

[`new_provder_num` ](#argument-new-provder-num)· [`Int`](/reference/2026-01-01/scalars/int)

[`new_provider_num` ](#argument-new-provider-num)· [`Int`](/reference/2026-01-01/scalars/int)

## Returns

[`String`](/reference/2026-01-01/scalars/string)

## Example

```
query newOrganizationPriceString(
  $new_provder_num: Int
  $new_provider_num: Int
) {
  newOrganizationPriceString(
    new_provder_num: $new_provder_num
    new_provider_num: $new_provider_num
  )
}
```
