from datetime import date, timedelta
from pydantic import BaseModel, Field, ConfigDict


def date_year_ago() -> date:
    """Returns the date one year ago from today."""
    today = date.today()
    if (today.year % 4 == 0 and today.month > 2) or ((today.year - 1) % 4 == 0 and today.month <= 2):
        return today - timedelta(days=366)
    return today - timedelta(days=365)


class Period(BaseModel):
    """Model representing a period with start and end dates."""

    start: date = Field(default_factory=date_year_ago, description="Start date of the period")
    end: date = Field(default_factory=date.today, description="End date of the period")


class Stats(BaseModel):
    """Model representing daily statistics."""

    period: Period = Field(default_factory=Period, description="Period for which statistics are collected")
    tanks: int = Field(default=0, description="Number of tanks")
    tanks_destroyed: int = Field(default=0, description="Number of tanks destroyed")
    mlrss: int = Field(default=0, description="Number of MLRS + SAM")
    mlrss_destroyed: int = Field(default=0, description="Number of MLRS + SAM destroyed")
    spas: int = Field(default=0, description="Number of self-propelled artillery")
    spas_destroyed: int = Field(default=0, description="Number of self-propelled artillery destroyed")
    afvs: int = Field(default=0, description="Number of AFV + APC")
    afvs_destroyed: int = Field(default=0, description="Number of AFV + APC destroyed")
    cars: int = Field(default=0, description="Number of cars + trucks")
    cars_destroyed: int = Field(default=0, description="Number of cars + trucks destroyed")
    motorcycles: int = Field(default=0, description="Number of motorcycles")
    motorcycles_destroyed: int = Field(default=0, description="Number of motorcycles destroyed")
    buggies: int = Field(default=0, description="Number of buggies")
    buggies_destroyed: int = Field(default=0, description="Number of buggies destroyed")
    rofs: int = Field(default=0, description="Number of ROF personnel")
    rofs_destroyed: int = Field(default=0, description="Number of ROF personnel destroyed")
    guns: int = Field(default=0, description="Number of guns + howitzers")
    guns_destroyed: int = Field(default=0, description="Number of guns + howitzers destroyed")
    mortars: int = Field(default=0, description="Number of mortars")
    mortars_destroyed: int = Field(default=0, description="Number of mortars destroyed")
    adss: int = Field(default=0, description="Number of air defense systems")
    adss_destroyed: int = Field(default=0, description="Number of air defense systems destroyed")
    radars: int = Field(default=0, description="Number of EW + radars")
    radars_destroyed: int = Field(default=0, description="Number of EW + radars destroyed")
    ammos: int = Field(default=0, description="Number of ammunition caches + storage facilities")
    ammos_destroyed: int = Field(default=0, description="Number of ammunition caches + storage facilities destroyed")
    shelters: int = Field(default=0, description="Number of shelters + dugouts")
    shelters_destroyed: int = Field(default=0, description="Number of shelters + dugouts destroyed")
    uavs: int = Field(default=0, description="Number of fixed-wing UAVs")
    uavs_destroyed: int = Field(default=0, description="Number of fixed-wing UAVs destroyed")
    antennas: int = Field(default=0, description="Number of antennas, cameras, network equipment")
    antennas_destroyed: int = Field(default=0, description="Number of antennas, cameras, network equipment destroyed")
    other: int = Field(default=0, description="Other statistics")
    other_destroyed: int = Field(default=0, description="Other statistics destroyed")
    impact_flights: int = Field(default=0, description="Number of impact flights")
    scouting_flights: int = Field(default=0, description="Number of scouting flights")
    found_targets: int = Field(default=0, description="Number of found targets")
    found_fpv_drones: int = Field(default=0, description="Number of found FPV drones")
    destroyed_fpv_drones: int = Field(default=0, description="Number of destroyed FPV drones")
    mining_flights: int = Field(default=0, description="Number of mining flights")
    setup_mines: int = Field(default=0, description="Number of setup mines")

    @property
    def total_impacted(self) -> int:
        """Calculate the total number of impacted items."""
        return (
            self.tanks + self.mlrss + self.spas + self.afvs + self.cars +
            self.motorcycles + self.buggies + self.rofs + self.guns +
            self.mortars + self.adss + self.radars + self.ammos +
            self.shelters + self.uavs + self.antennas + self.other
        )

    @property
    def total_destroyed(self) -> int:
        """Calculate the total number of destroyed items."""
        return (
            self.tanks_destroyed + self.mlrss_destroyed + self.spas_destroyed +
            self.afvs_destroyed + self.cars_destroyed + self.motorcycles_destroyed +
            self.buggies_destroyed + self.rofs_destroyed + self.guns_destroyed +
            self.mortars_destroyed + self.adss_destroyed + self.radars_destroyed +
            self.ammos_destroyed + self.shelters_destroyed + self.uavs_destroyed +
            self.antennas_destroyed + self.other_destroyed
        )

    model_config = ConfigDict(
        from_attributes=True,
    )
