from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ASSETS = DOCS / "assets"
BUILD = ROOT / "build"
CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
for path in (DOCS, ASSETS, BUILD):
    path.mkdir(parents=True, exist_ok=True)

CSS = """
:root{--navy:#0B1220;--lime:#B7F34A;--warm:#F6F3EA;--coral:#FF6B5E;--muted:#5C677D;--line:#DDE2EA;--white:#fff}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--warm);color:var(--navy);font-family:'Segoe UI',Arial,sans-serif;line-height:1.55}
img{display:block;max-width:100%}a{color:inherit}.wrap{max-width:1180px;margin:0 auto;padding:0 28px}
.nav{position:sticky;top:0;z-index:20;background:rgba(11,18,32,.94);backdrop-filter:blur(12px);border-bottom:1px solid rgba(255,255,255,.08)}
.nav .wrap{display:flex;justify-content:space-between;align-items:center;height:66px;gap:18px}.brand{color:#fff;font-weight:900;letter-spacing:.12em;font-size:13px;text-transform:uppercase}.brand b{color:var(--lime)}
.nav-links{display:flex;gap:18px;flex-wrap:wrap}.nav-links a{color:#C8D0DD;text-decoration:none;font-size:13px;font-weight:700}.nav-links a:hover{color:var(--lime)}
.hero{background:var(--navy);color:#fff;padding:74px 0 64px;position:relative;overflow:hidden}.hero:after{content:'';position:absolute;right:-120px;top:-120px;width:460px;height:460px;border-radius:50%;border:1px solid rgba(183,243,74,.25);box-shadow:0 0 0 46px rgba(183,243,74,.04),0 0 0 92px rgba(183,243,74,.03)}
.eyebrow{display:inline-flex;align-items:center;gap:8px;border:1px solid rgba(183,243,74,.35);background:rgba(183,243,74,.1);color:var(--lime);border-radius:999px;padding:7px 12px;font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase}
.dot{width:7px;height:7px;border-radius:50%;background:var(--lime);display:inline-block}.hero h1{font-size:clamp(44px,6.5vw,86px);line-height:.98;letter-spacing:-.055em;margin:24px 0 18px;max-width:980px}.hero h1 em{font-style:normal;color:var(--lime)}.hero p{font-size:20px;color:#C8D0DD;max-width:820px;margin:0 0 28px}
.hero-actions{display:flex;gap:12px;flex-wrap:wrap}.btn{display:inline-flex;align-items:center;justify-content:center;border-radius:11px;padding:13px 18px;font-weight:800;text-decoration:none;transition:.18s ease}.btn:hover{transform:translateY(-1px);filter:brightness(1.03)}.btn-primary{background:var(--lime);color:var(--navy)}.btn-ghost{background:rgba(255,255,255,.08);color:#fff;border:1px solid rgba(255,255,255,.2)}
.metric-row{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:34px}.metric{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.11);border-radius:16px;padding:18px 20px}.metric b{display:block;color:var(--lime);font-size:30px;line-height:1.1;letter-spacing:-.03em}.metric span{display:block;color:#AAB5C4;font-size:11px;text-transform:uppercase;letter-spacing:.09em;margin-top:6px}
section{padding:72px 0}section.tight{padding:38px 0}.kicker{font-size:12px;font-weight:800;letter-spacing:.15em;text-transform:uppercase;color:var(--muted);margin:0 0 12px}h2{font-size:clamp(30px,3.6vw,50px);line-height:1.06;letter-spacing:-.04em;margin:0 0 16px}.lead{font-size:18px;color:#435066;max-width:850px;margin:0 0 30px}
.cases{display:grid;gap:24px}.case-card{display:grid;grid-template-columns:1.05fr .95fr;background:#fff;border:1px solid var(--line);border-radius:22px;overflow:hidden;box-shadow:0 18px 48px rgba(11,18,32,.06)}.case-media{background:#0B1220;min-height:290px}.case-media img{width:100%;height:100%;object-fit:cover}.case-body{padding:28px}.case-body h3{font-size:27px;line-height:1.12;letter-spacing:-.03em;margin:8px 0 10px}.case-body p{color:#4B586D;font-size:15px;margin:0 0 18px}.case-meta{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 20px}.pill{border:1px solid #D7DDE6;border-radius:999px;padding:6px 10px;font-size:11px;font-weight:700;color:#435066;background:#F8F9FB}.case-link{font-weight:900;text-decoration:none;color:var(--navy);border-bottom:2px solid var(--lime);padding-bottom:2px}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.process{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px;position:relative}.process .num{width:32px;height:32px;border-radius:10px;background:var(--lime);display:flex;align-items:center;justify-content:center;font-weight:900;margin-bottom:14px}.process h3{font-size:16px;margin:0 0 7px}.process p{font-size:13px;color:#4B586D;margin:0}
.split{display:grid;grid-template-columns:1.05fr .95fr;gap:24px;align-items:start}.panel{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px;box-shadow:0 10px 30px rgba(11,18,32,.04)}.panel h3{margin:0 0 12px;font-size:18px}.checklist{list-style:none;padding:0;margin:0;display:grid;gap:10px}.checklist li{display:flex;gap:10px;align-items:flex-start;font-size:14px}.check{width:20px;height:20px;border-radius:50%;background:var(--lime);display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:12px;flex:none}
.service-table{width:100%;border-collapse:collapse;background:#fff;border:1px solid var(--line);border-radius:16px;overflow:hidden;font-size:14px}.service-table th{background:var(--navy);color:#fff;text-align:left;padding:13px 15px;font-size:12px;letter-spacing:.06em;text-transform:uppercase}.service-table td{padding:14px 15px;border-top:1px solid var(--line);vertical-align:top}.service-table td:first-child{font-weight:800}.service-table small{color:var(--muted)}
.proof-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.proof{background:var(--navy);color:#fff;border-radius:16px;padding:20px}.proof b{display:block;color:var(--lime);font-size:24px;margin-bottom:6px}.proof span{color:#C8D0DD;font-size:13px}.proof p{color:#AAB5C4;font-size:13px;margin:10px 0 0}
.profile-band{background:#fff;border:1px solid var(--line);border-radius:20px;padding:28px;display:grid;grid-template-columns:1.3fr .7fr;gap:26px}.profile-band h2{margin-bottom:12px}.profile-band p{color:#435066;font-size:15px;margin:0 0 12px}.tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}.tag{background:var(--warm);border:1px solid var(--line);border-radius:999px;padding:6px 10px;font-size:11px;font-weight:700;color:#435066}
.cta{background:var(--lime);border-radius:22px;padding:32px;display:flex;justify-content:space-between;gap:24px;align-items:center}.cta h2{margin:0 0 6px}.cta p{margin:0;color:#35421F;max-width:760px}.footer{padding:26px 0 48px;color:var(--muted);font-size:12px;border-top:1px solid var(--line);margin-top:24px}.note{font-size:12px;color:var(--muted)}
@media(max-width:900px){.case-card,.split,.profile-band{grid-template-columns:1fr}.grid4{grid-template-columns:1fr 1fr}.proof-grid{grid-template-columns:1fr}.metric-row{grid-template-columns:1fr 1fr}.cta{display:block}.cta .btn{margin-top:16px}}
@media(max-width:560px){.metric-row,.grid4{grid-template-columns:1fr}.wrap{padding:0 18px}}
@media print{body{background:#fff}.nav,.hero-actions,.cta .btn{display:none}.hero{background:#0B1220 !important;-webkit-print-color-adjust:exact;print-color-adjust:exact}.case-card,.panel,.proof,.profile-band{box-shadow:none;break-inside:avoid}section{padding:28px 0}}
"""

