from datetime import datetime
from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy import orm

from svarog.database import db
from svarog import schema as s

from .utils import ModelMixin, gen_uuid

if TYPE_CHECKING:
    from .recruit import Recruit
    from .user import User


class RecruitStatusChangeEvent(db.Model, ModelMixin):
    __tablename__ = "recruit_status_change_events"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    uuid: orm.Mapped[str] = orm.mapped_column(sa.String(32), default=gen_uuid, index=True)

    recruit_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("recruits.id"))

    user_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("users.id"))

    recruit: orm.Mapped["Recruit"] = orm.relationship("Recruit")

    user: orm.Mapped["User"] = orm.relationship("User")

    status: orm.Mapped[str] = orm.mapped_column(sa.String(32), default=s.RecruitStatus.IN_PROGRESS.value)

    created_at: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime,
        default=datetime.now,
    )

    def __repr__(self):
        return f"<Recruit {self.recruit_id} changed status to {self.recruit.status} for user {self.user_id}>"
