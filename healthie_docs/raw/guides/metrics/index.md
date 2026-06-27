---
title: Metrics | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/metrics/index
  md: https://docs.gethealthie.com/guides/metrics/index.md
---

# Metrics

## Storing Metric Data

```
mutation createEntry(
  $metric_stat: String # e.g "182"
  $category: String # e.g "Weight"
  $type: String # "MetricEntry"
  $user_id: String # e.g "61"
  $created_at: String # e.g "2021-09-23 15:27:01 -0400"
) {
  createEntry(
    input: { category: $category, type: $type, metric_stat: $metric_stat, user_id: $user_id, created_at: $created_at }
  ) {
    entry {
      id
    }
    messages {
      field
      message
    }
  }
}
```

Oftentimes, you may want to store and retrieve quantitative data (e.g weight, stress level, or A1C) on a patient. You would do this in Healthie using [`Entries`](/guides/journal), and more specifically, via a `MetricEntry` type. The most important fields when creating an `Entry` are `type`, `category`, `metric_stat`, `category`, `user_id`, and `created_at`. Let’s go over each one.

| Input         | Info                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`        | Specificies what type of `Entry` you are creating. We offer a (growing) range of entry types (e.g `FoodEntry` or `WorkoutEntry`). Since we storing a datapoint on the patient, the type would be `MetricEntry`.                                                                                                                                                                                                                                                                    |
| `category`    | Specifies what kind of metric we are storing. Healthie has built in metric categories like `Weight` or `A1C` that can be turned on or off. You can also add any metric category you’d like via our custom metrics feature. Managing these can be done via the API (by updating `FeatureToggle` objects), but you may just want to set this up in our UI. [Here is information about managing these in our UI](https://help.gethealthie.com/article/509-custom-metrics-in-healthie) |
| `metric_stat` | This is the actual data value for the metric. e.g if a patient weights 182 lbs, you would pass in `182` with a category of `Weight`.                                                                                                                                                                                                                                                                                                                                               |
| `user_id`     | The ID of the patient that this entry should be attached to.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `created_at`  | A timestamp that specifies when the data is from. You can backdate data, and forward-date data (up to 3 months in the future). If you don’t pass this in, the entry will be created with a timestamp of the current time.                                                                                                                                                                                                                                                          |

Those fields are used in a [`createEntry`](#creating-an-entry) mutation to create a Metric Entry. Please see the right sidebar for an example.

## Using the Entries Query for Metric Data

```
query entries(
  $category: String # e.g "Weight"
  $type: String # "MetricEntry"
) {
  entries(category: $category, type: $type) {
    id
  }
}
```

2248,2252 To retrieve metric data, you can use the `entries` query. The query is paginated, with a page size of 10. To see the total amount of metric data, you can use the `entriesCount` query.\
You can view all the argument options [here](/reference/2024-06-01/queries/entries#arguments) but lets go over some of the most important ones below.

First, since we only want metric data (and not other type of entry data like food), we will pass in `MetricEntry` to the `type` argument.

| Input       | Info                                                                                                                                                                 |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `category`  | Lets us specifiy what category of metric we want data for (e.g just get back `"Weight"` or `"Blood Pressure"`). If left blank, the query will return all categories. |
| `client_id` | ID of the Client to fetch metric Entries for.                                                                                                                        |
| `is_org`    | When set to `true`, the query will instead return Entries for all clients in the organization that the authenticated user can access.                                |
| `group_id`  | Whether to return Entries for clients in the specified user group.                                                                                                   |

If you are authenticating as a patient, then `client_id`, `is_org`, and `group_id` will have no effect on the query.

If none of the `client_id`, `is_org`, or `group_id` fields are passed in, the query will return entries posted by clients who have the authenticated user as their primary provider or care team member.

On the right, you can find an example of a simple query that returns metric data for the authenticated user’s patients.
