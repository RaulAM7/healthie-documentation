---
title: Video Chat | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/video_chat/index
  md: https://docs.gethealthie.com/guides/video_chat/index.md
---

# Video Chat

Appointments created in Healthie can optionally include video chat. If you’re building your own patient-facing app, you can embed Healthie video calls into your custom frontend.

Healthie video calls use either Zoom or OpenTok. The video calls that take place in the Healthie portal UI use the OpenTok API under the hood. When creating an appointment in Healthie that includes video chat, providers can choose either Zoom or Healthie video call.

Below is information about embedding a video chat experience into your own frontend app. Visit [our help center](https://help.gethealthie.com/article/325-video-calls-overview) for more general info about using video calls in Healthie.

## Using Zoom

To embed video calls that use Zoom, you’ll need to use a Zoom SDK. Zoom offers a [web SDK](https://devsupport.zoom.us/hc/en-us/articles/360060333111-How-to-embed-Zoom-into-a-website), as well as a [React Native SDK](https://marketplacefront.zoom.us/sdk/custom/reactnative/index.html) for mobile apps written in React Native.

The Appointment object from the Healthie API includes the participant `zoom_join_url` as well as other relevant Zoom call info.

## Using OpenTok

To embed a Healthie video call into your frontend application, you can use the [opentok-react](https://developer.vonage.com/en/blog/opentok-react-components-dr) package. You’ll need the `generated_token` and `session_id` that you can retrieve from an Appointment object via the Healthie API. You’ll also need Healthie’s public Vonage API key, which is `45624682`.

## Group calls

Please note that *group* video calls can only be conducted using the Zoom integration, not with Healthie video calls / OpenTok.