PRINT_CSS = CSS + """
@page{size:A4;margin:0}body{background:#fff}.print-page{width:210mm;min-height:297mm;padding:16mm 17mm;page-break-after:always;position:relative;background:#fff}.print-page.cover{background:#0B1220;color:#fff}.print-page.cover h1{font-size:48px;line-height:1.02;letter-spacing:-.05em;margin:24px 0 14px}.print-page.cover h1 em{font-style:normal;color:#B7F34A}.print-page .metric-row{grid-template-columns:repeat(4,1fr)}.print-page .metric b{font-size:22px}.print-page h2{font-size:30px}.print-page .lead{font-size:13px}.print-page .case-card{grid-template-columns:1fr 1fr}.print-page .case-media{min-height:150px}.print-page .case-body{padding:16px}.print-page .case-body h3{font-size:18px}.print-page .case-body p{font-size:11px}.print-page .proof p{font-size:10px}.print-page .service-table{font-size:10px}.print-page .service-table th,.print-page .service-table td{padding:7px 8px}.print-page .process{padding:12px}.print-page .process p{font-size:10px}.print-page .profile-band{padding:16px}.print-page .profile-band p{font-size:11px}.print-page .note{font-size:9px}
"""


def page(title: str, body: str, css: str = CSS, extra_head: str = "") -> str:
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>{extra_head}<style>{css}</style></head><body>{body}</body></html>"""


def index_html() -> str:
    body = """
