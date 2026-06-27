---
title: notificationSetting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/notificationsetting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/notificationsetting/index.md
---

fetch a Notification Setting by id

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`NotificationSetting`](/reference/2026-01-01/objects/notificationsetting)

## Example

```
query notificationSetting($id: ID) {
  notificationSetting(id: $id) {
    id
    marketing_communication_preference
    notification_on_module_completion
    receive_updates_and_offers
    send_comment_emails
    send_comment_push
    send_course_complete_email
    send_email_before_appointment
    send_email_on_appointment_book
    send_email_on_appointment_cancel
    send_email_on_appointment_reschedule
    send_email_on_appt_request_for_anyone
    send_email_on_appt_request_for_you
    send_email_on_client_has_been_assigned_to_you
    send_email_on_fax_delivery_failure
    send_email_on_fax_received
    send_email_on_intake_flow_complete
    send_email_on_intake_flow_item_complete
    send_email_on_intake_flow_start
    send_email_on_new_document
    send_email_on_new_folder
    send_email_on_package_purchase
    send_email_on_scheduled_payment_failed
    send_email_receipt_for_subscription_payment
    send_emoji_email
    send_emoji_push
    send_entry_emails
    send_goal_reminder_email
    send_goal_reminder_push
    send_group_message_emails
    send_group_message_push
    send_insurance_expiry_notifications
    send_message_emails
    send_message_push
    send_new_clients_emails
    send_new_insurance_added_notifications
    send_new_module_email
    send_new_module_push
    send_push_before_appointment
    send_recurring_payment_reminder_emails
    updated_at
    user
  }
}
```
