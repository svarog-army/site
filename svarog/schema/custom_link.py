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

    instagram_url: str = ""
    facebook_url: str = ""
    telegram_url: str = ""
    youtube_url: str = ""
    donate_url: str = ""
    test_drive_url: str = ""
