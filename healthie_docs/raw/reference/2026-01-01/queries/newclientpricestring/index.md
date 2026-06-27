---
title: newClientPriceString | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/newclientpricestring/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/newclientpricestring/index.md
---

String containing info for the user about the client upgrade price

## Arguments

[`new_client_num` ](#argument-new-client-num)· [`Int`](/reference/2026-01-01/scalars/int)

## Returns

[`String`](/reference/2026-01-01/scalars/string)

## Example

```
query newClientPriceString($new_client_num: Int) {
  newClientPriceString(new_client_num: $new_client_num)
}
```
