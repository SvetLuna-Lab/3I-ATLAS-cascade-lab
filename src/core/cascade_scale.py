## 2. Модуль шкалы каскадов

```python
# src/core/cascade_scale.py
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class CascadeLevel:
    """
    Описание одного уровня каскада в симуляторе.

    Здесь мы используем нейтральные поля:
    - cascade_id: номер уровня (1..23),
    - position: числовая координата в [0, 1] для проекции,
    - label_ru / label_en: короткие текстовые подписи.

    Полные метафоры, связь с нотами, образами и т.п. задаются
    в документации и могут дополняться отдельно.
    """
    cascade_id: int
    position: float
    label_ru: str
    label_en: str


def get_public_scale() -> List[CascadeLevel]:
    """
    Возвращает публичную шкалу каскадов 1–23.

    В первом приближении уровни равномерно распределены по [0, 1].
    При необходимости эту шкалу можно уточнить (например, сместить
    некоторые уровни в соответствии с музыкальным строем).
    """
    levels: List[CascadeLevel] = []

    # Равномерная сетка по 23 уровням (0.0 .. 1.0)
    n_levels = 23
    for cid in range(1, n_levels + 1):
        # Нормализованная позиция: 0.0 для 1-го, 1.0 для 23-го
        position = (cid - 1) / (n_levels - 1)

        # Минимальные подписи, которые можно уточнить позже
        label_ru = f"Каскад {cid}"
        label_en = f"Cascade {cid}"

        levels.append(
            CascadeLevel(
                cascade_id=cid,
                position=position,
                label_ru=label_ru,
                label_en=label_en,
            )
        )

    return levels
