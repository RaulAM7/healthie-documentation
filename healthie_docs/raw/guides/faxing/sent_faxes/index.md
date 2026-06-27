---
title: Sent Faxes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/faxing/sent_faxes/index
  md: https://docs.gethealthie.com/guides/faxing/sent_faxes/index.md
---

# Sent Faxes

## The SentFax Object

```
{
    "destination_number": "123-456-7890",
    "id": "12345",
    "resendable": true,
    "status": "OK",
    "status_display_string": "Delivered",
    "sender": {
        "id": "123456"
    },
    "patient": {
        "id": "987654"
    },
}
```

Sent Faxes are `SentFax` objects.

You can view the full list of available fields [here](/reference/2024-06-01/objects/sentfax).

## Listing Sent Faxes

```
query sentFaxes(
  $keywords: String
  $order_by: SentFaxOrderKeys
  $sort_by: String
  $offset: Int
  $page_size: Int
  $after: Cursor
) {
  sentFaxes(
    keywords: $keywords
    order_by: $order_by
    sort_by: $sort_by
    offset: $offset
    page_size: $page_size
    after: $after
  ) {
    created_at
    cursor
    destination_number
    id
    parsed_form_answer_group_ids
    patient
    resendable
    sender
    status
    status_display_string
    updated_at
  }
}
```

Listing Sent Faxes is done via the `sentFaxes` query.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/sentfaxes#arguments).

| Input      | Info                                                                                                                                                     |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `order_by` | Optional. Valid options can be found [here](/reference/2024-06-01/enums/sentfaxorderkeys). NOTE: `sort_by` is deprecated; should use `order_by` instead. |
| `keywords` | Optional. Keywords to search by.                                                                                                                         |

Returns a list of [`SentFax`](/reference/2024-06-01/objects/sentfax) objects.

## Retrieving a singular Sent Fax

```
query sentFax($id: ID!) {
  sentFax(id: $id) {
    created_at
    cursor
    destination_number
    id
    parsed_form_answer_group_ids
    patient
    resendable
    sender
    status
    status_display_string
    updated_at
  }
}
```

To search for a particular Sent Fax by ID, the `sentFax` query can be used. Returns a singular [`SentFax`](/reference/2024-06-01/objects/sentfax) object.

## Sending a Fax

```
mutation CreateSentFax {
    createSentFax(
        input: {
            date: null
            destination_number: null
            answer_ids: null
            dietitian: { id: null }
        }
    ) {
        messages {
            message
            field
        }
        sent_fax {
            created_at
            cursor
            destination_number
            id
            parsed_form_answer_group_ids
            resendable
            status
            status_display_string
            updated_at
        }
    }
}
```

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createsentfaxinput).

| Input         | Info                                                                                                                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `dietitian`   | **Required**. The sender associated with the sentFax; and the provider’s user ID must be provided. More information on this input can be found [here](/reference/2024-06-01/input-objects/faxdietitianinput) |
| `document_id` | Optional. The ID of a document sent as a fax.                                                                                                                                                                |
| `patient_id`  | Optional. ID of the patient associated with the `sentFax`.                                                                                                                                                   |

Returns a [`createSentFaxPayload`](/reference/2024-06-01/objects/createsentfaxpayload) object.
