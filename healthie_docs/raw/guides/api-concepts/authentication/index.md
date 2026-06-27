---
title: Authentication | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/api-concepts/authentication/index
  md: https://docs.gethealthie.com/guides/api-concepts/authentication/index.md
---

Healthie uses API keys to allow access to the API. Each Healthie user account can have its own API key, and one user account can have multiple API keys.

## Scopes

API keys are scoped to a user account, and the API key takes on the permissions and behaviors of the user account it is connected to. If you want to set up an “admin” API key for server-side actions, make sure you’ve granted all the appropriate permissions to the Healthie user account associated with that key. Actions done via a user’s API key are considered to be done by the user.

You can generate API keys programmatically for other users. If you want to use this functionality, contact Healthie at <hello@gethealthie.com> and we’ll set it up for the user account you specify.

For server-to-server integrations, this means you have a choice between using a “admin/service account” API key (that is tied to one specific user account), or creating and using API keys per-user. We see both approaches done and work, and the ultimate decision will depend on your use-case and needs.

In general, using a “service account” API key makes sense if your API integration is backend and/or data focused. If you are building out user experiences or custom user interfaces (e.g to use parts of Healthie headlessly), we normally recommend the API key per-user approach. Doing so allows you to utilize Healthie’s audit logging, notifications, and defaults in a way that mirrors how Healthie’s own front-end developers work. If you have any questions, this is also a great topic to discuss with a Healthie solutions engineer.

## Request headers

Healthie expects the API key to be included in all authenticated API requests to the server, via headers that look like the following:

`Authorization: Basic YOUR_API_KEY_HERE`

`AuthorizationSource: API`

Note

You must replace `YOUR_API_KEY_HERE` with your personal API key.

If your data is in a shard (you will know if this is the case), you must also include the following header:

`AuthorizationShard: YOUR_SHARD_AUTHORIZATION_ID`

You must replace `YOUR_SHARD_AUTHORIZATION_ID` with your shard authorization ID. If you don’t have this ID, write to <hello@gethealthie.com> to obtain it.

## Generating API keys

You can generate an API key with the `createApiKey` mutation.

```
mutation createApiKey($name: String, $user_id: ID) {
  createApiKey(
    input: {
      name: $name # A used-defined name for the API key. Optional
      user_id: $user_id # The ID of the user to create an API key for. Required
    }
  ) {
    api_key
    api_key_object {
      created_at
      displayable_key
      id
    }
    messages {
      field
      message
    }
  }
}
```
