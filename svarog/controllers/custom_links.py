from svarog import models as m, db
from svarog import schema as s


def get_custom_links() -> s.CustomLink:
    """Get custom links from the database."""

    links = s.CustomLink()
    db_session = db.session  # pyright: ignore[reportAttributeAccessIssue]
    for link_type in s.LinkType:
        link = db_session.scalar(m.CustomLink.select().where(m.CustomLink.link_type == link_type))
        if link:
            if link_type == s.LinkType.INSTAGRAM:
                links.instagram = link.link_url
            elif link_type == s.LinkType.FACEBOOK:
                links.facebook = link.link_url
            elif link_type == s.LinkType.TELEGRAM:
                links.telegram = link.link_url
            elif link_type == s.LinkType.YOUTUBE:
                links.youtube = link.link_url
            elif link_type == s.LinkType.DONATE:
                links.donate = link.link_url
            elif link_type == s.LinkType.TEST_DRIVE:
                links.test_drive = link.link_url
    return links
