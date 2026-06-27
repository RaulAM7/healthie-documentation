---
title: Filled Out Forms | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/filled_out_forms/index
  md: https://docs.gethealthie.com/guides/filled_out_forms/index.md
---

# Filled Out Forms

## Creating a Filled Out Form (e.g a chart note, or intake form)

```
mutation createFormAnswerGroup(
  # Should almost always true
  $finished: Boolean
  # ID of the custom_module_form (e.g "100")
  $custom_module_form_id: String
  # ID of the patient (e.g "61")
  $user_id: String
  # e.g [{custom_module_id: "1", answer: "foo", user_id: "61"}, {custom_module_id: "2", answer: "bar", user_id: "61"}]
  $form_answers: [FormAnswerInput!]!
) {
  createFormAnswerGroup(
    input: {
      finished: $finished
      custom_module_form_id: $custom_module_form_id
      user_id: $user_id
      form_answers: $form_answers
    }
  ) {
    form_answer_group {
      id
    }
    messages {
      field
      message
    }
  }
}
```

In the Healthie API, a filled-out form is known as a [`FormAnswerGroup`](/reference/2024-06-01/objects/formanswergroup). The most important fields when creating a `FormAnswerGroup` are `user_id`, `custom_module_form_id`, `finished`, `form_answers`. Let’s go over each one.

`user_id` is the ID of the patient who the form is on. When you create a `FormAnswerGroup` for a patient, that will be visible on the patient’s chart.

`custom_module_form_id` is the ID of the template (known as a `CustomModuleForm`) that the `FormAnswerGroup` completes. All filled-out forms need to be backed by a `CustomModuleForm`. These are the templates that you can create, view, and edit in the Form Builder in Healthie.

`finished` is a Boolean value. This needs to be passed in as true for the form to be visible in the patient’s chart and when you query for `formAnswerGroups`. If you do not pass in `finished` (or pass it in as false), you will need to query the `formAnswerGroup` by its ID.

`form_answers` is an array containing all the individual answers. Each submitted form answer needs to have a `custom_module_id`, `user_id`, and an `answer`. The `user_id` should match the `user_id` of the `FormAnswerGroup`. The `custom_module_id` should be the ID of the question (known as a `CustomModule`) that is being answered. The `answer` (as the name suggests) is the answer to the question.

Those fields are used in a `createFormAnswerGroup` mutation to create the filled-out form. Please see the right sidebar for an example.

This mutation triggers a `form_answer_group.created` webhook event.

## Querying Filled Out Forms

```
query formAnswerGroups(
  $date: String # e.g "2021-10-29"
  $custom_module_form_id: ID # e.g "11"
) {
  formAnswerGroups(date: $date, custom_module_form_id: $custom_module_form_id) {
    id
    name
    created_at
    form_answers {
      label
      displayed_answer
      id
      custom_module {
        required
        id
        mod_type
        label
      }
    }
  }
}
```

To retrieve filled out forms, you can use the `formAnswerGroups` query. You can view all the argument options [here](/reference/2024-06-01/queries/formanswergroups#arguments) but lets go over some of the most important ones below.

`filler_id` is the ID of the user who filled out the form. For example, you can use this argument to see all forms filled out by a given provider.

`user_id` is the ID of the patient whose chart the filled out form is in.

`custom_module_form_id` is the ID of the form template that was filled out. This can be helpful to use to see all filled out answers for a specific template (e.g you want to see all filled out “Health History” forms)

`date` refers to the date the form was filled out (or the date of service in the case of chart notes).

On the right, you can find an example of a simple query that returns filled out form data for a given form template and day.

## Retrieving a Charting Note PDF via the API

A Charting Note PDF can be retrieved via a cURL request. Below is an example request:

Terminal window

```
curl --request POST \


  --url 'https://api.gethealthie.com/selected_private_notes.pdf?form_answer_array=[123456]&patient_id=111111' \


  --header 'Authorization: Basic YOUR_API_KEY_HERE' \


  --header 'AuthorizationSource: API'
```

A list of `form_answer_group_ids` can be passed into the `form_answer_array` field in the URL, separated by commas.

As part of the Authorization header, a valid API key must be passed in. More information can be found in the [Authentication](/guides/api-concepts/authentication/) section.
