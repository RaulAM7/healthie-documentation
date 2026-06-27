---
title: offering | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/offering/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/offering/index.md
---

fetch an offering by id (considered public)

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`Offering`](/reference/2026-01-01/objects/offering)

## Example

```
query offering($id: ID) {
  offering(id: $id) {
    abbreviated_frequency_times_string
    archived
    ask_for_cc
    billing_frequency
    billing_items_count
    can_be_gifted
    charge_immediately
    course_id
    created_at
    currency
    description
    embed_question_form_id
    fb_pixel
    first_time_payment
    frequency_times_string
    id
    immediate_purchase_url
    includes_ended_fixed_course
    initial_payment_amount
    initial_price_with_taxes
    living_plate_meal_plan_id
    living_plate_meal_plan_name
    living_plate_preview_url
    max_purchases
    meal_plan_options
    minimum_quantity
    name
    offering_courses
    offering_group_visibilities
    offering_image
    offering_image_id
    offering_image_url
    offering_includes
    offering_includes_count
    offering_lab_options
    offering_product_taxes
    offering_products
    on_purchase_ifs_tag_id
    override_group_on_purchase
    price
    price_per_minute
    repeat_times
    require_booking_purchase
    row_order
    selected_image_id
    show_free_text
    show_offering
    show_price
    start_fb_pixel
    total_revenue
    under_purchase_cap
    updated_at
    user
    user_group_id
    user_group_name
    user_id
    user_package_selections_count
    user_pays
    video_url
    visibility_status
  }
}
```
