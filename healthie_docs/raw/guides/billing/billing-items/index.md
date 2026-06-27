---
title: Billing Items | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/billing/billing-items/index
  md: https://docs.gethealthie.com/guides/billing/billing-items/index.md
---

### The Billing Item Object

```
{
  "id": "1",
  "amount_paid": "1234.00",
  "currency": "USD",
  "note": "Test payment",
  "provider": {
    "id": "1"
  },
  "recipient": {
    "id": "1"
  },
  "sender": {
    "id": "2"
  }
}
```

Billing Items are `BillingItem` objects.

You can view the full list of available fields [here](/reference/2024-06-01/objects/billingitem).

### Listing Billing Items

```
query billingItems(
  $offset: Int
  keywords: String
  sort_by: String
  state: String
  provider_id: ID
  offerings_only: Boolean
) {
  billingItems(
    offset: $offset,
    keywords: $keywords,
    sort_by: $sort_by,
    state: $state,
    provider_id: $provider_id,
    offerings_only: $offerings_only
  ) {
    id
    amount_paid
    currency
    created_at
    failure_reason
    sender {
      id
    }
    recipient {
      id
    }
  }
}
```

Listing Billing Item is done via the `billingItems` query.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/billingitems#arguments).

| Input            | Info                                                                                                                                                                                                                                                 |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `offset`         | Optional. Offset for pagination.                                                                                                                                                                                                                     |
| `sort_by`        | Optional. Valid options are:- `newest` (default)
- `oldest`
- `smallestamount`
- `largestamount`
- `patient_name_asc`
- `patient_name_desc`
- `provider_name_asc`
- `provider_name_desc`
- `method_asc`
- `method_desc`
- `state_asc`
- `state_desc` |
| `keywords`       | Optional. Keywords to search by. Billing Items can be searched by `amount_paid` and `payment_medium`.                                                                                                                                                |
| `state`          | Optional. Valid options are:- `failed`
- `scheduled`
- `succeeded`                                                                                                                                                                                   |
| `offerings_only` | Optional. Return only Billing Items that are associated to an offering.                                                                                                                                                                              |

Returns a list of [`BillingItem`](/reference/2024-06-01/objects/billingitem) objects.

### Retrieving a Billing Item

```
query billingItem($id: ID) {
  billingItem(id: $id) {
    id
    amount_paid
    currency
    created_at
    failure_reason
    sender {
      id
    }
    recipient {
      id
    }
  }
}
```

Retrieving a specific Billing Item is done via the `billingItem` query.

| Input | Info                                           |
| ----- | ---------------------------------------------- |
| `id`  | **Required**. ID of the Billing Item to query. |

Returns a [`BillingItem`](/reference/2024-06-01/objects/billingitem) object.

### Creating a Billing Item

```
mutation createBillingItem(
  $amount_paid: String # e.g "567.53"
  $sender_id: ID # e.g "61"
  $requested_payment_id: ID # e.g 11
  $stripe_idempotency_key: String # Stripe recommends using V4 UUIDs
  $stripe_customer_detail_id: ID # e.g 21
  $should_charge: Boolean # true
) {
  createBillingItem(
    input: {
      amount_paid: $amount_paid
      sender_id: $sender_id
      should_charge: $should_charge
      stripe_customer_detail_id: $stripe_customer_detail_id
      requested_payment_id: $requested_payment_id
      stripe_idempotency_key: $stripe_idempotency_key
    }
  ) {
    billingItem {
      id
    }
    messages {
      field
      message
    }
  }
}
```

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createbillingiteminput).

