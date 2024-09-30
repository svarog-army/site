import sqlalchemy as sa
from svarog.database import db


application_specialty = sa.Table(
    "application_specialty",
    db.Model.metadata,
    sa.Column("application_id", sa.ForeignKey("applications.id")),
    sa.Column("specialty_id", sa.ForeignKey("specialties.id")),
)
