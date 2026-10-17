# Boyi Automation — Portfolio Hub

A single GitHub Pages portfolio for three working automation demos:

1. **Spreadsheet reporting** — messy Excel → one-click weekly report
2. **Invoice extraction** — PDF invoices → validated Excel data
3. **Meeting notes** — audio → notes, action items, and bilingual SRT

All three cases are **independent demos with synthetic data/audio**. No client names, logos, testimonials, or revenue claims are used.

## What is in this folder

```
docs/
  index.html                  portfolio homepage
  profile.html                full profile page
  downloads/
    boyi-automation-profile.pdf
    *-case-study.pdf
  cases/
    excel-report/             self-contained Excel case page + samples
    invoice-extraction/       self-contained invoice case page + samples
    meeting-notes/            self-contained meeting case page + samples + audio
  upload-pack/                profile copy, Fiverr/Contra copy, pricing, checklist
  assets/                     covers and OG image
scripts/build_hub.py          regenerates the hub pages and profile PDF
```

## GitHub Pages

1. Create a GitHub repository for this folder.
2. Push the repository.
3. Settings → Pages → Source: **Deploy from a branch**.
4. Branch: `main`; folder: `/docs`.
5. Open `https://<username>.github.io/<repo>/`.

Test these links after publishing:

- Homepage: `/`
- Excel case: `/cases/excel-report/`
- Invoice case: `/cases/invoice-extraction/`
- Meeting case: `/cases/meeting-notes/`
- Profile: `/profile.html`
- Profile PDF: `/downloads/boyi-automation-profile.pdf`

## Upload order

1. Publish this hub to GitHub Pages.
2. Build the Contra profile and 3 projects; add the case links.
3. Build the Fiverr profile and 3 gigs; upload images and videos from the individual proof packs.
4. Start with 3 tailored Contra proposals per day.
5. Use the first-3-orders playbook and keep delivery inside the platform.

## Compliance

- No off-platform contact or payment CTA in Fiverr/Contra.
- No fake proof or invented client results.
- AI-assisted work is disclosed.
- No “100% accuracy” or unlimited revisions.
- Scanned PDFs and raw ASR errors are shown and handled honestly.

## Regenerate

```powershell
python scripts/build_hub.py
```

The script regenerates `docs/index.html`, `docs/profile.html`, `docs/profile-print.html`, the OG image, and the profile PDF. It assumes the case folders and assets are already present.

## Source of truth

The three individual case repos remain the source for their code and tests:

- `D:\FreelanceWorkbench\03_projects\spreadsheet-report-automation`
- `D:\FreelanceWorkbench\03_projects\invoice-extraction-flagship`
- `D:\FreelanceWorkbench\03_projects\meeting-notes-flagship`

This hub contains copies of their public proof pages so one GitHub Pages site can link to all three.
