---
title: Webhook Event Reference | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/webhooks/event-reference/index
  md: https://docs.gethealthie.com/guides/webhooks/event-reference/index.md
---

This page documents every webhook event Healthie emits — including the payload format, which GraphQL mutations trigger each event, and any extra fields included beyond the standard payload.

See the [Webhooks overview](/guides/webhooks/) for how to set up endpoints, verify signatures, and handle retries.

## Standard payload

Every webhook POST body contains at minimum:

Standard payload

```
{
  "resource_id": "12345",
  "resource_id_type": "ResourceType",
  "event_type": "resource.action",
  "changed_fields": []
}
```

* **`resource_id`** — ID of the affected record. Use this to query the resource via GraphQL after receiving the event.
* **`resource_id_type`** — The GraphQL type name of the resource (e.g. `Appointment`, `User`, `FormAnswerGroup`).
* **`event_type`** — The event that occurred.
* **`changed_fields`** — For `updated` events, lists the field names that changed. Empty for `created` and `deleted` events.

Note

`updated_at` and `created_at` are excluded from `changed_fields` even when they change.

Some events include additional fields beyond these four — those are documented in each event’s section below.

***

## Appointment

Note

`appointment.created`, `appointment.updated`, and `appointment.deleted` are only triggered for one-time appointments by default. To also receive these events for recurring appointments, contact Healthie support at <hello@gethealthie.com>.

### `appointment.created`

#### Overview

Fires when a new appointment is created in the system.

#### GraphQL Mutations

* `createAppointment`
* `completeCheckout`

#### Example Payload

```
{
  "resource_id": "67890",
  "resource_id_type": "Appointment",
  "event_type": "appointment.created",
  "changed_fields": [],
  "resource_organization_id": "org_123"
}
```

***

### `appointment.deleted`

#### Overview

Fires when an appointment is deleted from the system.

#### When It Fires

When deleteAppointment mutation is called

#### GraphQL Mutations

* `deleteAppointment`

#### Example Payload

```
{
  "resource_id": "67890",
  "resource_id_type": "Appointment",
  "event_type": "appointment.deleted",
  "changed_fields": []
}
```

***

### `appointment.participant_joined`

#### Overview

appointment.participant\_joined fires when a participant joins a Zoom appointment.

#### When It Fires

* Manually triggered when a user joins the Zoom appointment session

#### Example Payload

```
{
  "resource_id": "67890",
  "resource_id_type": "Appointment",
  "event_type": "appointment.participant_joined",
  "changed_fields": [],
  "host_user_id": "1234",
  "user_name": "username",
  "user_email": "user@email.com"
  "event_ts": 1742900000
}
```

***

### `appointment.participant_left`

#### Overview

appointment.participant\_left fires when a participant leaves a Zoom appointment.

#### When It Fires

* Manually triggered when a user leaves the Zoom appointment session

#### Example Payload

```
{
  "resource_id": "67890",
  "resource_id_type": "Appointment",
  "event_type": "appointment.participant_left",
  "changed_fields": [],
  "host_user_id": "1234",
  "user_name": "username",
  "user_email": "user@email.com"
  "event_ts": 1742900000
}
```

***

### `appointment.patient_added`

#### Overview

Fires when a patient is added to an appointment.

#### When It Fires

* Manually triggered when a patient is assigned to the appointment

#### Example Payload

```
{
  "resource_id": "67890",
  "resource_id_type": "Appointment",
  "event_type": "appointment.patient_added",
  "changed_fields": []
}
```

***

### `appointment.patient_removed`

#### Overview

Fires when a patient is removed from an appointment.

#### When It Fires

* Manually triggered when a patient is unassigned from the appointment

#### Example Payload

```
{
  "resource_id": "67890",
  "resource_id_type": "Appointment",
  "event_type": "appointment.patient_removed",
  "changed_fields": []
}
```

***

### `appointment.recording_completed`

Fires when `appointment.recording_completed` occurs.

***

### `appointment.recording_started`

#### Overview

Fires when recording starts for an appointment.

#### When It Fires

* Manually triggered when appointment recording begins

#### Example Payload

```
{
  "resource_id": "67890",
  "resource_id_type": "Appointment",
  "event_type": "appointment.recording_started",
  "changed_fields": []
}
```

***

### `appointment.recording_stopped`

#### Overview

Fires when recording stops for an appointment.

#### When It Fires

When an appointment recording stops

#### GraphQL Mutations

No GraphQL mutations trigger this webhook. Recording status is controlled by third-party services and triggered internally.

#### Example Payload

```
{
  "resource_id": "67890",
  "resource_id_type": "Appointment",
  "event_type": "appointment.recording_stopped",
  "changed_fields": []
}
```

***

### `appointment.transcript_available`

#### Overview

Fires when a transcript becomes available for an appointment.

#### GraphQL Mutations

No GraphQL mutations trigger this webhook. Transcript availability is determined by third-party services and triggered internally.

#### Example Payload

```
{
  "resource_id": "67890",
  "resource_id_type": "Appointment",
  "event_type": "appointment.transcript_available",
  "changed_fields": []
}
```

***

### `appointment.updated`

#### Overview

Fires when an existing appointment is modified.

#### When It Fires

When updateAppointment mutation is called

#### GraphQL Mutations

* `updateAppointment`

#### Example Payload

```
{
  "resource_id": "67890",
  "resource_id_type": "Appointment",
  "event_type": "appointment.updated",
  "changed_fields": ["date", "pm_status"],
  "resource_organization_id": "org_123"
}
```

***

### `availability.deleted`

#### Overview

Fires when availability is deleted.

#### When It Fires

When deleteAvailability mutation is called

#### GraphQL Mutations

* `deleteAvailability`

#### Example Payload

```
{
  "resource_id": "40000",
  "resource_id_type": "Availability",
  "event_type": "availability.deleted",
  "changed_fields": []
}
```

***

### `availability.updated`

#### Overview

Fires when availability is updated.

#### GraphQL Mutations

* `updateAvailability`

#### Example Payload

```
{
  "resource_id": "40000",
  "resource_id_type": "Availability",
  "event_type": "availability.updated",
  "changed_fields": ["day_of_week"]
}
```

***

## User

### `applied_tag.created`

#### Overview

Fires when a tag is applied to a resource.

#### GraphQL Mutations

* `bulkApply`

#### Example Payload

```
{
  "resource_id": "18000",
  "resource_id_type": "AppliedTag",
  "event_type": "applied_tag.created",
  "changed_fields": [],
  "tag_id": "12000",
  "user_id": "22222"
}
```

#### Notes

* `tag_id`: ID of the tag that was applied
* `user_id`: ID of the user the tag was applied to

***

### `applied_tag.deleted`

#### Overview

Fires when a tag is removed from a resource.

#### When It Fires

* When `removeAppliedTag` mutation is called

#### GraphQL Mutations

* `removeAppliedTag`

#### Example Payload

```
{
  "resource_id": "18000",
  "resource_id_type": "AppliedTag",
  "event_type": "applied_tag.deleted",
  "changed_fields": [],
  "tag_id": "12000",
  "user_id": "22222"
}
```

#### Notes

* `tag_id`: ID of the tag that was removed
* `user_id`: ID of the user the tag was removed from

***

### `course_membership.created`

#### Overview

Fires when a course membership is created.

#### When It Fires

* When `createCourseMembership` mutation is called

#### GraphQL Mutations

* `createCourseMembership`

#### Example Payload

```
{
  "resource_id": "41000",
  "resource_id_type": "CourseMembership",
  "event_type": "course_membership.created",
  "changed_fields": []
}
```

***

### `course_membership.deleted`

#### Overview

Fires when a course membership is deleted.

#### GraphQL Mutations

* `deleteCourseMembership`

#### Example Payload

```
{
  "resource_id": "41000",
  "resource_id_type": "CourseMembership",
  "event_type": "course_membership.deleted",
  "changed_fields": []
}
```

***

### `course_membership.updated`

#### Overview

Fires when a course membership is updated.

#### When It Fires

When updateCourseMembership mutation is called

#### GraphQL Mutations

* `updateCourseMembership`

#### Example Payload

```
{
  "resource_id": "41000",
  "resource_id_type": "CourseMembership",
  "event_type": "course_membership.updated",
  "changed_fields": ["progress"]
}
```

***

### `feature_toggle.created`

#### Overview

Fires when a feature toggle is created.

#### GraphQL Mutations

* `createFeatureToggle`

#### Example Payload

```
{
  "resource_id": "52000",
  "resource_id_type": "FeatureToggle",
  "event_type": "feature_toggle.created",
  "changed_fields": [],
  "care_plan_id": "23000",
  "user_id": "22222",
  "user_group_id": "15000"
}
```

#### Notes

* `care_plan_id`: ID of the care plan this toggle is associated with (nullable)
* `user_id`: ID of the user this toggle is associated with (nullable)
* `user_group_id`: ID of the user group this toggle is associated with (nullable)

***

### `feature_toggle.deleted`

#### Overview

Fires when a feature toggle is deleted.

#### GraphQL Mutations

* `deleteFeatureToggle`

#### Example Payload

```
{
  "resource_id": "52000",
  "resource_id_type": "FeatureToggle",
  "event_type": "feature_toggle.deleted",
  "changed_fields": [],
  "care_plan_id": "23000",
  "user_id": "22222",
  "user_group_id": "15000"
}
```

