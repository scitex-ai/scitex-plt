---
description: |
  [TOPIC] Installation
  [DETAILS] pip install scitex-plt — pulls figrecipe automatically. The package is a thin namespace alias for figrecipe.
tags: [scitex-plt-installation]
---

# Installation

## Standard

```bash
pip install scitex-plt
```

Pulls `figrecipe>=0.24.0` and `pandas`. `scitex-plt` is a `sys.modules`
alias — `scitex_plt is figrecipe` evaluates to `True`.

## Verify

```bash
python -c "import scitex_plt; print(scitex_plt.__version__)"
python -c "import scitex_plt as plt; fig, ax = plt.subplots(); print('ok')"
scitex-plt --version
```

## Editable install (development)

```bash
git clone https://github.com/scitex-ai/scitex-plt
cd scitex-plt
pip install -e '.[dev]'
```

## When `figrecipe` is missing

`scitex-plt` raises an explicit `ImportError` pointing at
`pip install figrecipe`.

## Where the real docs live

All API, plot-types, paper modes, MCP tools — see **figrecipe's**
`_skills/figrecipe/`.
