---
title: TranscriptStatusEnum | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/transcriptstatusenum/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/transcriptstatusenum/index.md
---

Status of transcript processing

## Used By

[`Appointment.transcripts`](/reference/2026-01-01/objects/appointment)

[`Transcript.status`](/reference/2026-01-01/objects/transcript)

## Definition

```
"""
Status of transcript processing
"""
enum TranscriptStatusEnum {
  """
  Transcript is currently being processed
  """
  processing


  """
  Transcript processing has completed successfully
  """
  completed


  """
  Transcript processing has failed
  """
  failed


  """
  Transcript processing was interrupted but partial content is available
  """
  incomplete
}
```
