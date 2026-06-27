---
title: Received Faxes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/faxing/received_faxes/index
  md: https://docs.gethealthie.com/guides/faxing/received_faxes/index.md
---

# Received Faxes

## The ReceivedFax Object

```
{
    "archived": false,
    "comments": null,
    "id": "12345",
    "viewed_by_current_user": false
}
```

Received Faxes are `ReceivedFax` objects.

You can view the full list of available fields [here](/reference/2024-06-01/objects/receivedfax).

## Listing Received Faxes

```
query receivedFaxes(
  $active_status: String
  $keywords: String
  $sort_by: String
  $order_by: ReceivedFaxOrderKeys
  $offset: Int
  $page_size: Int
  $after: Cursor
) {
  receivedFaxes(
    active_status: $active_status
    keywords: $keywords
    sort_by: $sort_by
    order_by: $order_by
    offset: $offset
    page_size: $page_size
    after: $after
  ) {
    archived
    comments
    created_at
    cursor
    from_number
    id
    referring_provider_name
    viewed_by_current_user
  }
}
```

Listing Received Faxes is done via the `receivedFaxes` query.

You can view a full list of potential arguments [here](/reference/2024-06-01/queries/receivedfaxes#arguments).

| Input           | Info                                                                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `order_by`      | Optional. Valid options can be found [here](/reference/2024-06-01/enums/receivedfaxorderkeys). NOTE: `sort_by` is deprecated; should use `order_by` instead. |
| `keywords`      | Optional. Keywords to search by.                                                                                                                             |
| `active_status` | Optional. Status of the received fax. Can input ‘active’ or ‘archived’.                                                                                      |

Returns a list of [`ReceivedFax`](/reference/2024-06-01/objects/receivedfax) objects.

## Retrieving a singular Received Fax

```
query receivedFax($id: ID) {
  receivedFax(id: $id) {
    archived
    comments
    created_at
    cursor
    from_number
    id
    referring_provider_name
    viewed_by_current_user
  }
}
```

To search for a particular Received Fax by ID, the `receivedFax` query can be used. Returns a singular [`ReceivedFax`](/reference/2024-06-01/objects/receivedfax) object.

## Retrieving a PDF from a ReceivedFax

A PDF that was received via fax can be retrieved via a cURL request. Below is an example of the request:

```
curl --request POST \


  --url 'https://api.gethealthie.com/received_faxes/.pdf' \


  --header 'Authorization: Basic YOUR_API_KEY_HERE' \


  --header 'AuthorizationSource: API'
```

As part of the Authorization header, a valid API key must be passed in. More information can be found in the [Authentication](/guides/api-concepts/authentication/) section.
