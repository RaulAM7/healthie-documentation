---
title: deleteZoomRecordingFile | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletezoomrecordingfile/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletezoomrecordingfile/index.md
---

Delete a Zoom Recording File either via ID OR appointment and file ID

## Arguments

[`input` ](#argument-input)· [`deleteZoomRecordingFileInput` ](/reference/2026-01-01/input-objects/deletezoomrecordingfileinput)· Parameters for deleteZoomRecordingFile

## Returns

[`deleteZoomRecordingFilePayload`](/reference/2026-01-01/objects/deletezoomrecordingfilepayload)

## Example

```
mutation deleteZoomRecordingFile($input: deleteZoomRecordingFileInput) {
  deleteZoomRecordingFile(input: $input) {
    messages
    success
    zoom_recording_file
  }
}
```
