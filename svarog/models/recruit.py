from datetime import date, datetime

from typing import TYPE_CHECKING
from itertools import chain

import sqlalchemy as sa
from sqlalchemy import orm

from svarog import schema as s
from svarog.database import db

from .utils import ModelMixin, gen_uuid

if TYPE_CHECKING:
    from .application import Application
    from .specialty import Specialty


class Recruit(db.Model, ModelMixin):
    __tablename__ = "recruits"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    uuid: orm.Mapped[str] = orm.mapped_column(sa.String(32), default=gen_uuid, index=True)

    full_name: orm.Mapped[str] = orm.mapped_column(sa.String(64))
    birth_date: orm.Mapped[date] = orm.mapped_column(sa.Date)
    phone: orm.Mapped[str] = orm.mapped_column(
        sa.String(64),
        unique=True,
    )
    email: orm.Mapped[str | None] = orm.mapped_column(sa.String(256))
    city_of_actual_residence: orm.Mapped[str] = orm.mapped_column(sa.String(64))
    education: orm.Mapped[str] = orm.mapped_column(sa.Text)
    skills: orm.Mapped[str] = orm.mapped_column(sa.Text)
    last_job: orm.Mapped[str] = orm.mapped_column(sa.String(64))
    health_problems: orm.Mapped[str] = orm.mapped_column(sa.Text)
    have_driver_license: orm.Mapped[str] = orm.mapped_column(sa.String(64))
    is_serviceman: orm.Mapped[bool] = orm.mapped_column(sa.Boolean, server_default=sa.false())
    uav_experience: orm.Mapped[str] = orm.mapped_column(sa.Text)

    status: orm.Mapped[s.RecruitStatus] = orm.mapped_column(sa.Enum(s.RecruitStatus), default=s.RecruitStatus.APPLIED)
    comments: orm.Mapped[str] = orm.mapped_column(sa.Text, server_default="")

    created_at: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime,
        default=datetime.now,
    )
    is_deleted: orm.Mapped[bool] = orm.mapped_column(sa.Boolean, server_default=sa.false())
    applications: orm.Mapped[list["Application"]] = orm.relationship("Application", back_populates="recruit")

    @property
    def specialties(self) -> list["Specialty"]:
        flattened = list(chain.from_iterable(application.specialties for application in self.applications))

        seen_uuids = set()
        unique_specialties = []
        for specialty in flattened:
            if specialty.uuid not in seen_uuids:
                seen_uuids.add(specialty.uuid)
                unique_specialties.append(specialty)

        return unique_specialties
