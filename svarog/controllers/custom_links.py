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
                links.instagram_url = link.link_url
            elif link_type == s.LinkType.FACEBOOK:
                links.facebook_url = link.link_url
            elif link_type == s.LinkType.TELEGRAM:
                links.telegram_url = link.link_url
            elif link_type == s.LinkType.YOUTUBE:
                links.youtube_url = link.link_url
            elif link_type == s.LinkType.DONATE:
                links.donate_url = link.link_url
            elif link_type == s.LinkType.TEST_DRIVE:
                links.test_drive_url = link.link_url
    return links


def update_custom_links(links: s.CustomLink) -> None:
    """Update custom links in the database."""

    db_session = db.session  # pyright: ignore[reportAttributeAccessIssue]
    for link_type in s.LinkType:
        link_url = ""
        if link_type == s.LinkType.INSTAGRAM:
            link_url = links.instagram_url
        elif link_type == s.LinkType.FACEBOOK:
            link_url = links.facebook_url
        elif link_type == s.LinkType.TELEGRAM:
            link_url = links.telegram_url
        elif link_type == s.LinkType.YOUTUBE:
            link_url = links.youtube_url
        elif link_type == s.LinkType.DONATE:
            link_url = links.donate_url
        elif link_type == s.LinkType.TEST_DRIVE:
            link_url = links.test_drive_url

        existing_link = db_session.scalar(m.CustomLink.select().where(m.CustomLink.link_type == link_type))
        if existing_link:
            existing_link.link_url = link_url
        else:
            new_link = m.CustomLink(link_type=link_type, link_url=link_url)
            db_session.add(new_link)
    db_session.commit()
