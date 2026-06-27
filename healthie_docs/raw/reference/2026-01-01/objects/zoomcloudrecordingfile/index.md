---
title: ZoomCloudRecordingFile | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/zoomcloudrecordingfile/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/zoomcloudrecordingfile/index.md
---

A Zoom cloud recording file with metadata and download URL

## Fields

[`download_url` ](#field-download-url)· [`String` ](/reference/2026-01-01/scalars/string)· The URL to download the recording file

[`file_size` ](#field-file-size)· [`Int` ](/reference/2026-01-01/scalars/int)· The size of the recording file in bytes

[`file_type` ](#field-file-type)· [`ZoomRecordingFileTypeEnum` ](/reference/2026-01-01/enums/zoomrecordingfiletypeenum)· The file type of the recording

[`id` ](#field-id)· [`String` ](/reference/2026-01-01/scalars/string)· The unique identifier of the recording file

[`meeting_id` ](#field-meeting-id)· [`String` ](/reference/2026-01-01/scalars/string)· The Meeting ID for the Zoom call that was recorded

[`recording_end` ](#field-recording-end)· [`String` ](/reference/2026-01-01/scalars/string)· The end time of the recording

[`recording_start` ](#field-recording-start)· [`String` ](/reference/2026-01-01/scalars/string)· The start time of the recording

[`recording_type` ](#field-recording-type)· [`ZoomRecordingTypeEnum` ](/reference/2026-01-01/enums/zoomrecordingtypeenum)· The type of recording

[`status` ](#field-status)· [`ZoomRecordingStatusEnum` ](/reference/2026-01-01/enums/zoomrecordingstatusenum)· The status of the recording file

## Used By

[`Appointment.zoom_cloud_recording_files`](/reference/2026-01-01/objects/appointment)

[`deleteZoomRecordingFilePayload.zoom_recording_file`](/reference/2026-01-01/objects/deletezoomrecordingfilepayload)

## Definition

```
"""
A Zoom cloud recording file with metadata and download URL
"""
type ZoomCloudRecordingFile {
  """
  The URL to download the recording file
  """
  download_url: String


  """
  The size of the recording file in bytes
  """
  file_size: Int


  """
  The file type of the recording
  """
  file_type: ZoomRecordingFileTypeEnum


  """
  The unique identifier of the recording file
  """
  id: String


  """
  The Meeting ID for the Zoom call that was recorded
  """
  meeting_id: String


  """
  The end time of the recording
  """
  recording_end: String


  """
  The start time of the recording
  """
  recording_start: String


  """
  The type of recording
  """
  recording_type: ZoomRecordingTypeEnum


  """
  The status of the recording file
  """
  status: ZoomRecordingStatusEnum
}
```
