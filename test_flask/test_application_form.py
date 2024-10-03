import sqlalchemy as sa
from flask.testing import FlaskClient, FlaskCliRunner
from flask_babel import _

from svarog import db
from svarog import models as m


def test_application_form(client: FlaskClient, runner: FlaskCliRunner):
    res = runner.invoke(args=["create-specialties"])
    assert "specialties created" in res.output
    specialties = db.session.scalars(sa.select(m.Specialty)).all()
    assert len(specialties) == 10
    application_create_data = {
        "full_name": "test",
        "birth_date": "2000-01-01",
        "phone": "1234567890",
        "email": "test@gmail.com",
        "city_of_actual_residence": "test",
        "education": "test",
        "skills": "test",
        "last_job": "test",
        "health_problems": "test",
        "have_driver_license": "yes",
        "is_serviceman": "yes",
        "uav_experience": "test",
        "applied_specialties": [specialties[0], specialties[1]],
        "allow_data_processing": "yes",
    }
    res = client.get("/application/get-application-form")
    assert res.status_code == 200
    res = client.post("/application/create", data=application_create_data)
    assert res.status_code == 302
    res = client.get(res.location, follow_redirects=True)
    assert res.status_code == 200
    assert _("Application applied successfully") in res.get_data(as_text=True)
    assert m.Recruit.count() == 1
    assert m.Application.count() == 1
    application = m.Application.first()
    assert application
    assert application.full_name == application_create_data["full_name"]
    assert application.phone == application_create_data["phone"]
