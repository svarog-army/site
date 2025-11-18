import click
from flask import Flask
import sqlalchemy as sa
from sqlalchemy import orm
from svarog import models as m
from svarog import db, forms
from svarog import schema as s
from config import CFG


def init(app: Flask):
    # flask cli context setup
    @app.shell_context_processor
    def get_context():
        """Objects exposed here will be automatically available from the shell."""
        return dict(app=app, db=db, m=m, f=forms, s=s, sa=sa, orm=orm, CFG=CFG)

    if app.config["ENV"] != "production":

        @app.cli.command()
        @click.option("--count", default=100, type=int)
        def db_populate(count: int):
            """Fill DB by dummy data."""
            from test_flask.db import populate

            populate(count)
            print(f"DB populated by {count} instancies")

    @app.cli.command("create-admin")
    def create_admin():
        """Create super admin account"""
        query = m.User.select().where(m.User.email == app.config["ADMIN_EMAIL"])
        if db.session.execute(query).first():  # pyright: ignore[reportAttributeAccessIssue]
            print(f"User with e-mail: [{app.config['ADMIN_EMAIL']}] already exists")
            return
        m.User(
            username=app.config["ADMIN_USERNAME"],
            email=app.config["ADMIN_EMAIL"],
            password=app.config["ADMIN_PASSWORD"],
            is_admin=True,
            activated=True,
        ).save()
        print("admin created")

    @app.cli.command("create-specialties")
    def create_specialties():
        """Create specialties"""
        specialties = [
            ("UAV Operator", "Оператор БпЛА"),
            ("UAV Pilot", "Пілот БпЛА"),
            ("Handyman", "Майстер"),
            ("Driver", "Водій"),
            ("Aviation mechanic", "Авіаційний механік"),
            ("Decryptor", "Дешифрувальник"),
            ("Mechanic", "Механік"),
            ("Sapper", "Сапер"),
            ("The operator of the WB complex", "Оператор комплексу РЕБ"),
        ]
        counter = 0
        for en, uk in specialties:
            existing = db.session.scalar(  # pyright: ignore[reportAttributeAccessIssue]
                m.Specialty.select().where(m.Specialty.name_en == en, m.Specialty.is_deleted.is_(False))
            )
            if existing:
                print(f"Specialty [{en}] already exists")
                continue
            m.Specialty(name_en=en, name_uk=uk).save()
            counter += 1
        print(f"{counter} specialties created")

    @app.cli.command("fill-recruits")
    @click.option("--count", default=100, type=int)
    def fill_recruits(count: int):
        """Fill recruits table with dummy data."""
        from svarog.controllers import fill_test_recruits

        fill_test_recruits(count)
        print(f"DB populated by {count} recruits")

    @app.cli.command("fill-stats")
    @click.option("--count", default=100, type=int)
    def fill_stats(count: int):
        """Fill day_stats table with dummy data."""
        from svarog.controllers.stats import fill_test_stats

        fill_test_stats(count)
        print(f"DB populated by {count} day_stats records")

    @app.cli.command("fill-custom-links")
    def fill_custom_links():
        """Fill custom_links table with data from config."""
        links = {
            s.LinkType.INSTAGRAM: app.config["LINK_INSTAGRAM"],
            s.LinkType.FACEBOOK: app.config["LINK_FACEBOOK"],
            s.LinkType.TELEGRAM: app.config["LINK_TELEGRAM"],
            s.LinkType.YOUTUBE: app.config["LINK_YOUTUBE"],
            s.LinkType.DONATE: app.config["LINK_DONATE"],
            s.LinkType.TEST_DRIVE: app.config["LINK_TEST_DRIVE"],
        }
        counter = 0
        for link_type, link_url in links.items():
            existing = db.session.scalar(m.CustomLink.select().where(m.CustomLink.link_type == link_type))  # pyright: ignore[reportAttributeAccessIssue]
            if existing:
                print(f"Custom link [{link_type}] already exists")
                continue
            m.CustomLink(link_type=link_type, link_url=link_url).save()
            counter += 1
        print(f"{counter} custom links created")
