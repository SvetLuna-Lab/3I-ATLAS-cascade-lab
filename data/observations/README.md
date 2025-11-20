# 3I/ATLAS observation log

This folder contains observation logs for the interstellar comet 3I/ATLAS
and similar objects.

Each campaign is stored in a separate CSV file, for example:

- `3I_ATLAS_2025.csv`

Each row in the CSV is one observation or event.

## Columns

- **datetime_utc** — время события в UTC (ISO-формат, например `2025-11-20T18:45:00Z`).
- **source** — источник информации: `NASA_live`, `paper`, `own_observation`, `news` и т.п.
- **observer** — кто фиксирует наблюдение (сейчас: `Svetlana Romanova`).
- **location** — место/канал наблюдения: `Syktyvkar, RU`, `online stream`,
  `amateur telescope …`.
- **channel** — диапазон: `optical`, `IR`, `radio`, `mixed` и др.
- **ra_deg** — прямое восхождение объекта в градусах (если известно, иначе пусто).
- **dec_deg** — склонение в градусах (если известно, иначе пусто).
- **mag_or_flux** — звёздная величина или поток (может быть пустым, если нет чисел).
- **velocity_info** — текстовое описание движения: `approach`, `outbound`,
  `non-Keplerian behaviour` и т.п.
- **cascade_level** — уровень каскада в твоей модели:
  `19` (Sol — Солнце), `21` (La — Млечный Путь), `23` (зеркальный вход) и т.д.
- **notes** — свободное текстовое поле для комментариев:
  что именно показалось важным в этом наблюдении.

Поле `cascade_level` связывает физическое событие с каскадной картой
(нотный ряд Do–Si и соответствующие уровни 19, 21, 23…).
