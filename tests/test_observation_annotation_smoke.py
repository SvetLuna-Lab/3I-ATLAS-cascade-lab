# tests/test_observation_annotation_smoke.py
"""
Простой smoke-тест для пайплайна аннотации наблюдений каскадами.

Идея:
- создаём временный CSV с парой строк наблюдений;
- прогоняем через annotate_observations(...);
- проверяем, что:
  - появились колонки sim_main_cascade и sim_confidence;
  - количество строк сохранилось;
  - значения лежат в допустимых диапазонах.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from scripts.annotate_observations_with_cascade import annotate_observations


def test_annotate_observations_creates_sim_columns(tmp_path):
    # Временный входной CSV
    input_csv: Path = tmp_path / "observations_input.csv"
    output_csv: Path = tmp_path / "observations_with_cascade.csv"

    # Минимальный набор колонок, совместимый с нашим скриптом
    df_in = pd.DataFrame(
        [
            {
                "datetime_utc": "2025-11-20T18:45:00Z",
                "source": "NASA_live",
                "observer": "Test Observer",
                "location": "Earth, online stream",
                "channel": "optical",
                "ra_deg": "",
                "dec_deg": "",
                "mag_or_flux": "",
                "velocity_info": "approach",
                "cascade_level": 19,
                "notes": "Synthetic test row 1",
            },
            {
                "datetime_utc": "2025-11-21T00:00:00Z",
                "source": "paper",
                "observer": "Test Observer",
                "location": "Syktyvkar, RU",
                "channel": "radio",
                "ra_deg": "",
                "dec_deg": "",
                "mag_or_flux": "",
                "velocity_info": "outbound",
                "cascade_level": "",
                "notes": "Synthetic test row 2",
            },
        ]
    )
    df_in.to_csv(input_csv, index=False)

    # Запускаем аннотацию
    annotate_observations(input_csv, output_csv)

    # Читаем результат
    assert output_csv.exists()
    df_out = pd.read_csv(output_csv)

    # Количество строк не изменилось
    assert len(df_out) == len(df_in)

    # Новые колонки присутствуют
    assert "sim_main_cascade" in df_out.columns
    assert "sim_confidence" in df_out.columns

    # Значения в корректных диапазонах
    for _, row in df_out.iterrows():
        cascade = int(row["sim_main_cascade"])
        conf = float(row["sim_confidence"])

        assert 1 <= cascade <= 23
        assert 0.0 <= conf <= 1.0
