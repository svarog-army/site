from datetime import datetime, date, timezone

import sqlalchemy as sa
from sqlalchemy import orm

from svarog.database import db
from svarog import schema as s
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
        default=current_date,
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
    tanks_destroyed: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Tanks destroyed
    mlrss: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # MLRS + SAM
    mlrss_destroyed: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # MLRS + SAM destroyed
    spas: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Self-propelled artillery
    spas_destroyed: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # SPA destroyed
    afvs: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # AFV + APC
    afvs_destroyed: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # AFV + APC destroyed
    cars: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Cars + trucks
    cars_destroyed: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Cars + trucks destroyed
    motorcycles: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Motorcycles
    motorcycles_destroyed: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Motorcycles destroyed
    buggies: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Buggies
    buggies_destroyed: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Buggies destroyed
    rofs: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # ROF personnel
    rofs_destroyed: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # ROF personnel destroyed
    guns: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Guns + howitzers
    guns_destroyed: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Guns + howitzers destroyed
    mortars: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Mortars
    mortars_destroyed: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Mortars destroyed
    adss: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Air defense systems
    adss_destroyed: orm.Mapped[int | None] = orm.mapped_column(
        sa.Integer, default=None
    )  # Air defense systems destroyed
    radars: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # EW + Radars
    radars_destroyed: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # EW + Radars destroyed
    ammos: orm.Mapped[int | None] = orm.mapped_column(
        sa.Integer, default=None
    )  # Ammunition caches + storage facilities
    ammos_destroyed: orm.Mapped[int | None] = orm.mapped_column(
        sa.Integer, default=None
    )  # Ammunition caches + storage facilities destroyed
    shelters: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Shelters + dugouts
    shelters_destroyed: orm.Mapped[int | None] = orm.mapped_column(
        sa.Integer, default=None
    )  # Shelters + dugouts destroyed
    uavs: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Fixed-wing UAV
    uavs_destroyed: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Fixed-wing UAV destroyed
    antennas: orm.Mapped[int | None] = orm.mapped_column(
        sa.Integer, default=None
    )  # Antennas, cameras, network equipment
    antennas_destroyed: orm.Mapped[int | None] = orm.mapped_column(
        sa.Integer, default=None
    )  # Antennas, cameras, network equipment destroyed
    other: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Other
    other_destroyed: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Other destroyed
    impact_flights: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Impact Flights
    scouting_flights: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Scouting Flights
    found_targets: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Found targets
    found_fpv_drones: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Found FPV drones
    destroyed_fpv_drones: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Destroyed FPV drones
    mining_flights: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Mining Flights
    setup_mines: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, default=None)  # Setup mines

    def __repr__(self):
        return f"<{self.id}: {self.day}>"

    @classmethod
    def last_day(cls) -> s.Stats:
        """Returns the last day stats."""
        last_day_stats = db.session.scalar(
            sa.select(cls).where(cls.is_deleted.is_(False)).order_by(cls.day.desc()).limit(1)
        )
        if not last_day_stats:
            return s.Stats(period=s.Period(start=date.today(), end=date.today()))
        stats = s.Stats.model_validate(last_day_stats)
        stats.period.start = last_day_stats.day
        stats.period.end = last_day_stats.day
        return stats

    @classmethod
    def get_stats_for_period(cls, period: s.Period) -> s.Stats:
        """Returns stats for the given period."""
        where = sa.and_(cls.is_deleted.is_(False), cls.day >= period.start, cls.day <= period.end)
        query = sa.select(cls).where(where).order_by(cls.day.desc())
        stats_list = db.session.scalars(query).all()
        assert stats_list, "No stats found for the specified period"

        stats = s.Stats(period=period)
        for stat in stats_list:
            stats.tanks += stat.tanks or 0
            stats.tanks_destroyed += stat.tanks_destroyed or 0
            stats.mlrss += stat.mlrss or 0
            stats.mlrss_destroyed += stat.mlrss_destroyed or 0
            stats.spas += stat.spas or 0
            stats.spas_destroyed += stat.spas_destroyed or 0
            stats.afvs += stat.afvs or 0
            stats.afvs_destroyed += stat.afvs_destroyed or 0
            stats.cars += stat.cars or 0
            stats.cars_destroyed += stat.cars_destroyed or 0
            stats.motorcycles += stat.motorcycles or 0
            stats.motorcycles_destroyed += stat.motorcycles_destroyed or 0
            stats.buggies += stat.buggies or 0
            stats.buggies_destroyed += stat.buggies_destroyed or 0
            stats.rofs += stat.rofs or 0
            stats.rofs_destroyed += stat.rofs_destroyed or 0
            stats.guns += stat.guns or 0
            stats.guns_destroyed += stat.guns_destroyed or 0
            stats.mortars += stat.mortars or 0
            stats.mortars_destroyed += stat.mortars_destroyed or 0
            stats.adss += stat.adss or 0
            stats.adss_destroyed += stat.adss_destroyed or 0
            stats.radars += stat.radars or 0
            stats.radars_destroyed += stat.radars_destroyed or 0
            stats.ammos += stat.ammos or 0
            stats.ammos_destroyed += stat.ammos_destroyed or 0
            stats.shelters += stat.shelters or 0
            stats.shelters_destroyed += stat.shelters_destroyed or 0
            stats.uavs += stat.uavs or 0
            stats.uavs_destroyed += stat.uavs_destroyed or 0
            stats.antennas += stat.antennas or 0
            stats.antennas_destroyed += stat.antennas_destroyed or 0
            stats.other += stat.other or 0
            stats.other_destroyed += stat.other_destroyed or 0
            stats.impact_flights += stat.impact_flights or 0
            stats.scouting_flights += stat.scouting_flights or 0
            stats.found_targets += stat.found_targets or 0
            stats.found_fpv_drones += stat.found_fpv_drones or 0
            stats.destroyed_fpv_drones += stat.destroyed_fpv_drones or 0
            stats.mining_flights += stat.mining_flights or 0
            stats.setup_mines += stat.setup_mines or 0

        return stats
