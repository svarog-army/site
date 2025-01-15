from datetime import datetime
from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy import orm

from svarog.database import db

from .utils import ModelMixin, gen_uuid
from .application_specialty import application_specialty


if TYPE_CHECKING:
    from .application import Application


class Specialty(db.Model, ModelMixin):
    __tablename__ = "specialties"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    uuid: orm.Mapped[str] = orm.mapped_column(sa.String(32), default=gen_uuid, index=True)

    name_en: orm.Mapped[str] = orm.mapped_column(sa.String(64), server_default="None")
    name_uk: orm.Mapped[str] = orm.mapped_column(sa.String(64), server_default="Нема")

    created_at: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime,
        default=datetime.now,
    )

    is_deleted: orm.Mapped[bool] = orm.mapped_column(sa.Boolean, server_default=sa.false())

    is_active: orm.Mapped[bool] = orm.mapped_column(sa.Boolean, server_default=sa.true())

    # relationships
    applications: orm.Mapped[list["Application"]] = orm.relationship(
        "Application",
        secondary=application_specialty,
        back_populates="specialties",
    )

    @property
    def name(self) -> str:
        return self.name_en

    @property
    def can_be_deleted(self) -> bool:
        return not self.applications
