from datetime import date, timedelta
from random import randint

import sqlalchemy as sa

from svarog import models as m
from svarog import db
from svarog.logger import log


def fill_test_stats(num: int = 100):
    """Fill DB by dummy stats data."""
    log(log.INFO, "Filling DB with dummy stats data")

    # delete all existing stats
    db.session.execute(sa.delete(m.DayStats))

    # start day - today - num days ago
    start_day = date.today() - timedelta(days=num - 1)
    for i in range(num):
        day = start_day + timedelta(days=i)
        stats = m.DayStats(
            day=day,
            tanks=randint(0, 10),
            mlrss=randint(0, 50),
            spas=randint(0, 30),
            afvs=randint(0, 40),
            cars=randint(0, 100),
            motorcycles=randint(0, 20),
            buggies=randint(0, 10),
            rofs=randint(5, 100),
            guns=randint(0, 25),
            mortars=randint(0, 15),
            adss=randint(0, 20),
            radars=randint(0, 10),
            ammos=randint(0, 5),
            shelters=randint(0, 8),
            uavs=randint(0, 12),
            antennas=randint(0, 7),
            other=randint(0, 10),
        )
        db.session.add(stats)
    db.session.commit()
    log(log.INFO, "Dummy stats data filled successfully")
