---
title: Offering | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/offering/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/offering/index.md
---

Offering (or Package)

## Fields

[`abbreviated_frequency_times_string` ](#field-abbreviated-frequency-times-string)· [`String` ](/reference/2026-01-01/scalars/string)· Formatted frequency string abbreviated for offering list page

[`archived` ](#field-archived)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether or not this packages has been archived

[`ask_for_cc` ](#field-ask-for-cc)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Ask for a CC (even on a free package)

[`billing_frequency` ](#field-billing-frequency)· [`String` ](/reference/2026-01-01/scalars/string)· frequency client will be billed for package

[`billing_items_count` ](#field-billing-items-count)· [`Int` ](/reference/2026-01-01/scalars/int)· count of billing items for a given offering

[`can_be_gifted` ](#field-can-be-gifted)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · True if package is allowed to be gifted to other clients. Currently only available for non-recurring offerings

[`charge_immediately` ](#field-charge-immediately)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If false the payment for the offering should be collected manually at a later time

[`course_id` ](#field-course-id)· [`ID` ](/reference/2026-01-01/scalars/id)· course id associated with this package

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · created at

[`currency` ](#field-currency)· [`String` ](/reference/2026-01-01/scalars/string)· currency used to pay for this package

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· Description of the package, not allowing nil

[`embed_question_form_id` ](#field-embed-question-form-id)· [`String` ](/reference/2026-01-01/scalars/string)· ID of the embedded custom module form

[`fb_pixel` ](#field-fb-pixel)· [`String` ](/reference/2026-01-01/scalars/string)· fb\_pixel

[`first_time_payment` ](#field-first-time-payment)· [`String` ](/reference/2026-01-01/scalars/string)· first time payment price of package

[`frequency_times_string` ](#field-frequency-times-string)· [`String` ](/reference/2026-01-01/scalars/string)· Formatted frequency string

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the offering

[`immediate_purchase_url` ](#field-immediate-purchase-url)· [`String` ](/reference/2026-01-01/scalars/string)· A URL to purchase the package

[`includes_ended_fixed_course` ](#field-includes-ended-fixed-course)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the package includes a course that has ended

[`initial_payment_amount` ](#field-initial-payment-amount)· [`String` ](/reference/2026-01-01/scalars/string)· initial payment amount of package

[`initial_price_with_taxes` ](#field-initial-price-with-taxes)· [`String` ](/reference/2026-01-01/scalars/string)· initial price of package including applicable taxes

[`living_plate_meal_plan_id` ](#field-living-plate-meal-plan-id)· [`String` ](/reference/2026-01-01/scalars/string)· selected meal plan from living plate

[`living_plate_meal_plan_name` ](#field-living-plate-meal-plan-name)· [`String` ](/reference/2026-01-01/scalars/string)· if this offering has a living plate meal plan associated, returns a link to living plate meal plan preview

[`living_plate_preview_url` ](#field-living-plate-preview-url)· [`String` ](/reference/2026-01-01/scalars/string)· if this offering has a living plate meal plan associated, returns a link to living plate meal plan preview

[`max_purchases` ](#field-max-purchases)· [`String` ](/reference/2026-01-01/scalars/string)· Number of times the package could be purchased. Unlimited if set to nil

[`meal_plan_options` ](#field-meal-plan-options)· [`[MealPlan!]` ](/reference/2026-01-01/objects/mealplan)· meal plan options in offering (currently only from living plate)

[`minimum_quantity` ](#field-minimum-quantity)· [`String` ](/reference/2026-01-01/scalars/string)· minimum\_quantity

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· name of package

[`offering_courses` ](#field-offering-courses)· [`[OfferingCourse!]` ](/reference/2026-01-01/objects/offeringcourse)· courses related to offering

[`offering_group_visibilities` ](#field-offering-group-visibilities)· [`[OfferingGroupVisibility!]` ](/reference/2026-01-01/objects/offeringgroupvisibility)· user groups that are specific to this offering

[`offering_image` ](#field-offering-image)· [`OfferingImage` ](/reference/2026-01-01/objects/offeringimage)· offering image

[`offering_image_id` ](#field-offering-image-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of offering image

[`offering_image_url` ](#field-offering-image-url)· [`String` ](/reference/2026-01-01/scalars/string)· URL of the offering image to use

[`offering_includes` ](#field-offering-includes)· [`[OfferingInclude!]` ](/reference/2026-01-01/objects/offeringinclude)· appointment types related to offering

[`offering_includes_count` ](#field-offering-includes-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · count of offering includes associated with offering

[`offering_lab_options` ](#field-offering-lab-options)· [`[OfferingLabOption!]` ](/reference/2026-01-01/objects/offeringlaboption)· lab options included in offering

[`offering_product_taxes` ](#field-offering-product-taxes)· [`Float` ](/reference/2026-01-01/scalars/float)· Taxes on offering products

[`offering_products` ](#field-offering-products)· [`[OfferingProduct!]` ](/reference/2026-01-01/objects/offeringproduct)· Products included in the offering

[`on_purchase_ifs_tag_id` ](#field-on-purchase-ifs-tag-id)· [`String` ](/reference/2026-01-01/scalars/string)· on on\_purchase\_ifs\_tag\_id

[`override_group_on_purchase` ](#field-override-group-on-purchase)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Shows whether user group should be changed when client which is already in the user group is buying the package

[`price` ](#field-price)· [`String` ](/reference/2026-01-01/scalars/string)· price of package

[`price_per_minute` ](#field-price-per-minute)· [`String` ](/reference/2026-01-01/scalars/string)· price per minute

[`repeat_times` ](#field-repeat-times)· [`Int` ](/reference/2026-01-01/scalars/int)· repeat times

[`require_booking_purchase` ](#field-require-booking-purchase)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · When true, the package requires appointment booking during package purchase

[`row_order` ](#field-row-order)· [`String` ](/reference/2026-01-01/scalars/string)· position of package when displayed in packages list

[`selected_image_id` ](#field-selected-image-id)· [`String` ](/reference/2026-01-01/scalars/string)· offering image id

[`show_free_text` ](#field-show-free-text)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · show free text to customers on offerings of zero price

[`show_offering` ](#field-show-offering)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · show offering toggle

[`show_price` ](#field-show-price)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · show price toggle

[`start_fb_pixel` ](#field-start-fb-pixel)· [`String` ](/reference/2026-01-01/scalars/string)· start\_fb\_pixel

[`total_revenue` ](#field-total-revenue)· [`Float` ](/reference/2026-01-01/scalars/float)· total of billing\_items.amount\_paid for a given offering

[`under_purchase_cap` ](#field-under-purchase-cap)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When false, the package is at its purchase cap, and cannot be bought by a client

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · updated at

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The user who owns the package

[`user_group_id` ](#field-user-group-id)· [`ID` ](/reference/2026-01-01/scalars/id)· user group id associated with this package

[`user_group_name` ](#field-user-group-name)· [`String` ](/reference/2026-01-01/scalars/string)· User group name associated with this offering

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of user

[`user_package_selections_count` ](#field-user-package-selections-count)· [`Int` ](/reference/2026-01-01/scalars/int)· count of user package selections for a given offering

[`user_pays` ](#field-user-pays)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · user pays toggle

[`video_url` ](#field-video-url)· [`String` ](/reference/2026-01-01/scalars/string)· video associated with offering

[`visibility_status` ](#field-visibility-status)· [`String!` ](/reference/2026-01-01/scalars/string)· required · Whether the package is visible to all or to a specific group or completely hidden.

## Used By

[`AppointmentCreditChange.offering`](/reference/2026-01-01/objects/appointmentcreditchange)

[`BillingItem.offering`](/reference/2026-01-01/objects/billingitem)

[`Course.offerings`](/reference/2026-01-01/objects/course)

[`FormAnswerGroup.offering_with_recommended_products`](/reference/2026-01-01/objects/formanswergroup)

[`OfferingEdge.node`](/reference/2026-01-01/objects/offeringedge)

[`OfferingPaginationConnection.nodes`](/reference/2026-01-01/objects/offeringpaginationconnection)

[`RequestedPayment.offering`](/reference/2026-01-01/objects/requestedpayment)

[`ScheduledUserPackageSelection.offering`](/reference/2026-01-01/objects/scheduleduserpackageselection)

[`User.offerings`](/reference/2026-01-01/objects/user)

[`UserPackageSelection.offering`](/reference/2026-01-01/objects/userpackageselection)

[`copyOfferingPayload.offering`](/reference/2026-01-01/objects/copyofferingpayload)

[`createOfferingPayload.offering`](/reference/2026-01-01/objects/createofferingpayload)

[`deleteOfferingPayload.offering`](/reference/2026-01-01/objects/deleteofferingpayload)

[`updateOfferingPayload.offering`](/reference/2026-01-01/objects/updateofferingpayload)

[`Query.offering`](/reference/2026-01-01/queries/offering)

## Definition

```
"""
Offering (or Package)
"""
type Offering {
  """
  Formatted frequency string abbreviated for offering list page
  """
  abbreviated_frequency_times_string: String


  """
  Whether or not this packages has been archived
  """
  archived: Boolean!


  """
  Ask for a CC (even on a free package)
  """
  ask_for_cc: Boolean!


  """
  frequency client will be billed for package
  """
  billing_frequency: String


  """
  count of billing items for a given offering
  """
  billing_items_count: Int


  """
  True if package is allowed to be gifted to other clients. Currently only available for non-recurring offerings
  """
  can_be_gifted: Boolean!


  """
  If false the payment for the offering should be collected manually at a later time
  """
  charge_immediately: Boolean!


  """
  course id associated with this package
  """
  course_id: ID


  """
  created at
  """
  created_at: ISO8601DateTime!


  """
  currency used to pay for this package
  """
  currency: String


  """
  Description of the package, not allowing nil
  """
  description: String


  """
  ID of the embedded custom module form
  """
  embed_question_form_id: String


  """
  fb_pixel
  """
  fb_pixel: String


  """
  first time payment price of package
  """
  first_time_payment: String


  """
  Formatted frequency string
  """
  frequency_times_string: String


  """
  The unique identifier of the offering
  """
  id: ID!


  """
  A URL to purchase the package
  """
  immediate_purchase_url: String


  """
  Whether the package includes a course that has ended
  """
  includes_ended_fixed_course: Boolean


  """
  initial payment amount of package
  """
  initial_payment_amount: String


  """
  initial price of package including applicable taxes
  """
  initial_price_with_taxes: String


  """
  selected meal plan from living plate
  """
  living_plate_meal_plan_id: String


  """
  if this offering has a living plate meal plan associated, returns a link to living plate meal plan preview
  """
  living_plate_meal_plan_name: String


  """
  if this offering has a living plate meal plan associated, returns a link to living plate meal plan preview
  """
  living_plate_preview_url: String


  """
  Number of times the package could be purchased. Unlimited if set to nil
  """
  max_purchases: String


  """
  meal plan options in offering (currently only from living plate)
  """
  meal_plan_options: [MealPlan!]


  """
  minimum_quantity
  """
  minimum_quantity: String


  """
  name of package
  """
  name: String


  """
  courses related to offering
  """
  offering_courses: [OfferingCourse!]


  """
  user groups that are specific to this offering
  """
  offering_group_visibilities: [OfferingGroupVisibility!]


  """
  offering image
  """
  offering_image: OfferingImage


  """
  id of offering image
  """
  offering_image_id: ID


  """
  URL of the offering image to use
  """
  offering_image_url: String


  """
  appointment types related to offering
  """
  offering_includes(
    """
    If present, only return offering includes that include the given appointment type
    """
    appointment_type_id: ID


    """
    If true, only return offering includes that are bookable by the client
    """
    only_bookable_by_client: Boolean
  ): [OfferingInclude!]


  """
  count of offering includes associated with offering
  """
  offering_includes_count: Int!


  """
  lab options included in offering
  """
  offering_lab_options: [OfferingLabOption!]


  """
  Taxes on offering products
  """
  offering_product_taxes: Float


  """
  Products included in the offering
  """
  offering_products: [OfferingProduct!]


  """
  on on_purchase_ifs_tag_id
  """
  on_purchase_ifs_tag_id: String


  """
  Shows whether user group should be changed when client which is already in the user group is buying the package
  """
  override_group_on_purchase: Boolean!


  """
  price of package
  """
  price: String


  """
  price per minute
  """
  price_per_minute: String


  """
  repeat times
  """
  repeat_times: Int


  """
  When true, the package requires appointment booking during package purchase
  """
  require_booking_purchase: Boolean!


  """
  position of package when displayed in packages list
  """
  row_order: String


  """
  offering image id
  """
  selected_image_id: String


  """
  show free text to customers on offerings of zero price
  """
  show_free_text: Boolean!


  """
  show offering toggle
  """
  show_offering: Boolean!


  """
  show price toggle
  """
  show_price: Boolean!


  """
  start_fb_pixel
  """
  start_fb_pixel: String


  """
  total of billing_items.amount_paid for a given offering
  """
  total_revenue: Float


  """
  When false, the package is at its purchase cap, and cannot be bought by a client
  """
  under_purchase_cap: Boolean


  """
  updated at
  """
  updated_at: ISO8601DateTime!


  """
  The user who owns the package
  """
  user: User


  """
  user group id associated with this package
  """
  user_group_id: ID


  """
  User group name associated with this offering
  """
  user_group_name: String


  """
  id of user
  """
  user_id: ID


  """
  count of user package selections for a given offering
  """
  user_package_selections_count: Int


  """
  user pays toggle
  """
  user_pays: Boolean!


  """
  video associated with offering
  """
  video_url: String


  """
  Whether the package is visible to all or to a specific group or completely hidden.
  """
  visibility_status: String!
}
```
