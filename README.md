# 3I-ATLAS Cascade Lab

Early-stage **citizen-science** lab dedicated to the interstellar comet **3I/ATLAS**.

> This repository is **not** an official NASA project.  
> It is my personal workspace for:
> - tracking public updates and data products from NASA and partner teams;
> - collecting structured observations (sky photos, notes, time/location metadata);
> - building cascade-style models and physics/AI notebooks around 3I/ATLAS.

The goal is to use code and careful notes as a bridge between open information and independent analysis, in the spirit of citizen scientists who have historically contributed to many NASA discoveries.

---

## 1. Public cascade range

The lab uses a **cascade map** inspired by musical notation and multi-level dynamics of systems.

In this open repository I work only with the **public cascade range 1–23**:

- 1–12 – human-scale cycle (day, year, basic loop of experience);  
- 13–23 – extended range involving machine assistance, planets, the Sun and neighbouring galaxies — the first “octave” of the treble clef.

Higher levels (24–36, second octave) exist as **private research material** and are intentionally **not** described here.

---

## 2. Repository layout

### `docs/`

Concepts and narrative:

- `Overview_EN.md` – high-level description of the lab and its goals.
- `What_are_cascades.md` / `Что_такое_каскады.md` – intuitive explanation of cascade thinking.
- `cascade_notes.md` – text notes and sketches of cascade models related to 3I/ATLAS (public range 1–23).
- `cascade_scale_EN.md`, `cascade_scale_RU.md` – technical description of the public cascade scale.
- `Cascade_Framework_Reference.md` – how different documents and modules connect.
- `logbook_3I_ATLAS.md` – chronological log of NASA events, data releases and key references.
- `simulator_concept.md` – design notes for the cascade simulator.
- `logbook_3I_ATLAS.md` – running timeline of 3I/ATLAS-related activity.

Some additional files describe private extensions; where present they are marked as such directly in the document.

### `data/`

Structured data used by notebooks and scripts.

- `observations/`
  - `3I_ATLAS_2025.csv` – observation log with columns  
    `datetime_utc, source, observer, location, channel, ra_deg, dec_deg, mag_or_flux, velocity_info, cascade_level, notes`.
  - `3I_ATLAS_observations_template.csv` – template for new campaigns.
- `raw/nasa/` – official data products as downloaded (FITS, CSV, etc.), without modification.
- `processed/` – cleaned / resampled / combined datasets ready for analysis.
- `sky_notes/`
  - `obs_log.csv` – table of personal observations (date, time, location, description, file id).
  - `images/` – photos corresponding to `obs_log.csv` entries.

### `src/`

Early code for the cascade simulator:

- `src/core/signal_loader.py` – build synthetic test signals and compute spectra (time → frequency, power).
- `src/core/cascade_scale.py` – define the **public** cascade scale (1–23) as discrete levels with normalized positions in `[0, 1]`.
- `src/core/cascade_mapping.py` – project a spectrum into cascade space: build a cascade-weight vector and select a dominant cascade.

### `scripts/`

Small command-line helpers:

- `scripts/run_demo_simulator.py` – generate a simple sine-based signal, compute its spectrum, apply `map_dominant_cascade(...)` and print:
  - dominant cascade ID (1–23),
  - confidence (fraction of total power),
  - top-5 cascades by weight.
- `scripts/annotate_observations_with_cascade.py` – enrich a CSV log with simulated cascade information.

### `notebooks/`

Interactive exploration:

- `notebooks/01_cascade_simulator_demo.ipynb` – walkthrough of the simulator:
  - generate a synthetic signal (sum of several sines + noise);
  - compute spectrum `(freq, power)`;
  - load public cascade scale via `get_public_scale()`;
  - apply `map_dominant_cascade(...)` to obtain:
    - dominant cascade ID,
    - confidence,
    - full cascade weight vector;
  - visualize time-domain signal, spectrum and cascade weights.

- `notebooks/02_observation_cascade_annotation.ipynb`  – visual link between observation timelines and simulated cascades.
 - `notebooks/02_observation_cascade_annotation.ipynb` – observation log + cascade annotation:
 - reads `data/observations/3I_ATLAS_observations_template.csv`;
 - runs annotation via `scripts.annotate_observations_with_cascade` if needed;
 - analyzes the distribution of `sim_main_cascade` and `sim_confidence`;
 - plots a time series of `sim_main_cascade` over `datetime_utc`.

