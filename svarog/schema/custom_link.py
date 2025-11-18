from enum import StrEnum

from pydantic import BaseModel


class LinkType(StrEnum):
    INSTAGRAM = "instagram"
    FACEBOOK = "facebook"
    TELEGRAM = "telegram"
    YOUTUBE = "youtube"
    DONATE = "donate"
    TEST_DRIVE = "test_drive"


class CustomLink(BaseModel):
    """Custom links"""

    instagram: str = ""
    facebook: str = ""
    telegram: str = ""
    youtube: str = ""
    donate: str = ""
    test_drive: str = ""
