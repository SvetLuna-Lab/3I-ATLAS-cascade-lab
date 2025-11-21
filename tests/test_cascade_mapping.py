# tests/test_cascade_mapping.py
"""
Базовый smoke-тест для каскадного мэппинга.

Идея: генерируем синусоидальный сигнал с одной частотой,
строим спектр и проверяем, что map_dominant_cascade возвращает
какой-то устойчивый каскад (число от 1 до 23) и разумную уверенность.
"""

from __future__ import annotations

import numpy as np

from src.core.cascade_scale import get_public_scale
from src.core.signal_loader import generate_test_signal, compute_spectrum
from src.core.cascade_mapping import map_dominant_cascade


def test_dominant_cascade_for_simple_sine():
    # Сигнал: одна частота 2 Гц
    t, x = generate_test_signal(
        duration=10.0,
        dt=0.01,
        freqs=(2.0,),
        amplitudes=(1.0,),
        seed=123,
    )

    freq, power = compute_spectrum(t, x)
    scale = get_public_scale()

    result = map_dominant_cascade(freq, power, scale)

    main_cascade = result["main_cascade"]
    confidence = result["confidence"]

    # Должен быть корректный номер (1..23)
    assert 1 <= main_cascade <= 23

    # Уверенность не должна быть совсем нулевой
    assert confidence > 0.05

    # Вектор должен суммироваться примерно к 1
    vec = result["vector"]
    assert np.isclose(vec.sum(), 1.0, atol=1e-6)
