# Contra Project — Meeting Audio to Reviewed Notes, Actions & SRT

## Project title

Meeting Audio → Reviewed Notes, Actions & SRT

## Short description

Reviewed meeting notes, owned action items, and English/Chinese/bilingual SRT from one recording. ASR first, human correction for names/numbers/terms, and every action linked to its source sentence. Not a certified verbatim transcript; no 100% accuracy claim.

## Project type

Audio automation · Reviewed notes · Action items · Subtitles · Python

## The problem

A meeting recording contains decisions, risks, and next steps, but raw ASR is not ready to send. Names, numbers, and similar-sounding words get misrecognized. Turning the recording into an action list and subtitles is still manual work.

## What I built

- Synthetic meeting audio and ground-truth transcripts
- ASR with word timestamps
- Word error rate measurement against ground truth
- Human-corrected transcript used for final notes
- Extraction of key points, decisions, risks, and action items
- Owner, task, due date, due phrase, and source sentence for each action
- English, Chinese, and bilingual SRT generation
- Excel workbook with dashboard, meetings, actions, decisions, risks, key points, and transcript segments
- Self-contained proof page and 72-second narrated walkthrough (English voiceover, burned-in captions)

## How it works

1. You send a 2–5 minute sample.
2. I check audio quality, speaker turns, names, and output format.
3. I confirm fit, scope, and a fixed price before work starts.
4. I run ASR with word timestamps.
5. I do a human correction pass for names, numbers, and terms.
6. I extract decisions, risks, and action items from the corrected transcript.
7. I generate notes, CSV/Excel, and SRT, then check cue timing and line length.
8. I deliver with a short review note for uncertain names or dates.

## Demo results

| Metric | Result |
|---|---:|
| Meetings | 3 |
| Audio duration | 4:21 |
| Raw ASR WER* | 19.5% |
| Action items | 13 |
| Decisions | 3 |
| Risks | 3 |
| Captions | 25 |
| Automated tests | 6 / 6 passed |

\* Measured on synthetic ground truth with a small offline model. The final notes use the human-corrected transcript. This is not a claim about every real recording.

### Proof video

72-second narrated walkthrough: `https://boy438.github.io/boyi-automation-portfolio/cases/meeting-notes/` — English voiceover, burned-in captions, real waveform and raw ASR, human-corrected notes, 13 owned actions, and English / Chinese / bilingual SRT.

## What you get

- Meeting notes (Markdown): summary, key points, decisions, risks, action items
- Action-item CSV: owner, task, due date, due phrase, source sentence
- Decisions and risks CSV
- Excel workbook: dashboard, meetings, actions, decisions, risks, key points, transcript segments
- English SRT, Chinese SRT, and bilingual SRT (by scope)
- Clean readable transcript (not certified verbatim)
- Review note for uncertain names/dates
- Repeatable source script and README with assumptions and limits

## Fit

- Weekly team meetings, client calls, onboarding calls
- Interviews and coaching sessions
- Webinars/training with clear audio
- English audio with English or Chinese subtitles
- Teams that need owned actions, due dates, and source-linked notes

## Not a fit

- Heavily overlapping speakers with no separate tracks
- Very noisy recordings or phone-speaker recordings
- Legal, medical, or financial advice requiring a certified transcript
- Secret recording or content you do not have permission to process
- “100% accuracy” or unlimited revisions
- Account passwords or unattended access

## What I need from you

1. A 2–5 minute sample.
2. Speaker count and names/glossary.
3. Meeting language and subtitle language.
4. Output: notes, actions, SRT, Excel, or all.
5. Confirmation that there are no overlapping speakers or certified-transcript requirements.
6. Deadline and revision expectations.
7. Confirmation that you have permission to process the recording.

## Scope and limits

- Not a certified verbatim transcript; filler words are removed.
- No 100% accuracy claim.
- Speaker labels only with clear turns or separate tracks; otherwise Speaker 1/2 or no labels.
- SRT is edited for readability (line length and timing), not a legal record.
- No account access; exported audio only.
- Revisions: 1 / 2 / 3 by package; new requirements are a new order.
- Audio over 90 minutes: quote separately.
- Overlapping speakers, heavy noise, or poor audio may be declined before the order.

## Stack

Python 3.15, ASR with word timestamps, openpyxl, Pillow, imageio-ffmpeg, Windows Speech Synthesis for the synthetic audio.

## Status

**Independent demo — synthetic audio.** No client names, logos, testimonials, or revenue claims are used.

## CTA

Send one 2–5 minute sample recording and the output format you need. I will confirm fit, scope, and a fixed price before work starts. A small paid pilot is available for one meeting.

## Proposal template

Hi [name] — I saw you need [specific meeting output].

I built a similar demo: [case page / sample output link]. For your recording, I would:

1. Check the audio quality and run ASR with timestamps.
2. Apply a human correction pass for names, numbers, and terms.
3. Extract decisions, risks, and action items.
4. Package notes and the subtitle format you need.

The main risk is [overlapping speakers / noisy audio / missing names], so I would review a short sample before scaling. We can start with a paid pilot on one meeting and expand only if the output meets your spec.

## Service listing

### Meeting Notes + Action Items — from $150

- Up to 45 minutes of clear audio
- Summary, key points, decisions, risks, action items
- CSV/Excel action list
- Clean readable transcript
- 3-day delivery
- 2 revisions

### Bilingual Meeting Subtitles — from $180

- English + Chinese SRT
- Bilingual SRT
- Timestamped transcript
- Glossary/name pass
- 3-day delivery
- 2 revisions

### Recurring Meeting Pack — from $350

- Weekly or monthly meeting batch
- Notes, action items, decisions, risks
- English/Chinese/bilingual subtitles
- Excel workbook and review queue
- Optional monitoring quote
