---
title: Client completed an intake form | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/automation-examples/client-completed-an-intake-form/index
  md: https://docs.gethealthie.com/guides/automation-examples/client-completed-an-intake-form/index.md
---

The following example demonstrates how to listen to Intake Form submission events and create a new Task for a Provider based on the Form answer. Let’s say that we want to send a thank-you gift every time a person refers a Client.

Steps necessary to implement this automation:

* listen to a `form_answer_group.created` webhook
* fetch the Form Answer Group from API using the received `resource_id` key
* verify if this is a Referral-related Form
* if the Form contains an answer with the name of the referrer, create a Task to send a thank-you gift

### Implementation

```
{
  "resource_id": "123",
  "resource_id_type": "FormAnswerGroup",
  "event_type": "form_answer_group.created"
}
```

The webhook payload may look like the JSON on the right side.

```
query getFormAnswerGroups($id: ID) {
  formAnswerGroup(id: $id) {
    id
    finished
    user {
      id
      dietitian_id
    }
    custom_module_form {
      id
    }
    form_answers {
      id
      label
      answer
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

Now, let’s query the Healthie API to retrieve Form answers.

```
{
  "data": {
    "formAnswerGroup": {
      "id": "123",
      "finished": true,
      "user": {
        "id": "200",
        "dietitian_id": "100"
      },
      "custom_module_form": {
        "id": "50"
      },
      "form_answers": [
        {
          "id": "640",
          "label": "Please enter some information about the person who referred you.",
          "answer": ""
        },
        {
          "id": "641",
          "label": "Name",
          "answer": "Chris"
        }
      ]
    }
  }
}
```

The response should look like this.

First, check if `custom_module_form.id` is equal to the ID of the referral form. We can ignore the webhook otherwise.

Next, find the `Name` question answer in the `form_answers` array. The `answer` property contains the user input.

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
  "content": "Send a thank-you gift to Chris",
  "user_id": "100", // Provider ID
  "client_id": "200" // Patient ID
}
```

Now let’s create a task for the Provider.

Replace the following input variables with data from the response:

| Input       | Response variable   |
| ----------- | ------------------- |
| `user_id`   | `user.dietitian_id` |
| `client_id` | `user.id`           |

This mutation will create a new Task for the Provider and associate it with the Patient.

Please refer to Tasks documentation to learn more about additional options like reminders and due dates.
