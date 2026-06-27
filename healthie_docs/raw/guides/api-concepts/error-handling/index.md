---
title: Error Handling | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/api-concepts/error-handling/index
  md: https://docs.gethealthie.com/guides/api-concepts/error-handling/index.md
---

Our goal is to adhere to the latest [GraphQL specification](https://spec.graphql.org/), including [Section 7.1.2](https://spec.graphql.org/October2021/#sec-Errors) on errors. Although the spec is transport-agnostic, our system runs over HTTP and, therefore, we strive to adhere to the latest HTTP specifications, including the [semantics](https://datatracker.ietf.org/doc/html/rfc9110) described in [RFC 9110](https://datatracker.ietf.org/doc/html/rfc9110). As such, our API responds with the most appropriate HTTP response code where applicable.

Note

We are aware that some responses from our API that return `404 Not Found` do not conform with the GraphQL spec. We are working to remedy this issue.
