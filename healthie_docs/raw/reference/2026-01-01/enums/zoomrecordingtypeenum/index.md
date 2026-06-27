---
title: ZoomRecordingTypeEnum | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/zoomrecordingtypeenum/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/zoomrecordingtypeenum/index.md
---

Types of Zoom recordings

## Used By

[`ZoomCloudRecordingFile.recording_type`](/reference/2026-01-01/objects/zoomcloudrecordingfile)

## Definition

```
"""
Types of Zoom recordings
"""
enum ZoomRecordingTypeEnum {
  """
  Recording with shared screen and speaker view
  """
  shared_screen_with_speaker_view


  """
  Recording with shared screen and gallery view
  """
  shared_screen_with_gallery_view


  """
  Recording with only speaker view
  """
  speaker_view


  """
  Recording with only gallery view
  """
  gallery_view


  """
  Recording with only shared screen
  """
  shared_screen


  """
  Audio-only recording
  """
  audio_only


  """
  Recording focused on the active speaker
  """
  active_speaker


  """
  a transcript-only recording
  """
  audio_transcript


  """
  a timeline with timestamps of the recording
  """
  timeline


  """
  Recording with shared screen and speaker view (CC)
  """
  shared_screen_with_speaker_view_cc
}
```