<nav class="nav"><div class="wrap"><div class="brand">BOYI <b>AUTOMATION</b></div><div class="nav-links"><a href="#work">Work</a><a href="#services">Services</a><a href="#process">Process</a><a href="#profile">Profile</a><a href="profile.html">About</a></div></div></nav>
<div class="hero"><div class="wrap">
  <span class="eyebrow"><span class="dot"></span> Independent portfolio · synthetic demos</span>
  <h1>Messy input.<br><em>Clean output.</em></h1>
  <p>I build small, auditable automations for spreadsheets, invoices, and meetings. Fixed scope. Tested outputs. Source included.</p>
  <div class="hero-actions"><a class="btn btn-primary" href="#work">View the work</a><a class="btn btn-ghost" href="#process">How I work</a></div>
  <div class="metric-row"><div class="metric"><b>3</b><span>proof projects</span></div><div class="metric"><b>1,206</b><span>rows cleaned</span></div><div class="metric"><b>48</b><span>PDFs processed</span></div><div class="metric"><b>4:21</b><span>audio transcribed</span></div></div>
</div></div>

<section id="work"><div class="wrap">
  <p class="kicker">The work</p><h2>One pattern. Three input types.</h2><p class="lead">Each case is a self-contained demo with sample files, tests, metrics, and a clear audit trail. No fake client logos, no invented testimonials.</p>
  <div class="cases">
    <article class="case-card"><div class="case-media"><img src="assets/excel-cover.png" alt="Messy Excel to clean weekly report cover"></div><div class="case-body"><span class="eyebrow">01 · Spreadsheets</span><h3>Messy Excel → one-click weekly report</h3><p>Normalize, validate, deduplicate, and package a weekly Excel report with an exception log and repeatable script.</p><div class="case-meta"><span class="pill">1,206 raw rows</span><span class="pill">78 quality events</span><span class="pill">8/8 tests*</span></div><a class="case-link" href="cases/excel-report/index.html">Read the Excel case study →</a></div></article>
    <article class="case-card"><div class="case-media"><img src="assets/invoice-cover.png" alt="PDF invoices to clean Excel cover"></div><div class="case-body"><span class="eyebrow">02 · Documents</span><h3>PDF invoices → validated Excel data</h3><p>Extract header fields and line items, reconcile line math, tax, and totals, then export a clean workbook with an exception queue.</p><div class="case-meta"><span class="pill">48 PDFs</span><span class="pill">41 clean invoices</span><span class="pill">100% typed-demo accuracy*</span></div><a class="case-link" href="cases/invoice-extraction/index.html">Read the invoice case study →</a></div></article>
    <article class="case-card"><div class="case-media"><img src="assets/meeting-cover.png" alt="Meeting audio to notes and SRT cover"></div><div class="case-body"><span class="eyebrow">03 · Audio</span><h3>Meeting audio → notes, actions, and SRT</h3><p>Transcribe with timings, apply human correction, extract owners and deadlines, and package English, Chinese, and bilingual subtitles.</p><div class="case-meta"><span class="pill">3 meetings</span><span class="pill">13 action items</span><span class="pill">25 captions</span></div><a class="case-link" href="cases/meeting-notes/index.html">Read the meeting case study →</a></div></article>
  </div>
  <p class="note" style="margin-top:16px">*Controlled benchmarks on synthetic demo data. See each case for assumptions and limits.</p>
