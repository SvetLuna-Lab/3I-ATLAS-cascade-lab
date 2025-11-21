# tests/test_cascade_scale.py
from src.core.cascade_scale import get_public_scale


def test_public_scale_basic_properties():
    scale = get_public_scale()
    # 23 уровня
    assert len(scale) == 23
    # номера от 1 до 23
    ids = [lvl.cascade_id for lvl in scale]
    assert ids == list(range(1, 24))
    # позиции в [0, 1] и строго неубывающие
    positions = [lvl.position for lvl in scale]
    assert positions[0] == 0.0
    assert positions[-1] == 1.0
    assert all(0.0 <= p <= 1.0 for p in positions)
    assert all(positions[i] <= positions[i + 1] for i in range(len(positions) - 1))
