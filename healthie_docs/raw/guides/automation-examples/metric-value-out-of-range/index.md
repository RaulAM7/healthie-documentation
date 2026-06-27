---
title: Metric Value is out of range | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/automation-examples/metric-value-out-of-range/index
  md: https://docs.gethealthie.com/guides/automation-examples/metric-value-out-of-range/index.md
---

In this example we are going to implement an automation script that assign a Task to Provider every time a Patient weighs themselves and the measured body weight is over a specific threshold. We are going to use `220` lbs as an example limit, however you should adjust it to your business needs.

Steps necessary to implement this automation:

* listen to a `metric_entry.created` webhook
* fetch the Entry from API using the received `resource_id` key
* verify if the Metric is of the correct category (`Weight`)
* if Metric value is above `220`, send a mutation to create a new Task

### Implementation

```
{
  "resource_id": "555",
  "resource_id_type": "Entry",
  "event_type": "metric_entry.created"
}
```

The webhook payload may look like the JSON on the right side.

There was a new Metric created with an ID `555`.

Note

Please note that `resource_id_type` is `Entry` for both Entry and Metric webhooks.

```
query getEntry($id: ID) {
  entry(id: $id) {
    id
    type
    category
    metric_stat
    third_party_source
    poster {
      id
      full_name
      dietitian_id
    }
    added_by_user {
      id
      full_name
      is_patient
      dietitian_id
    }
  }
}
```

> Variables (replace with the `resource_id` from webhook payload):

```
{
  "id": "555"
}
```

Now, let’s query the Healthie API to retrieve information about the Metric.

```
{
  "data": {
    "entry": {
      "id": "555",
      "type": "MetricEntry",
      "category": "Weight",
      "metric_stat": 250,
      "third_party_source": null,
      "poster": {
        "id": "2",
        "full_name": "John Doe",
        "dietitian_id": "1"
      },
      "added_by_user": {
        "id": "2",
        "full_name": "John Doe",
        "dietitian_id": "1",
        "is_patient": true
      }
    }
  }
}
```

The response should look like this.

You may want to check the value of `added_by_user.is_patient` in order to determine if the Metric was added by the Patient and not by the Provider.

If necessary, perform additional checks, e.g. if the Metric was added from a third-party source, like Apple Health (`third_party_source` field).

In our example, the body weight is 250 lbs, which 30 lbs above the safe threshold.

```
mutation createTask($input: createTaskInput!) {
  createTask(input: $input) {
    task {
      id
      content
    }
  }
}
```

> Input:

```
{
  "content": "Follow up to double check the body weight excessed by 30 lbs",
  "user_id": "1", // Provider ID
  "client_id": "2" // Patient ID
}
```

Once performing all checks and confirming that the `metric_stat` is out of the safe range (`250 > 220`), we can run our mutation.

Replace the following input variables with data from the response:

| Input       | Response variable     |
| ----------- | --------------------- |
| `user_id`   | `poster.dietitian_id` |
| `client_id` | `poster.id`           |

This mutation will create a new Task for the Provider and associate it with the Patient.

Please refer to Tasks documentation to learn more about additional options like reminders and due dates.
