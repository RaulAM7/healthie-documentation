---
title: Getting started | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/websockets-and-subscriptions/getting-started/index
  md: https://docs.gethealthie.com/guides/websockets-and-subscriptions/getting-started/index.md
---

import { Aside } from ‘@astrojs/starlight/components’;

# Websockets and Subscriptions

Healthie offers GraphQL subscriptions via Websockets. This enables you to build interfaces that automatically listen for new data changes (e.g a new chat message comes in). Healthie’s GraphQL subscription implementation is currently offered via AnyCable (which itself is a more peformant implementation of the ActionCable spec).

**Important**: The ActionCable spec differs from the Apollo Websockets spec. Healthie is evaluating a translation layer between the two, but currently you cannot use Apollo's default subscription connection functionality.

Please find step-by-step instructions on how to connect and use GraphQL subscriptions via Healthie’s API.

**1) Open the Websocket Connection**

Open a Websocket Connection to the URL listed below. URL parameters are used for authentication via Websockets, because the Websockets protocol specification does not support headers.

| Name       | URL                                                                  |
| ---------- | -------------------------------------------------------------------- |
| Sandbox    | wss\://ws.staging.gethealthie.com/subscriptions?token=`API_KEY_HERE` |
| Production | wss\://ws.gethealthie.com/subscriptions?token=`API_KEY_HERE`         |

```
// Example Welcome


{
  "type": "welcome",
  "sid": "0czVwnltbucBy23AanKFJ"
}


// Example Ping


{
  "type": "ping",
  "message": 1664558222
}
```

**2) Receive Connection Confirmation**

Once you connect in Step 1, You should receive a connection successful/welcome message, and will start to receive pings. See examples to the right

```
// This is Vanilla JS
const channelId = Math.round(Date.now() + Math.random() * 100000).toString(16);
```

**3) Generate a Channel ID**

ActionCable works via channels. Generate a unique channel ID and then subscribe to it. See generation example to the right.

```
{
  "command": "subscribe",
  "identifier": "{\"channel\":\"GraphqlChannel\",\"channelId\":\"<ID_HERE>\"}"
}
```

**4) Subscribe to the Generated ID**

Once you have the channel ID, you need to subscribe to it. Do so via sending in the subscribe command to the open Websocket connection.

```
# Subscription query


subscription onNoteAddedSubscription($id: String) {
  noteAddedSubscription(conversationId: $id) {
    ...NoteFragment
    __typename
  }
}


fragment NoteFragment on Note {
  id
  content
  user_id
  conversation_id
  attached_image_url
  attached_audio_url
  document_id
  created_at
  updated_at
  is_autoresponse
  deleted_by_user
  scheduled_at
  image_name
  document_name
  on_behalf_user {
    id
    full_name
    __typename
  }
  creator {
    id
    full_name
    avatar_url
    is_patient
    first_name_last_initial
    __typename
  }
  __typename
}
```

```
// Use the query above to send it as the `data` property below
{
  "command": "message",
  "identifier": "{\"channel\":\"GraphqlChannel\",\"channelId\":\"<ID_HERE>\"}",
  "data": "<STRINGIFIED_QUERY_HERE>"
}
```

**5) Subscribe to the specific GraphQL Subscription**

Once you subscribe to channel, you then need to let it know which GraphQL subscription you want to listen to. Do so via sending in the message command to the open Websocket channel. You can get a list of subscriptions [here](https://docs.gethealthie.com/reference/2024-06-01/objects/subscription). Here’s an example for `noteAddedSubscription`.

```
{
  "identifier": "{\"channel\":\"GraphqlChannel\",\"channelId\":\"1838f674dff\"}",
  "message": {
    "more": true,
    "result": {
      "data": {
        "noteAddedSubscription": {
          "__typename": "Note",
          "attached_audio_url": null,
          "attached_image_url": null,
          "content": "\u003cp\u003eCheck Check Check\u003c/p\u003e",
          "conversation_id": "2060148",
          "created_at": "2022-09-30 17:20:14 UTC",
          "creator": {
            "__typename": "User",
            "avatar_url": "https://example.com",
            "first_name_last_initial": "Dr. Melanie K",
            "full_name": "Dr. Melanie Klesse",
            "id": "30",
            "is_patient": false
          },
          "deleted_by_user": false,
          "document_id": null,
          "document_name": null,
          "id": "10637345",
          "image_name": null,
          "is_autoresponse": false,
          "on_behalf_user": null,
          "scheduled_at": null,
          "updated_at": "2022-09-30 17:20:14 UTC",
          "user_id": "30"
        }
      }
    }
  }
}
```

**6) Receive Subscription Events**

Now, you will begin to receive new subscription events that are sent to that channel. Here’s an example, also for the `noteAddedSubscription`.
