---
title: ZoomRecordingStatusEnum | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/zoomrecordingstatusenum/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/zoomrecordingstatusenum/index.md
---

Status of Zoom recording files

## Used By

[`ZoomCloudRecordingFile.status`](/reference/2026-01-01/objects/zoomcloudrecordingfile)

## Definition

```
"""
Status of Zoom recording files
"""
enum ZoomRecordingStatusEnum {
  """
  The recording is still being processed
  """
  processing


  """
  The recording is ready to be viewed
  """
  completed


  """
  The recording failed to process
  """
  failed
}
```
