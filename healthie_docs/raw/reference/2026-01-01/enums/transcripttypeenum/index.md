---
title: TranscriptTypeEnum | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/transcripttypeenum/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/transcripttypeenum/index.md
---

Types of transcripts

## Used By

[`Appointment.transcripts`](/reference/2026-01-01/objects/appointment)

[`Transcript.transcript_type`](/reference/2026-01-01/objects/transcript)

## Definition

```
"""
Types of transcripts
"""
enum TranscriptTypeEnum {
  """
  Transcript captured in real-time during the meeting
  """
  realtime_capture


  """
  Transcript generated from processed recording
  """
  processed_recording
}
```
