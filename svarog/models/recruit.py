from datetime import date, datetime
from enum import Enum
from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy import orm

from svarog.database import db
from svarog.utils import gen_uuid

from .utils import ModelMixin

if TYPE_CHECKING:
    from .application import Application


class RecruitStatus(Enum):
    APPLIED = "APPLIED"
    IN_PROGRESS = "IN_PROGRESS"
    REJECTED = "REJECTED"
    HIRED = "HIRED"


class Recruit(db.Model, ModelMixin):
    __tablename__ = "recruits"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    uuid: orm.Mapped[str] = orm.mapped_column(sa.String(36), default=gen_uuid, index=True)

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

    status: orm.Mapped[str] = orm.mapped_column(sa.Enum(RecruitStatus), default=RecruitStatus.APPLIED)

    created_at: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime,
        default=datetime.now,
    )
    is_deleted: orm.Mapped[bool] = orm.mapped_column(sa.Boolean, server_default=sa.false())
    applications: orm.Mapped[list["Application"]] = orm.relationship("Application", back_populates="recruit")
