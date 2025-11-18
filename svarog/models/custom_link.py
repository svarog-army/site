from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import orm

from svarog.database import db

from .utils import ModelMixin


class CustomLink(db.Model, ModelMixin):  # pyright: ignore[reportGeneralTypeIssues]
    __tablename__ = "custom_links"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    link_type: orm.Mapped[str] = orm.mapped_column(sa.String(32))
    link_url: orm.Mapped[str] = orm.mapped_column(sa.String(256))

    updated_at: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
    )
