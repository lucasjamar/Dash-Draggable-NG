# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-10-05

First release of **`dash-draggable-ng`**, a modernized, Python-only fork of
[`dash-draggable`](https://github.com/MehdiChelh/dash-draggable) by Mehdi Echchelh.
The import name is unchanged (`import dash_draggable`), so it is a drop-in
replacement; only the PyPI distribution name differs.

### Changed
- Upgraded the JS build toolchain to **webpack 5** (from 4), **webpack-cli 5**,
  and replaced the deprecated `webpack-serve` with **webpack-dev-server**.
- Targeted **React 18.3** (from 16.8) to align with the React version bundled by
  Dash 4.
- Bumped **react-grid-layout 1.2 → 1.5**.
- Updated loaders: **css-loader 3 → 6**, **style-loader 0.23 → 3**;
  **babel-loader 8 → 9**.
- Updated **react-docgen 4 → 5.4.3** for Dash component generation.
- Regenerated the Python component wrappers with **Dash 4** (typed signatures).
- Modernized `usage.py` and all examples to the current Dash API
  (`from dash import Input, Output, dcc, html`, `app.run(...)`).
- Migrated Python packaging to **`pyproject.toml`** (PEP 517, setuptools backend);
  the project now builds and publishes with **uv** (`uv build` / `uv publish`).
- Regenerated `package-lock.json`.

### Fixed
- Replaced the deprecated **`componentWillMount`** lifecycle with a `constructor`
  in `GridLayout`, `ResponsiveGridLayout`, `DraggableDashboard`, and
  `DraggableDashboardResponsive` (safe under React 18 StrictMode).
- Removed leftover `console.log` debug statements from `ResponsiveGridLayout`.

### Removed
- Dropped the unused **`styled-jsx`** dependency.
- Removed the **R and Julia** bindings and their generated artifacts; this fork
  is Python-only.
- Cleaned stale generated files and old `webpack-serve` HMR bundles.

### Components
No components were added or removed. The library still ships the six components:
`GridLayout`, `ResponsiveGridLayout`, `DraggableDashboard`,
`DraggableDashboardResponsive`, `DashboardItem`, and `DashboardItemResponsive`.

## Earlier history

Versions 0.0.x–0.1.x were released by the upstream project
[`MehdiChelh/dash-draggable`](https://github.com/MehdiChelh/dash-draggable)
under the PyPI name `dash-draggable`.

[0.2.0]: https://github.com/lucasjamar/Dash-Draggable-NG/releases/tag/v0.2.0
