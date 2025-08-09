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
            tanks=randint(5, 10),
            tanks_destroyed=randint(0, 5),
            mlrss=randint(20, 50),
            mlrss_destroyed=randint(0, 20),
            spas=randint(15, 30),
            spas_destroyed=randint(0, 15),
            afvs=randint(20, 40),
            afvs_destroyed=randint(0, 20),
            cars=randint(50, 100),
            cars_destroyed=randint(0, 50),
            motorcycles=randint(10, 20),
            motorcycles_destroyed=randint(0, 10),
            buggies=randint(5, 10),
            buggies_destroyed=randint(0, 5),
            rofs=randint(50, 100),
            rofs_destroyed=randint(0, 50),
            guns=randint(10, 25),
            guns_destroyed=randint(0, 10),
            mortars=randint(5, 15),
            mortars_destroyed=randint(0, 5),
            adss=randint(10, 20),
            adss_destroyed=randint(0, 10),
            radars=randint(5, 10),
            radars_destroyed=randint(0, 5),
            ammos=randint(3, 5),
            ammos_destroyed=randint(1, 3),
            shelters=randint(4, 8),
            shelters_destroyed=randint(0, 4),
            uavs=randint(6, 12),
            uavs_destroyed=randint(0, 6),
            antennas=randint(3, 7),
            antennas_destroyed=randint(0, 3),
            other=randint(5, 10),
            other_destroyed=randint(0, 5),
            impact_flights=randint(0, 20),
            scouting_flights=randint(0, 15),
            found_targets=randint(0, 30),
            found_fpv_drones=randint(5, 10),
            destroyed_fpv_drones=randint(0, 5),
            mining_flights=randint(0, 10),
            setup_mines=randint(10, 43),
        )
        db.session.add(stats)
    db.session.commit()
    log(log.INFO, "Dummy stats data filled successfully")
