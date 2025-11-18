from flask import current_app as app
from flask.testing import FlaskCliRunner, FlaskClient
from click.testing import Result
from svarog import models as m, db
from svarog import schema as s


def test_populate_db_by_custom_links(runner: FlaskCliRunner):
    db_session = db.session  # pyright: ignore[reportAttributeAccessIssue]
    count_before = db_session.query(m.CustomLink).count()
    assert count_before == 0, "CustomLink table must be empty before test"
    TEST_COUNT = len(s.LinkType)
    res: Result = runner.invoke(args=["fill-custom-links"])
    assert f"{TEST_COUNT} custom links created" in res.stdout
    assert (db_session.query(m.CustomLink).count()) == TEST_COUNT
    # Run second time to check for duplicates
    res = runner.invoke(args=["fill-custom-links"])
    for link_type in s.LinkType:
        assert f"Custom link [{link_type}] already exists" in res.stdout
    assert "0 custom links created" in res.stdout


def test_get_custom_links(runner: FlaskCliRunner, client: FlaskClient):
    runner.invoke(args=["fill-custom-links"])
    from svarog.controllers import get_custom_links

    links = get_custom_links()
    assert links.instagram, "Instagram link must be set"
    assert links.instagram == app.config["LINK_INSTAGRAM"]
    assert links.facebook, "Facebook link must be set"
    assert links.facebook == app.config["LINK_FACEBOOK"]
    assert links.telegram, "Telegram link must be set"
    assert links.telegram == app.config["LINK_TELEGRAM"]
    assert links.youtube, "YouTube link must be set"
    assert links.youtube == app.config["LINK_YOUTUBE"]
    assert links.donate, "Donate link must be set"
    assert links.donate == app.config["LINK_DONATE"]
    assert links.test_drive, "Test Drive link must be set"
    assert links.test_drive == app.config["LINK_TEST_DRIVE"]
