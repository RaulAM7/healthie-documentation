---
title: Packages | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/billing/packages/index
  md: https://docs.gethealthie.com/guides/billing/packages/index.md
---

## The Package Object

```
// Some Example Fields for an Offering


{
  "id": "1",
  "name": "Example Package",
  "price": "100.0",
  "currency": "USD",
  "repeat_times": null,
  "show_offering": false,
  "frequency_times_string": "a week",
  "abbreviated_frequency_times_string": "",
  "living_plate_meal_plan_name": null,
  "billing_frequency": "Weekly",
  "first_time_payment": null,
  "archived": false,
  "visibility_status": "hidden",
  "initial_payment_amount": "100.0",
  "initial_price_with_taxes": "100.0",
  "offering_includes": [
    {
      "id": "1",
      "quantity": "1",
      "is_repeating": true,
      "appointment_type": {
        "id": "1",
        "name": "Initial Consultation",
        "clients_can_book": true
      }
    },
    {
      "id": "2",
      "quantity": "3",
      "is_repeating": true,
      "appointment_type": {
        "id": "2",
        "name": "Follow-up Session",
        "clients_can_book": true
      }
    }
  ]
}
```

Within the API, Packages are known as `Offering` objects. In this documentation we will use both terms interchangeably.

You can view the full list of available fields [here](/reference/2024-06-01/objects/offering).

If you have questions about the overall functionality of Client Packages, you can find information [here](https://help.gethealthie.com/article/194-faq-client-packages).

## Retrieving a Package

```
query getOffernig($id: ID) {
  offering(id: $id) {
    id
    name
    billing_frequency
    currency
    price
    initial_payment_amount
    initial_price_with_taxes
  }
}
```

Retrieving a specific Package is done via the `offering` query.

| Input | Info                                      |
| ----- | ----------------------------------------- |
| `id`  | **Required**. ID of the Package to query. |

Returns an [`Offering`](/reference/2024-06-01/objects/offering) object.

## Creating a Package

```
mutation createOffering(
  $name: String
  $price: String
  $billing_frequency: String
  $offering_includes: [OfferingIncludesFields]
  $first_time_payment: String
  $visibility_status: String
  $charge_immediately: Boolean
  $course_ids: String
) {
  createOffering(
    input: {
      name: $name
      price: $price
      billing_frequency: $billing_frequency
      offering_includes: $offering_includes
      first_time_payment: $first_time_payment
      visibility_status: $visibility_status
      charge_immediately: $charge_immediately
      course_ids: $course_ids
    }
  ) {
    offering {
      id
    }
    messages {
      field
      message
    }
  }
}
```

Packages are created using the `createOffering` mutation.

The `createOffering` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createofferinginput). We will go over some of inputs used to create an Offering.

