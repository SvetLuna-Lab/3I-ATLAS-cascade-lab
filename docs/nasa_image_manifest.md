# NASA 3I/ATLAS Image Manifest

This document serves as a **reference catalog** of official 3I/ATLAS images and
related pages published by NASA / ESA and partner teams.

> **Policy:**  
> This lab does **not** store NASA or ESA images of 3I/ATLAS locally.  
> We work only with links to official pages and derived numerical/analytical
> results (where available).

The purpose of this manifest is to:

- keep track of where the official images live;
- briefly describe what type of view each source provides;
- connect visual data with later cascade/physics analysis (via dates, missions,
  and qualitative notes).

---

## 1. Main public galleries

High-level landing pages and consolidated galleries:

| id                     | agency | short_label                          | url                                                                 |
|------------------------|--------|--------------------------------------|---------------------------------------------------------------------|
| `NASA_MAIN_GALLERY`    | NASA   | 3I/ATLAS image gallery               | https://science.nasa.gov/solar-system/comets/3i-atlas/comet-3i-atlas-image-gallery/ |
| `NASA_MULTI_MISSION`   | NASA   | Multi-mission 3I/ATLAS views         | https://science.nasa.gov/solar-system/view-interstellar-comet-3i-atlas-through-nasas-multiple-lenses/ |
| `ESA_EXOMARS_MEX`      | ESA    | ExoMars + Mars Express observations  | https://www.esa.int/Science_Exploration/Space_Science/ESA_s_ExoMars_and_Mars_Express_observe_comet_3I_ATLAS |

These pages aggregate multiple images and videos (SOHO, MAVEN, Perseverance,
ExoMars, Mars Express, etc.) and are the primary entry points for visual data.

---

## 2. Mission-specific views (reference only)

Below is a coarse breakdown by mission/instrument.  
At this stage we only list representative references; detailed per-image
cataloging can be added later if it becomes necessary.

| id                      | mission / instrument         | gallery_or_article_url                                                                 | channel  | notes_en                                                                                     |
|-------------------------|------------------------------|----------------------------------------------------------------------------------------|----------|----------------------------------------------------------------------------------------------|
| `SOHO_LASCO_C3_OVERVIEW` | SOHO / LASCO C3 coronagraph | https://science.nasa.gov/solar-system/comets/3i-atlas/comet-3i-atlas-image-gallery/   | optical  | 3I/ATLAS appears as a very faint point against a grainy coronal background.                 |
| `MAVEN_UV_VIEW`         | MAVEN / UV instrument        | https://science.nasa.gov/solar-system/view-interstellar-comet-3i-atlas-through-nasas-multiple-lenses/ | UV       | UV view of the gas coma; more a diffuse halo than a narrow “classical” tail.                |
| `PERSEVERANCE_MASTCAMZ` | Perseverance / Mastcam-Z     | https://science.nasa.gov/solar-system/view-interstellar-comet-3i-atlas-through-nasas-multiple-lenses/ | optical  | 3I/ATLAS as a weak smudge in a star field, imaged from the surface of Mars.                 |
| `ESA_EXOMARS_TGO`       | ExoMars TGO                  | https://www.esa.int/Science_Exploration/Space_Science/ESA_s_ExoMars_and_Mars_Express_observe_comet_3I_ATLAS | mixed    | Combined European views (e.g. ExoMars TGO, Mars Express) complementing NASA observations.   |

You can extend this table later with:

- additional missions (if new data appear),
- more precise dates and observing geometry,
- links to any derived numerical products (e.g. brightness curves, centroid tracks).

---

## 3. How this manifest is used in the lab

In this repository, the manifest plays a **linking** role:

- It keeps the visual context of 3I/ATLAS without redistributing images.
- It provides anchors for:
  - timeline correlations (date of observation ↔ cascade models),
  - cross-references between missions and observing geometries,
  - future notebooks that may, for example, use publicly available brightness
    estimates or positional data derived from these campaigns.

If at some later point we decide to work with local copies (e.g. one or two
small PNGs for demonstration purposes), a separate section can be added:

- with a clear list of `local_filename` values under `data/raw/nasa/`,
- and explicit credit back to the original NASA / ESA pages.

For now, this manifest remains **link-only**, by design.
