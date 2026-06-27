---
title: Clinician has signed a Chart Note | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/automation-examples/clinician-signed-chart-note/index
  md: https://docs.gethealthie.com/guides/automation-examples/clinician-signed-chart-note/index.md
---

The following example demonstrates how to listen to `form_answer_group.locked` events and create a Task for another Organization Member to submit a CMS 1500 Claim. We assume that Biller is a designated person in your Organization and you can hardcode their User ID in the webhook handler.

Steps necessary to implement this automation:

* listen to a `form_answer_group.locked` webhook
* query the Healthie API to get the information about the related Patient
* create a task for the Biller to submit a CMS 1500 Claim

### Implementation

```
{
  "resource_id": "123",
  "resource_id_type": "FormAnswerGroup",
  "event_type": "form_answer_group.locked"
}
```

The webhook payload may look like the JSON on the right side.

This event indicates that a Form has been signed and locked.

```
query getFormAnswerGroups($id: ID) {
  formAnswerGroup(id: $id) {
    id
    user {
      id
    }
  }
}
```

> Variables (replace with the `resource_id` from webhook payload):

```
{
  "id": "123"
}
```

Now, let’s query the Healthie API to retrieve Form Answers.

```
{
  "data": {
    "formAnswerGroup": {
      "id": "123",
      "user": {
        "id": "200"
      }
    }
  }
}
```

The response should look like this.

The `user.id` property contains the Patient ID which we will use to create a Task related to this Patient.

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
  "content": "Submit a CMS 1500 Claim",
  "user_id": "190", // Biller ID
  "client_id": "200" // Patient ID
}
```

Now let’s create a task for the Provider.

Replace the following input variables with data from the response:

| Input       | Response variable                   |
| ----------- | ----------------------------------- |
| `user_id`   | Use your hardcoded ID of the Biller |
| `client_id` | `user.id`                           |

This mutation will create a new Task for the Biller and associate it with the Patient.

Please refer to Tasks documentation to learn more about additional options like reminders and due dates.
