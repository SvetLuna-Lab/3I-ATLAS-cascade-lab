# tests/test_cascade_mapping.py
import numpy as np

from src.core.cascade_scale import get_public_scale
from src.core.cascade_mapping import map_dominant_cascade


def _make_sine(freq_hz: float, fs: float, duration_s: float = 2.0) -> np.ndarray:
    """
    Вспомогательная функция: генерируем чистый синус заданной частоты.

    freq_hz  – частота сигнала, Гц
    fs       – частота дискретизации, Гц
    duration_s – длительность сигнала, секунды
    """
    t = np.linspace(0.0, duration_s, int(fs * duration_s), endpoint=False)
    return np.sin(2 * np.pi * freq_hz * t)


def test_single_tone_stable_cascade():
    """
    Для одного и того же синусоидального сигнала функция
    map_dominant_cascade должна возвращать устойчивый номер каскада.

    Идея:
    - генерируем синус с одной доминирующей частотой;
    - дважды вызываем map_dominant_cascade для одного и того же сигнала;
    - проверяем, что cascade_id совпадает, а confidence находится в [0, 1].
    """
    fs = 100.0  # Гц
    freq = 3.0  # Гц

    scale = get_public_scale()
    signal = _make_sine(freq_hz=freq, fs=fs, duration_s=2.0)

    cid1, conf1 = map_dominant_cascade(signal, fs, scale)
    cid2, conf2 = map_dominant_cascade(signal, fs, scale)

    # Номера каскадов должны совпадать
    assert cid1 == cid2
    # Уверенность должна быть в разумном диапазоне
    assert 0.0 <= conf1 <= 1.0
    assert 0.0 <= conf2 <= 1.0


def test_cascade_id_monotonic_with_frequency():
    """
    Простейшая проверка монотонности:

    - для низкой, средней и высокой частоты
      рассчитываем доминирующий каскад;
    - ожидаем, что cascade_id не убывает с ростом частоты.

    Это не строгий физический закон, а sanity-check для выбранной
    шкалы и реализации map_dominant_cascade.
    """
    fs = 200.0  # Гц
    scale = get_public_scale()

    freqs = [1.0, 5.0, 15.0]  # низкая, средняя, более высокая частоты
    cascade_ids = []

    for f in freqs:
        sig = _make_sine(freq_hz=f, fs=fs, duration_s=2.0)
        cid, conf = map_dominant_cascade(sig, fs, scale)
        cascade_ids.append(cid)
        # уверенность тоже должна быть в допустимых границах
        assert 0.0 <= conf <= 1.0

    low, mid, high = cascade_ids
    assert low <= mid <= high