</div></section>

<section id="services" class="tight"><div class="wrap">
  <p class="kicker">Services</p><h2>Small, fixed-scope builds.</h2><p class="lead">Start with a sample. I confirm fit, scope, and a fixed price before work starts. The prices below are launch ranges; the final quote depends on file quality and output rules.</p>
  <table class="service-table"><thead><tr><th>Service</th><th>Fiverr from</th><th>Contra from</th><th>Typical output</th></tr></thead><tbody>
    <tr><td>Spreadsheet cleanup & reporting</td><td>$45</td><td>$120</td><td>Clean workbook, dashboard, exception log, repeatable script</td></tr>
    <tr><td>PDF invoice → Excel/CSV</td><td>$65</td><td>$150</td><td>Invoice table, line-item table, math checks, exception log</td></tr>
    <tr><td>Meeting notes & action items</td><td>$45</td><td>$95</td><td>Summary, decisions, risks, action items, SRT</td></tr>
  </tbody></table>
</div></section>

<section id="process"><div class="wrap"><p class="kicker">Process</p><h2>Proof before promises.</h2><div class="grid4">
  <div class="process"><div class="num">1</div><h3>Sample first</h3><p>You send one representative file or recording. I inspect it before quoting.</p></div>
  <div class="process"><div class="num">2</div><h3>Fixed scope</h3><p>Deliverables, assumptions, revisions, and exclusions are written down.</p></div>
  <div class="process"><div class="num">3</div><h3>AI-assisted + human QA</h3><p>Automation does the heavy lifting; I review and test the output against the sample.</p></div>
  <div class="process"><div class="num">4</div><h3>Source + audit trail</h3><p>You get working files, source code where applicable, and an exception/test report.</p></div>
</div>
<div class="split" style="margin-top:26px">
  <div class="panel"><h3>Good fit</h3><ul class="checklist"><li><span class="check">✓</span><div>Small teams and solo founders with repetitive data work</div></li><li><span class="check">✓</span><div>CSV/XLSX exports, typed PDFs, and clear meeting audio</div></li><li><span class="check">✓</span><div>Fixed-scope pilots that may become recurring workflows</div></li><li><span class="check">✓</span><div>Buyers who value an audit trail over a black box</div></li></ul></div>
  <div class="panel"><h3>Not a fit</h3><ul class="checklist"><li><span class="check">—</span><div>Handwritten scans, heavily overlapping audio, or undefined data rules</div></li><li><span class="check">—</span><div>Requests that need account passwords or sensitive credentials</div></li><li><span class="check">—</span><div>“100% accuracy” or unlimited revisions without a spec</div></li><li><span class="check">—</span><div>Illegal scraping, off-platform payment, or undisclosed AI use</div></li></ul></div>
</div></div></section>

<section class="tight"><div class="wrap"><p class="kicker">Proof, not claims</p><h2>What is verifiable.</h2><div class="proof-grid">
  <div class="proof"><b>3</b><span>working case studies</span><p>Each case has a live proof page, sample files, a PDF, and a short video.</p></div>
  <div class="proof"><b>Source</b><span>included</span><p>Python code, tests, README, and a repeatable command are part of the proof.</p></div>
  <div class="proof"><b>Synthetic</b><span>clearly labeled</span><p>No client logos, testimonials, or invented revenue claims. The demo label is explicit.</p></div>
</div></div></section>

