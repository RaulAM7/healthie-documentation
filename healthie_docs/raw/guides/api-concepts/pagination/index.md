---
title: Pagination | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/api-concepts/pagination/index
  md: https://docs.gethealthie.com/guides/api-concepts/pagination/index.md
---

Many queries in Healthie’s API are paginated. We use offset-based pagination. When a query takes in an `offset` argument, that specifies where the data returned should start. For example, our `entries` query has a page size of 10. if you have a list of 20 entries, and want to load all of them in, you would first do an `entries` query with `offset` of `0` and then an `entries` query with an offset of 10. Many queries have a corresponding “count” query (e.g `entries` has an `entriesCount`), That “count” query lets you see the total amount of data that you will need to page through.

If you send in an `offset` value that is too large (e.g 150 for a data set that only contains 100 objects), our API will just return an empty array.

## Cursor Pagination

Healthie suggests using the new Cursor pagination instead of the previously available offset-based pagination. It is more stable, performant, and easier to use. Each query supporting Cursor pagination has an `after` input argument and returned objects provide a `cursor` field. To fetch the next page of results, use the `cursor` value from the last item returned in the current query.

Note

Note that Cursor Pagination is closely related to sorting. You must reset your pagination whenever you change the value of the `order_by`/`sort_by` argument.

Consider the following query:

```
{
  announcements(page_size: 2, should_paginate: true) {
    id
    cursor
  }
  announcementsCount
}
```

Which should give a result like this:

```
{
  "data": {
    "announcements": [
      {
        "id": "3",
        "cursor": "eyJrIjpbIjMiXX0="
      },
      {
        "id": "2",
        "cursor": "eyJrIjpbIjIiXX0="
      }
    ],
    "announcementsCount": 3
  }
}
```

Now, let’s take the `cursor` value of the last item on the list and use it in the next query:

```
{
  announcements(page_size: 1, should_paginate: true, after: "eyJrIjpbIjIiXX0=") {
    id
    cursor
  }
  announcementsCount
}
```

It should return the next set of result after the specified cursor.

```
{
  "data": {
    "announcements": [
      {
        "id": "1",
        "cursor": "eyJrIjpbIjEiXX0="
      }
    ],
    "announcementsCount": 3
  }
}
```

Queries that currently support Cursor pagination:

* `announcements`
* `api_keys`
* `appointment_types`
* `appointments`
* `audit_log`
* `billing_items`
* `card_issues`
* `care_plans`
* `cms1500s`
* `comments`
* `conversation_memberships`
* `course_memberships`
* `courses`
* `cpt_codes`
* `customEmails`
* `custom_module_forms`
* `documents`
* `document_viewings`
* `entries`
* `food_search`
* `form_answer_groups`
* `goals`
* `goals_data`
* `goal_histories`
* `goal_instances`
* `icd_codes`
* `insurance_plans`
* `lab_orders`
* `locations`
* `meal_search`
* `notes`
* `notifications`
* `offerings`
* `offering_coupons`
* `onboarding_flows`
* `permission_templates`
* `products`
* `received_faxes`
* `referring_physicians`
* `requested_payments`
* `sent_faxes`
* `sent_webhooks`
* `smart_phrases`
* `super_bills`
* `tasks`
* `users`
* `user_groups`
* `user_package_selections`
* `webhooks`

## Connection-based Cursor Pagination

