from random import choice
from flask_login import current_user

from svarog import models as m
from svarog import schema as s
from svarog import db
from svarog.logger import log

TEST_CITIES = [
    "Київ",
    "Харків",
    "Одеса",
    "Дніпро",
    "Донецьк",
    "Запоріжжя",
    "Львів",
    "Кривий Ріг",
    "Миколаїв",
    "Маріуполь",
    "Севастополь",
    "Херсон",
    "Полтава",
    "Чернігів",
    "Черкаси",
    "Суми",
    "Житомир",
    "Чернівці",
    "Хмельницький",
    "Івано-Франківськ",
    "Кам'янець-Подільський",
    "Кропивницький",
    "Луцьк",
    "Мукачево",
    "Павлоград",
    "Рівне",
    "Тернопіль",
    "Ужгород",
    "Хуст",
    "Хмельницький",
    "Червоноград",
]

TEST_EDUCATIONS = [
    "Вища",
    "Середня спеціальна",
    "Середня",
]

TEST_SKILLS = [
    "Програмування",
    "Маркетинг",
    "Дизайн",
    "Медицина",
    "Педагогіка",
    "Фізика",
    "Математика",
    "Хімія",
    "Біологія",
    "Продажі",
    "Менеджмент",
]

TEST_JOBS = [
    "Програміст",
    "Маркетолог",
    "Дизайнер",
    "Лікар",
    "Вчитель",
    "Фізик",
    "Математик",
    "Хімік",
    "Біолог",
    "Продавець",
    "Менеджер",
]

TEST_DRIVE_LICENSES = [
    "A",
    "A, B",
    "A, B, C",
    "B, C",
    "C",
    "B",
]


def fill_test_recruits(num: int = 100):
    for i in range(num):
        recruit = m.Recruit(
            full_name=f"Recruit {i}",
            birth_date="1990-01-01",
            phone=f"{1234567890 + i}",
            email=f"recruit{i}@test.com",
            city_of_actual_residence=choice(TEST_CITIES),
            education=choice(TEST_EDUCATIONS),
            skills=choice(TEST_SKILLS),
            last_job=choice(TEST_JOBS),
            health_problems="немає",
            have_driver_license=choice(TEST_DRIVE_LICENSES),
            is_serviceman=False,
            uav_experience="немає",
        )
        db.session.add(recruit)
    db.session.commit()


def change_recruit_status(recruit: m.Recruit, status: s.RecruitStatus):
    recruit.status = status.value
    recruit.save()

    m.RecruitStatusChangeEvent(
        recruit_id=recruit.id,
        user_id=current_user.id,
        status=status.value,
    ).save()

    log(log.INFO, "Recruit status change history saved successfully")
