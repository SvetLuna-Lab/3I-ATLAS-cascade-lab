# Observations and cascade mapping (range 1–23)

This note explains how the observation logs in `data/observations/`
are connected to the cascade simulator.

## Observation CSV structure

A typical file has the following columns:

- `datetime_utc` – event time in UTC (ISO 8601).
- `source` – where the information comes from (NASA_live, paper, own_observation, news, …).
- `observer` – who records the entry (e.g. “Svetlana Romanova”).
- `location` – observation location (“Earth, online stream”, “Syktyvkar, RU”, etc.).
- `channel` – observational channel: optical / IR / radio / mixed.
- `ra_deg`, `dec_deg` – sky coordinates (if available).
- `mag_or_flux` – brightness or flux (optional, may be empty).
- `velocity_info` – text notes on motion (“approach”, “outbound”, “non-Keplerian behaviour”…).
- `cascade_level` – manual estimate in the cascade framework (e.g. 19 for Sun, 21 for Milky Way).
- `notes` – free text for any additional context.

## Simulated cascade fields

The script


python -m scripts.annotate_observations_with_cascade


reads an input CSV (by default
data/observations/3I_ATLAS_observations_template.csv) and produces
an output file (by default
data/observations/3I_ATLAS_observations_with_cascade.csv) with two extra
columns:

sim_main_cascade – dominant cascade level (1–23) chosen by the simulator;

sim_confidence – fraction of total spectral power assigned to this level
(a rough “confidence” in [0, 1]).

At the current stage, the simulator uses synthetic test signals:

a simple sine-based signal is generated per observation;

the frequency is chosen heuristically from the channel field
(optical / IR / radio / mixed);

the signal is passed through the cascade mapping
(compute_spectrum → map_dominant_cascade).

This is not a physical model of any specific object. It is a technical
tool to experiment with mapping signals into the public cascade range 1–23
and to prepare visual/analytic examples.

In the future, the same interface can be reused for real time series
(e.g. flux vs. time), once such data become available.

