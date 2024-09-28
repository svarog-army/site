import sqlalchemy as sa
from flask.testing import FlaskClient, FlaskCliRunner

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
    }
    res = client.get("/application/get-application-form")
    assert res.status_code == 200
    res = client.post("/application/create", data=application_create_data)
    assert res.status_code == 201
    pass
