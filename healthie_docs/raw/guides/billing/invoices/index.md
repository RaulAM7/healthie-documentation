---
title: Invoices | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/billing/invoices/index
  md: https://docs.gethealthie.com/guides/billing/invoices/index.md
---

# Invoices

Invoices (called `RequestedPayment`s in our API) allow you to request and track owed payments from patients. Patients can be invoiced for a Package ([`Offering`](/guides/billing/packages) in our API), a CMS1500, or for other custom products/services. Invoices can be sent to third-party payers even if they don’t have a Healthie account (helpful in cases like corporate wellness), but are most commonly sent directly to the patient. [In the examples below](#creating-an-invoice), we’ll cover how to send an invoice to a patient.

## The Invoice Object

```
{
  "id": "1",
  "price": "1234.00",
  "status": "Not Yet Paid",
  "invoice_id": "UU-1-2022",
  "details": "Other: example description",
  "currency": "USD",
  "invoice_type": "other",
  "debt": 1234,
  "notes": "Example notes",
  "billing_item_id": null,
  "billing_items": [],
  "is_manually_paid": false,
  "requested_payer": {
    "id": "3"
  },
  "recipient": {
    "id": "3",
    "dietitian": {
      "id": "1"
    }
  },
  "sender": {
    "id": "1"
  },
  "date_to_show": "2022-08-15 14:22:14 -0400"
}
```

Invoices are `RequestedPayment` objects.

You can view the full list of available fields [here](/reference/2024-06-01/objects/requestedpayment).

## Listing Invoices

```
query requestedPayments(
  $offset: Int
  $keywords: String
  $sort_by: String
  $only_unpaid: Boolean
  $sender_id: ID
  $status_filter: String
  $preview: Boolean
) {
  requestedPayments(
    offset: $offset
    keywords: $keywords
    sort_by: $sort_by
    only_unpaid: $only_unpaid
    sender_id: $sender_id
    status_filter: $status_filter
    preview: $preview
  ) {
    id
    price
    status
    invoice_id
    recipient {
      id
    }
    sender {
      id
    }
  }
}
```

Listing Invoices is done via the `requestedPayments` query.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/requestedpayments#arguments).

| Input           | Info                                                                                                                                                                                                                                                                               |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `offset`        | Optional. Offset for pagination.                                                                                                                                                                                                                                                   |
| `keywords`      | Optional. Keywords to search by. Billing Items can be searched by status, recipient’s first or last name, and offering’s name.                                                                                                                                                     |
| `sort_by`       | Optional. Valid options are:- `requested_on_asc`
- `requested_on_desc` (default)
- `client_asc`
- `client_desc`
- `provider_asc`
- `provider_desc`
- `amount_asc`
- `amount_desc`
- `status_asc`
- `status_desc`
- `type_asc`
- `type_desc`
- `invoice_id_asc`
- `invoice_id_desc` |
| `only_unpaid`   | Optional. Return only unpaid Invoices.                                                                                                                                                                                                                                             |
| `sender_id`     | Optional. ID of the Sender.                                                                                                                                                                                                                                                        |
| `status_filter` | Optional. Valid options are:- `paid`
- `partial`
- `unpaid`                                                                                                                                                                                                                        |
| `preview`       | Optional. Return only Invoices that are in preview.                                                                                                                                                                                                                                |

Returns a list of [`RequestedPayment`](/reference/2024-06-01/objects/requestedpayment) objects.

### Retrieving an Invoice

```
query requestedPayment($id: ID, $invoice_id: String, $uuid: String, $preview: Boolean) {
  requestedPayment(id: $id, invoice_id: $invoice_id, uuid: $uuid, preview: $preview) {
    id
    price
    status
    invoice_id
    recipient {
      id
    }
    sender {
      id
    }
  }
}
```

Retrieving a specific Invoice is done via the `requestedPayment` query.

At least one of the `id`, `invoice_id` and `uuid` inputs must be provided.

| Input        | Info                                                |
| ------------ | --------------------------------------------------- |
| `id`         | ID of the Invoice to query.                         |
| `invoice_id` | Invoice ID, must be used together with `uuid`.      |
| `uuid`       | External ID of the Requested Payer.                 |
| `preview`    | Optional. Return only if the Invoice is in preview. |

Returns a [`RequestedPayment`](/reference/2024-06-01/objects/requestedpayment) object.

## Creating an Invoice

```
mutation createRequestedPayment(
  $recipient_id: ID # e.g "61"
  $offering_id: ID # e.g "11"
  $price: String # can be left blank since it will default to the price of the package
  $invoice_type: String # "offering"
) {
  createRequestedPayment(
    input: { recipient_id: $recipient_id, offering_id: $offering_id, price: $price, invoice_type: $invoice_type }
  ) {
    requestedPayment {
      id
    }
    messages {
      field
      message
    }
  }
}
```

Invoices are created via the `createRequestedPayment` mutation. Let’s break down the inputs that mutation accepts.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createrequestedpaymentinput).

