from datetime import date, datetime
from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy import orm

from svarog.database import db

from .utils import ModelMixin, gen_uuid
from .application_specialty import application_specialty

if TYPE_CHECKING:
    from .recruit import Recruit
    from .specialty import Specialty


class Application(db.Model, ModelMixin):
    __tablename__ = "applications"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    uuid: orm.Mapped[str] = orm.mapped_column(sa.String(32), default=gen_uuid, index=True)

    full_name: orm.Mapped[str] = orm.mapped_column(sa.String(64))
    birth_date: orm.Mapped[date] = orm.mapped_column(sa.Date)
    phone: orm.Mapped[str] = orm.mapped_column(
        sa.String(64),
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

    created_at: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime,
        default=datetime.now,
    )
    is_deleted: orm.Mapped[bool] = orm.mapped_column(sa.Boolean, server_default=sa.false())

    # relationships
    recruit_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("recruits.id"))
    recruit: orm.Mapped["Recruit"] = orm.relationship("Recruit", back_populates="applications")
    # many-to-many
    specialties: orm.Mapped[list["Specialty"]] = orm.relationship(
        "Specialty",
        secondary=application_specialty,
        back_populates="applications",
    )

    def make_delete(self) -> None:
        self.is_deleted = True
        self.phone = f"{self.phone}-deleted-{datetime.now().timestamp()}"
        db.session.add(self)
        db.session.commit()