<section id="profile" class="tight"><div class="wrap"><div class="profile-band"><div><p class="kicker">Profile</p><h2>Boyi Automation</h2><p>I build small automations that turn messy business inputs into clean, usable outputs. My current focus is spreadsheet reporting, PDF data extraction, and meeting-to-action workflows.</p><p>I use AI-assisted tooling to build quickly, then personally review and test every deliverable against real sample data. You get the working files, source code, and an audit trail — not a black box.</p><div class="tags"><span class="tag">Python</span><span class="tag">Excel / CSV</span><span class="tag">PDF extraction</span><span class="tag">ASR / SRT</span><span class="tag">Data quality</span><span class="tag">Human QA</span></div></div><div><a class="btn btn-primary" href="profile.html" style="background:#0B1220;color:#fff">Open full profile</a><p class="note" style="margin-top:14px">No off-platform payment or contact. Use the platform where we connected.</p></div></div></div></section>

<section><div class="wrap"><div class="cta"><div><h2>Have a messy input?</h2><p>Send one representative sample through the platform where we connected. I will confirm fit, scope, and a fixed price before work starts.</p></div><a class="btn" style="background:#0B1220;color:#fff" href="cases/excel-report/index.html">Start with a case</a></div></div></section>
<div class="wrap"><div class="footer">Independent demos. Synthetic data and audio only. No client names, logos, testimonials, or revenue claims. © 2026 CHEN BOYI / Boyi Automation.</div></div>
"""
    extra = '<meta name="description" content="Boyi Automation — AI-assisted automation for messy spreadsheets, invoices, and meetings. Independent demo portfolio."><meta property="og:title" content="Boyi Automation — Messy input, clean output"><meta property="og:description" content="Three working automation case studies: Excel reporting, PDF invoice extraction, and meeting notes + SRT."><meta property="og:image" content="assets/og-image.png"><meta property="og:type" content="website">'
    return page("Boyi Automation — Messy input, clean output", body, CSS, extra)


def profile_html() -> str:
    body = """
<nav class="nav"><div class="wrap"><div class="brand">BOYI <b>AUTOMATION</b></div><div class="nav-links"><a href="index.html">Portfolio</a><a href="profile.html">Profile</a></div></div></nav>
<div class="hero"><div class="wrap"><span class="eyebrow"><span class="dot"></span> Profile · independent portfolio</span><h1>Boyi<br><em>Automation.</em></h1><p>AI-assisted automation for messy data, documents, and meeting notes. Fixed scope, tested outputs, source included.</p><div class="hero-actions"><a class="btn btn-primary" href="index.html#work">View the work</a><a class="btn btn-ghost" href="downloads/boyi-automation-profile.pdf">Download profile PDF</a></div></div></div>
<section><div class="wrap"><div class="split"><div><p class="kicker">Profile</p><h2>Small automations. Visible quality.</h2><p class="lead">I help small teams replace repetitive manual work with small, reliable workflows. The goal is not a giant AI platform. It is one clean output you can trust, with the source and audit trail attached.</p><p style="color:#435066">My current proof set covers three inputs: spreadsheets, typed invoice PDFs, and meeting audio. Each case shows the problem, the build, the validation, and the sample output. I use AI-assisted tooling, then personally review and test every deliverable.</p><h2 style="font-size:30px;margin-top:30px">What I can build</h2><table class="service-table"><thead><tr><th>Service</th><th>Starting point</th><th>Output</th></tr></thead><tbody><tr><td>Excel / CSV cleanup & reporting</td><td>$45 Fiverr / $120 Contra</td><td>Clean workbook, dashboard, exception log, script</td></tr><tr><td>PDF invoice → Excel/CSV</td><td>$65 Fiverr / $150 Contra</td><td>Invoice table, line items, math checks, exception log</td></tr><tr><td>Meeting notes & action items</td><td>$45 Fiverr / $95 Contra</td><td>Summary, decisions, risks, actions, SRT</td></tr></tbody></table></div><div><div class="panel"><h3>Working style</h3><ul class="checklist"><li><span class="check">✓</span><div>Sample-first quote: no guessing from a vague brief</div></li><li><span class="check">✓</span><div>Fixed scope and written assumptions</div></li><li><span class="check">✓</span><div>Human review after the automated pass</div></li><li><span class="check">✓</span><div>Source, README, and exception/test report</div></li><li><span class="check">✓</span><div>No account access needed for the first sample</div></li></ul></div><div class="panel" style="margin-top:16px"><h3>Good fit</h3><p style="color:#4B586D;font-size:14px">Small teams and solo founders with recurring spreadsheet reports, typed invoice batches, or meeting recordings that need notes and subtitles.</p><h3 style="margin-top:18px">Not a fit</h3><p style="color:#4B586D;font-size:14px">Handwritten scans, heavily overlapping audio, undefined data rules, credential access, or requests for “100% accuracy” without a written spec.</p></div></div></div></div></section>
<section class="tight"><div class="wrap"><div class="proof-grid"><div class="proof"><b>3</b><span>working case studies</span><p>Excel, PDF invoices, and meeting audio.</p></div><div class="proof"><b>20</b><span>automated tests total</span><p>6 + 8 + 6 across the three demos.</p></div><div class="proof"><b>Source</b><span>included</span><p>Every case includes a repeatable script and README.</p></div></div></div></section>
<div class="wrap"><div class="footer">Independent demos. Synthetic data and audio only. No client names, logos, testimonials, or revenue claims. © 2026 CHEN BOYI / Boyi Automation.</div></div>
"""
    return page("Boyi Automation — Profile", body)


def profile_print_html() -> str:
    body = """
