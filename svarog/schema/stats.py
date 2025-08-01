from datetime import date, timedelta
from pydantic import BaseModel, Field


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
