# tests/test_cascade_scale.py
"""
Базовые проверки публичной шкалы каскадов (1–23).

Задачи теста:
- убедиться, что уровней ровно 23;
- проверить, что cascade_id идут по порядку от 1 до 23;
- проверить, что position монотонно возрастает от 0.0 до 1.0.
"""

from src.core.cascade_scale import get_public_scale


def test_public_scale_has_23_levels():
    levels = get_public_scale()
    assert len(levels) == 23, "Должно быть ровно 23 уровня в публичной шкале"


def test_cascade_ids_are_sequential():
    levels = get_public_scale()
    ids = [lvl.cascade_id for lvl in levels]
    assert ids == list(range(1, 24)), "cascade_id должны идти от 1 до 23 без пропусков"


def test_positions_are_monotonic_and_normalized():
    levels = get_public_scale()
    positions = [lvl.position for lvl in levels]

    # монотонный рост
    assert all(
        positions[i] < positions[i + 1] for i in range(len(positions) - 1)
    ), "position должны строго возрастать от уровня к уровню"

    # первый ~0.0, последний ~1.0 (с небольшим допуском на float)
    assert abs(positions[0] - 0.0) < 1e-9, "Первый уровень должен иметь position≈0.0"
    assert abs(positions[-1] - 1.0) < 1e-9, "Последний уровень должен иметь position≈1.0"

