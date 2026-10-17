# Contra Project Copy — Python File & Folder Automation

## Project title

Messy File Inbox → Clean, Auditable Folder

## Short description

A deterministic Python workflow that scans a messy folder, detects CSV/JSON/TXT/PDF files, catches duplicates and corrupt files, normalizes names, and produces an Excel manifest plus exception log before copying anything.

## Project body

If your shared drive, download folder, or client intake folder keeps collecting inconsistent names, duplicate copies, broken exports, and unsupported files, I can turn it into a repeatable audit-first workflow.

Send me one representative folder and the naming rule you want. I will confirm fit, scope, and a fixed price before work starts.

**What the demo does**

- Scans 20 synthetic files and records size plus SHA-256 hash
- Detects CSV, JSON, TXT, PDF, and extensionless files from content
- Reads CSV rows/columns, JSON record counts, text line counts, and PDF page counts
- Marks byte-identical duplicates and prefers the cleanest source name
- Quarantines empty, malformed, corrupt, unsupported, or oversized files
- Writes a manifest, exception log, organize plan, JSON summary, and Excel report
- Copies only with an explicit `--apply` flag; the source folder is untouched

## Proof points

| Metric | Result |
|---|---:|
| Files scanned | 20 |
| Organized | 9 |
| Duplicate files skipped | 4 |
| Quarantined | 4 |
| Ignored system/template files | 3 |
| Automated tests | 10 / 10 passed |
| Demo runtime | under 0.1s |

### Proof video

72-second narrated walkthrough: `https://boy438.github.io/boyi-automation-portfolio/cases/python-file-automation/` — English voiceover, burned-in captions, real 20-file inbox, SHA-256 duplicate pairs, quarantine reasons, dry-run plan, and audit log.

## Deliverables

- `file_inbox_report.xlsx` — summary, manifest, exceptions, and plan
- `manifest.csv` — every file with type, hash, metadata, status, and target
- `exceptions.csv` — duplicate, quarantine, and ignore events
- `organize_plan.csv` — source-to-target copy plan
- `organized/`, `duplicates/`, `quarantine/` — safe copies for review
- Python source, dependency list, README, and test report

## Scope language

- One folder and one naming convention
- Up to 50 files for the basic audit; larger batches quoted after inspecting the sample
- CSV, JSON, TXT, and typed PDF files
- No file deletion by default
- No account passwords or unattended access
- No promise of 100% classification accuracy without a written rule set

## Demo disclosure

Independent demo — synthetic files only. No client names, logos, testimonials, or revenue claims. AI-assisted build, human-reviewed and tested. The runtime pipeline is deterministic and does not call an external model.

## Proposal angle

Hi [name] — I saw you need [specific folder outcome].

I built a similar demo: [case link]. For your folder, I would:

1. Inspect 20–30 representative files and confirm the naming and duplicate rules
2. Run a dry-run audit and send the manifest plus exception log
3. Apply the approved plan and hand over the Python script, README, and test report

The main risk is [mixed file types / ambiguous dates / duplicate policy], so I would validate that before scaling. We can start with one folder as a paid pilot and expand only if the output meets your spec.
