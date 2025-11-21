#!/usr/bin/env python
"""
Простой демо-скрипт для симулятора каскадов.

Шаги:
1. Генерируем синтетический сигнал (одна доминирующая частота).
2. Строим спектр.
3. Проецируем спектр в каскадную шкалу 1–23.
4. Печатаем доминирующий каскад и уверенность,
   а также несколько наиболее нагруженных уровней.
"""

from __future__ import annotations

from typing import List, Tuple

import numpy as np

from src.core.signal_loader import generate_test_signal, compute_spectrum
from src.core.cascade_scale import get_public_scale, CascadeLevel
from src.core.cascade_mapping import map_dominant_cascade


def _top_k_cascades(
    vector: np.ndarray,
    scale: List[CascadeLevel],
    k: int = 5,
) -> List[Tuple[int, float]]:
    """
    Возвращает топ-k каскадов по весу вектора.

    Результат: список (cascade_id, weight), отсортированный по убыванию weight.
    """
    if len(vector) != len(scale):
        raise ValueError("vector length must match scale length")

    idx_sorted = np.argsort(vector)[::-1]  # по убыванию
    result: List[Tuple[int, float]] = []

    for idx in idx_sorted[:k]:
        lvl = scale[idx]
        result.append((lvl.cascade_id, float(vector[idx])))

    return result


def main() -> None:
    # 1. Генерируем тестовый сигнал:
    # одна доминирующая частота 2 Гц, немного шума.
    t, x = generate_test_signal(
        duration=10.0,
        dt=0.01,
        freqs=(2.0,),
        amplitudes=(1.0,),
        seed=123,
    )

    # 2. Строим спектр
    freq, power = compute_spectrum(t, x)

    # 3. Загружаем публичную шкалу каскадов 1–23
    scale = get_public_scale()

    # 4. Проецируем спектр в каскадную шкалу
    result = map_dominant_cascade(freq, power, scale)

    main_cascade = result["main_cascade"]
    confidence = result["confidence"]
    vector = result["vector"]

    # 5. Печатаем результат
    print("=== Cascade simulator demo ===")
    print(f"Доминирующий каскад: {main_cascade}")
    print(f"Уверенность (доля мощности): {confidence:.3f}")

    # Выведем несколько наиболее нагруженных уровней
    top = _top_k_cascades(vector, scale, k=5)
    print("\nТоп-5 каскадов по весу:")
    for cid, w in top:
        print(f"  каскад {cid:2d}: вес = {w:.3f}")


if __name__ == "__main__":
    main()
