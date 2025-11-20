# 3I-ATLAS Cascade Lab

Early-stage citizen-science lab dedicated to the interstellar comet **3I/ATLAS**.

This repository is not an official NASA project.  
It is my personal workspace for:

- tracking public updates and data products from NASA and other teams;
- collecting **structured observations** (sky photos, notes, time/location metadata);
- building **cascade-style models** and physics/AI notebooks around 3I/ATLAS.

The goal is simple: use code and careful notes as a bridge between
public information and independent analysis, in the spirit of
citizen scientists who have historically contributed to many NASA discoveries.

---

## Repository layout

- `docs/`
  - `Overview_EN.md` — high-level description of the lab and its goals.
  - `logbook_3I_ATLAS.md` — chronological log of NASA events, data releases, and key references.
  - `cascade_notes.md` — text notes and sketches of cascade models related to 3I/ATLAS.

- `data/`
  - `raw/nasa/` — official data products as downloaded (FITS, CSV, etc.), without modification.
  - `processed/` — cleaned / resampled / combined datasets used in notebooks.
  - `sky_notes/`
    - `obs_log.csv` — structured table of personal observations (date, time, location, description, file id).
    - `images/` — photos corresponding to entries in `obs_log.csv`.

- `notebooks/`
  - `01_briefing_3I_ATLAS.md` — initial briefing: what is known about 3I/ATLAS, key parameters, links.
  - `02_cascade_patterns.md` — first ideas and visualisations for cascade-style behaviour and timelines.

- project meta:
  - `CHANGELOG.md` — history of changes in the lab.
  - `requirements*.txt` — Python dependencies for future analysis notebooks.
  - `pytest.ini` — reserved for simple tests once code appears.
  - `LICENSE` — MIT license.
  - `.gitignore` — ignore virtualenvs, caches, and large generated files.

---

## Status

This lab is currently in **v0.1.0 – scaffolding only**:

- no real data yet,
- no final models,
- only structure, logbook template and observation formats.

As NASA and partner teams publish more information and data on 3I/ATLAS,
I plan to:

1. keep the logbook up to date,
2. add structured sky observations when relevant,
3. build several physics- and AI-inspired cascade models and publish
   the notebooks here.

---

## License

MIT — see `LICENSE` for details.
