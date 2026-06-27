---
title: ZoomRecordingFileTypeEnum | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/zoomrecordingfiletypeenum/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/zoomrecordingfiletypeenum/index.md
---

Types of Zoom recording files

## Used By

[`ZoomCloudRecordingFile.file_type`](/reference/2026-01-01/objects/zoomcloudrecordingfile)

## Definition

```
"""
Types of Zoom recording files
"""
enum ZoomRecordingFileTypeEnum {
  """
  Video recording file
  """
  MP4


  """
  Audio-only recording file
  """
  M4A


  """
  Audio transcript file
  """
  TRANSCRIPT


  """
  Recording chat text file
  """
  CHAT


  """
  Closed caption file
  """
  CC


  """
  Timeline file for the recording
  """
  TIMELINE


  """
  Thumbnail image of the recording
  """
  THUMBNAIL
}
```