| Input                | Info                                                                                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`               | **Required**. The name of the Package.                                                                                                                              |
| `price`              | **Required**. Package price as string. Check the `minimumOfferingPrice` query to get a minimum Package price.                                                       |
| `billing_frequency`  | **Required**. Valid options are:- `One-Time`
- `Monthly`
- `Yearly`
- `Weekly`
- `Bi-Weekly`
- `Every 4 Weeks`
- `Every 8 Weeks`
- `Quarterly`                      |
| `offering_includes`  | Optional. A list of appointment sessions included in the Program. Objects of type [`OfferingIncludesFields`](/reference/2024-06-01/objects/offeringincludesfields). |
| `first_time_payment` | Optional. Price for the first payment.                                                                                                                              |
| `charge_immediately` | Optional. Whether to charge the Client immediately.                                                                                                                 |
| `course_ids`         | Optional. A comma-separated string of Program IDs to include in the Package.                                                                                        |

Returns a [`createOfferingPayload`](/reference/2024-06-01/objects/createofferingpayload) object.

## Updating a Package

```
mutation updateOffering(
  $name: String
  $price: String
  $billing_frequency: String
  $offering_includes: [OfferingIncludesFields]
  $first_time_payment: String
  $visibility_status: String
  $charge_immediately: Boolean
  $course_ids: String
) {
  updateOffering(
    input: {
      name: $name
      price: $price
      billing_frequency: $billing_frequency
      offering_includes: $offering_includes
      first_time_payment: $first_time_payment
      visibility_status: $visibility_status
      charge_immediately: $charge_immediately
      course_ids: $course_ids
    }
  ) {
    offering {
      id
    }
    messages {
      field
      message
    }
  }
}
```

Packages are updated via the `updateOffering` mutation.

The `updateOffering` mutation is called from an authenticated account.

The `updateOffering` mutation shares many common inputs with [`createOffering`](#creating-a-package) and those inputs (e.g `first_time_payment` or `visibility_status` work the same in both places).

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updateofferinginput).

| Input      | Info                                            |
| ---------- | ----------------------------------------------- |
| `id`       | **Required**. ID of the Package to update.      |
| `archived` | Optional. Set to `true` to archive the Package. |

Returns a [`updateOfferingPayload`](/reference/2024-06-01/objects/updateofferingpayload) object.

## Cloning a Package

```
mutation copyOffering($id: ID) {
  copyOffering(input: { id: $id }) {
    offering {
      id
    }


    messages {
      field
      message
    }
  }
}
```

You can create a copy of a Package by running the `copyOffering` mutation.

The `copyOffering` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/copyofferinginput).

| Input | Info                                      |
| ----- | ----------------------------------------- |
| `id`  | **Required**. ID of the Package to clone. |

Returns a [`copyOfferingPayload`](/reference/2024-06-01/objects/copyofferingpayload) object.

## Deleting a Package

```
mutation deleteOffering($id: ID) {
  deleteOffering(input: { id: $id }) {
    offering {
      id
    }


    messages {
      field
      message
    }
  }
}
```

Packages can be (soft) deleted by authorized providers and staff members via the `deleteOffering` mutation.

The `deleteOffering` mutation is called from an authenticated provider/staff account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deleteofferinginput).

| Input | Info                                       |
| ----- | ------------------------------------------ |
| `id`  | **Required**. ID of the Package to delete. |

Returns a [`deleteOfferingPayload`](/reference/2024-06-01/objects/deleteofferingpayload) object.

## Listing all Packages

```
query getOfferings(
  $offset: Int
  $should_paginate: Boolean
  $keywords: String
  $sort_by: String
  $provider_id: ID
  $offering_id: ID
  $offering_ids: [ID]
  $only_client_visible: Boolean
  $status: String
  $client_visibility: String
  $offering_user_group_id: ID
  $show_only_visible: Boolean
) {
  offerings(
    offset: $offset
    should_paginate: $should_paginate
    keywords: $keywords
    sort_by: $sort_by
    provider_id: $provider_id
    offering_id: $offering_id
    offering_ids: $offering_ids
    only_client_visible: $only_client_visible
    status: $status
    client_visibility: $client_visibility
    offering_user_group_id: $offering_user_group_id
    show_only_visible: $show_only_visible
  ) {
    id
    name
    billing_frequency
    currency
    price
    initial_payment_amount
    initial_price_with_taxes
  }
}
```

A list of Packages can be retrieved via the `offerings` query. This query is called from an authenticated account.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/offerings#arguments).

We will go over some of them below.

| Input                    | Info                                                                                                                                                                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `keywords`               | Optional. A term to search Packages by. Can be searched by the name, description and price fields.                                                                                                                                                            |
| `offering_id`            | Optional. An ID of a single Offering to return.                                                                                                                                                                                                               |
| `offering_ids`           | Optional. An array of Offering IDs to return.                                                                                                                                                                                                                 |
| `client_visibility`      | Optional. Filters by Package visibility to clients. Possible options:- `all` - return all Packages
- `visible` - Returns Packages with `visibility_status` equal to `visible_to_all` or `visible_to_specific_groups`
- `hidden` - return only hidden Packages |
| `show_only_visible`      | Optional. Returns Packages that are visible to everyone.                                                                                                                                                                                                      |
| `only_client_visible`    | Optional. Returns Packages that are either visibile to everyone or to the Client Groups that the current user belongs to.                                                                                                                                     |
| `offering_user_group_id` | Optional. Returns Packages that are visible only to a specific User Group.                                                                                                                                                                                    |
| `status`                 | Optional. Provide `archived` to fetch only archived Packages.                                                                                                                                                                                                 |

Returns a list of [`Offering`](/reference/2024-06-01/objects/offering) objects.
