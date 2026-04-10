# research_codex
AI-assisted literature workflow based on codex
# Research Codex Lite

一个用于文献探索的小型工作流模板，适合公开到 GitHub 作为基础版仓库。

这个版本刻意保持轻量：
- 保留核心流程和目录结构
- 提供基础模板
- 不包含实际项目产出、已整理好的文献数据或成熟提示词
- 不包含针对某一研究方向深度优化过的细节

## Core Workflow

Search -> Filter -> Download -> Extract -> Synthesize

## Folder Structure

```text
research-codex-lite/
├── AGENTS.md
├── README.md
├── literature/
│   ├── notes/
│   └── pdfs/
├── output/
├── scripts/
│   └── download_open_access_pdf.py
└── templates/
    ├── final_summary_template.md
    └── paper_extraction_template.md
```

## Suggested Use

1. 选定一个研究主题。
2. 在 PubMed、CrossRef、arXiv 等数据库中搜索候选文献。
3. 初筛并记录高相关论文。
4. 下载开放获取文献，保存到 `literature/pdfs/`。
5. 按模板提取每篇论文的信息。
6. 在 `output/` 中汇总研究方向、机制、模型和局限性。

## Notes

- 这是一个公开版骨架，不是完整生产版本。
- 更适合展示方法，而不是直接复现完整研究流程。
- 如果要做长期项目，建议你在私有仓库里继续维护自己的强化版提示词和经验。
