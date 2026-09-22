# SciTeX Plt (<code>scitex-plt</code>)

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-banner.png" alt="SciTeX Plt" width="400">
  </a>
</p>

<p align="center"><b>Publication-ready plotting with auto CSV export — sys.modules alias for figrecipe</b></p>

<p align="center">
  <a href="https://scitex-plt.readthedocs.io/">Full Documentation</a> · <code>uv pip install scitex-plt[all]</code>
</p>

<!-- scitex-badges:start -->
<p align="center">
  <a href="https://pypi.org/project/scitex-plt/"><img src="https://img.shields.io/pypi/v/scitex-plt?label=pypi" alt="pypi"></a>
  <a href="https://pypi.org/project/scitex-plt/"><img src="https://img.shields.io/pypi/pyversions/scitex-plt?label=python" alt="python"></a>
  <a href="https://scitex-plt.readthedocs.io/en/latest/"><img src="https://img.shields.io/readthedocs/scitex-plt?label=docs" alt="docs"></a>
</p>
<p align="center">
  <a href="https://github.com/scitex-ai/scitex-plt/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/scitex-ai/scitex-plt/ci.yml?branch=develop&label=tests" alt="tests"></a>
  <a href="https://github.com/scitex-ai/scitex-plt/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/scitex-ai/scitex-plt/ci.yml?branch=develop&label=install-check" alt="install-check"></a>
  <a href="https://github.com/scitex-ai/scitex-plt/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/scitex-ai/scitex-plt/ci.yml?branch=develop&label=quality" alt="quality"></a>
  <a href="https://codecov.io/gh/scitex-ai/scitex-plt"><img src="https://img.shields.io/codecov/c/github/scitex-ai/scitex-plt/develop?label=cov" alt="cov"></a>
</p>
<!-- scitex-badges:end -->

---

## Problem and Solution

| # | Problem | Solution |
|---|---------|----------|
| 1 | **Matplotlib boilerplate for publication figures** — manually setting DPI, fonts, axis labels, CSV sidecars, and mm-precision layout for every paper figure | **`stx.plt.subplots()`** — thin wrapper around figrecipe returning a tracked axes with `.plot_line(...)`, `set_xyt(...)`, and publication-ready defaults |
| 2 | **Figure and underlying data drift apart** — the PNG lives in the repo, the CSV that generated it sits in a notebook cell and eventually disappears | **Auto CSV export on save** — `stx.io.save(fig, "plot.png")` writes `plot.png` + `plot.csv` + `plot.yaml` atomically so the data is always reproducible |
| 3 | **No agent figure API** — coding agents need a structured API, not matplotlib's stateful pyplot | **MCP figure tools** — agents compose publication plots from CSVs via `plt_line`, `plt_scatter`, and `plt_stx_*` column specs, no inline arrays needed |

## Quick Start

```python
import scitex_plt as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
plt.save(fig, "figure.png")  # writes figure.png + figure.csv
```

## Demo

```mermaid
flowchart LR
    data[("session.csv")] --> load["stx.io.load"]
    load --> arr["NumPy / DataFrame"]
    arr --> ax["ax.plot_line(...)\nax.set_xyt(...)"]
    ax --> fig["fig"]
    fig --> savefig["stx.io.save(fig, 'plot.png')"]
    savefig --> png[("plot.png")]
    savefig --> sidecar[("plot.csv\nplot.yaml")]
```

<p align="center"><sub><b>Figure 1.</b> CSV-to-figure pipeline: load data, compose the plot from column specs, and save the figure with its data sidecars.</sub></p>

## Installation

```bash
uv pip install "scitex-plt[all]"
```

Through the umbrella: `uv pip install "scitex[plt]"`. Requires Python ≥ 3.10.

<details>
<summary><b>Per-extra installs</b></summary>

<br>

| Extra | Pulls in |
|---|---|
| `dev` | `pytest`, `pytest-cov`, `ruff`, `scitex-dev` |
| `docs` | `sphinx`, `sphinx-rtd-theme`, `myst-parser`, `sphinx-copybutton`, `sphinx-autodoc-typehints` |

</details>

This installs `figrecipe` as a dependency. `scitex-plt` is a `sys.modules` alias:
`scitex_plt is figrecipe` evaluates to `True` after import.

## Architecture

```mermaid
flowchart LR
    user["user code\nimport scitex_plt as plt"] -->|"sys.modules alias"| fr["figrecipe\n(actual implementation)"]
    fr --> mpl["matplotlib"]
    fr --> save["stx.io.save(fig, 'plot.png')"]
    save --> png[("plot.png")]
    save --> csv[("plot.csv\n(auto-tracked data)")]
    save --> yaml[("plot.yaml\n(recipe / params)")]
```

<p align="center"><sub><b>Figure 2.</b> Alias architecture: <code>scitex_plt</code> resolves to figrecipe, which renders via matplotlib and persists figure plus data sidecars.</sub></p>

## 4 Interfaces

`scitex-plt` exposes the same four-interface surface as the rest of the SciTeX
ecosystem (delegated to figrecipe):

<details open>
<summary><b>Python API</b> — <code>import scitex_plt as plt</code></summary>

```python
import scitex_plt as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
plt.save(fig, "figure.png")  # writes figure.png + figure.csv
```

</details>

<details>
<summary><b>CLI</b> — <code>scitex-plt --help</code></summary>

```bash
scitex-plt --help
scitex-plt info
```

</details>

<details>
<summary><b>MCP tools</b> — <code>plt_*</code> namespace</summary>

AI agents call `plt_line`, `plt_scatter`, `plt_stx_*` etc. from CSV column specs.

</details>

<details>
<summary><b>Skills</b> — <code>figrecipe</code> skill loaded by agents at startup</summary>

Loaded automatically by SciTeX-aware agents.

</details>

## Part of SciTeX

> `scitex-plt` is part of [**SciTeX**](https://scitex.ai). Install via
> the umbrella with `pip install scitex[plt]` to use as
> `scitex.plt` (Python) or `scitex plt ...` (CLI).

`scitex-plt` is the namespace alias for
[figrecipe](https://github.com/ywatanabe1989/figrecipe), used by sibling
packages such as `scitex-stats`, `scitex-io`, and `scitex-clew`.

```python
import scitex as stx
stx.plt.subplots()        # routed through scitex.plt → figrecipe
```
```bash
scitex plt --help         # umbrella subcommand
```

The SciTeX system follows the Four Freedoms for Research below, inspired by [the Free Software Definition](https://www.gnu.org/philosophy/free-sw.en.html):

>Four Freedoms for Research
>
>0. The freedom to **run** your research anywhere — your machine, your terms.
>1. The freedom to **study** how every step works — from raw data to final manuscript.
>2. The freedom to **redistribute** your workflows, not just your papers.
>3. The freedom to **modify** any module and share improvements with the community.
>
>AGPL-3.0 — because we believe research infrastructure deserves the same freedoms as the software it runs on.

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
</p>

<!-- EOF -->