Healthie is introducing a new pagination model based on the Relay Connection specification. This model provides a more robust and feature-rich way to paginate through collections of data and is being used by tech leaders like [GitHub](https://docs.github.com/en/graphql/guides/using-pagination-in-the-graphql-api) and [Shopify](https://shopify.dev/docs/api/admin-graphql#endpoints).

### Key Differences from Previous Pagination

Previously, our API supported a hybrid approach to cursor pagination where:

* Queries accepted an `after` parameter for basic cursor-based navigation
* Each model had a `cursor` field
* Separate count queries (e.g., `usersCount`) were required for total counts
* Limited metadata about the result set was available

The new Connection-based pagination provides several improvements:

* Standardized way to navigate through result sets
* Built-in metadata about the connection (e.g., total count)
* Information about whether more results are available
* Clear separation between connection metadata and node data

### Using Connection-based Pagination

#### Basic Query Structure

```
{
  users(first: 10) {
    edges {
      node {
        id
        name
        email
      }
      cursor
    }
    page_info {
      has_next_page
      has_previous_page
      start_cursor
      end_cursor
    }
    total_count
  }
}
```

Here’s an example of how to query a collection using the new pagination model:

#### Connection Fields

Each connection provides the following fields:

* `edges`: A list of edge objects, each containing:

  * `node`: The actual object (e.g., User, Appointment, Document)
  * `cursor`: An opaque string used for pagination; the value represents the cursor for the given edge

* `page_info`: Metadata about the current page:

  * `has_next_page`: Boolean indicating if more results exist after this page
  * `has_previous_page`: Boolean indicating if more results exist before this page
  * `start_cursor`: Opaque cursor for the first edge in the current page
  * `end_cursor`: Opaque cursor for the last edge in the current page

* `total_count`: The total number of items in the collection

### Pagination Arguments

Connections support both forward and backward pagination:

Forward pagination:

* `first`: Number of items to return
* `after`: Cursor to start after (use the `end_cursor` from previous query)

Backward pagination:

* `last`: Number of items to return
* `before`: Cursor to end before (use the `start_cursor` from previous query)

#### Example: Forward Pagination

Initial query:

```
{
  appointments(first: 10) {
    edges {
      node {
        id
        start
        contact_type
        appointment_type {
          id
        }
        attendees {
          id
          email
        }
      }
      cursor
    }
    page_info {
      has_next_page
      end_cursor
    }
  }
}
```

Next page:

```
{
  appointments(first: 10, after: "previously_returned_end_cursor") {
    edges {
      node {
        id
        start
        contact_type
        appointment_type {
          id
        }
        attendees {
          id
          email
        }
      }
      cursor
    }
    page_info {
      has_next_page
      end_cursor
    }
  }
}
```

#### Example: Backward Pagination

Previous page:

```
{
  appointments(last: 10, before: "previously_returned_start_cursor") {
    edges {
      node {
        id
        start
        contact_type
        appointment_type {
          id
        }
        attendees {
          id
          email
        }
      }
      cursor
    }
    page_info {
      has_previous_page
      start_cursor
    }
  }
}
```

#### Best Practices

1. **Avoid Mixed Pagination**: While the API supports both `first/after` and `last/before` arguments, using them together is discouraged as it can lead to confusing results.

2. **Cursor Handling**:

   * For forward pagination, use the `end_cursor` from `page_info` as the `after` parameter
   * For backward pagination, use the `start_cursor` from `page_info` as the `before` parameter
   * Treat cursors as opaque strings; do not attempt to decode or modify them

3. **Page Size**:

   * Always specify either `first` or `last`
   * Keep page sizes reasonable (recommended: 10-50 items)
   * Be aware that requesting very large page sizes may impact performance or result in query complexity limits

### Migration Guide

If you’re currently using our hybrid cursor pagination, here’s how to migrate to the new Connection-based pagination:

1. Remove separate count queries (e.g., `usersCount`) and use `total_count` from the connection (`users { total_count }`)
2. Update your pagination logic to use the `page_info` object for navigation
3. Update your data processing to handle the edges/node structure

**Before migration:**

```
{
  users(after: "some_cursor") {
    id
    name
    cursor
  }
  usersCount
}
```

**After migration:**

```
{
  users(first: 10, after: "some_cursor") {
    edges {
      node {
        id
        name
       cursor
      }
      cursor
    }
    page_info {
      has_next_page
      end_cursor
    }
    total_count
  }
}
```

### References

For deeper understanding of cursor-based pagination and the Connection specification:

1. [GraphQL Cursor Connections Specification](https://relay.dev/graphql/connections.htm) - The official Relay Connection specification that this implementation follows
2. [GraphQL Pagination Best Practices](https://graphql.org/learn/pagination/) - GraphQL’s official documentation on pagination approaches
3. [Explaining GraphQL Connections](https://www.apollographql.com/blog/explaining-graphql-connections) - Apollo’s detailed guide on implementing and using GraphQL connections
