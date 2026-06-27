---
title: offeringCoupons | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/offeringcoupons/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/offeringcoupons/index.md
---

Fetch paginated coupon offerings collection

## Arguments

[`from_package_details` ](#argument-from-package-details)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`offering_id` ](#argument-offering-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`OfferingCouponOrderKeys`](/reference/2026-01-01/enums/offeringcouponorderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`OfferingCouponPaginationConnection`](/reference/2026-01-01/objects/offeringcouponpaginationconnection)

## Example

```
query offeringCoupons(
  $from_package_details: Boolean
  $keywords: String
  $offering_id: ID
  $user_id: ID
  $sort_by: String
  $order_by: OfferingCouponOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  offeringCoupons(
    from_package_details: $from_package_details
    keywords: $keywords
    offering_id: $offering_id
    user_id: $user_id
    sort_by: $sort_by
    order_by: $order_by
    after: $after
    before: $before
    first: $first
    last: $last
  ) {
    edges
    nodes
    page_info
    total_count
  }
}
```