| Input                       | Info                                                                                                                                                                                                                                                                      |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `invoice_type`              | **Required**. The options are- `cms1500`
- `offering`
- `other`                                                                                                                                                                                                           |
| `recipient_id`              | Ihe ID of the patient. **This is required unless are you invoicing a third-party** (in which case you’d send in `requested_payer`).                                                                                                                                       |
| `sender_id`                 | Optional. The ID of the staff member that the invoice is associated with. This defaults to the current user if not sent in.                                                                                                                                               |
| `offering_id`               | Optional. The ID of the package that the invoice is associated with. This is only used if you are invoicing for a package.                                                                                                                                                |
| `cms1500_id`                | Optional. The ID of the CMS1500 that the invoice is associated with. This is only used if you are invoicing for a CMS1500.                                                                                                                                                |
| `price`                     | **Required if invoicing without a package**. The amount you are invoicing the patient for. If you are invoicing for a package, this field is optional (and the invoice will default to the package price if this is left out)                                             |
| `notes`                     | Optional. Lets you add extra details to the invoice. These notes are visible to the patient.                                                                                                                                                                              |
| `service_date`              | Optional. Can only be used the `invoice_type` is `other`.                                                                                                                                                                                                                 |
| `services_provided`         | **Required if `invoice_type` is `other`**. Otherwise, it should not be sent in. This lets you describe the products/services that you are invoicing the patient for.                                                                                                      |
| `status`                    | Optional (and is normally not sent in). `status` lets you explicitly set the status of the invoice. The options are:- `Paid`
- `Not Yet Paid`
- `Partial`Normally it is best to let Healthie automatically determine the status based on payments applied to the invoice. |
| `is_preview`                | Optional. Defaults to `false`. When passed in as `true`, the invoice is kept in a preview state and hidden from the Healthie UI.                                                                                                                                          |
| `user_package_selection_id` | Optional. Only used if you are invoicing a patient for an existing `UserPackageSelection`.                                                                                                                                                                                |

So in sum, you’d normally send in a `recipient_id`, `invoice_type`, `price` (unless it is for a package and you want to default to the package price), and what you are invoicing for (either a `offering_id`, `cms1500_id`, or `services_provided`). The example on the sidebar shows creating an invoice for a package.

Returns a [`createRequestedPaymentPayload`](/reference/2024-06-01/objects/createrequestedpaymentpayload) object.

## Updating an Invoice

```
mutation updateRequestedPayment(
  $id: ID!
  $recipient_id: ID # e.g "61"
  $offering_id: ID # e.g "11"
  $price: String # can be left blank since it will default to the price of the package
  $invoice_type: String # "offering",
  $send_request_email: Boolean
  $resend_receipt: Boolean
) {
  updateRequestedPayment(
    input: {
      id: $id
      recipient_id: $recipient_id
      offering_id: $offering_id
      price: $price
      invoice_type: $invoice_type
      send_request_email: $send_request_email
      resend_receipt: $resend_receipt
    }
  ) {
    requestedPayment {
      id
    }
    messages {
      field
      message
    }
  }
}
```

The `updateRequestedPayment` mutation shares many common inputs with [`createRequestedPayment`](#creating-an-invoice) and those inputs (e.g `invoice_type` or `is_preview` work the same in both places).

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updaterequestedpaymentinput).

| Input                | Info                                                         |
| -------------------- | ------------------------------------------------------------ |
| `id`                 | **Required**. The ID of the Invoice to update.               |
| `send_request_email` | Optional. Whether to resend the Invoice email.               |
| `resend_receipt`     | Optional. Whether to resend the charge confirmation receipt. |

Returns an [`updateRequestedPaymentPayload`](/reference/2024-06-01/objects/updaterequestedpaymentpayload) object.

## Deleting an Invoice

Invoices can be (soft) deleted by authorized providers and staff members via the `deleteRequestedPayment` mutation.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/deleterequestedpaymentinput).

```
mutation deleteRequestedPayment($id: ID) {
  deleteRequestedPayment(input: { id: $id }) {
    requestedPayment {
      id
    }


    messages {
      field
      message
    }
  }
}
```

The `deleteRequestedPayment` mutation is called from an authenticated provider/staff account.

| Input | Info                                       |
| ----- | ------------------------------------------ |
| `id`  | **Required**. ID of the Invoice to delete. |

Returns a [`deleteRequestedPaymentPayload`](/reference/2024-06-01/objects/deleterequestedpaymentpayload) object.
