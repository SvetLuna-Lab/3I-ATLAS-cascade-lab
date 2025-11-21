# src/core/cascade_mapping.py
"""
Проекция спектра сигнала в каскадную шкалу 1–23.

Базовый подход:
- берём спектр (freq, power),
- выделяем диапазон интересующих частот,
- нормируем его в [0, 1],
- сопоставляем с позициями каскадов (cascade_scale),
- получаем вектор весов и доминирующий каскад.
"""

from __future__ import annotations

from typing import Dict, Sequence

import numpy as np

from .cascade_scale import CascadeLevel


def _normalize_freqs(freq: np.ndarray) -> np.ndarray:
    """Нормализация частот в интервал [0, 1] по минимуму/максимуму."""
    if freq.ndim != 1:
        raise ValueError("freq must be 1D array")

    f_min = float(freq.min())
    f_max = float(freq.max())
    if f_max <= f_min:
        return np.zeros_like(freq, dtype=float)

    return (freq - f_min) / (f_max - f_min)


def compute_cascade_vector(
    freq: np.ndarray,
    power: np.ndarray,
    scale: Sequence[CascadeLevel],
    eps: float = 1e-12,
) -> np.ndarray:
    """
    Строит вектор "веса" для каждого каскада на основе спектра.

    Идея:
    - нормируем частоты в [0, 1];
    - для каждой частоты определяем ближайший по position каскад;
    - суммируем мощность в этот каскад;
    - нормируем итоговый вектор по сумме.

    Parameters
    ----------
    freq : np.ndarray
        Частоты (Гц).
    power : np.ndarray
        Мощность спектра (неотрицательная).
    scale : sequence of CascadeLevel
        Описания каскадов.
    eps : float
        Малое число для защиты от деления на ноль.

    Returns
    -------
    vector : np.ndarray
        Вектор длины len(scale), сумма ≈ 1.0.
    """
    if freq.shape != power.shape:
        raise ValueError("freq and power must have the same shape")

    if len(scale) == 0:
        raise ValueError("scale must not be empty")

    # Нормализуем частоты в [0, 1]
    f_norm = _normalize_freqs(freq)

    positions = np.array([lvl.position for lvl in scale], dtype=float)
    n_levels = len(scale)
    weights = np.zeros(n_levels, dtype=float)

    for f, p in zip(f_norm, power):
        # пропускаем отрицательную или NaN-мощность
        if not np.isfinite(p) or p <= 0.0:
            continue

        # находим ближайший каскад по позиции
        idx = int(np.argmin(np.abs(positions - f)))
        weights[idx] += float(p)

    total = float(weights.sum())
    if total <= eps:
        # если мощности почти нет, возвращаем равномерное распределение
        return np.ones(n_levels, dtype=float) / n_levels

    return weights / total


def map_dominant_cascade(
    freq: np.ndarray,
    power: np.ndarray,
    scale: Sequence[CascadeLevel],
) -> Dict[str, object]:
    """
    Определяет доминирующий каскад для заданного спектра.

    Возвращает словарь:
    - main_cascade: номер уровня (cascade_id),
    - confidence: доля мощности, пришедшейся на этот уровень,
    - vector: полный вектор распределения по каскадам (np.ndarray).
    """
    vector = compute_cascade_vector(freq, power, scale)

    idx_max = int(np.argmax(vector))
    best_level = scale[idx_max]
    confidence = float(vector[idx_max])

    return {
        "main_cascade": best_level.cascade_id,
        "confidence": confidence,
        "vector": vector,
    }
