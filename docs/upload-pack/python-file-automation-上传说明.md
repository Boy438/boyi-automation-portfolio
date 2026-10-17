# Python 文件与文件夹自动化 — 上传说明

> 这是第 4 套证明包。定位：**Messy folder → clean, auditable output**。  
> 独立演示，全部使用合成文件；不要写成真实客户案例。

## 一、素材位置

| 素材 | 文件 |
|---|---|
| 案例页 | `docs/cases/python-file-automation/index.html` |
| 4 页 PDF | `docs/downloads/python-automation-case-study.pdf` |
| Fiverr 主图 | `docs/cases/python-file-automation/assets/gig-01-cover.png` |
| Fiverr 第二张 | `docs/cases/python-file-automation/assets/gig-02-before-after.png` |
| Fiverr 第三张 | `docs/cases/python-file-automation/assets/gig-03-workflow.png` |
| Contra 封面 | `docs/cases/python-file-automation/assets/contra-cover.png` |
| 80 秒视频 | `docs/cases/python-file-automation/assets/demo.mp4` |
| 视频预览 GIF | `docs/cases/python-file-automation/assets/demo-preview.gif` |
| 样例输入 | `docs/cases/python-file-automation/sample/messy_inbox_sample.zip` |
| Excel 报告 | `docs/cases/python-file-automation/sample/file_inbox_report.xlsx` |
| 清单 / 异常 / 计划 | `sample/manifest.csv`、`exceptions.csv`、`organize_plan.csv` |
| 运行指标 | `sample/run_summary.json` |

## 二、Contra 上传

1. 新建 Project：**Messy File Inbox → Clean, Auditable Folder**
2. 简介直接复制 `python-file-automation-contra-project.md`
3. 上传 Contra 封面 `contra-cover.png`
4. 作品链接填案例页
5. 附件上传 4 页 PDF、`file_inbox_report.xlsx`、`manifest.csv`、`exceptions.csv`
6. 标注：**Independent demo — synthetic files. Not a client case study.**
7. 新建 Service：**Python File & Folder Automation — from $250**
8. 服务范围写死：
   - 1 个文件夹 / 1 套命名规则
   - Basic 审计最多 50 个文件
   - CSV / JSON / TXT / typed PDF
   - 默认 dry run，不删除源文件
   - 不接账号密码 / 无人值守访问

## 三、Fiverr 上传

### Gig 标题

`I will build a Python automation to organize and clean your files`

### 套餐

| 套餐 | 价格 | 范围 |
|---|---:|---|
| Basic | $75 | 1 个文件夹，最多 50 个文件，dry-run 报告 |
| Standard | $150 | 最多 200 个文件，safe apply + Python 脚本 + README |
| Premium | $300 | 最多 2 个文件夹或 500 个文件，自定义规则 + 测试报告 |

### 图片顺序

1. `gig-01-cover.png` — 主图：Messy file inbox → clean, auditable folder
2. `gig-02-before-after.png` — 前后对比：重复、损坏、隔离
3. `gig-03-workflow.png` — 流程：Scan → Detect → Validate → Plan → Apply

### 视频

上传 `demo.mp4`，时长 80 秒，1600×900，H.264。

### 描述 / FAQ / 买家要求

直接复制 `python-file-automation-fiverr-gig.md`。不要添加站外联系方式或收款方式。

## 四、首单澄清问题

1. 一个代表性文件夹或 20–30 个文件
2. 你希望的目标命名规则
3. 重复文件怎么处理：跳过、保留、还是人工确认
4. 日期格式是月/日还是日/月
5. 运行环境：Windows、macOS、还是共享盘
6. 截止时间

## 五、交付前检查

- [ ] 先跑 dry run，检查 manifest 和 exceptions
- [ ] 确认源文件夹没有被修改
- [ ] 确认 organized / duplicates / quarantine 三个输出目录
- [ ] 确认 Excel 报告能打开
- [ ] 确认 README 和依赖列表
- [ ] 测试报告写明 10/10 通过
- [ ] 不承诺 100% 分类准确率
- [ ] 不接账号密码、不删除源文件、不做未授权抓取

## 六、不能写的话

- “100% accurate file classification”
- “Fully automatic, no review needed”
- “Deletes duplicates permanently”
- “Works on every PDF and every folder”
- “Send me your password / cloud account”

## 七、建议提案角度

> I can build a dry-run audit first: you review the manifest and exception log, then approve the safe copy plan. The source folder stays untouched. If the output matches your naming rule, we can turn it into a recurring monthly workflow.
