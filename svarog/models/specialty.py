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

    name: orm.Mapped[str] = orm.mapped_column(sa.String(64))

    created_at: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime,
        default=datetime.now,
    )
    is_deleted: orm.Mapped[bool] = orm.mapped_column(sa.Boolean, server_default=sa.false())

    # relationships
    applications: orm.Mapped[list["Application"]] = orm.relationship(
        "Application",
        secondary=application_specialty,
        back_populates="specialties",
    )
