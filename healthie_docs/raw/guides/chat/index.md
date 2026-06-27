---
title: Chat | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/chat/index
  md: https://docs.gethealthie.com/guides/chat/index.md
---

# Chat

For more information on the feature in general, view our help articles [here](https://help.gethealthie.com/article/82-overview-chatting-with-a-client).

## Chat Objects

```
 # Some example fields for a conversation.


{
  "conversation": {
    "id": "9900",
    "conversation_memberships_count": "2",
    "name": "Quick Question",
    "includes_multiple_clients": false,
    "owner": {
      "id": "11",
      "full_name": "Jeff Smith"
    },
    "notes": [
      {
        "user_id": "123451",
        "content": "<p>Hey</p>"
      },
      {
        "user_id": "123451",
        "content": "<p>Example message</p>"
      }
    ]
  }
}
```

Within the API, a “Chat” is known as a [`Conversation`](/reference/2024-06-01/objects/conversation). A message in a conversation is a [`Note`](/reference/2024-06-01/objects/note) object.

### Conversation Memberships

```
# Example ConversationMembership


{
  "conversationMembership": {
    "convo": {
      "id": "12345",
      "viewed": false, # has unread messages
      "notes": [
        {
          "user_id": "123451",
          "content": "<p>Hey</p>"
        },
        {
          "user_id": "123451",
          "content": "<p>Example message</p>"
        }
      ]
    }
  }
}
```

A conversation has multiple [`ConversationMemberships`](/reference/2024-06-01/objects/conversationmembership) objects which are connectors between a `Conversation` and a [`User`](/reference/2024-06-01/objects/user).

To determine a given conversation has unread messages for the current user, check the `viewed` field on the `ConversationMembership` object.

### Note content formatting

The `content` field on a `Note` object is a string of HTML. Healthie allows only subset of HTML elements and attributes. The rest will be stripped out. Basic formatting such as bold, italics, and underline, as well as images and video embeds are supported. New lines can be supported either by wrapping the content in separate `<p>` tags, or by using `\n` escape characters.

## Creating a Conversation

A `Conversation` is created in two main ways — automatically and via `createConversation`.

A `Conversation` is automatically created when a patient is assigned to a provider (either as their primary provider or part of their care team) and the ‘Has Chat conversation automatically created with client’ permission is enabled. When this happens, our system automatically creates a two-person conversation between the patient and the provider (if one does not exist already). Note that ‘Has Chat conversation automatically created with client’ only applies to Care Team Providers and not the patient’s Primary provider, a two-person conversation between the patient and their primary provider is always created.

A `Conversation` can also be manually created with `createConversation`.

| Method                | Corresponding Mutation |
| --------------------- | ---------------------- |
| Automatically Created | N/A                    |
| Manually Created      | `createConversation`   |

Users have no limits on the number of conversations they can be in, and the same patient and provider can have multiple conversations together. Healthie also supports internal conversations, which are conversations that just have providers and staff, with no patients involved.

### `createConversation` Mutation

```
mutation createConversation(
  $simple_added_users: String # e.g "user-1,group-2,user-3"
  $owner_id: ID # e.g "4"
  $name: String # e.g "Questions for Next Appointment"
) {
  createConversation(input: { simple_added_users: $simple_added_users, owner_id: $owner_id, name: $name }) {
    conversation {
      id
    }
    messages {
      field
      message
    }
  }
}
```

Conversations are manually created via the `createConversation` mutation, which needs to be called from an authenticated staff/provider account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/createconversationinput). We will go over some of the most common inputs below.

| Input                | Info                                                                                                                                                                                                                                                                       |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `owner_id`           | The staff member who is the “Owner” of the conversation. The owner is automatically added to the conversation, and has full ability to add and remove patients and staff from the conversation. If left blank, this defaults to the current user.                          |
| `simple_added_users` | A comma-seperated string of which patients, staff, and user groups should be added to the conversation. This comma seperated string uses the doc\_share\_id (which is a field on `UserType` and `UserGroupType`). For example, it could look like `user-1,group-2,user-3`. |
| `name`               | The subject title for the conversation. Defaults to the names of the users and groups in the conversation.                                                                                                                                                                 |

### createNote mutation

A chat message in the Healthie API is referred to as a “note.” To add a message to a chat conversation, use the `createNote` mutation.

```
mutation createNote(
  $user_id: String
  $content: String
  $conversation_id: String
  $attached_image_string: String
  $scheduled_at: String
  $org_chat: Boolean
  $hide_org_chat_confirmation: Boolean
) {
  createNote(
    input: {
      user_id: $user_id
      content: $content # Content of the note
      conversation_id: $conversation_id
      attached_image_string: $attached_image_string
      scheduled_at: $scheduled_at # for scheduling notes, time note will be sent
      org_chat: $org_chat # Pass `true` when creating a note by someone who is not the conversation owner (e.g., by another provider on the client's care team)
      hide_org_chat_confirmation: $hide_org_chat_confirmation # When True, will hide org chat confirmation modal
    }
  ) {
    note {
      id
      content
      user_id
    }
    messages {
      field
      message
    }
  }
}
```

## Retrieving a Conversation

