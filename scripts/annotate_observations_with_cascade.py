#!/usr/bin/env python
"""
Аннотация журнала наблюдений каскадной симуляцией.

Идея:
- читаем CSV с наблюдениями (например, data/observations/3I_ATLAS_2025.csv);
- для каждой строки синтезируем простой тестовый сигнал
  (пока только эвристика по полю channel);
- прогоняем сигнал через каскадный симулятор (1–23);
- дополняем CSV двумя колонками:
  - sim_main_cascade  — доминирующий каскад,
  - sim_confidence    — доля мощности (уверенность модели).

Это НЕ физическая модель объекта, а техническая проекция сигнала
в дискретную шкалу каскадов 1–23.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd

from src.core.signal_loader import generate_test_signal, compute_spectrum
from src.core.cascade_scale import get_public_scale
from src.core.cascade_mapping import map_dominant_cascade


def _freq_from_channel(channel: str | float | int) -> float:
    """
    Простая эвристика: частоту синтетического сигнала выбираем из поля channel.

    Это заглушка, чтобы показать связку:
    наблюдение → (условный) сигнал → каскад.

    optical  → 2 Гц
    IR       → 3 Гц
    radio    → 5 Гц
    mixed    → 4 Гц
    иначе    → 1.5 Гц
    """
    if not isinstance(channel, str):
        return 1.5

    ch = channel.strip().lower()
    if ch == "optical":
        return 2.0
    if ch in ("ir", "infrared"):
        return 3.0
    if ch == "radio":
        return 5.0
    if ch == "mixed":
        return 4.0
    return 1.5


def _simulate_signal_for_row(row: pd.Series, seed: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Генерация синтетического сигнала для одной строки наблюдений.

    Сейчас это:
    - одна синусоида с частотой, выбранной по channel;
    - небольшой шум (seed зависит от индекса строки, чтобы сигналы были различимы).
    """
    freq = _freq_from_channel(row.get("channel", ""))
    t, x = generate_test_signal(
        duration=10.0,
        dt=0.01,
        freqs=(freq,),
        amplitudes=(1.0,),
        seed=seed,
    )
    return t, x


def annotate_observations(
    input_path: Path,
    output_path: Path,
) -> None:
    """
    Главная функция:
    - читает CSV с наблюдениями;
    - генерирует синтетический сигнал для каждой строки;
    - проецирует спектр в каскады 1–23;
    - дополняет таблицу колонками sim_main_cascade, sim_confidence;
    - сохраняет результат в output_path.
    """
    if not input_path.exists():
        raise FileNotFoundError(f"Input CSV not found: {input_path}")

    df = pd.read_csv(input_path)

    scale = get_public_scale()

    sim_main: list[int] = []
    sim_conf: list[float] = []

    # Проходим по строкам, seed берём из индекса, чтобы сигналы отличались
    for idx, row in df.iterrows():
        t, x = _simulate_signal_for_row(row, seed=123 + int(idx))
        freq, power = compute_spectrum(t, x)

        result = map_dominant_cascade(freq, power, scale)
        sim_main.append(int(result["main_cascade"]))
        sim_conf.append(float(result["confidence"]))

    df["sim_main_cascade"] = sim_main
    df["sim_confidence"] = sim_conf

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"[OK] Annotated observations saved to: {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Annotate observation CSV with cascade simulation fields.",
    )
    parser.add_argument(
        "--input",
        type=str,
        default="data/observations/3I_ATLAS_observations_template.csv",
        help="Входной CSV с наблюдениями (по умолчанию data/observations/3I_ATLAS_observations_template.csv).",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/observations/3I_ATLAS_observations_with_cascade.csv",
        help="Выходной CSV с добавленными полями sim_main_cascade и sim_confidence.",
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    annotate_observations(input_path, output_path)


if __name__ == "__main__":
    main()