#### Notes

* `care_plan_id`: ID of the care plan this toggle was associated with (nullable)
* `user_id`: ID of the user this toggle was associated with (nullable)
* `user_group_id`: ID of the user group this toggle was associated with (nullable)

***

### `feature_toggle.updated`

#### Overview

Fires when a feature toggle is updated.

#### GraphQL Mutations

* `updateFeatureToggle`

#### Example Payload

```
{
  "resource_id": "52000",
  "resource_id_type": "FeatureToggle",
  "event_type": "feature_toggle.updated",
  "changed_fields": ["enabled"],
  "care_plan_id": "23000",
  "user_id": "22222",
  "user_group_id": "15000"
}
```

#### Notes

* `care_plan_id`: ID of the care plan this toggle is associated with (nullable)
* `user_id`: ID of the user this toggle is associated with (nullable)
* `user_group_id`: ID of the user group this toggle is associated with (nullable)

***

### `notification_contact.created`

#### Overview

Fires when a notification contact is created.

#### GraphQL Mutations

* `createNotificationContact`

#### Example Payload

```
{
  "resource_id": "49000",
  "resource_id_type": "NotificationContact",
  "event_type": "notification_contact.created",
  "changed_fields": [],
  "linked_client_id": "22222",
  "user_id": "22222"
}
```

#### Notes

* `linked_client_id`: ID of the linked client associated with this contact (nullable)
* `user_id`: ID of the provider/user this notification contact belongs to

***

### `notification_contact.deleted`

#### Overview

Fires when a notification contact is deleted.

#### When It Fires

When deleteNotificationContact mutation is called

#### GraphQL Mutations

* `deleteNotificationContact`

#### Example Payload

```
{
  "resource_id": "49000",
  "resource_id_type": "NotificationContact",
  "event_type": "notification_contact.deleted",
  "changed_fields": [],
  "linked_client_id": "22222",
  "user_id": "22222"
}
```

#### Notes

* `linked_client_id`: ID of the linked client associated with this contact (nullable)
* `user_id`: ID of the provider/user this notification contact belonged to

***

### `notification_contact.updated`

#### Overview

Fires when a notification contact is updated.

#### When It Fires

When updateNotificationContact mutation is called

#### GraphQL Mutations

* `updateNotificationContact`

#### Example Payload

```
{
  "resource_id": "49000",
  "resource_id_type": "NotificationContact",
  "event_type": "notification_contact.updated",
  "changed_fields": ["email"],
  "linked_client_id": "22222",
  "user_id": "22222"
}
```

#### Notes

* `linked_client_id`: ID of the linked client associated with this contact (nullable)
* `user_id`: ID of the provider/user this notification contact belongs to

***

### `notification_setting.created`

#### Overview

Fires when a notification setting is created.

#### When It Fires

Automatically created when notification preferences are configured

#### GraphQL Mutations

No GraphQL mutations trigger notification setting creation. Settings are created automatically through internal mechanisms.

#### Example Payload

```
{
  "resource_id": "56000",
  "resource_id_type": "NotificationSetting",
  "event_type": "notification_setting.created",
  "changed_fields": [],
  "user_id": "22222"
}
```

#### Notes

* `user_id`: ID of the user this notification setting belongs to (nullable)

***

### `notification_setting.deleted`

#### Overview

Fires when a notification setting is deleted.

#### When It Fires

Triggers internally at custom requests

#### GraphQL Mutation

No graphql mutations trigger this.

#### Example Payload

```
{
  "resource_id": "56000",
  "resource_id_type": "NotificationSetting",
  "event_type": "notification_setting.deleted",
  "changed_fields": [],
  "user_id": "22222"
}
```

#### Notes

* `user_id`: ID of the user this notification setting belonged to (nullable)

***

### `notification_setting.updated`

#### Overview

Fires when a notification setting is updated.

#### GraphQL Mutations

* `updateNotificationSetting`

#### Example Payload

```
{
  "resource_id": "56000",
  "resource_id_type": "NotificationSetting",
  "event_type": "notification_setting.updated",
  "changed_fields": ["enabled"],
  "user_id": "22222"
}
```

#### Notes

* `user_id`: ID of the user this notification setting belongs to (nullable)

***

### `other_id_number.created`

#### Overview

Fires when an alternate ID is added to a provider.

#### When It Fires

* After an OtherIdNumber record is created (triggered internally)

#### GraphQL Mutations

No dedicated mutation exists for OtherIdNumber. Other ID numbers are created as nested inputs within `createCms1500` and `updateCms1500` mutations.

#### Example Payload

```
{
  "resource_id": "38000",
  "resource_id_type": "OtherIdNumber",
  "event_type": "other_id_number.created",
  "changed_fields": []
}
```

***

### `other_id_number.deleted`

#### Overview

Fires when an alternate ID is removed.

#### When It Fires

* After an OtherIdNumber record is destroyed (triggered internally)

#### GraphQL Mutations

No mutation exists for deleting OtherIdNumber records. Deletions are handled internally.

#### Example Payload

```
{
  "resource_id": "38000",
  "resource_id_type": "OtherIdNumber",
  "event_type": "other_id_number.deleted",
  "changed_fields": []
}
```

***

### `other_id_number.updated`

#### Overview

Fires when an alternate ID is updated.

#### When It Fires

* After an OtherIdNumber record is updated (triggered internally)

#### GraphQL Mutations

No dedicated mutation exists for OtherIdNumber. Other ID numbers are updated as nested inputs within `updateCms1500` mutation.

#### Example Payload

```
{
  "resource_id": "38000",
  "resource_id_type": "OtherIdNumber",
  "event_type": "other_id_number.updated",
  "changed_fields": ["id_number"]
}
```

***

### `patient.created`

#### Overview

Fires when a new patient is created.

#### When It Fires

When `createClient`, `completeCheckout`, or `createNotificationContact` mutation is called

#### GraphQL Mutations

* `createClient` - Creates a new patient/client record
* `completeCheckout` - Completes a checkout process which can create a patient
* `createNotificationContact` - Creates a notification contact which can trigger patient creation

#### Example Payload

```
{
  "resource_id": "45678",
  "resource_id_type": "User",
  "event_type": "patient.created",
  "changed_fields": []
}
```

***

### `patient.merged`

#### Overview

Fires when two patient records are merged.

#### When It Fires

When two patient records are merged together

#### GraphQL Mutations

* `mergeClients`

#### Example Payload

```
{
  "resource_id": "45678",
  "resource_id_type": "User",
  "event_type": "patient.merged",
  "changed_fields": [],
  "destination_user_id": "1234",
  "source_user_id": "5678"
}
```

***

### `patient.updated`

#### Overview

Fires when an existing patient is modified.

#### When It Fires

When `updateClient`, `bulkUpdateClients`, or `toggleCarePlanStatusForSpecificUser` mutation is called, or when patient fields are modified through form submissions or appointment check-ins

#### GraphQL Mutations

* `updateClient` - Updates a patient/client record
* `bulkUpdateClients` - Updates multiple patient records at once
* `toggleCarePlanStatusForSpecificUser` - Activates/deactivates a care plan for a specific patient
* Also fires when form submissions or appointment check-ins update patient fields

#### Example Payload

```
{
  "resource_id": "45678",
  "resource_id_type": "User",
  "event_type": "patient.updated",
  "changed_fields": ["first_name", "email"]
}
```

***

## Form

### `appointment_form_answer_group_connection.created`

#### Overview

Fires when a form is connected to an appointment.

#### Example Payload

```
{
  "resource_id": "42000",
  "resource_id_type": "AppointmentFormAnswerGroupConnection",
  "event_type": "appointment_form_answer_group_connection.created",
  "changed_fields": [],
  "appointment_id": "10000",
  "form_answer_group_id": "14000"
}
```

#### Notes

* `appointment_id`: ID of the appointment this form is connected to
* `form_answer_group_id`: ID of the form answer group connected to this appointment

***

### `appointment_form_answer_group_connection.deleted`

#### Overview

Fires when a form is disconnected from an appointment.

#### Example Payload

```
{
  "resource_id": "42000",
  "resource_id_type": "AppointmentFormAnswerGroupConnection",
  "event_type": "appointment_form_answer_group_connection.deleted",
  "changed_fields": [],
  "appointment_id": "10000",
  "form_answer_group_id": "14000"
}
```

#### Notes

* `appointment_id`: ID of the appointment this form was connected to
* `form_answer_group_id`: ID of the form answer group that was connected to this appointment

***

### `appointment_form_answer_group_connection.updated`

#### Overview

Fires when a form-appointment connection is updated.

#### When It Fires

When a form-appointment connection is updated

#### Example Payload

```
{
  "resource_id": "42000",
  "resource_id_type": "AppointmentFormAnswerGroupConnection",
  "event_type": "appointment_form_answer_group_connection.updated",
  "changed_fields": [],
  "appointment_id": "10000",
  "form_answer_group_id": "14000"
}
```

#### Notes

* `appointment_id`: ID of the appointment this form is connected to
* `form_answer_group_id`: ID of the form answer group connected to this appointment

***

### `completed_onboarding_item.created`

#### Overview

Fires when an onboarding item is completed.

#### GraphQL Mutations

* `createCompletedOnboardingItem`

#### Example Payload

```
{
  "resource_id": "39000",
  "resource_id_type": "CompletedOnboardingItem",
  "event_type": "completed_onboarding_item.created",
  "changed_fields": []
}
```