```
query getConversation($id: ID, $provider_id: ID) {
  conversation(id: $id, provider_id: $provider_id) {
    id
    conversation_memberships_count
    includes_multiple_clients
  }
}
```

Retrieving a specific conversation is done via the `conversation` query.

| Input | Info                                  |
| ----- | ------------------------------------- |
| `id`  | Required. The ID of the conversation. |

## Updating a Conversation

A `Conversation` is updated via `updateConversation`. This can be called from an authenticated provider or staff account.

| Method                       | Corresponding Mutation |
| ---------------------------- | ---------------------- |
| Updated by provider or staff | `updateConversation`   |

Users have no limits on the number of conversations they can be in, and the same patient and provider can have multiple conversations together. Healthie also supports internal conversations, which are conversations that just have providers and staff, with no patients involved.

### `updateConversation` Mutation

```
mutation updateConversation($id: ID, $simple_added_users: String, $name: String, $closed_by_id: ID) {
  updateConversation(
    input: { id: $id, simple_added_users: $simple_added_users, name: $name, closed_by_id: $closed_by_id }
  ) {
    conversation {
      id
    }
    messages {
      field
      message
    }
  }
}
```

Conversations are updated via the `updateConversation` mutation, which needs to be called from an authenticated staff/provider account.

You can view a full list of potential inputs [here](/reference/2024-06-01/input-objects/updateconversationinput). We will go over some of the most common inputs below.

| Input                | Info                                                                                                                                                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                 | Required. The ID of the conversation to update                                                                                                                                                                                                                                              |
| `simple_added_users` | A comma-seperated string of which patients, staff, and user groups should be in the conversation. See [`createConversation` section](/docs#creating-a-conversation) for how to format. Any existing conversation members not included in this string will be removed from the conversation. |
| `name`               | Optional. The subject title for the conversation. Defaults to the names of the users and groups in the conversation.                                                                                                                                                                        |
| `closed_by_id`       | When passed in, the conversation is closed. This prevents new messages from being sent. This ID should be the ID of the current user.                                                                                                                                                       |

## Deleting a Conversation

`Conversation` objects cannot be deleted via the Healthie API. Instead, you should close the conversation using the `updateConversation` mutation mentioned above.

## Listing Conversations

```
query conversationMemberships(
  $offset: Int
  $keywords: String
  $active_status: String
  $client_id: String
  $read_status: String
  $conversation_type: String
  $provider_id: ID
  $is_scheduled_tab: Boolean!
) {
  conversationMembershipsCount(
    keywords: $keywords
    active_status: $active_status
    client_id: $client_id
    read_status: $read_status
    conversation_type: $conversation_type
    provider_id: $provider_id
  )
  conversationMemberships(
    offset: $offset
    keywords: $keywords
    active_status: $active_status
    client_id: $client_id
    read_status: $read_status
    conversation_type: $conversation_type
    provider_id: $provider_id
  ) {
    id
    display_name
    archived
    viewed
    convo {
      id
      conversation_memberships_count
    }
  }
}
```

To retrieve a list of conversations, it is best to use the `conversationMemberships` query, *not* the `conversations`query. The `conversationMemberships` gives you additional argument options and context. You can view a full list of potential arguments [here](/reference/2024-06-01/queries/conversationmemberships#arguments).

We will go over some of them below.

| Input               | Info                                                                                                                                                                                                                                                                                                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_id`         | Optional. Retrieve `conversationMemberships` for a specific patient. To retrieve `conversationMemberships` that the authenticated user is not a part of, you must be authenticated as an organization admin. **Important: While optional, if a valid `client_id` is not passed in the query, all `conversationMemberships` for the current user will be returned.** |
| `provider_id`       | Optional. Defaults to the authenticated user if left blank. Retrieve `conversationMemberships` for a specific provider. You must be authenticated as an organization admin.                                                                                                                                                                                         |
| `keywords`          | Optional. Allows for searching the conversation by the conversation name, or by the names of users in the conversation.                                                                                                                                                                                                                                             |
| `read_status`       | Defaults to `all`. Options are `all`, `read`, and `unread`. Returns `conversationMemberships` matching the read/unread status.                                                                                                                                                                                                                                      |
| `active_status`     | Defaults to `active`. Options are `active`, `archived`, `closed`. Retrieves `conversationMemberships` with the matching conversation status.                                                                                                                                                                                                                        |
| `conversation_type` | Defaults to `all`. Options are `all`, `individual`, `community`. Retrieves `conversationMemberships` with the matching conversation type.                                                                                                                                                                                                                           |

## Chat SDK for React

The Healthie React SDK offers an easy integration of Healthie’s Chat functionality into your application by providing pre-built React components and hooks. With minimal setup and configuration, these components can be rendered as is or restyled to match your application’s design by overriding CSS classess.

The SDK should be sufficient in most use cases, providing the following capabilities:

* Conversation list
* Conversation view
* Individual (1:1) conversations
* Community Chat conversations
* Rendering all message types (text, image, audio, file attachments, video embeds)

It is however not possible to create conversations (outside of the Healthie web app or mobile app), and some features that exist in the Healthie web or mobile app may not be available via the SDK.

For more information and usage guide, refer to the SDK documentation [here](https://www.npmjs.com/package/@healthie/chat).
