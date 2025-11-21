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

## Cascade simulator (experimental)

The repository contains an experimental cascade simulator that maps simple
signals into the public cascade range **1–23**.

**Core modules:**

- `src/core/signal_loader.py` – generate synthetic test signals and compute
  spectra (`time → freq, power`).
- `src/core/cascade_scale.py` – define the public cascade scale (1–23) as
  discrete levels with normalized positions in `[0, 1]`.
- `src/core/cascade_mapping.py` – project a spectrum into the cascade space:
  build a cascade weight vector and select a dominant cascade.

**Demo script:**

- `scripts/run_demo_simulator.py` – generates a simple sine-based signal,
  computes its spectrum, applies `map_dominant_cascade(...)` and prints:

  - the dominant cascade ID (1–23),
  - the confidence (fraction of total power),
  - top-5 cascades by weight.

Example run from the project root:

python -m scripts.run_demo_simulator


This module is experimental and works only within the public range 1–23.
It is intended for testing mappings between signals and the cascade scale,
not as a physical model of any specific object.

### Observation logs and simulated cascade annotation

For external events (e.g. 3I/ATLAS briefings) the project uses CSV logs
under `data/observations/`:

- `data/observations/3I_ATLAS_observations_template.csv` – example log
  with columns like `datetime_utc`, `source`, `channel`, `cascade_level`, `notes`.

These logs can be enriched with simulated cascade information (range 1–23)
using:

python -m scripts.annotate_observations_with_cascade


This script:

reads the input CSV,

generates a simple synthetic signal per row (based on the channel field),

runs the cascade simulator,

writes an output CSV with two extra columns:

sim_main_cascade – dominant cascade level (1–23),

sim_confidence – fraction of total spectral power assigned to this level.

This is an experimental tool for linking observation timelines to the
public cascade scale, not a physical model of any specific object.



## Jupyter notebook demo

For interactive exploration there is a notebook:

- `notebooks/01_cascade_simulator_demo.ipynb`

The notebook walks through the same pipeline as the demo script, but with plots:

1. Generate a synthetic signal (sum of a few sines with noise).
2. Compute its spectrum (`freq`, `power`).
3. Load the public cascade scale 1–23 (`get_public_scale()`).
4. Apply `map_dominant_cascade(...)` to obtain:
   - the dominant cascade ID,
   - the confidence (fraction of total power),
   - the full cascade weight vector.
5. Visualize:
   - time-domain signal,
   - power spectrum,
   - cascade weight vector over levels 1–23.

To run the notebook:

cd <project-root>
jupyter notebook notebooks/01_cascade_simulator_demo.ipynb


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
