from datetime import datetime, date, timezone

import sqlalchemy as sa
from sqlalchemy import orm

from svarog.database import db
from .utils import ModelMixin, gen_uuid


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def current_date() -> date:
    return utcnow().date()


class DayStats(db.Model, ModelMixin):
    __tablename__ = "day_stats"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    uuid: orm.Mapped[str] = orm.mapped_column(sa.String(32), default=gen_uuid, index=True)
    day: orm.Mapped[date] = orm.mapped_column(
        sa.Date,
        default=datetime.utcnow().date,
        unique=True,
    )
    created_at: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime,
        default=utcnow,
    )
    updated_at: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime,
        default=utcnow,
        onupdate=utcnow,
    )
    is_deleted: orm.Mapped[bool] = orm.mapped_column(sa.Boolean, server_default=sa.false())

    tanks: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Tanks
    mlrss: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # MLRS + SAM
    spas: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Self-propelled artillery
    afvs: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # AFV + APC
    cars: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Cars + trucks
    motorcycles: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Motorcycles
    buggies: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Buggies
    rofs: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # ROF personnel
    guns: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Guns + howitzers
    mortars: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Mortars
    adss: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Air defense systems
    radars: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # EW + Radars
    ammos: orm.Mapped[int | None] = orm.mapped_column(
        sa.Integer, default=None
    )  # Ammunition caches + storage facilities
    shelters: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Shelters + dugouts
    uavs: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Fixed-wing UAV
    antennas: orm.Mapped[int | None] = orm.mapped_column(
        sa.Integer, default=None
    )  # Antennas, cameras, network equipment
    other: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Other

    def __repr__(self):
        return f"<{self.id}: {self.day},{self.email}>"
