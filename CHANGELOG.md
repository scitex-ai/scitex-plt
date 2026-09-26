# Changelog

All notable changes to `scitex-plt` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.24.9]

### Fixed
- Bumped the `figrecipe` dependency floor `>=0.31.0` → `>=0.32.1`, so a fresh
  install cannot resolve a figrecipe that still has the heatmap-tick bug.
  figrecipe 0.32.1 fixes an `imshow` whose axis-chrome suppression was
  irreversible: it pinned a `NullFormatter` on the axis, so any tick the caller
  set *afterwards* rendered blank. A heatmap or spectrogram — whose x/y axes
  carry physical meaning — silently lost its tick numbers with no way to get
  them back. 0.32.0 also adds `figrecipe.StatResult`, which builds a
  doctrine-complete statistical annotation (n / CI / method / p / effect size /
  test statistic, italic symbols) instead of making the caller hand-type the
  mathtext.

## [0.24.8]

### Fixed
- Bumped the `figrecipe` dependency floor `>=0.30.0` → `>=0.31.0`. figrecipe
  0.31.0 fixes a 500 on the GUI's `/api/files` endpoint: a symlinked file
  escaping the project root (e.g. `node_modules/@scitex/ui`) made the backend
  correctly refuse the read, but the file-tree walker didn't catch that and
  took down the entire tree — so `scitex-plt gui serve` rendered but its file
  browser was dead. 0.31.0 also fixes `imshow` tick labels being dropped on
  record/replay, and adds the `comma_format` tick formatter and the
  `ax.stx_annotate_n()` sample-size annotation helper.

## [0.24.7]

### Fixed
- Bumped the `figrecipe` dependency floor `>=0.24.0` → `>=0.30.0`. figrecipe
  0.30.0 is the first release carrying the `gui` command GROUP (`open`/
  `serve`/`status`/`stop`) that `scitex-plt gui serve` requires — a fresh
  install on the old floor could still resolve an older figrecipe lacking
  the group entirely, breaking `scitex-plt gui serve` at runtime
  (`'serve'` was read as a positional SOURCE path, not a subcommand).

## [0.24.4]

- Initial CHANGELOG entry — see git log for prior history.