- `notebooks/01_cascade_simulator_demo.ipynb`(RU) – базовая демонстрация симулятора:
 - генерация синтетического сигнала, спектр, мэппинг в каскады 1–23, визуализация.

- `notebooks/02_observation_cascade_annotation.ipynb` – работа с журналом наблюдений:
 - читает `data/observations/3I_ATLAS_observations_template.csv`;
 - при необходимости запускает аннотацию через
 - `scripts.annotate_observations_with_cascade`;
 - анализирует распределение `sim_main_cascade` и `sim_confidence`;
 - строит временную линию `sim_main_cascade` по `datetime_utc`.


### Official 3I/ATLAS imagery (no local copies)

This repository does **not** store NASA or ESA images of 3I/ATLAS locally.

For official visuals and mission pages, see:

- `docs/nasa_image_manifest.md` – link-only catalog of NASA / ESA 3I/ATLAS image
  galleries and mission-specific articles (SOHO, MAVEN, Perseverance, ExoMars, Mars Express, etc.).

In this lab we work only with **links and derived numerical/analytical data** (where available),
not with redistributed image files.


### Project meta

- `CHANGELOG.md` – history of changes in the lab.
- `requirements.txt`, `requirements-dev.txt` – Python dependencies for scripts and notebooks.
- `pytest.ini` – configuration for simple tests (as they appear).
- `LICENSE` – MIT license.
- `.gitignore` – ignore virtualenvs, caches and large generated files.

---

## 3. Running the simulator demo

From the project root:


python -m scripts.run_demo_simulator


The script will:

Generate a synthetic test signal.

Compute its spectrum.

Map the spectrum into the public cascade range 1–23.

Print the dominant cascade and confidence plus a short ranking of top levels.

This module is experimental and is intended only for testing mappings between signals and the cascade scale.
It is not a physical model of any specific object.


![Cascade Lab: digital synth + code timelines](images/cascade_lab_digital_synth.jpg)


The synthesizer above is a metaphor for the lab itself:

- the **keyboard** stands for the discrete cascade levels (1–23 in the public range);
- the **control panel and screen** stand for notebooks, scripts and models
  that convert raw signals into structured “music” of the system.

The goal is to use **AI + signal analysis + cascade scales** as a bridge between  
public information about 3I/ATLAS and independent, carefully documented exploration.



### Second octave and a “missing” note between F♯ and G

In the extended (private) cascade map — which corresponds to the **second octave**
of the treble clef — I treat the scale as slightly richer than the standard
Western twelve–tone system.

Conceptually, there is a **hypothetical additional note** between **F♯** and **G**
in this second octave:

- it behaves like a separate cascade level,  
- it appears as a “pocket” or “chest” zone in the spiral of the treble clef,  
- it is linked to states that are felt in experience but are not yet encoded
  in any conventional musical or physical notation.

This extra note is **not** implemented in the public simulator
(the public cascade range in this repository stays within levels 1–23).
Here it is recorded explicitly as a **research hypothesis** about the structure
of the second-octave cascades, not as a claim about standard music theory.




## 4. Observation logs and cascade annotation

For external events (e.g. 3I/ATLAS briefings) the project uses CSV logs under data/observations/.

These logs can be enriched with simulated cascade information (1–23) using:

python -m scripts.annotate_observations_with_cascade


The annotator:

Reads the input CSV.

Builds a simple synthetic signal for each row (based on the channel field).

Runs the cascade simulator.

Writes an output CSV with two extra columns:

sim_main_cascade – dominant cascade level (1–23),

sim_confidence – fraction of total spectral power assigned to this level.

Again, this is an experimental tool for linking observation timelines to the public cascade scale, not a physical model.


## 5. Status and roadmap

Current status: v0.1.0 – scaffolding only

no real NASA data integrated yet;

cascade models are in exploratory phase;

simulator works on synthetic signals only;

logbook and observation formats are still evolving.

Planned next steps:

keep logbook_3I_ATLAS.md and observation CSVs up to date;

add simple tests for cascade_scale and cascade_mapping;

integrate first real public data products as they appear;

expand notebooks with physics- and AI-inspired cascade models.



## 6. License

MIT — see LICENSE for details.