| Input                       | Info                                                                                                                                                                                                                                                                   |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `created_at`                | Optional. Used when [tracking outside payments](https://help.gethealthie.com/article/294-viewing-payment-history-processing-and-past#Section1), and should be left out when actually charging a card.                                                                  |
| `amount_paid`               | Optional. The amount to charging the patient. If left blank, the patient will be charged the full amount of the package or invoice.                                                                                                                                    |
| `note`                      | Optional. Used to provide info about outside payments.                                                                                                                                                                                                                 |
| `sender_id`                 | **Required**. The ID of the patient to charge.                                                                                                                                                                                                                         |
| `recipient_id`              | Optional. The ID of the provider/staff member who should be listed as the recipient of the payment. This is primarily important in sitatuons where each provider has their own bank account. If left out, it defaults to the sender’s primary provider.                |
| `payment_medium`            | Optional. Used for outside payments and can be ignored.                                                                                                                                                                                                                |
| `offering_coupon_id`        | Optional. is the ID of the promo code you want to apply to the payment. The promo code discount is applied to the initial payment amount. (e.g if you want to apply a 30% promo code, and have the client end up paying $700, you would pass in amount\_paid of 1000). |
| `offering_id`               | The ID of the package that the patient is paying for. If you are charging the patient for a package via an invoice connected to the package, you should send in the `requested_payment_id` instead.                                                                    |
| `should_charge`             | Determine whether the charge actually runs through our payment processor. This should be passed in as true if you want to charge the card.                                                                                                                             |
| `stripe_customer_detail_id` | Optional. The ID of the `StripeCustomerDetail` (e.g the payment source) that the patient is using to pay. If left out, the patient is charged on their default payment source.                                                                                         |
| `requested_payment_id`      | Optional. The ID of the invoice that the patient is paying for. You can have the patient make multiple payments that apply to the same invoice. To do so, just include the same `requested_payment_id` in each charge.                                                 |
| `user_package_selection_id` | Optional. Is only used if you are charging a patient for an existing `UserPackageSelection`.                                                                                                                                                                           |
| `stripe_idempotency_key`    | Optional. A key generated on the front-end that is used by Stripe to prevent duplicate requests. Find more info about them [here](https://stripe.com/docs/api/idempotent_requests). This is optional, but highly recommended.                                          |

Returns a [`createBillingItemPayload`](/reference/2024-06-01/objects/createbillingitempayload) object.

Sometimes the charge will be declined by the card issuer. The decline reason is included in the `messages` you can get back from the mutation. For more information on specific decline reasons, please view [Stripe’s list of decline codes](https://stripe.com/docs/declines/codes).

### Updating a Billing Item

```
mutation updateBillingItem(
  $id: ID
  $amount_paid: String # e.g "567.53"
  $sender_id: ID # e.g "61"
  $stripe_idempotency_key: String # Stripe recommends using V4 UUIDs
  $resend_payment: Boolean
) {
  updateBillingItem(
    input: {
      id: $id
      amount_paid: $amount_paid
      sender_id: $sender_id
      stripe_idempotency_key: $stripe_idempotency_key
      resend_payment: $resend_payment
    }
  ) {
    billingItem {
      id
    }
    messages {
      field
      message
    }
  }
}
```

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updatebillingiteminput).

| Input                    | Info                                                                                                                                                                                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                     | **Required**. The ID of the Billing Item to update.                                                                                                                                                                                                     |
| `created_at`             | Optional. Used when [tracking outside payments](https://help.gethealthie.com/article/294-viewing-payment-history-processing-and-past#Section1), and should be left out when actually charging a card.                                                   |
| `amount_paid`            | Optional. The amount to charging the patient. If left blank, the patient will be charged the full amount of the package or invoice.                                                                                                                     |
| `note`                   | Optional. Used to provide info about outside payments.                                                                                                                                                                                                  |
| `sender_id`              | Optional. The ID of the patient to charge.                                                                                                                                                                                                              |
| `recipient_id`           | Optional. The ID of the provider/staff member who should be listed as the recipient of the payment. This is primarily important in sitatuons where each provider has their own bank account. If left out, it defaults to the sender’s primary provider. |
| `payment_medium`         | Optional. Used for outside payments and can be ignored.                                                                                                                                                                                                 |
| `chosen_refund_amount`   | Optional. If provided, a given amount will be refunded to the sender.                                                                                                                                                                                   |
| `is_canceled`            | Optional. If set to `true`, the payment will be cancelled.                                                                                                                                                                                              |
| `resend_receipt`         | Optional. Set to `true` to resend the receipt to sender.                                                                                                                                                                                                |
| `is_paused`              | Optional. If set to `true`, will pause the recurring payment.                                                                                                                                                                                           |
| `resend_payment`         | Optional. Use this to retry a failed payment. It’s highly recommended to use combined with `stripe_idempotency_key`.                                                                                                                                    |
| `new_payment_date`       | Optional. Update the payment day of a recurring payment.                                                                                                                                                                                                |
| `stripe_idempotency_key` | Optional. A key generated on the front-end that is used by Stripe to prevent duplicate requests. Find more info about them [here](https://stripe.com/docs/api/idempotent_requests). This is optional, but highly recommended.                           |

Returns an [`updateBillingItemPayload`](/reference/2024-06-01/objects/updatebillingitempayload) object.

Sometimes the charge will be declined by the card issuer. The decline reason is included in the `messages` you can get back from the mutation. For more information on specific decline reasons, please view [Stripe’s list of decline codes](https://stripe.com/docs/declines/codes).

### Deleting a Billing Item

Billing Items can be (soft) deleted by authorized providers and staff members via the `deleteBillingItem` mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deletebillingiteminput).

```
mutation deleteBillingItem($id: ID) {
  deleteBillingItem(input: { id: $id }) {
    billingItem {
      id
    }


    messages {
      field
      message
    }
  }
}
```

The `deleteBillingItem` mutation is called from an authenticated provider/staff account.

| Input | Info                                            |
| ----- | ----------------------------------------------- |
| `id`  | **Required**. ID of the Billing Item to delete. |

Returns a [`deleteBillingItemPayload`](/reference/2024-06-01/objects/deletebillingitempayload) object.
