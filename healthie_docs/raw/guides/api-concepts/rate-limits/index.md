---
title: Rate Limits | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/api-concepts/rate-limits/index
  md: https://docs.gethealthie.com/guides/api-concepts/rate-limits/index.md
---

To ensure stability and fairness in our API usage, several limits are in place. Understanding these limits will help you design efficient queries and avoid disruptions to your API access.

## Request rate limits

Healthie sets limits on how many requests can made against our API within a certain period of time. These limits are subject to dynamic adjustment to maintain optimal system performance.

Rate limits may vary based on several factors including:

* The specific endpoints being accessed
* The type of operation being performed
* Current system load and performance conditions

We recommend implementing proper error handling and retry logic to gracefully handle rate limit responses. If a client exceeds the rate limits, they will receive a GraphQL error response.

Example error response

```
{
  "errors": [
    {
      "message": "Too many requests. Please try again later.",
      "extensions": {
        "code": "TOO_MANY_REQUESTS"
      }
    }
  ]
}
```

## Complexity limit

Our GraphQL API uses a complexity scoring system to limit the amount of computation that can be performed in a single request. Each query is assigned a complexity score based on the fields it requests and their potential computation cost.

* The maximum complexity allowed per request is **2000**
* Fields have different complexity costs based on their type and potential data volume
* Connection fields with pagination arguments increase complexity based on requested page size

Note

It is highly unlikely to exceed the query complexity limit with normal usage, and we have never encountered an intentional query with a complexity cost exceeding 1600.

### Calculating complexity

Complexity is calculated by assigning costs to fields based on their type:

* Simple scalar fields (like strings or integers) typically have minimal cost
* Object fields and connections have higher costs
* Connection field costs are multiplied by the requested page size (`first` or `last` argument)
  * If no page size is defined, the default page size is 100 and will be used for the calculation

For example, in this query:

```
query {
  users {
    id
    appointments {
      id
      appointment_type {
        id
        name
      }
    }
  }
}
```

The complexity calculation would include base cost for each field since it does not use connection pagination.

However, in this query:

```
query {
  users(first: 3) {     # +1
    nodes {             # +1
      id                # +3 (3 nodes)
      appointments {    # +3
        id              # +3
        notes           # +3
      }
    }
  }
}
```

The complexity calculation would include:

* Base costs for each field
* Multiplier for the `users` connection (×3)
* Multiplier for the nested `appointments` array (×3 for each user)

Which results in a complexity of **14**. If no page size (e.g. `first: 3`) is defined, the default page size of 100 would be used and the resulting complexity would be **402**.

## Depth limit

To prevent excessively nested queries that could impact performance, we enforce a depth limit on all requests:

* The maximum depth allowed per query is **25 levels**
* Depth is calculated by counting the levels of nesting in your query
* Fragments and inline fragments are considered in the depth calculation

### Example of depth calculation

```
query {                # depth 0
  users(first: 3) {    # depth 1
    nodes {            # depth 2
      id               # depth 3
      appointments {   # depth 3
        id             # depth 4
        notes          # depth 4
      }
    }
  }
}
```

This query has a depth of **4**.

## Exceeding limits

If your query exceeds the complexity or depth limits, you will receive an error response with details about which limit was exceeded.

Example complexity limit error:

```
{
  "errors": [
    {
      "message": "Query has complexity of 2274, which exceeds max complexity of 2000"
    }
  ]
}
```

Example depth limit error:

```
{
  "errors": [
    {
      "message": "Query has depth of 30, which exceeds max depth of 25"
    }
  ]
}
```

## Tips for staying within limits

To optimize your queries and stay within the limits:

1. **Request only the fields you need** - Avoid requesting unnecessary data
2. **Use pagination properly** - Request smaller page sizes with pagination
3. **Break complex queries** - Split large operations into multiple smaller queries
4. **Avoid deep nesting** - Flatten your data model where possible
5. **Use aliases** - When requesting the same field multiple times with different arguments

## Connection best practices

When working with connections (lists of objects), follow these best practices:

* Always use pagination with reasonable `first` or `last` values
* Consider the total number of nodes your query will access
* Use the `nodes` shorthand for connections when you don’t need edge information

## Monitoring your usage

You can monitor your API usage and limits by:

1. Checking response messages that contain limit information
2. Testing complex queries in development before using them in production
