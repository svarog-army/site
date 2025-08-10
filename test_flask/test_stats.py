from datetime import date, timedelta

from flask.testing import FlaskClient
from svarog import models as m, db
from test_flask.utils import login


def test_admin_stats(populate: FlaskClient):
    login(populate)
    response = populate.get("/admin/stats/")
    assert response
    assert response.status_code == 200
    html = response.data.decode()
    stats = db.session.scalars(m.DayStats.select().order_by(m.DayStats.id).limit(11)).all()
    assert len(stats) == 11

    populate.application.config["PAGE_LINKS_NUMBER"] = 6
    response = populate.get("/admin/stats/?page=6")
    assert response
    assert response.status_code == 200
    html = response.data.decode()
    assert "/admin/stats/?page=6" in html
    assert "/admin/stats/?page=3" in html
    assert "/admin/stats/?page=8" in html
    assert "/admin/stats/?page=10" not in html
    assert "/admin/stats/?page=2" not in html


# def test_edit_user(populate: FlaskClient):
#     login(populate)
#     user: m.User = db.session.scalar(m.User.select())
#     response = populate.get(f"/admin/get-edit-form/{user.uuid}")
#     assert response.status_code == 200
#     assert user.username in response.data.decode()
#     assert user.email in response.data.decode()
#     assert user.uuid in response.data.decode()
#     assert user.password not in response.data.decode()


# def test_delete_user(populate: FlaskClient):
#     login(populate)
#     user: m.User = db.session.scalar(m.User.select())
#     uc = db.session.query(m.User).count()
#     response = populate.delete(f"/admin/delete/{user.uuid}")
#     assert db.session.query(m.User).filter(m.User.is_deleted.is_(False)).count() < uc
#     assert response.status_code == 202


def test_get_statistics_for_last_days(populate: FlaskClient):
    res = populate.get("/en/stats/")
    assert res.status_code == 200
    html = res.data.decode()
    today = date.today() - timedelta(days=1)
    assert f"{today.strftime("%d.%m")} (18:00)" in html


def test_get_statistics_for_last_week(populate: FlaskClient):
    res = populate.get("/en/stats/?period=week")
    assert res.status_code == 200
    html = res.data.decode()
    start_day = date.today() - timedelta(days=7)
    assert f"{start_day.strftime("%d.%m")} (18:00)" in html
