# src/core/signal_loader.py
"""
Загрузка и генерация сигналов для симулятора каскадов.

Здесь две основные задачи:
- генерация простых тестовых сигналов (набор синусоид),
- расчёт спектра (частота–мощность) для дальнейшей проекции в каскады.
"""

from __future__ import annotations

from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd


def generate_test_signal(
    duration: float = 10.0,
    dt: float = 0.01,
    freqs: Tuple[float, ...] = (1.0,),
    amplitudes: Tuple[float, ...] = (1.0,),
    seed: int | None = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Генерация синтетического сигнала как суммы синусоид + небольшой шум.

    Parameters
    ----------
    duration : float
        Длительность сигнала (секунды).
    dt : float
        Шаг по времени.
    freqs : tuple of float
        Набор частот (Гц).
    amplitudes : tuple of float
        Соответствующие амплитуды (по длине как freqs).
    seed : int or None
        Seed для генерации шума (для воспроизводимости).

    Returns
    -------
    t : np.ndarray
        Вектор времени.
    x : np.ndarray
        Сигнал (сумма синусоид + шум).
    """
    t = np.arange(0.0, duration, dt)
    x = np.zeros_like(t)

    for f, a in zip(freqs, amplitudes):
        x += a * np.sin(2.0 * np.pi * f * t)

    if seed is not None:
        rng = np.random.default_rng(seed)
        noise = 0.05 * rng.standard_normal(size=t.shape)
        x = x + noise

    return t, x


def compute_spectrum(
    t: np.ndarray,
    x: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Расчёт амплитудного спектра сигнала с помощью БПФ.

    Возвращает частоты и мощность (квадрат модуля спектра), обрезанные
    до неотрицательных частот (rfft).
    """
    # Предполагаем равномерный шаг
    if len(t) < 2:
        raise ValueError("Time array is too short for spectrum computation.")

    dt = float(t[1] - t[0])
    n = len(t)

    # Реальная БПФ
    fft_vals = np.fft.rfft(x)
    freqs = np.fft.rfftfreq(n, d=dt)

    power = np.abs(fft_vals) ** 2

    return freqs, power


def load_timeseries_csv(
    path: Path,
    time_col: str = "time",
    value_col: str = "value",
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Загрузка простого временного ряда из CSV-файла.

    Ожидается таблица вида:
    time,value
    0.0, 1.23
    0.1, 1.19
    ...

    Возвращает t, x (как np.ndarray).
    """
    df = pd.read_csv(path)
    if time_col not in df.columns or value_col not in df.columns:
        raise ValueError(
            f"CSV must contain '{time_col}' and '{value_col}' columns."
        )

    t = df[time_col].to_numpy(dtype=float)
    x = df[value_col].to_numpy(dtype=float)
    return t, x