***

### `completed_onboarding_item.deleted`

#### Overview

Fires when a completed onboarding item is deleted.

#### When It Fires

After a CompletedOnboardingItem record is destroyed (triggered internally)

#### GraphQL Mutations

No delete mutation exists for CompletedOnboardingItem. Deletions are handled internally.

#### Example Payload

```
{
  "resource_id": "39000",
  "resource_id_type": "CompletedOnboardingItem",
  "event_type": "completed_onboarding_item.deleted",
  "changed_fields": []
}
```

***

### `completed_onboarding_item.updated`

#### Overview

Fires when a completed onboarding item is updated.

#### When It Fires

After a CompletedOnboardingItem record is updated (triggered internally)

#### GraphQL Mutations

No update mutation exists for CompletedOnboardingItem. Updates are handled internally.

#### Example Payload

```
{
  "resource_id": "39000",
  "resource_id_type": "CompletedOnboardingItem",
  "event_type": "completed_onboarding_item.updated",
  "changed_fields": ["response"]
}
```

***

### `custom_module_form.created`

#### Overview

Fires when a custom module form is created.

#### When It Fires

When createCustomModuleForm mutation is called

#### GraphQL Mutations

* `createCustomModuleForm`

#### Example Payload

```
{
  "resource_id": "44000",
  "resource_id_type": "CustomModuleForm",
  "event_type": "custom_module_form.created",
  "changed_fields": []
}
```

***

### `custom_module_form.deleted`

#### Overview

Fires when a custom module form is deleted.

#### When It Fires

When deleteCustomModuleForm mutation is called

#### GraphQL Mutations

* `deleteCustomModuleForm`

#### Example Payload

```
{
  "resource_id": "44000",
  "resource_id_type": "CustomModuleForm",
  "event_type": "custom_module_form.deleted",
  "changed_fields": []
}
```

***

### `custom_module_form.updated`

#### Overview

Fires when a custom module form is updated.

#### When It Fires

When updateCustomModuleForm mutation is called

#### GraphQL Mutations

* `updateCustomModuleForm`

#### Example Payload

```
{
  "resource_id": "44000",
  "resource_id_type": "CustomModuleForm",
  "event_type": "custom_module_form.updated",
  "changed_fields": ["name"]
}
```

***

### `custom_module.created`

#### Overview

Fires when a custom module is created.

#### When It Fires

When createCustomModule mutation is called

#### GraphQL Mutations

* `createCustomModule`

#### Example Payload

```
{
  "resource_id": "45000",
  "resource_id_type": "CustomModule",
  "event_type": "custom_module.created",
  "changed_fields": [],
  "custom_module_form_id": "31000"
}
```

#### Notes

* `custom_module_form_id`: ID of the custom module form this module belongs to (nullable)

***

### `custom_module.deleted`

#### Overview

Fires when a custom module is deleted.

#### When It Fires

When deleteCustomModule mutation is called

#### GraphQL Mutations

* `deleteCustomModule`

#### Example Payload

```
{
  "resource_id": "45000",
  "resource_id_type": "CustomModule",
  "event_type": "custom_module.deleted",
  "changed_fields": [],
  "custom_module_form_id": "31000"
}
```

#### Notes

* `custom_module_form_id`: ID of the custom module form this module belonged to (nullable)

***

### `custom_module.updated`

#### Overview

Fires when a custom module is updated.

#### When It Fires

When updateCustomModule mutation is called

#### GraphQL Mutations

* `updateCustomModule`

#### Example Payload

```
{
  "resource_id": "45000",
  "resource_id_type": "CustomModule",
  "event_type": "custom_module.updated",
  "changed_fields": ["label"],
  "custom_module_form_id": "31000"
}
```

#### Notes

* `custom_module_form_id`: ID of the custom module form this module belongs to (nullable)

***

### `form_answer_group.created`

#### Overview

Fires when a form submission is created.

#### GraphQL Mutations

* `createFormAnswerGroup`

#### Example Payload

```
{
  "resource_id": "98765",
  "resource_id_type": "FormAnswerGroup",
  "event_type": "form_answer_group.created",
  "changed_fields": []
}
```

***

### `form_answer_group.deleted`

#### Overview

Fires when a form submission is deleted.

#### When It Fires

When deleteFormAnswerGroup mutation is called

#### GraphQL Mutations

* `deleteFormAnswerGroup`

#### Example Payload

```
{
  "resource_id": "98765",
  "resource_id_type": "FormAnswerGroup",
  "event_type": "form_answer_group.deleted",
  "changed_fields": []
}
```

***

### `form_answer_group.locked`

#### Overview

Fires when a form submission is locked.

#### When It Fires

When lockFormAnswerGroup mutation is called

#### GraphQL Mutations

* `lockFormAnswerGroup`

#### Example Payload

```
{
  "resource_id": "98765",
  "resource_id_type": "FormAnswerGroup",
  "event_type": "form_answer_group.locked",
  "changed_fields": []
}
```

***

### `form_answer_group.signed`

#### Overview

Fires when a form submission is signed.

#### GraphQL Mutations

* `createFormAnswerGroupSigning`

#### Example Payload

```
{
  "resource_id": "98765",
  "resource_id_type": "FormAnswerGroup",
  "event_type": "form_answer_group.signed",
  "changed_fields": []
}
```

***

### `form_answer_group.unlocked`

#### Overview

Fires when a form submission is unlocked.

#### When It Fires

When unlockFormAnswerGroup mutation is called

#### GraphQL Mutations

* `unlockFormAnswerGroup`

#### Example Payload

```
{
  "resource_id": "98765",
  "resource_id_type": "FormAnswerGroup",
  "event_type": "form_answer_group.unlocked",
  "changed_fields": []
}
```

***

### `generated_form_answer_group.created`

#### Overview

Fires when a generated form answer group is created.

#### Example Payload

```
{
  "resource_id": "11223",
  "resource_id_type": "GeneratedFormAnswerGroup",
  "event_type": "generated_form_answer_group.created",
  "changed_fields": [],
  "patient_id": "22222"
}
```

#### Notes

* `patient_id`: ID of the patient this generated form answer group belongs to

***

### `requested_form_completion.created`

#### Overview

Fires when a form is requested to be completed.

#### GraphQL Mutations

* `createRequestedFormCompletion`

#### Example Payload

```
{
  "resource_id": "15000",
  "resource_id_type": "RequestedFormCompletion",
  "event_type": "requested_form_completion.created",
  "changed_fields": []
}
```

***

### `requested_form_completion.deleted`

#### Overview

Fires when a requested form completion is deleted.

#### When It Fires

When a requested form completion is deleted

#### GraphQL Mutations

* `deleteRequestedForm`

#### Example Payload

```
{
  "resource_id": "15000",
  "resource_id_type": "RequestedFormCompletion",
  "event_type": "requested_form_completion.deleted",
  "changed_fields": []
}
```

***

### `requested_form_completion.updated`

#### Overview

Fires when a requested form completion is updated.

#### When It Fires

When a requested form completion is updated

