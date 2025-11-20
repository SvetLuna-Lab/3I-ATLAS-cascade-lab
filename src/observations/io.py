from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

import csv
from datetime import datetime


@dataclass
class Observation:
    datetime_utc: datetime
    source: str
    observer: str
    location: str
    channel: str
    ra_deg: Optional[float]
    dec_deg: Optional[float]
    mag_or_flux: Optional[float]
    velocity_info: str
    cascade_level: Optional[int]
    notes: str


def load_observations(path: Path) -> List[Observation]:
    observations: List[Observation] = []
    with path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            observations.append(
                Observation(
                    datetime_utc=datetime.fromisoformat(row["datetime_utc"].replace("Z", "+00:00")),
                    source=row["source"],
                    observer=row["observer"],
                    location=row["location"],
                    channel=row["channel"],
                    ra_deg=float(row["ra_deg"]) if row["ra_deg"] else None,
                    dec_deg=float(row["dec_deg"]) if row["dec_deg"] else None,
                    mag_or_flux=float(row["mag_or_flux"]) if row["mag_or_flux"] else None,
                    velocity_info=row["velocity_info"],
                    cascade_level=int(row["cascade_level"]) if row["cascade_level"] else None,
                    notes=row["notes"],
                )
            )
    return observations
