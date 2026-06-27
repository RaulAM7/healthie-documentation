---
title: Webhooks | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/webhooks/index
  md: https://docs.gethealthie.com/guides/webhooks/index.md
---

Healthie’s API offers webhooks for common events.

When the event happens, Healthie will send a HTTP POST request with the following body to a URL you provide us.

You can see an example HTTP POST body below:

Example webhook payload

```
{
    "resource_id": "resource_id", # The ID of the resource that was affected
    "resource_id_type": "resource_id_type", # The type of resource (can be 'Appointment', 'FormAnswerGroup', 'Entry', or 'Note')
    "event_type": "event_type" # The event that occurred
}
```

We support different URLs for each event, as well as multiple URLs for the same event.

### Retry Logic

You can choose to opt into having us retry a failed webhook if your service returns an error when we send a webhook to you. We will retry sending the webhook for up 3 days based on an exponential backoff. After retrying for up to 3 days, we will disable the webhook.

### Email on Failure

If your service continues to return an error, we will send an email notification to let you know after approximately 24 hours.

### Email on disable

If your service continues to return an error, we will disable the webhook after approximately 3 days.

### Better URL validation

We have better validations around the URL of the service that you specify. You will be notified sooner if your URL does not validate.

### Signed payloads

#### Overview

When you receive webhooks from our service, it is important to verify that they were indeed sent by us. This can be achieved by validating the signature in the webhook’s headers. Below, we provide the steps and a code sample for verifying the signature using JavaScript.

#### Signature Verification Process

Each webhook request includes several headers that are used to ensure the authenticity and integrity of the request:

* `Content-Type`: Specifies the media type of the resource (should be `application/json`).
* `Content-Digest`: Contains a SHA-256 hash of the request payload.
* `Signature-Input`: Specifies the components used to construct the signature.
* `Signature`: Contains the actual cryptographic signature of the message that you need to verify.

The signature is computed using HMAC (Hash-Based Message Authentication Code) with SHA-256 hashing. The data string used to generate the signature is constructed using specific parts of the request, including the HTTP method, path, query, and body content.

#### Steps to Verify the Signature

1. **Construct the Data String**: Replicate the construction of the data string that was signed on the server side. This involves concatenating the HTTP method, path, query string, content digest, content type, and content length of the request.

2. **Compute the HMAC**: Using the same key that the server used, compute the HMAC with SHA-256 of the data string.

3. **Compare the Computed HMAC with the Signature in the Request**: The signature provided in the webhook’s `Signature` header should match the HMAC you computed. If they match, the request is verified.

#### JavaScript Code Sample

verify-signature.js

```
async function getSigningKey(secretKey) {
  const encoder = new TextEncoder();
  const keyData = encoder.encode(secretKey);
  return await crypto.subtle.importKey('raw', keyData, { name: 'HMAC', hash: { name: 'SHA-256' } }, false, ['sign']);
}


function constructDataToSign({ method, path, query, headers, body }) {
  const contentDigest = headers['content-digest'].split('=')[1];
  const contentType = 'application/json';
  const contentLength = JSON.stringify(body).length;
  return `${method.toLowerCase()} ${path} ${query} ${contentDigest} ${contentType} ${contentLength}`;
}


async function generateSignature(key, data) {
  const encoder = new TextEncoder();
  const signature = await crypto.subtle.sign('HMAC', key, encoder.encode(data));
  return Array.from(new Uint8Array(signature))
    .map(byte => byte.toString(16).padStart(2, '0'))
    .join('');
}


async function verifySignature(requestData, secretKey) {
  const key = await getSigningKey(secretKey);
  const dataToSign = constructDataToSign(requestData);
  const computedSignature = await generateSignature(key, dataToSign);
  const actualSignature = requestData.headers['signature'].split('=')[1];


  return computedSignature === actualSignature;
}


// Example usage
const requestData = {
  method: 'post',
  path: '/uri/path/here',
  query: '', // any query params. leave blank if none
  body: {
    resource_id: 123123123,
    resource_id_type: 'Appointment',
    event_type: 'appointment.updated',
    changed_fields: ['pm_status_last_changed_by_id', 'last_updated_by_id'],
  },
  headers: {
    'content-type': 'application/json',
    'content-digest': 'SHA-256=content-digest-from-header',
    signature: 'sig1=signature-from-header',
  },
};


const secretKey = 'whsec_my-secret-key'; // The secret shared with you
verifySignature(requestData, secretKey)
  .then(isValid => console.log('Is the signature valid?', isValid))
  .catch(err => console.error('Error verifying signature:', err));
```

### Thin payloads

When webhooks are sent for updates, we will include a `changed_fields` property to the payload we send. This property will contain a list of fields that changed during the update.

Please note: For webhooks related to a `created` event or `deleted` event, we do not send data about the event other than the resource ID and event category. We expect you to make a GraphQL API call after receiving the event, using the resource ID, to get the data you need.

### Security

In addition to signing our webhooks, you can whitelist Healthie’s current IP addresses as an additional security measure:

| Environment                   | IP Addresses                                                    |
| ----------------------------- | --------------------------------------------------------------- |
| Staging / sandbox environment | `18.206.70.225`,`44.195.8.253`, `44.198.216.125`                |
| Production environment        | `52.4.158.130`,`3.216.152.234`, `54.243.233.84`, `50.19.211.21` |

Caution

**Please note that Healthie’s IP addresses are subject to change**. However, a change would be unusual and Healthie would notify your team ahead of time about the change.

### Available Webhook Event Types

For the full list of webhook events — including payload examples and the GraphQL mutations that trigger each event — see the [Webhook Event Reference](/guides/webhooks/event-reference/).

Don’t see a webhook for an event you want to listen to? Please reach out to us.

### Examples

Say you would like to add a special external video link when patients under a particular provider book an appointment. You could:

* listen to the `appointment.created` webhook event
* fetch the appointment when the event is received
* if the appointment’s provider is a match, use the `updateAppointment` mutation to update the appointment’s `external_videochat_url`

You can find more examples how to leverage Healthie API Webhooks in the [Automation Examples section](/guides/automation-examples/client-completed-an-intake-form/).

### Webhook behavior in the context of sub-organizations

If your company is using sub-organizations in Healthie, you may want certain webhook events to fire only when they are triggered by an action in a given sub-org. Here is how webhook events behave in the context of parent organizations and sub-organizations:

* If the parent org has a webhook set up, all relevant events from *all* sub-orgs will be sent to that endpoint
* If a sub-org has a webhook set up, only relevant events from that sub-org will be sent to that endpoint
