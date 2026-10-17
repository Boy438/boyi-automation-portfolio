# Contra Project — PDF Invoices to Validated Excel Data

## Project title

PDF Invoices → Validated Excel Data

## Short description

A reproducible extraction workflow that reads typed invoice PDFs, pulls header fields and line items, checks the math, logs exceptions, and exports a client-ready workbook.

## Project type

Data extraction · PDF automation · Python · Excel reporting · Data quality

## The problem

A folder of invoice PDFs is not a spreadsheet. It is a pile of exceptions: scanned files, ambiguous dates, missing PO numbers, duplicate invoices, line-math errors, tax/total mismatches, and unsupported currencies. Manual entry is slow and hard to audit.

## What I built

- A batch PDF reader with text-layer detection
- Header extraction: vendor, customer, invoice number, dates, PO, currency, terms, subtotal, tax, total
- Line-item extraction: description, quantity, unit price, amount
- Math validation: quantity × unit price, subtotal, tax, total
- Duplicate invoice detection
- Currency and missing-field validation
- Row-level exception log
- Excel workbook with dashboard, invoices, line items, exceptions, vendor and currency summaries
- A self-contained proof page and 72-second narrated walkthrough

## Demo results

| Metric | Result |
|---|---:|
| PDF files | 48 |
| Text-layer PDFs | 46 |
| Usable invoices | 41 |
| Review warnings | 5 files kept with warning |
| Excluded files | 7 |
| Quality events logged | 15 |
| Header fields matched* | 506 / 506 |
| Line-item fields matched* | 548 / 548 |
| Automated tests | 8 / 8 passed |

\* Controlled benchmark on the 46 synthetic typed PDFs. Not a guarantee for every real-world PDF. “Usable” includes 5 files kept with review warnings; excluded files are not in the clean output. The 72-second demo video shows the full validation workflow; service inclusions vary as listed below.

## What was validated

- Text-layer presence
- Required header fields
- Ambiguous date formats
- Line amount = quantity × unit price
- Sum of line items = subtotal
- Subtotal + tax = total
- Duplicate invoice numbers
- Supported currencies
- Missing PO numbers
- Image-only PDFs

## Deliverables

- Clean invoice table (CSV/XLSX)
- Line-item table
- Exception log
- Excel workbook with summaries and charts
- Repeatable source script
- README with assumptions and limits
- 72-second narrated walkthrough
- Validation/test report
- Sample PDFs and outputs

## Stack

Python 3.15, pdfplumber, PyMuPDF, openpyxl, reportlab, Pillow, imageio-ffmpeg.

## Status

**Independent demo — synthetic data.** No client names, logos, testimonials, or revenue claims are used.

## CTA

Send 1–3 sample PDFs and the exact columns you need. I will confirm fit, scope, and a fixed price before work starts. A small paid pilot is available for one batch.

## Proposal template

Hi [name] — I saw you need [specific invoice extraction outcome].

I built a similar demo: [case page / sample output link]. For your batch, I would:

1. Inspect 1–3 sample PDFs and document the field mapping
2. Extract header fields and line items with validation checks
3. Deliver a clean Excel/CSV file plus a row-level exception log

The main risk is [scanned pages / multi-page tables / inconsistent labels], so I would validate that before scaling. We can start with a paid pilot on 10–25 PDFs and expand only if the output meets your spec.

## Service listing

The demo shows the full validation workflow. Service inclusions vary as listed below.

### PDF Invoice to Excel / CSV Extraction — from $150

- Up to 100 typed PDFs
- Header + line-item extraction
- Math validation + exception log
- Excel workbook with summaries
- 3-day delivery
- 2 revisions

### Invoice Batch Cleanup & Validation — from $280

- Custom field mapping and validation rules
- Duplicate detection
- Vendor/currency summaries
- Repeatable script + README
- 14-day bug-fix support

### Recurring Invoice Reporting Workflow — from $450

- Monthly batch extraction
- One-click rerun
- Exception queue and delivery pack
- Optional monitoring quote