* \`

#### Example Payload

```
{
  "resource_id": "15000",
  "resource_id_type": "RequestedFormCompletion",
  "event_type": "requested_form_completion.updated",
  "changed_fields": ["is_complete"]
}
```

***

## Message

### `conversation_membership.created`

#### Overview

Fires when a user is added to a conversation.

#### When It Fires

When createConversationMembership mutation is called

#### GraphQL Mutations

* `createConversationMembership`

#### Example Payload

```
{
  "resource_id": "14000",
  "resource_id_type": "ConversationMembership",
  "event_type": "conversation_membership.created",
  "changed_fields": []
}
```

***

### `conversation_membership.deleted`

#### Overview

Fires when a user is removed from a conversation.

#### When It Fires

When deleteConversationMembership mutation is called

#### GraphQL Mutations

* `deleteConversationMembership`

#### Example Payload

```
{
  "resource_id": "14000",
  "resource_id_type": "ConversationMembership",
  "event_type": "conversation_membership.deleted",
  "changed_fields": []
}
```

***

### `conversation_membership.viewed`

#### Overview

Fires when a user views a conversation.

#### GraphQL Mutations

No GraphQL mutations trigger the conversation\_membership.viewed webhook. Viewing status is updated through internal mechanisms.

#### Example Payload

```
{
  "resource_id": "14000",
  "resource_id_type": "ConversationMembership",
  "event_type": "conversation_membership.viewed",
  "changed_fields": []
}
```

***

### `conversation.created`

#### Overview

Fires when a new conversation is started.

#### When It Fires

When a new conversation is started

#### GraphQL Mutations

* `createConversation`

#### Example Payload

```
{
  "resource_id": "13000",
  "resource_id_type": "Conversation",
  "event_type": "conversation.created",
  "changed_fields": []
}
```

***

### `conversation.updated`

#### Overview

Fires when a conversation is updated.

#### When It Fires

When `updateConversation` mutation is called

#### GraphQL Mutations

* `updateConversation`

#### Example Payload

```
{
  "resource_id": "13000",
  "resource_id_type": "Conversation",
  "event_type": "conversation.updated",
  "changed_fields": ["name"]
}
```

***

### `message.created`

#### Overview

Fires when a new message is sent.

#### When It Fires

When createNote mutation is called

#### GraphQL Mutations

* `createNote`

#### Example Payload

```
{
  "resource_id": "55443",
  "resource_id_type": "Note",
  "event_type": "message.created",
  "changed_fields": []
}
```

***

### `message.deleted`

#### Overview

Fires when a message is deleted.

#### When It Fires

When deleteNote mutation is called

#### GraphQL Mutations

* `deleteNote`

#### Example Payload

```
{
  "resource_id": "55443",
  "resource_id_type": "Note",
  "event_type": "message.deleted",
  "changed_fields": []
}
```

***

### `scheduled_message.sent`

#### Overview

Fires when a scheduled message is sent.

#### Example Payload

```
{
  "resource_id": "46000",
  "resource_id_type": "NoteScheduler",
  "event_type": "scheduled_message.sent",
  "changed_fields": []
}
```

***

## Billing

### `accepted_insurance_plan.created`

#### Overview

Fires when an accepted insurance plan is added.

#### GraphQL Mutations

* `createAcceptedInsurancePlan`

#### Example Payload

```
{
  "resource_id": "47000",
  "resource_id_type": "AcceptedInsurancePlan",
  "event_type": "accepted_insurance_plan.created",
  "changed_fields": []
}
```

***

### `accepted_insurance_plan.deleted`

#### Overview

Fires when an accepted insurance plan is removed.

#### GraphQL Mutations

* `deleteAcceptedInsurancePlan`

#### Example Payload

```
{
  "resource_id": "47000",
  "resource_id_type": "AcceptedInsurancePlan",
  "event_type": "accepted_insurance_plan.deleted",
  "changed_fields": []
}
```

***

### `billing_item.created`

#### Overview

Fires when a new billing item is created.

#### When It Fires

When createBillingItem mutation is called

#### GraphQL Mutations

* `createBillingItem`
* `completeCheckout`

#### Example Payload

```
{
  "resource_id": "55555",
  "resource_id_type": "BillingItem",
  "event_type": "billing_item.created",
  "changed_fields": [],
  "requested_payment_id": "40000"
}
```

#### Notes

* `requested_payment_id`: ID of the requested payment this billing item was created for (nullable)

***

### `billing_item.deleted`

#### Overview

Fires when a billing item is deleted.

#### When It Fires

When deleteBillingItem mutation is called

#### GraphQL Mutations

* `deleteBillingItem`

#### Example Payload

```
{
  "resource_id": "55555",
  "resource_id_type": "BillingItem",
  "event_type": "billing_item.deleted",
  "changed_fields": [],
  "requested_payment_id": "40000"
}
```

#### Notes

* `requested_payment_id`: ID of the requested payment this billing item was created for (nullable)

***

### `billing_item.updated`

#### Overview

Fires when a billing item is updated.

#### When It Fires

When updateBillingItem mutation is called

#### GraphQL Mutations

* `updateBillingItem`

#### Example Payload

```
{
  "resource_id": "55555",
  "resource_id_type": "BillingItem",
  "event_type": "billing_item.updated",
  "changed_fields": ["amount", "code"],
  "requested_payment_id": "40000"
}
```

#### Notes

* `requested_payment_id`: ID of the requested payment this billing item was created for (nullable)

***

### `charge_back.created`

#### Overview

Fires when a chargeback is created.

#### GraphQL Mutations

No GraphQL mutations directly trigger this webhook. It’s triggered internally when a chargeback is created by the payment processor.

#### Example Payload

```
{
  "resource_id": "54000",
  "resource_id_type": "ChargeBack",
  "event_type": "charge_back.created",
  "changed_fields": [],
  "billing_item_id": "55555"
}
```

#### Notes

* `billing_item_id`: ID of the billing item this chargeback is associated with

***

### `charge_back.deleted`

#### Overview

Fires when a chargeback is deleted.

#### GraphQL Mutations

No GraphQL mutations directly trigger this webhook. It’s triggered internally when a chargeback is deleted by the payment processor.

#### Example Payload

```
{
  "resource_id": "54000",
  "resource_id_type": "ChargeBack",
  "event_type": "charge_back.deleted",
  "changed_fields": [],
  "billing_item_id": "55555"
}
```

#### Notes

* `billing_item_id`: ID of the billing item this chargeback was associated with

***

### `charge_back.updated`

#### Overview

Fires when a chargeback is updated.

#### GraphQL Mutations

* `updateChargeBack`

#### Example Payload

```
{
  "resource_id": "54000",
  "resource_id_type": "ChargeBack",
  "event_type": "charge_back.updated",
  "changed_fields": ["status"],
  "billing_item_id": "55555"
}
```

#### Notes

* `billing_item_id`: ID of the billing item this chargeback is associated with

***

### `claim_submission.created`

#### Overview

Fires when a claim submission is created.

#### When It Fires

When a claim submission is created

#### Example Payload

```
{
  "resource_id": "55000",
  "resource_id_type": "ClaimSubmission",
  "event_type": "claim_submission.created",
  "changed_fields": [],
  "cms1500_id": "32000"
}
```

#### Notes

* `cms1500_id`: ID of the CMS 1500 form associated with this claim submission

***

### `claim_submission.deleted`

#### Overview

Fires when a claim submission is deleted.

#### When It Fires

* After a ClaimSubmission record is destroyed (triggered internally)

#### GraphQL Mutations

No mutation exists for deleting ClaimSubmission records. Deletions are handled internally.

#### Example Payload

```
{
  "resource_id": "55000",
  "resource_id_type": "ClaimSubmission",
  "event_type": "claim_submission.deleted",
  "changed_fields": [],
  "cms1500_id": "32000"
}
```

#### Notes

* `cms1500_id`: ID of the CMS 1500 form associated with this claim submission

***

### `claim_submission.updated`

#### Overview

Fires when a claim submission is updated.

#### Example Payload

```
{
  "resource_id": "55000",
  "resource_id_type": "ClaimSubmission",
  "event_type": "claim_submission.updated",
  "changed_fields": ["status"],
  "cms1500_id": "32000"
}
```

#### Notes

* `cms1500_id`: ID of the CMS 1500 form associated with this claim submission

***

### `cms1500.created`

#### Overview

Fires when a CMS1500 is created.

#### When It Fires

When a CMS1500 is created

#### GraphQL Mutations

* `createCms1500`

#### Example Payload

```
{
  "resource_id": "88888",
  "resource_id_type": "Cms1500",
  "event_type": "cms1500.created",
  "changed_fields": []
}
```

***

### `cms1500.deleted`

#### Overview

Fires when a CMS1500 form is deleted.

#### When It Fires

When a CMS1500 is deleted

#### GraphQL Mutations

* `deleteCms1500`

#### Example Payload

```
{
  "resource_id": "88888",
  "resource_id_type": "Cms1500",
  "event_type": "cms1500.deleted",
  "changed_fields": []
}
```

***

### `cms1500.updated`

#### Overview

Fires when a CMS1500 updated.

#### When It Fires

When a CMS1500 is updated

#### GraphQL Mutations

* `updateCms1500`

#### Example Payload

```
{
  "resource_id": "88888",
  "resource_id_type": "Cms1500",
  "event_type": "cms1500.updated",
  "changed_fields": ["status"]
}
```

***

### `insurance_authorization.created`

#### Overview

Fires when an insurance authorization is created.

#### When It Fires

When `createInsuranceAuthorization` mutation is called

#### GraphQL Mutations

* `createInsuranceAuthorization`

#### Example Payload

```
{
  "resource_id": "17000",
  "resource_id_type": "InsuranceAuthorization",
  "event_type": "insurance_authorization.created",
  "changed_fields": []
}
```

***

### `insurance_authorization.deleted`

#### Overview

Fires when an insurance authorization is deleted.

#### When It Fires

When deleteInsuranceAuthorization mutation is called

#### GraphQL Mutations

* `deleteInsuranceAuthorization`

#### Example Payload

```
{
  "resource_id": "17000",
  "resource_id_type": "InsuranceAuthorization",
  "event_type": "insurance_authorization.deleted",
  "changed_fields": []
}
```

***

### `insurance_authorization.updated`

#### Overview

Fires when an insurance authorization is updated.

#### When It Fires

When updateInsuranceAuthorization mutation is called

#### GraphQL Mutations

* `updateInsuranceAuthorization`

#### Example Payload

```
{
  "resource_id": "17000",
  "resource_id_type": "InsuranceAuthorization",
  "event_type": "insurance_authorization.updated",
  "changed_fields": ["units_authorized"]
}
```

***

### `policy.created`

#### Overview

Fires when an insurance policy is created.

#### GraphQL Mutations

* `updateClient`

#### Example Payload

```
{
  "resource_id": "16000",
  "resource_id_type": "Policy",
  "event_type": "policy.created",
  "changed_fields": []
}
```

***

### `policy.deleted`

#### Overview

Fires when an insurance policy is deleted.

#### GraphQL Mutations

* `updateClient`

#### Example Payload

```
{
  "resource_id": "16000",
  "resource_id_type": "Policy",
  "event_type": "policy.deleted",
  "changed_fields": []
}
```

***

### `policy.updated`

#### Overview

Fires when an insurance policy is updated.

#### When It Fires

When updatePolicy mutation is called

#### GraphQL Mutations

* `updatePolicy`

#### Example Payload

```
{
  "resource_id": "16000",
  "resource_id_type": "Policy",
  "event_type": "policy.updated",
  "changed_fields": ["holder_relationship"]
}
```

***

### `recurring_payment.created`

#### Overview

Fires when a recurring payment is set up.

#### When it Fires

When a recurring payment is created via internal mechanisms

#### GraphQL Mutations

* `createBillingItem`

#### Example Payload

```
{
  "resource_id": "77777",
  "resource_id_type": "RecurringPayment",
  "event_type": "recurring_payment.created",
  "changed_fields": []
}
```

***

### `recurring_payment.updated`

#### Overview

Fires when a recurring payment is modified.

#### When It Fires

* When `updateBillingItem` or `cancelRecurringPayment` mutation is called

#### GraphQL Mutations

* `updateBillingItem`
* `cancelRecurringPayment`

#### Example Payload

```
{
  "resource_id": "77777",
  "resource_id_type": "RecurringPayment",
  "event_type": "recurring_payment.updated",
  "changed_fields": ["amount"]
}
```

***

### `requested_payment.created`

#### Overview

Fires when a payment request is created.

#### GraphQL Mutations

* `createRequestedPayment`

#### Example Payload

```
{
  "resource_id": "66666",
  "resource_id_type": "RequestedPayment",
  "event_type": "requested_payment.created",
  "changed_fields": []
}
```

***

### `requested_payment.deleted`

#### Overview

Fires when a payment request is deleted.

#### When It Fires

When deleteRequestedPayment mutation is called

#### GraphQL Mutations

* `deleteRequestedPayment`

#### Example Payload

```
{
  "resource_id": "66666",
  "resource_id_type": "RequestedPayment",
  "event_type": "requested_payment.deleted",
  "changed_fields": []
}
```

***

### `requested_payment.updated`

#### Overview

Fires when a payment request is updated.

#### When It Fires

When updateRequestedPayment mutation is called

#### GraphQL Mutations

* `updateRequestedPayment`

#### Example Payload

```
{
  "resource_id": "66666",
  "resource_id_type": "RequestedPayment",
  "event_type": "requested_payment.updated",
  "changed_fields": ["is_paid"]
}
```

***

### `stripe_customer_detail.created`

#### Overview

Fires when Stripe customer details are created.

#### GraphQL Mutations

* `createStripeCustomerDetail`

#### Example Payload

```
{
  "resource_id": "48000",
  "resource_id_type": "StripeCustomerDetail",
  "event_type": "stripe_customer_detail.created",
  "changed_fields": [],
  "user_id": "22222"
}
```

#### Notes

* `user_id`: ID of the user these Stripe customer details belong to

***

### `stripe_customer_detail.deleted`

#### Overview

Fires when Stripe customer details are deleted.

#### GraphQL Mutations

* `deleteStripeCustomerDetail`

#### Example Payload

```
{
  "resource_id": "48000",
  "resource_id_type": "StripeCustomerDetail",
  "event_type": "stripe_customer_detail.deleted",
  "changed_fields": [],
  "user_id": "22222"
}
```

#### Notes

* `user_id`: ID of the user these Stripe customer details belonged to

***

### `stripe_customer_detail.updated`

#### Overview

Fires when Stripe customer details are updated.

#### GraphQL Mutations

* `updateStripeCustomerDetail`

#### Example Payload

```
{
  "resource_id": "48000",
  "resource_id_type": "StripeCustomerDetail",
  "event_type": "stripe_customer_detail.updated",
  "changed_fields": ["stripe_id"],
  "user_id": "22222"
}
```

#### Notes

* `user_id`: ID of the user these Stripe customer details belong to

***

### `super_bill.created`

#### Overview

Fires when a superbill is created.

#### When It Fires

When createSuperBill mutation is called

#### GraphQL Mutations

* `createSuperBill`

#### Example Payload

```
{
  "resource_id": "53000",
  "resource_id_type": "SuperBill",
  "event_type": "super_bill.created",
  "changed_fields": [],
  "patient_id": "22222"
}
```

#### Notes

* `patient_id`: ID of the patient this superbill is for (nullable)

***

### `super_bill.deleted`

#### Overview

Fires when a superbill is deleted.

#### When It Fires

When deleteSuperBill mutation is called

#### GraphQL Mutations

* `deleteSuperBill`

#### Example Payload

```
{
  "resource_id": "53000",
  "resource_id_type": "SuperBill",
  "event_type": "super_bill.deleted",
  "changed_fields": [],
  "patient_id": "22222"
}
```

#### Notes

* `patient_id`: ID of the patient this superbill was for (nullable)

***

### `super_bill.updated`

#### Overview

Fires when a superbill is updated.

#### GraphQL Mutations

* `updateSuperBill`

#### Example Payload

```
{
  "resource_id": "53000",
  "resource_id_type": "SuperBill",
  "event_type": "super_bill.updated",
  "changed_fields": ["status"],
  "patient_id": "22222"
}
```

#### Notes

* `patient_id`: ID of the patient this superbill is for (nullable)

***

## Clinical

### `allergy_sensitivity.created`

#### Overview

Fires when an allergy or sensitivity is recorded.

#### When It Fires

When createAllergySensitivity mutation is called

#### GraphQL Mutations

* `createAllergySensitivity`

#### Example Payload

```
{
  "resource_id": "25000",
  "resource_id_type": "AllergySensitivity",
  "event_type": "allergy_sensitivity.created",
  "changed_fields": [],
  "user_id": "22222"
}
```

#### Notes

* `user_id`: ID of the patient this allergy or sensitivity belongs to

***

### `allergy_sensitivity.deleted`

#### Overview

Fires when an allergy or sensitivity is removed.

#### When It Fires

When deleteAllergySensitivity mutation is called

#### GraphQL Mutations

* `deleteAllergySensitivity`

#### Example Payload

```
{
  "resource_id": "25000",
  "resource_id_type": "AllergySensitivity",
  "event_type": "allergy_sensitivity.deleted",
  "changed_fields": [],
  "user_id": "22222"
}
```

#### Notes

* `user_id`: ID of the patient this allergy or sensitivity belonged to

***

### `allergy_sensitivity.updated`

#### Overview

Fires when an allergy or sensitivity is updated.

#### When It Fires

When updateAllergySensitivity mutation is called

#### GraphQL Mutations

* `updateAllergySensitivity`

#### Example Payload

```
{
  "resource_id": "25000",
  "resource_id_type": "AllergySensitivity",
  "event_type": "allergy_sensitivity.updated",
  "changed_fields": ["category"],
  "user_id": "22222"
}
```

#### Notes

* `user_id`: ID of the patient this allergy or sensitivity belongs to

***

### `care_plan.activated`

#### Overview

Fires when a care plan is activated.

#### When It Fires

When a care plan is set as the active plan for a patient or user group

#### Example Payload

```
{
  "resource_id": "23000",
  "resource_id_type": "CarePlan",
  "event_type": "care_plan.activated",
  "changed_fields": []
}
```

***

### `care_plan.created`

#### Overview

Fires when a care plan is created.

#### When It Fires

When createCarePlan mutation is called

#### GraphQL Mutations

* `createCarePlan`

#### Example Payload

```
{
  "resource_id": "23000",
  "resource_id_type": "CarePlan",
  "event_type": "care_plan.created",
  "changed_fields": [],
  "patient_id": "22222",
  "user_group_id": "15000"
}
```

#### Notes

* `patient_id`: ID of the patient this care plan belongs to (nullable)
* `user_group_id`: ID of the user group this care plan belongs to (nullable)

***

### `care_plan.deactivated`

#### Overview

Fires when a care plan is deactivated.

#### When It Fires

When a care plan is removed as the active plan

#### Example Payload

```
{
  "resource_id": "23000",
  "resource_id_type": "CarePlan",
  "event_type": "care_plan.deactivated",
  "changed_fields": []
}
```

***

### `care_plan.deleted`

#### Overview

Fires when a care plan is deleted.

#### When It Fires

When deleteCarePlan mutation is called

#### GraphQL Mutations

* `deleteCarePlan`

#### Example Payload

```
{
  "resource_id": "23000",
  "resource_id_type": "CarePlan",
  "event_type": "care_plan.deleted",
  "changed_fields": [],
  "patient_id": "22222",
  "user_group_id": "15000"
}
```

#### Notes

* `patient_id`: ID of the patient this care plan belonged to (nullable)
* `user_group_id`: ID of the user group this care plan belonged to (nullable)

***

### `care_plan.updated`

#### Overview

Fires when a care plan is updated.

#### When It Fires

When updateCarePlan mutation is called

#### GraphQL Mutations

* `updateCarePlan`

#### Example Payload

```
{
  "resource_id": "23000",
  "resource_id_type": "CarePlan",
  "event_type": "care_plan.updated",
  "changed_fields": ["name"],
  "patient_id": "22222",
  "user_group_id": "15000"
}
```

#### Notes

* `patient_id`: ID of the patient this care plan belongs to (nullable)
* `user_group_id`: ID of the user group this care plan belongs to (nullable)

***

### `charting_note_addendum.created`

#### Overview

Fires when an addendum is added to a charting note.

#### When It Fires

When createAddendum mutation is called

#### GraphQL Mutations

* `createAddendum`

#### Example Payload

```
{
  "resource_id": "28000",
  "resource_id_type": "ChartingNoteAddendum",
  "event_type": "charting_note_addendum.created",
  "changed_fields": []
}
```

***

### `charting_note_addendum.deleted`

#### Overview

Fires when a charting note addendum is deleted.

#### When It Fires

When a charting note addendum is destroyed

#### Example Payload

```
{
  "resource_id": "28000",
  "resource_id_type": "ChartingNoteAddendum",
  "event_type": "charting_note_addendum.deleted",
  "changed_fields": []
}
```

***

### `charting_note_addendum.updated`

#### Overview

Fires when a charting note addendum is updated.

#### Example Payload

```
{
  "resource_id": "28000",
  "resource_id_type": "ChartingNoteAddendum",
  "event_type": "charting_note_addendum.updated",
  "changed_fields": ["content"]
}
```

***

### `diagnosis.create`

#### Overview

Fires when a diagnosis is added.

#### Example Payload

```
{
  "resource_id": "26000",
  "resource_id_type": "Diagnosis",
  "event_type": "diagnosis.created",
  "changed_fields": [],
  "icd_code_id": "67890",
  "user_id": "22222"
}
```

***

### `diagnosis.deleted`

#### Overview

Fires when a diagnosis is removed.

#### Example Payload

```
{
  "resource_id": "26000",
  "resource_id_type": "Diagnosis",
  "event_type": "diagnosis.deleted",
  "changed_fields": [],
  "icd_code_id": "67890",
  "user_id": "22222"
}
```

***

### `diagnosis.updated`

#### Overview

Fires when a diagnosis is updated.

#### Example Payload

```
{
  "resource_id": "26000",
  "resource_id_type": "Diagnosis",
  "event_type": "diagnosis.updated",
  "changed_fields": ["code"],
  "icd_code_id": "67890",
  "user_id": "22222"
}
```

***

### `dosespot_notification.created`

#### Overview

Fires when a DoseSpot notification is received.

#### GraphQL Mutations

No GraphQL mutations trigger this webhook. It’s triggered by external notifications from DoseSpot’s prescription system.

#### Example Payload

```
{
  "resource_id": "29000",
  "resource_id_type": "DosespotNotification",
  "event_type": "dosespot_notification.created",
  "changed_fields": []
}
```

***

### `entry.created`

#### Overview

Fires when a new journal entry is created.

#### GraphQL Mutations

* `createEntry`

#### Example Payload

```
{
  "resource_id": "22222",
  "resource_id_type": "Entry",
  "event_type": "entry.created",
  "changed_fields": []
}
```

***

### `entry.deleted`

#### Overview

Fires when a journal entry is deleted.

#### When It Fires

When `deleteEntry` mutation is called

#### GraphQL Mutations

* `deleteEntry`

#### Example Payload

```
{
  "resource_id": "22222",
  "resource_id_type": "Entry",
  "event_type": "entry.deleted",
  "changed_fields": []
}
```

***

### `entry.updated`

#### Overview

Fires when a journal entry is updated.

#### GraphQL Mutations

* `updateEntry`

#### Example Payload

```
{
  "resource_id": "22222",
  "resource_id_type": "Entry",
  "event_type": "entry.updated",
  "changed_fields": ["description"]
}
```

***

### `family_history_condition.created`

#### Overview

Fires when a family history condition is recorded.

#### GraphQL Mutations

* `createFamilyHistory`

#### Example Payload

```
{
  "resource_id": "27000",
  "resource_id_type": "FamilyHistoryCondition",
  "event_type": "family_history_condition.created",
  "changed_fields": [],
  "user_id": "22222"
}
```

#### Notes

* `user_id`: ID of the patient this family history condition belongs to

***

### `family_history_condition.deleted`

#### Overview

Fires when a family history condition is removed.

#### GraphQL Mutations

* `deleteFamilyHistory`

#### Example Payload

```
{
  "resource_id": "27000",
  "resource_id_type": "FamilyHistoryCondition",
  "event_type": "family_history_condition.deleted",
  "changed_fields": [],
  "user_id": "22222"
}
```

#### Notes

* `user_id`: ID of the patient this family history condition belonged to

***

### `family_history_condition.updated`

#### Overview

Fires when a family history condition is updated.

#### GraphQL Mutations

* `updateFamilyHistory`

#### Example Payload

```
{
  "resource_id": "27000",
  "resource_id_type": "FamilyHistoryCondition",
  "event_type": "family_history_condition.updated",
  "changed_fields": ["deceased"],
  "user_id": "22222"
}
```

#### Notes

* `user_id`: ID of the patient this family history condition belongs to

***

### `goal_history.created`

#### Overview

Fires when goal history is recorded.

#### When It Fires

* When `createGoalHistory` mutation is called

#### GraphQL Mutations

* `createGoalHistory`

#### Example Payload

```
{
  "resource_id": "44444",
  "resource_id_type": "GoalHistory",
  "event_type": "goal_history.created",
  "changed_fields": [],
  "goal_id": "33333",
  "user_id": "22222"
}
```

#### Notes

* `goal_id`: ID of the goal this history entry belongs to
* `user_id`: ID of the user who recorded the goal history

***

### `goal_history.deleted`

#### Overview

Fires when goal history is deleted.

#### GraphQL Mutations

* `deleteGoalHistory`

#### Example Payload

```
{
  "resource_id": "44444",
  "resource_id_type": "GoalHistory",
  "event_type": "goal_history.deleted",
  "changed_fields": [],
  "goal_id": "33333",
  "user_id": "22222"
}
```

#### Notes

* `goal_id`: ID of the goal this history entry belonged to
* `user_id`: ID of the user who recorded the goal history

***

### `goal_template.created`

#### Overview

Fires when a goal template is created.

#### GraphQL Mutations

No GraphQL mutations trigger goal template creation directly. Goal templates are created internally when goals are favorited via `createGoal`.

#### Example Payload

```
{
  "resource_id": "24000",
  "resource_id_type": "GoalTemplate",
  "event_type": "goal_template.created",
  "changed_fields": [],
  "goal_id": "33333",
  "parent_id": "11111",
  "user_id": "22222"
}
```

#### Notes

* `goal_id`: ID of the goal this template was created from (nullable)
* `parent_id`: ID of the parent goal template for sub-templates (nullable)
* `user_id`: ID of the user this template belongs to (nullable)

***

### `goal_template.deleted`

#### Overview

Fires when a goal template is deleted.

#### GraphQL Mutations

No GraphQL mutations directly trigger this webhook. Goal templates are managed internally through the UI.

#### Example Payload

```
{
  "resource_id": "24000",
  "resource_id_type": "GoalTemplate",
  "event_type": "goal_template.deleted",
  "changed_fields": [],
  "goal_id": "33333",
  "parent_id": "11111",
  "user_id": "22222"
}
```

#### Notes

* `goal_id`: ID of the goal this template was created from (nullable)
* `parent_id`: ID of the parent goal template for sub-templates (nullable)
* `user_id`: ID of the user this template belonged to (nullable)

***

### `goal_template.updated`

#### Overview

Fires when a goal template is updated.

#### GraphQL Mutations

No GraphQL mutations directly trigger this webhook. Goal templates are managed internally through the UI.

#### Example Payload

```
{
  "resource_id": "24000",
  "resource_id_type": "GoalTemplate",
  "event_type": "goal_template.updated",
  "changed_fields": ["name"],
  "goal_id": "33333",
  "parent_id": "11111",
  "user_id": "22222"
}
```

#### Notes

* `goal_id`: ID of the goal this template was created from (nullable)
* `parent_id`: ID of the parent goal template for sub-templates (nullable)
* `user_id`: ID of the user this template belongs to (nullable)

***

### `goal.created`

#### Overview

Fires when a new goal is created for a patient.

#### GraphQL Mutations

* `createGoal`

#### Example Payload

```
{
  "resource_id": "33333",
  "resource_id_type": "Goal",
  "event_type": "goal.created",
  "changed_fields": [],
  "care_plan_id": "67890",
  "parent_id": "11111",
  "user_id": "22222"
}
```

#### Notes

* `care_plan_id`: ID of the care plan this goal belongs to
* `parent_id`: ID of the parent goal (for subgoals)
* `user_id`: ID of the patient this goal is assigned to

***

### `goal.deleted`

#### Overview

Fires when a goal is deleted.

#### When It Fires

When deleteGoal mutation is called

#### GraphQL Mutations

* `deleteGoal`

#### Example Payload

```
{
  "resource_id": "33333",
  "resource_id_type": "Goal",
  "event_type": "goal.deleted",
  "changed_fields": [],
  "care_plan_id": "67890",
  "parent_id": "11111",
  "user_id": "22222"
}
```

#### Notes

* `care_plan_id`: ID of the care plan this goal belonged to (nullable)
* `parent_id`: ID of the parent goal for subgoals (nullable)
* `user_id`: ID of the patient this goal was assigned to

***

### `goal.updated`

#### Overview

Fires when a goal is updated.

#### GraphQL Mutations

* `updateGoal`

#### Example Payload

```
{
  "resource_id": "33333",
  "resource_id_type": "Goal",
  "event_type": "goal.updated",
  "changed_fields": ["name", "repeat"]
}
```

#### Notes

Since Goal includes webhook association data, the actual payload will also contain:

```
{
  "resource_id": "33333",
  "resource_id_type": "Goal",
  "event_type": "goal.updated",
  "changed_fields": ["name", "repeat"],
  "care_plan_id": "67890",
  "parent_id": "11111",
  "user_id": "22222"
}
```

These additional fields are included in the webhook payload.

***

### `lab_order.created`

#### Overview

Fires when a lab order is created.

#### When It Fires

When createLabOrder mutation is called

#### GraphQL Mutations

* `createLabOrder`

#### Example Payload

```
{
  "resource_id": "19000",
  "resource_id_type": "LabOrder",
  "event_type": "lab_order.created",
  "changed_fields": []
}
```

***

### `lab_order.updated`

#### Overview

Fires when a lab order is updated.

#### When It Fires

When updateLabOrder mutation is called

#### GraphQL Mutations

* `updateLabOrder`

#### Example Payload

```
{
  "resource_id": "19000",
  "resource_id_type": "LabOrder",
  "event_type": "lab_order.updated",
  "changed_fields": ["status"]
}
```

***

### `lab_result.created`

#### Overview

Fires when a lab result is received.

#### When It Fires

When createLabResult mutation is called

#### GraphQL Mutations

* `createLabResult`

#### Example Payload

```
{
  "resource_id": "20000",
  "resource_id_type": "LabResult",
  "event_type": "lab_result.created",
  "changed_fields": [],
  "lab_order_id": "16000",
  "document_id": "17000",
  "patient_id": "22222",
  "ordering_physician_id": "19000"
}
```

#### Notes

* `lab_order_id`: ID of the lab order this result belongs to
* `document_id`: ID of the document associated with this lab result
* `patient_id`: ID of the patient this lab result belongs to (nullable)
* `ordering_physician_id`: ID of the ordering physician

***

### `lab_result.updated`

#### Overview

Fires when a lab result is updated.

#### GraphQL Mutations

* `updateLabResult`

#### Example Payload

```
{
  "resource_id": "20000",
  "resource_id_type": "LabResult",
  "event_type": "lab_result.updated",
  "changed_fields": ["file_string"],
  "lab_order_id": "16000",
  "document_id": "17000",
  "patient_id": "22222",
  "ordering_physician_id": "19000"
}
```

#### Notes

* `lab_order_id`: ID of the lab order this result belongs to
* `document_id`: ID of the document associated with this lab result
* `patient_id`: ID of the patient this lab result belongs to (nullable)
* `ordering_physician_id`: ID of the ordering physician

***

### `medication.created`

#### Overview

Fires when a medication is added to a patient’s profile.

#### GraphQL Mutations

This webhook is triggered by the following GraphQL mutations:

* `createMedication`

#### Example Payload

```
{
  "resource_id": "21000",
  "resource_id_type": "Medication",
  "event_type": "medication.created",
  "changed_fields": []
}
```

#### Notes

Since Medication includes webhook association data, the actual payload will also contain:

```
{
  "resource_id": "21000",
  "resource_id_type": "Medication",
  "event_type": "medication.created",
  "changed_fields": [],
  "user_id": "22222"
}
```

The `user_id` field is included in the webhook payload.

***

### `medication.deleted`

#### Overview

Fires when a medication is removed.

#### GraphQL Mutations

* `deleteMedication`

#### Example Payload

```
{
  "resource_id": "21000",
  "resource_id_type": "Medication",
  "event_type": "medication.deleted",
  "changed_fields": [],
  "user_id": "22222"
}
```

#### Notes

The `user_id` field is included in the webhook payload.

***

### `medication.updated`

#### Overview

Fires when a medication is modified.

#### GraphQL Mutations

This webhook is triggered by the following GraphQL mutations:

* `updateMedication`

#### Example Payload

```
{
  "resource_id": "21000",
  "resource_id_type": "Medication",
  "event_type": "medication.updated",
  "changed_fields": ["active"]
}
```

#### Notes

Since Medication includes webhook association data, the actual payload will also contain:

```
{
  "resource_id": "21000",
  "resource_id_type": "Medication",
  "event_type": "medication.updated",
  "changed_fields": [],
  "user_id": "22222"
}
```

The `user_id` field is included in the webhook payload.

***

### `metric_entry.created`

#### Overview

Fires when a new metric entry is created.

#### GraphQL Mutations

* `createEntry`

#### Example Payload

```
{
  "resource_id": "11111",
  "resource_id_type": "Entry",
  "event_type": "metric_entry.created",
  "changed_fields": []
}
```

***

### `metric_entry.deleted`

#### Overview

Fires when a metric entry is deleted.

#### When It Fires

When deleteEntry mutation is called

#### GraphQL Mutations

* `deleteEntry`

#### Example Payload

```
{
  "resource_id": "11111",
  "resource_id_type": "Entry",
  "event_type": "metric_entry.deleted",
  "changed_fields": []
}
```

***

### `metric_entry.updated`

#### Overview

Fires when a metric entry is updated.

#### When It Fires

When updateEntry mutation is called

#### GraphQL Mutations

* `updateEntry`

#### Example Payload

```
{
  "resource_id": "11111",
  "resource_id_type": "Entry",
  "event_type": "metric_entry.updated",
  "changed_fields": ["value", "category"]
}
```

***

### `prescription.medication_status_updated`

#### Overview

Fires when a prescription medication is updated.

#### When It Fires

When a prescription medication is updated

#### GraphQL Mutations

No GraphQL mutations trigger prescription medications updates directly. Prescriptions are updated through internal mechanisms or third-party integrations.

#### Example Payload

```
{
  "resource_id": "22000",
  "resource_id_type": "Prescription",
  "event_type": "prescription.medication_status_updated",
  "changed_fields": ["status"],
  "patient_erx_id": "12345",
  "patient_id": "1234",
  "clinician_id": "6789",
  "medication_status": "3",
  "status_notes": "medication discontinued",
  "status_date_time": "2026-05-21T09:30:00.123Z",
  "clinic_id": "56789",
}
```

***

### `prescription.updated`

#### Overview

Fires when a prescription is updated.

#### When It Fires

When a prescription is updated

#### GraphQL Mutations

No GraphQL mutations trigger prescription updates directly. Prescriptions are updated through internal mechanisms or third-party integrations.

#### Example Payload

```
{
  "resource_id": "22000",
  "resource_id_type": "Prescription",
  "event_type": "prescription.updated",
  "changed_fields": ["status"],
  "clinician_id": "6789",
  "prescription_status": "13",
  "status_details": "Prescription delivery verified",
  "clinic_id": "56789",
}
```

***

### `referral.created`

#### Overview

Fires when a referral is created.

#### GraphQL Mutations

This webhook is triggered by the following GraphQL mutations:

* `createReferral`

#### Example Payload

```
{
  "resource_id": "32000",
  "resource_id_type": "Referral",
  "event_type": "referral.created",
  "changed_fields": []
}
```

***

### `referral.deleted`

#### Overview

Fires when a referral is deleted.

#### When It Fires

When deleteReferral mutation is called

#### GraphQL Mutations

* `deleteReferral`

#### Example Payload

```
{
  "resource_id": "32000",
  "resource_id_type": "Referral",
  "event_type": "referral.deleted",
  "changed_fields": []
}
```

***

### `referral.updated`

#### Overview

Fires when a referral is updated.

#### GraphQL Mutations

This webhook is triggered by the following GraphQL mutations:

* `updateReferral`

#### Example Payload

```
{
  "resource_id": "32000",
  "resource_id_type": "Referral",
  "event_type": "referral.updated",
  "changed_fields": ["status"]
}
```

***

### `referring_physician.created`

#### Overview

Fires when a referring physician is added.

#### When It Fires

When a referring physician is added

#### GraphQL Mutations

* `createReferringPhysician`

#### Example Payload

```
{
  "resource_id": "33000",
  "resource_id_type": "ReferringPhysician",
  "event_type": "referring_physician.created",
  "changed_fields": []
}
```

***

### `referring_physician.deleted`

#### Overview

Fires when a referring physician is removed.

#### When It Fires

When a referring physician is removed

#### Example Payload

```
{
  "resource_id": "33000",
  "resource_id_type": "ReferringPhysician",
  "event_type": "referring_physician.deleted",
  "changed_fields": []
}
```

***

### `referring_physician.updated`

#### Overview

Fires when a referring physician is updated.

#### When It Fires

When a referring physician is updated

#### GraphQL Mutations

* `updateReferringPhysician`

#### Example Payload

```
{
  "resource_id": "33000",
  "resource_id_type": "ReferringPhysician",
  "event_type": "referring_physician.updated",
  "changed_fields": ["business_name"]
}
```

***

## Document

### `document.created`

#### Overview

Fires when a new document is uploaded.

#### GraphQL Mutations

* `createDocument`

#### Example Payload

```
{
  "resource_id": "99999",
  "resource_id_type": "Document",
  "event_type": "document.created",
  "changed_fields": []
}
```

***

### `document.deleted`

#### Overview

Fires when a document is deleted.

#### GraphQL Mutations

* `deleteDocument`

#### Example Payload

```
{
  "resource_id": "99999",
  "resource_id_type": "Document",
  "event_type": "document.deleted",
  "changed_fields": []
}
```

***

### `document.updated`

#### Overview

Fires when a document is updated.

#### When It Fires

When `updateDocument` mutation is called

#### GraphQL Mutations

* `updateDocument`

#### Example Payload

```
{
  "resource_id": "99999",
  "resource_id_type": "Document",
  "event_type": "document.updated",
  "changed_fields": ["display_name"]
}
```

***

### `folder_sharing.created`

#### Overview

Fires when a folder is shared.

#### GraphQL Mutations

* `createSharings`

#### Example Payload

```
{
  "resource_id": "50000",
  "resource_id_type": "FolderSharing",
  "event_type": "folder_sharing.created",
  "changed_fields": [],
  "folder_id": "30000",
  "user_id": "22222"
}
```

#### Notes

* `folder_id`: ID of the folder being shared
* `user_id`: ID of the user the folder is shared with

***

### `folder_sharing.deleted`

#### Overview

Fires when folder sharing is removed.

#### GraphQL Mutations

* `destroySharings`

#### Example Payload

```
{
  "resource_id": "50000",
  "resource_id_type": "FolderSharing",
  "event_type": "folder_sharing.deleted",
  "changed_fields": [],
  "folder_id": "30000",
  "user_id": "22222"
}
```

#### Notes

* `folder_id`: ID of the folder that was shared
* `user_id`: ID of the user the folder was shared with

***

### `received_fax.created`

#### Overview

Fires when a fax is received.

#### GraphQL Mutations

External webhook ingestion

#### Example Payload

```
{
  "resource_id": "30000",
  "resource_id_type": "ReceivedFax",
  "event_type": "received_fax.created",
  "changed_fields": []
}
```

***

### `sent_fax.created`

#### Overview

Fires when a fax is sent.

#### When It Fires

When a fax is sent

#### GraphQL Mutations

* `createSentFax`

#### Example Payload

```
{
  "resource_id": "31000",
  "resource_id_type": "SentFax",
  "event_type": "sent_fax.created",
  "changed_fields": []
}
```

***

### `sent_fax.status_changed`

#### Overview

Fires when a sent fax status changes.

#### When It Fires

When a fax transmission status changes

#### Example Payload

```
{
  "resource_id": "31000",
  "resource_id_type": "SentFax",
  "event_type": "sent_fax.status_changed",
  "changed_fields": []
}
```

***

### `sent_fax.updated`

#### Overview

Fires when a sent fax status is updated.

#### Example Payload

```
{
  "resource_id": "31000",
  "resource_id_type": "SentFax",
  "event_type": "sent_fax.updated",
  "changed_fields": ["status"]
}
```

***

## Task

### `task.created`

#### Overview

Fires when a new task is created.

#### GraphQL Mutations

This webhook is triggered by the following GraphQL mutations:

* `createTask`

#### Example Payload

```
{
  "resource_id": "11000",
  "resource_id_type": "Task",
  "event_type": "task.created",
  "changed_fields": []
}
```

#### Notes

Task does not have webhook association data configured, so no additional fields are included beyond the standard payload shown above.

***

### `task.deleted`

#### Overview

Fires when a task is deleted.

#### GraphQL Mutations

* `deleteTask`

#### Example Payload

```
{
  "resource_id": "11000",
  "resource_id_type": "Task",
  "event_type": "task.deleted",
  "changed_fields": []
}
```

***

### `task.updated`

#### Overview

Fires when a task is updated.

#### GraphQL Mutations

* `updateTask`

#### Example Payload

```
{
  "resource_id": "11000",
  "resource_id_type": "Task",
  "event_type": "task.updated",
  "changed_fields": ["complete", "completed_by_id"]
}
```

***

## Organization

### `availability.created`

#### Overview

Fires when availability is created.

#### GraphQL Mutations

This webhook is triggered by the following GraphQL mutations:

* `createAvailability`
* `bulkCreateAvailability`

#### Example Payload

```
{
  "resource_id": "40000",
  "resource_id_type": "Availability",
  "event_type": "availability.created",
  "changed_fields": []
}
```

***

### `location.created`

#### Overview

Fires when a location is created.

#### GraphQL Mutations

This webhook is triggered by the following GraphQL mutations:

* `createLocation`

#### Example Payload

```
{
  "resource_id": "34000",
  "resource_id_type": "Location",
  "event_type": "location.created",
  "changed_fields": [],
  "user_id": "12345"
}
```

***

### `location.deleted`

#### Overview

Fires when a location is deleted.

#### GraphQL Mutations

This webhook is triggered by the following GraphQL mutations:

* `deleteLocation`

#### Example Payload

```
{
  "resource_id": "34000",
  "resource_id_type": "Location",
  "event_type": "location.deleted",
  "changed_fields": [],
  "user_id": "12345"
}
```

***

### `location.updated`

#### Overview

Fires when a location is updated.

#### GraphQL Mutations

This webhook is triggered by the following GraphQL mutations:

* `updateLocation`

#### Example Payload

```
{
  "resource_id": "34000",
  "resource_id_type": "Location",
  "event_type": "location.updated",
  "changed_fields": ["name", "line1"],
  "user_id": "12345"
}
```

***

### `organization_info.created`

#### Overview

Fires when organization info is created.

#### GraphQL Mutations

* `createOrganization`

#### Example Payload

```
{
  "resource_id": "37000",
  "resource_id_type": "OrganizationInfo",
  "event_type": "organization_info.created",
  "changed_fields": []
}
```

***

### `organization_info.deleted`

#### Overview

Fires when organization info is deleted.

#### GraphQL Mutations

* `deleteOrganizationInfo`

#### Example Payload

```
{
  "resource_id": "37000",
  "resource_id_type": "OrganizationInfo",
  "event_type": "organization_info.deleted",
  "changed_fields": []
}
```

***

### `organization_info.updated`

#### Overview

Fires when organization info is updated.

#### GraphQL Mutations

* `updateOrganization`

#### Example Payload

```
{
  "resource_id": "37000",
  "resource_id_type": "OrganizationInfo",
  "event_type": "organization_info.updated",
  "changed_fields": ["name"]
}
```

***

### `organization_member.updated`

#### Overview

Fires when an organization member is updated.

#### GraphQL Mutations

update, updateOrganizationMember

#### Example Payload

```
{
  "resource_id": "36000",
  "resource_id_type": "OrganizationMember",
  "event_type": "organization_member.updated",
  "changed_fields": []
}
```

***

### `organization_membership.created`

#### Overview

Fires when an organization membership is created.

#### When It Fires

* When `createOrganizationMembership` mutation is called

#### GraphQL Mutations

* `createOrganizationMembership`

#### Example Payload

```
{
  "resource_id": "35000",
  "resource_id_type": "OrganizationMembership",
  "event_type": "organization_membership.created",
  "changed_fields": []
}
```

***

### `organization_membership.updated`

#### Overview

Fires when an organization membership is updated.

#### When It Fires

* When `updateOrganizationMembership` mutation is called

#### GraphQL Mutations

* `updateOrganizationMembership`

#### Example Payload

```
{
  "resource_id": "35000",
  "resource_id_type": "OrganizationMembership",
  "event_type": "organization_membership.updated",
  "changed_fields": ["user_group_id"]
}
```

***

## Other

### \`

patient\_education\_resource.created\`

Fires when `patient_education_resource.created` occurs.

***

### `comment.created`

#### Overview

Fires when a new comment is posted.

#### GraphQL Mutations

* `createComment`

#### Example Payload

```
{
  "resource_id": "12000",
  "resource_id_type": "Comment",
  "event_type": "comment.created",
  "changed_fields": []
}
```

***

### `comment.deleted`

#### Overview

Fires when a comment is deleted.

#### GraphQL Mutations

* `deleteComment`

#### Example Payload

```
{
  "resource_id": "12000",
  "resource_id_type": "Comment",
  "event_type": "comment.deleted",
  "changed_fields": []
}
```

***

### `comment.updated`

#### Overview

Fires when a comment is edited.

#### When It Fires

When updateComment mutation is called

#### GraphQL Mutations

* `updateComment`

#### Example Payload

```
{
  "resource_id": "12000",
  "resource_id_type": "Comment",
  "event_type": "comment.updated",
  "changed_fields": ["content"]
}
```

***

### `external_calendar.authorization_error`

#### Overview

Fires when external calendar authorization encounters an error.

#### Example Payload

```
{
  "resource_id": "43000",
  "resource_id_type": "ExternalCalendar",
  "event_type": "external_calendar.authorization_error",
  "changed_fields": []
}
```

***

### `patient_educational_resource.deleted`

Fires when `patient_educational_resource.deleted` occurs.

***

### `patient_educational_resource.updated`

Fires when `patient_educational_resource.updated` occurs.

***

### `sent_notification_record.created`

#### Overview

Fires when a notification is sent.

#### When It Fires

When a notification is sent

#### Example Payload

```
{
  "resource_id": "51000",
  "resource_id_type": "SentNotificationRecord",
  "event_type": "sent_notification_record.created",
  "changed_fields": []
}
```

***

### `sent_notification_record.updated`

#### Overview

Fires when a sent notification record is updated.

#### When It Fires

When a sent notification record is updated

#### Example Payload

```
{
  "resource_id": "51000",
  "resource_id_type": "SentNotificationRecord",
  "event_type": "sent_notification_record.updated",
  "changed_fields": ["status"]
}
```

***

### `test.created`

#### Overview

Test webhook event used for verifying webhook configuration.

#### GraphQL Mutations

No GraphQL mutations trigger test webhooks. Test events are manually triggered for configuration verification only.

* Used for webhook setup verification
* Does not correspond to an actual resource

#### Example Payload

```
{
  "resource_id": "12345",
  "resource_id_type": "Test",
  "event_type": "test.created",
  "changed_fields": []
}
```

***
