# Contra Project — Messy Spreadsheets to One-Click Weekly Report

## Project title

Messy Spreadsheets → One-Click Weekly Report

## Short description

A reproducible Python workflow that normalizes messy CSV exports, validates every row, logs exceptions, and turns the result into a client-ready Excel report.

## Project type

Data automation · Python · Excel reporting · Data quality

## The problem

Weekly reporting often starts with three exports that do not agree: mixed date formats, duplicate order IDs, inconsistent SKUs, currency symbols, blank prices, invalid discounts, and orphan customer/product references. The manual cleanup is slow, hard to audit, and easy to repeat incorrectly next week.

## What I built

- A deterministic Python cleanup pipeline for orders, customers, and products
- Date, money, quantity, SKU, discount, status, and region normalization
- Duplicate detection and referential-integrity checks
- A row-level exception log with severity and action taken
- A styled Excel workbook with dashboard, clean orders, exceptions, weekly summary, category summary, and charts
- A repeatable command that can run on next week's exports
- A self-contained proof page and captioned walkthrough

## Demo results

| Metric | Result |
|---|---:|
| Raw order rows | 1,206 |
| Clean rows | 1,166 |
| Invalid rows excluded | 40 |
| Duplicate order IDs removed | 6 |
| Quality events logged | 78 |
| Automated tests | 6 / 6 passed |
| Runtime | ~0.03s |

These numbers are from the synthetic demo dataset generated for this project. They are benchmarks, not client results.

## What was validated

- Mixed date formats
- Currency symbols and decimal/thousands separators
- Positive integer quantities
- Discount percentages and bounds
- Duplicate order IDs
- Unknown customer IDs and SKUs
- Customer email format
- Paid revenue vs cancelled/refunded orders
- Excel output generation

## Deliverables

- Cleaned workbook (`.xlsx`)
- Clean order-level CSV
- Exception log CSV
- Weekly and category summaries
- KPI JSON
- Source code + README
- Captioned walkthrough
- Sample input/output files

## Stack

Python 3.15, `csv`, `decimal`, `openpyxl`, `unittest`, Pillow, imageio-ffmpeg.

## Status

**Independent demo — synthetic data.** No client names, logos, testimonials, or revenue claims are used.

## CTA

Send one sample file and the exact output format you need. I will confirm fit, scope, and a fixed price before work starts. A small paid pilot is available for one file or one report.

## Proposal template

Hi [name] — I saw you need [specific outcome].

I built a similar demo: [case page / sample output link]. For your case, I would:

1. Inspect one sample file and document the input/output mapping
2. Normalize and validate the data with an exception log
3. Deliver a cleaned workbook plus a repeatable script

The main risk is [data quality / ambiguous dates / missing master data], so I would validate that before scaling. We can start with a paid pilot on one file and expand only if the output meets your spec.

## Service listing

### Excel / CSV Cleanup & Reporting Automation — from $120

- 1–3 files
- Up to 20,000 rows
- Cleaning, deduplication, validation, exception log
- Excel dashboard + weekly summary
- Repeatable script + README
- 3-day delivery
- 2 revisions

### PDF/Excel Data Consolidation — from $150

- Combine multiple exports or PDF-derived tables into one schema
- Validation rules and exception queue
- Dashboard-ready output
- Source files included

### Recurring Weekly Reporting Workflow — from $280

- Custom rules for your recurring report
- One-click rerun
- Exception log and README
- 14-day bug-fix support
- Optional monthly monitoring quote
