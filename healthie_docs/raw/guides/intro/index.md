---
title: Introduction | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/intro/index
  md: https://docs.gethealthie.com/guides/intro/index.md
---

# About

Healthie offers a web and mobile platform for healthcare tech organizations to launch and scale digital services. Developer teams can use our API to build client-facing, and provider-facing, apps, leveraging Healthie’s back-end, data architecture, and sample front-ends.

## For Developers & Customers

Healthie makes available the same API that our own front-end developers use to build Healthie (Healthie [Help Guide Linked Here](http://help.gethealthie.com/)), so the [functionality](https://www.gethealthie.com/telehealth-technology-and-software) covers our entire platform, including client engagement, coaching, provider management, telehealth, insurance billing, EHR, and more. As a result, product and engineering teams are able to focus on the implementation of specific care models to deliver ideal client-facing experiences.

Many organizations also leverage our API to pull detailed data for reporting & analytics that spans business operations, financial performance, client engagement, and client outcomes.

Our developer support team is here to help answer questions you may have about the API. We encourage you to contact us: <hello@gethealthie.com> and also share your feedback & requests as you explore and utilize our API.

## For Marketplace Partners

At Healthie, it’s our vision to improve access to healthcare and enable better healthcare outcomes through technology. By building partnerships across the healthcare and technology industry, our [Marketplace](https://help.gethealthie.com/article/1088-become-a-marketplace-partner) helps to break down barriers to workflows, processes, and care.

Our Marketplace makes it easy for businesses to use software solutions together to enhance efficiency, increase revenue, and deliver patient care. Healthie partners with a wide range of technology platforms, as well as service providers, that collectively enable our customers to achieve the solutions they need for better business or client care outcomes.

If you are an independent software provider serving a mutual customer base with Healthie, you can leverage our API and sandbox access to self-build an integration with our platform.

Learn more about becoming a Marketplace Partner [here](https://help.gethealthie.com/article/1088-become-a-marketplace-partner) or email <marketplace@gethealthie.com>.

# GraphQL Overview

Healthie offers a [GraphQL API](https://www.graphql.org/). If you have not worked with GraphQL before, we recommend that you read *Introduction to GraphQL* and *Queries and Mutations* over at [Learn about GraphQL](https://graphql.org/learn/) before you begin development.

Note

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119).

Our goal is to adhere to the latest [GraphQL specification](https://spec.graphql.org/). If you do not believe that we are adhering to the spec, please [contact us](mailto:hello@gethealthie.com?subject=GraphQL%20Spec%20Question) and we will work to make your experience better.

## Operations

The GraphQL spec provides three types of [operations](https://spec.graphql.org/October2021/#sec-Language.Operations): Queries, Mutations, and Subscriptions.

| Operation     | Usage                                                               |
| ------------- | ------------------------------------------------------------------- |
| Queries       | A read-only fetch                                                   |
| Mutations     | A write followed by a fetch                                         |
| Subscriptions | A long-lived request that fetches data in response to source events |

### Queries

Requests to the Healthie API are all HTTP requests, so any HTTP client (cURL, Axios, Net:HTTP, etc) can be used to make API requests. However, using tools with better GraphQL support can help a lot when using Healthie’s API. Here are our recommendations.

The easiest way to learn about and run your first GraphQL query is by using our API Explorer. It is a fully-fledged GraphQL IDE based on GraphiQL, providing you documentation and an easy to use interface to run queries.

As you progress beyond that, you can make queries via API tools like [Insomnia](https://insomnia.rest/) or [Postman](https://www.postman.com/).

Finally, when it comes time to write the actual code, we highly recommend using a GraphQL client, versus trying to construct the direct HTTP requests. Two examples are [Apollo Client](https://www.apollographql.com/docs/react/) (for JS) and [GraphQL-Client](https://github.com/github/graphql-client) (for Ruby).

Note

You MUST have an API Key to use the API Explorer. [Contact us](mailto:hello@gethealthie.com?subject=API%20Key%20Request) if you do not have one.

## Example Projects

We have an open-source widget that utilizes the API [on Github](https://github.com/healthie/healthie_sample_booking_widget). That repo is a great place is to get started if you are looking for an example project that uses our API.

## Developer Support

Healthie prides ourselves on our hands-on developer support, available to all API customers.

* We’re happy to answer any questions as they come up
* We can help you break down workflows and talk through how you can use the API to accomplish a specific goal
* We’re also happy to be in a Slack channel with your developers, or schedule screenshares/calls
