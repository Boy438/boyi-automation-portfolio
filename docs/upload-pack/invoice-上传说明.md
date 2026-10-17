# PDF 发票提取：上传说明

> 这是 2 号作品「PDF 发票 → 结构化 Excel」的完整证明包。所有 PDF 和字段都是合成数据，页面和文案都标注 **Independent demo — synthetic data**，没有编造客户名、logo 或好评。

## 一、先看哪里

1. `case-study.html`：交互案例页，可直接给客户看。
2. `pdf/case-study.pdf`：4 页英文案例。
3. `video/demo.mp4`：80 秒英文演示，无配音、有字幕。
4. `images/`：3 张 Fiverr 图 + 1 张 Contra 封面。
5. `copy/`：Fiverr/Contra 文案、提案模板、上传清单、样例 PDF 和输出。

## 二、Fiverr 怎么上传

1. 新建 gig，标题：
   `I will extract invoice data from PDF into a clean Excel or CSV file`
2. 主图：`images/gig-01-cover.png`
3. 第 2 张：`images/gig-02-before-after.png`
4. 第 3 张：`images/gig-03-workflow.png`
5. 视频：`video/demo.mp4`
6. 描述复制 `copy/fiverr-gig.md` 的 **Gig description**。
7. 套餐：**$65 / $150 / $320**；交付 **2 / 3 / 5 天**；修改 **1 / 2 / 3 次**。
8. 标签：`invoice`、`pdf to excel`、`data extraction`、`excel`、`data entry`。
9. Portfolio 放 `pdf/case-study.pdf`、`copy/invoices_clean.csv`、`copy/line_items_clean.csv`、`copy/exceptions.csv`、`copy/extracted_invoices.xlsx`。
10. Fiverr 描述里不要放站外联系方式、收款方式或导流链接。

## 三、Contra 怎么上传

1. 新建 Project，标题：
   `PDF Invoices → Validated Excel Data`
2. 封面：`images/contra-cover.png`
3. 项目描述复制 `copy/contra-project.md`。
4. 附上 `case-study.html` 的在线链接（GitHub Pages 开通后）。
5. 附上 GitHub 仓库、样例 PDF 和输出文件。
6. 明确写：`Independent demo — synthetic data`。
7. 新建 Service：
   `PDF Invoice to Excel / CSV Extraction — from $150`
8. 每天投 3 个定制提案，模板在 `copy/contra-project.md` 的 **Proposal template**。
9. 提案必须引用对方的具体需求，并附一个相关作品链接。

## 四、GitHub Pages 怎么开

1. 在 GitHub 新建仓库，把 `D:\FreelanceWorkbench\03_projects\invoice-extraction-flagship` 推上去。
2. Settings → Pages → Source 选 `Deploy from a branch`。
3. Branch 选 `main`，Folder 选 `/docs`。
4. 等 1–2 分钟，访问：
   `https://<你的用户名>.github.io/<仓库名>/`
5. 检查页面、Run extraction 按钮、三个下载按钮、PDF 预览图是否正常。
6. 把链接放到 Contra 项目页和 profile。

## 五、第一单策略

- 前 3 单不要打价格战，Basic 保持 $65，保证是完整小结果。
- 先让客户发 1–3 个样例 PDF，确认是 typed PDF 再做。
- 交付时多送一个 CSV 或 Excel 格式，但**不要和好评绑定**。
- 交付后只做一次礼貌评价请求，不用折扣/赠品换评价。
- 第 3 个真实评价后，统一涨价 25%–30%。
- 遇到扫描件、手写件、低质量照片，先说明需要 OCR，单独报价，不要硬接。

## 六、不要做的事

- 不要承诺“100% accuracy”。
- 不要把 scanned PDF 说成能自动识别；先标记 `no_text_layer`。
- 不要编客户案例、假 logo、假评价。
- 不要在 Fiverr 描述里放站外链接或收款方式。
- 不要把 demo 说成真实客户项目。写 Independent demo 反而更可信。

## 七、文件对应表

| 文件 | 用途 |
|---|---|
| `images/gig-01-cover.png` | Fiverr 主图 |
| `images/gig-02-before-after.png` | Fiverr 第 2 张 |
| `images/gig-03-workflow.png` | Fiverr 第 3 张 |
| `images/contra-cover.png` | Contra 封面 |
| `video/demo.mp4` | Fiverr 视频 / Contra 附件 |
| `pdf/case-study.pdf` | 4 页英文案例 |
| `case-study.html` | 交互案例页 |
| `copy/fiverr-gig.md` | Fiverr 全量文案 |
| `copy/contra-project.md` | Contra 项目文案和提案模板 |
| `copy/upload-checklist.md` | 上传勾选清单 |
| `copy/benchmark.md` | 可验证的 demo 指标 |
| `copy/extracted_invoices.xlsx` | 实际生成的 Excel 工作簿 |
| `copy/invoices_clean.csv` | 清洗后发票表 |
| `copy/line_items_clean.csv` | 行项目表 |
| `copy/exceptions.csv` | 异常日志 |
| `copy/invoice-001.pdf` | 正常样例发票 |
| `copy/invoice-037.pdf` | 扫描件样例 |
| `copy/invoice-042.pdf` | total mismatch 样例 |
| `copy/invoice-045.pdf` | 歧义日期样例 |