<div class="print-page cover"><span class="eyebrow"><span class="dot"></span> INDEPENDENT PORTFOLIO · SYNTHETIC DEMOS</span><h1>Boyi<br><em>Automation.</em></h1><p style="font-size:17px;color:#C8D0DD;max-width:760px">AI-assisted automation for messy data, documents, and meeting notes. Fixed scope, tested outputs, source included.</p><div class="metric-row" style="margin-top:30px"><div class="metric"><b>3</b><span>proof projects</span></div><div class="metric"><b>1,206</b><span>rows cleaned</span></div><div class="metric"><b>48</b><span>PDFs processed</span></div><div class="metric"><b>4:21</b><span>audio transcribed</span></div></div><p class="note" style="margin-top:40px;color:#AAB5C4">Independent demos. Synthetic data and audio only. No client names, logos, testimonials, or revenue claims.</p></div>
<div class="print-page"><p class="kicker">01 · The work</p><h2>Three input types. One pattern.</h2><div class="cases" style="gap:12px"><article class="case-card"><div class="case-media"><img src="assets/excel-cover.png" alt=""></div><div class="case-body"><h3 style="font-size:17px">Excel → weekly report</h3><p>Clean, validate, deduplicate, and package a repeatable workbook.</p></div></article><article class="case-card"><div class="case-media"><img src="assets/invoice-cover.png" alt=""></div><div class="case-body"><h3 style="font-size:17px">PDF invoices → Excel</h3><p>Header fields, line items, math checks, exception log.</p></div></article><article class="case-card"><div class="case-media"><img src="assets/meeting-cover.png" alt=""></div><div class="case-body"><h3 style="font-size:17px">Meeting audio → notes/SRT</h3><p>Summary, actions, decisions, risks, bilingual subtitles.</p></div></article></div><p class="note">Controlled benchmarks on synthetic demo data. See each case for assumptions and limits.</p></div>
<div class="print-page"><p class="kicker">02 · Services</p><h2>Small, fixed-scope builds.</h2><table class="service-table"><thead><tr><th>Service</th><th>Fiverr from</th><th>Contra from</th><th>Output</th></tr></thead><tbody><tr><td>Spreadsheet cleanup & reporting</td><td>$45</td><td>$120</td><td>Workbook, dashboard, exception log, script</td></tr><tr><td>PDF invoice → Excel/CSV</td><td>$65</td><td>$150</td><td>Invoice/line-item tables, math checks, exception log</td></tr><tr><td>Meeting notes & action items</td><td>$45</td><td>$95</td><td>Summary, decisions, risks, actions, SRT</td></tr></tbody></table><h2 style="font-size:26px;margin-top:28px">How I work</h2><div class="grid4"><div class="process"><div class="num">1</div><h3>Sample first</h3><p>One representative file or recording before a quote.</p></div><div class="process"><div class="num">2</div><h3>Fixed scope</h3><p>Deliverables, assumptions, revisions, exclusions.</p></div><div class="process"><div class="num">3</div><h3>Human QA</h3><p>Automation does the heavy lifting; I review the output.</p></div><div class="process"><div class="num">4</div><h3>Audit trail</h3><p>Working files, source, exception/test report.</p></div></div></div>
<div class="print-page"><p class="kicker">03 · Profile</p><h2>Boyi Automation</h2><p class="lead">I build small automations that turn messy business inputs into clean, usable outputs. My current focus is spreadsheet reporting, PDF data extraction, and meeting-to-action workflows.</p><p style="color:#435066;font-size:13px">I use AI-assisted tooling to build quickly, then personally review and test every deliverable against real sample data. You get the working files, source code, and an audit trail — not a black box.</p><div class="proof-grid" style="margin-top:24px"><div class="proof"><b>3</b><span>working case studies</span><p>Excel, PDF invoices, and meeting audio.</p></div><div class="proof"><b>20</b><span>automated tests total</span><p>6 + 8 + 6 across the demos.</p></div><div class="proof"><b>Source</b><span>included</span><p>Repeatable scripts and README files.</p></div></div><p class="note" style="margin-top:24px">No off-platform payment or contact. Use the platform where we connected. Independent demos. Synthetic data and audio only.</p></div>
"""
    return page("Boyi Automation — Profile Overview", body, PRINT_CSS)


def og_html() -> str:
    body = """<div style="box-sizing:border-box;width:1200px;height:630px;background:#0B1220;color:#fff;padding:58px 64px;position:relative;overflow:hidden;font-family:'Segoe UI',Arial,sans-serif"><div style="position:absolute;right:-100px;top:-120px;width:420px;height:420px;border-radius:50%;border:1px solid rgba(183,243,74,.3);box-shadow:0 0 0 44px rgba(183,243,74,.05),0 0 0 88px rgba(183,243,74,.035)"></div><div style="font-size:14px;letter-spacing:.16em;text-transform:uppercase;color:#B7F34A;font-weight:800">● BOYI AUTOMATION</div><div style="font-size:64px;line-height:1.02;letter-spacing:-.05em;font-weight:800;margin-top:34px">Messy input.<br><span style="color:#B7F34A">Clean output.</span></div><div style="font-size:23px;color:#C8D0DD;margin-top:18px;max-width:900px">Three working automation case studies: spreadsheets, invoices, and meetings.</div><div style="display:flex;gap:12px;margin-top:36px"><div style="background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);border-radius:14px;padding:14px 18px"><b style="display:block;color:#B7F34A;font-size:24px">1,206</b><span style="color:#AAB5C4;font-size:11px;text-transform:uppercase;letter-spacing:.08em">rows cleaned</span></div><div style="background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);border-radius:14px;padding:14px 18px"><b style="display:block;color:#B7F34A;font-size:24px">48</b><span style="color:#AAB5C4;font-size:11px;text-transform:uppercase;letter-spacing:.08em">PDFs processed</span></div><div style="background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);border-radius:14px;padding:14px 18px"><b style="display:block;color:#B7F34A;font-size:24px">13</b><span style="color:#AAB5C4;font-size:11px;text-transform:uppercase;letter-spacing:.08em">action items</span></div><div style="background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);border-radius:14px;padding:14px 18px"><b style="display:block;color:#B7F34A;font-size:24px">20</b><span style="color:#AAB5C4;font-size:11px;text-transform:uppercase;letter-spacing:.08em">tests passed</span></div></div><div style="position:absolute;left:64px;bottom:42px;color:#AAB5C4;font-size:13px">Independent demos · synthetic data · source included</div></div>"""
    return page("OG Image", body, "body{margin:0}")




def avatar_html() -> str:
    body = """<div style="box-sizing:border-box;width:800px;height:800px;background:#0B1220;color:#fff;padding:54px;position:relative;overflow:hidden;font-family:'Segoe UI',Arial,sans-serif"><div style="position:absolute;right:-120px;top:-120px;width:520px;height:520px;border-radius:50%;border:1px solid rgba(183,243,74,.3);box-shadow:0 0 0 44px rgba(183,243,74,.05),0 0 0 88px rgba(183,243,74,.035)"></div><div style="font-size:18px;letter-spacing:.16em;text-transform:uppercase;color:#B7F34A;font-weight:800">● BOYI AUTOMATION</div><div style="margin-top:190px;font-size:220px;line-height:.9;letter-spacing:-.08em;font-weight:900">B<span style="color:#B7F34A">A</span></div><div style="font-size:26px;color:#C8D0DD;margin-top:26px">Messy input → clean output.</div><div style="position:absolute;left:54px;bottom:48px;color:#AAB5C4;font-size:16px">Independent demos · synthetic data</div></div>"""
    return page("Boyi Automation avatar", body, "body{margin:0}")


def banner_html() -> str:
    body = """<div style="box-sizing:border-box;width:1600px;height:900px;background:#0B1220;color:#fff;padding:70px 86px;position:relative;overflow:hidden;font-family:'Segoe UI',Arial,sans-serif"><div style="position:absolute;right:-150px;top:-150px;width:620px;height:620px;border-radius:50%;border:1px solid rgba(183,243,74,.3);box-shadow:0 0 0 50px rgba(183,243,74,.05),0 0 0 100px rgba(183,243,74,.035)"></div><div style="font-size:20px;letter-spacing:.16em;text-transform:uppercase;color:#B7F34A;font-weight:800">● BOYI AUTOMATION</div><div style="font-size:88px;line-height:1.02;letter-spacing:-.055em;font-weight:900;margin-top:70px">Messy input.<br><span style="color:#B7F34A">Clean output.</span></div><div style="font-size:30px;color:#C8D0DD;margin-top:24px;max-width:1200px">AI-assisted automation for spreadsheets, invoices, and meeting notes.</div><div style="display:flex;gap:16px;margin-top:54px"><div style="border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.06);border-radius:16px;padding:18px 22px;font-size:20px">Excel reporting</div><div style="border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.06);border-radius:16px;padding:18px 22px;font-size:20px">PDF extraction</div><div style="border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.06);border-radius:16px;padding:18px 22px;font-size:20px">Meeting notes + SRT</div></div><div style="position:absolute;left:86px;bottom:56px;color:#AAB5C4;font-size:18px">Independent demos · synthetic data · source included</div></div>"""
    return page("Boyi Automation banner", body, "body{margin:0}")

def chrome_screenshot(html_path: Path, png_path: Path, width: int, height: int) -> None:
    profile = BUILD / "chrome-profile"
    cmd = [str(CHROME), "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-sandbox", f"--user-data-dir={profile}", f"--window-size={width},{height}", f"--screenshot={png_path}", html_path.as_uri()]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)


def chrome_pdf(html_path: Path, pdf_path: Path) -> None:
    profile = BUILD / "chrome-pdf-profile"
    cmd = [str(CHROME), "--headless=new", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer", f"--user-data-dir={profile}", f"--print-to-pdf={pdf_path}", html_path.as_uri()]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=90)


def main() -> None:
    (DOCS / "index.html").write_text(index_html(), encoding="utf-8")
    (DOCS / "profile.html").write_text(profile_html(), encoding="utf-8")
    print_path = DOCS / "profile-print.html"
    print_path.write_text(profile_print_html(), encoding="utf-8")
    og_path = BUILD / "og.html"
    og_path.write_text(og_html(), encoding="utf-8")
    chrome_screenshot(og_path, ASSETS / "og-image.png", 1200, 630)
    avatar_path = BUILD / "avatar.html"
    avatar_path.write_text(avatar_html(), encoding="utf-8")
    chrome_screenshot(avatar_path, ASSETS / "avatar.png", 800, 800)
    banner_path = BUILD / "banner.html"
    banner_path.write_text(banner_html(), encoding="utf-8")
    chrome_screenshot(banner_path, ASSETS / "profile-banner.png", 1600, 900)
    chrome_pdf(print_path, DOCS / "downloads" / "boyi-automation-profile.pdf")
    print("hub built")


if __name__ == "__main__":
    main()
