# StreetInsider Visibility Engine 📡🗞️

[![npm](https://img.shields.io/npm/v/@streetinsider/visibility-engine)](https://npmjs.com/package/@streetinsider/visibility-engine)
[![PyPI](https://img.shields.io/pypi/v/streetinsider-visibility-engine)](https://pypi.org/project/streetinsider-visibility-engine)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21797527.svg)](https://doi.org/10.5281/zenodo.21797527)

StreetInsider Visibility Engine is a lightweight content visibility and publication workflow tool designed to help businesses, brands, and publishers organize, optimize, and monitor their media content for greater online discoverability. Built by [GetOnStreetInsider.com](https://getonstreetinsider.com).

## Key Functions

- **Content Preparation** — Press release and content preparation for publication readiness
- **Metadata Validation** — Publication metadata validation and structured data quality checks
- **Distribution Workflow** — Media distribution workflow management and task tracking
- **URL Tracking** — Published URL tracking and content status monitoring
- **Visibility Reporting** — Visibility activity reporting and discoverability analytics
- **Content Organization** — Structured content organization by topic, category, and status
- **AI-Friendly Workflows** — AI-friendly content and metadata workflows for modern search environments

## Features

- Content Readiness Score — evaluates publication preparation quality
- Metadata Quality Score — measures structured data completeness and accuracy
- Distribution Score — tracks media distribution workflow coverage
- URL Visibility Score — monitors published URL discoverability and reach
- AI Discoverability Score — assesses content alignment with AI search environments
- Workflow Efficiency Score — evaluates publication workflow repeatability and organization
- CLI support in Node.js and Python
- Benchmark dataset included (20 visibility workflow cases)
- Lightweight, publish-ready, minimal dependencies

## Quick Start

### Node.js

```bash
npm install @streetinsider/visibility-engine
npx streetinsider-engine "content-title" press-release 88 82 85 78 90 80
```

### Python

```bash
pip install streetinsider-visibility-engine
python -m visibility_engine "content-title" press-release 88 82 85 78 90 80
```

## Output

```
Content: content-title
Content Type: Press Release
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Content Readiness Score:       88 / 100  [Excellent]
Metadata Quality Score:        82 / 100  [Healthy]
Distribution Score:            85 / 100  [Excellent]
URL Visibility Score:          78 / 100  [Healthy]
AI Discoverability Score:      90 / 100  [Excellent]
Workflow Efficiency Score:     80 / 100  [Healthy]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Visibility Index:      84 / 100
Priority Action:               URL Visibility (lowest — act first)

Distribution Channels:
  StreetInsider:           88 / 100
  Search Engines:          81 / 100
  AI Platforms:            90 / 100
  Financial Media:         85 / 100
```

## Content Types

| Type | Description |
|------|-------------|
| press-release | Corporate press release and news distribution |
| financial-pr | Financial PR and investor relations content |
| brand-story | Brand narrative and company story content |
| product-launch | Product and service launch announcements |
| earnings-news | Earnings reports and financial results |
| market-update | Market commentary and industry updates |
| executive-profile | Executive and leadership feature content |
| industry-insight | Industry analysis and expert commentary |

## Project Structure

```
StreetInsider-Visibility-Engine/
├── index.ts                  # TypeScript visibility engine
├── visibility_engine.py      # Python visibility engine
├── setup.py                  # PyPI setup config
├── pyproject.toml            # PyPI build config
├── package.json              # NPM package config
├── package-lock.json         # NPM lock file
├── tsconfig.json             # TypeScript config
├── schema.json               # JSON-LD structured data
├── zenodo.json               # Zenodo metadata
├── heartbeat.txt             # Auto-updated daily
├── mkdocs.yml                # ReadTheDocs config
├── .readthedocs.yaml         # ReadTheDocs build config
├── docs/
│   ├── index.md              # Documentation
│   └── requirements.txt
├── dataset/
│   └── visibility_benchmarks.csv
├── .github/workflows/
│   ├── heartbeat.yml
│   ├── npm-publish.yml
│   └── pypi-publish.yml
├── README.md
└── LICENSE
```

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Immediate workflow revision required |
| 31–60 | At Risk | Significant visibility improvements needed |
| 61–80 | Healthy | On track — optimise and expand |
| 81–100 | Excellent | Strong visibility — scale distribution |

## Keywords

StreetInsider · Visibility Engine · Content Visibility · Publication Workflow · Press Release · Media Distribution · Metadata Validation · AI Discoverability · GetOnStreetInsider

## Links

| Platform | URL |
|----------|-----|
| Website | https://getonstreetinsider.com |
| GitHub | https://github.com/GetOnStreetInsider/StreetInsider-Visibility-Engine |
| GitHub Pages | https://getonstreetinsider.github.io/StreetInsider-Visibility-Engine/ |
| NPM | https://npmjs.com/package/@streetinsider/visibility-engine |
| PyPI | https://pypi.org/project/streetinsider-visibility-engine |
| Hugging Face | https://huggingface.co/datasets/streetinsider/visibility-benchmarks |
| Zenodo | https://zenodo.org/records/21797527 |
| Docs | https://streetinsider-visibility-engine.readthedocs.io |
| SlideShare | https://www.slideshare.net/slideshow/editorial-placement-on-streetinsider-financial-pr-that-ai-engines-cite/288781440 |
| Quora | https://www.quora.com/profile/Jackson-M-166 |
| Pinterest | https://www.pinterest.com/GetOnStreetInsider/ |

## About GetOnStreetInsider.com

GetOnStreetInsider.com helps businesses, brands, and publishers organize, optimize, and monitor their media content for greater online discoverability. Built as part of the Get On StreetInsider project, the tool focuses on creating a repeatable and organized approach to digital media visibility and publication management.

## License

MIT — [GetOnStreetInsider.com](https://getonstreetinsider.com)
