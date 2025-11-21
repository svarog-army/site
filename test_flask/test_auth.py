from test_flask.utils import register, login, logout
from flask import url_for

from svarog import schema as s


TEST_EMAIL = "sam@test.com"


def test_auth_pages(client):
    response = client.get("/admin/login")
    assert response.status_code == 200
    response = client.get("/admin/logout")
    assert response.status_code == 302
    response = client.get("/admin/")
    assert response.status_code == 302


def test_login_and_logout(client):
    # Access to logout view before login should fail.
    response = logout(client)
    register("sam", "sam@test.com")
    response = login(client, "sam")
    assert b"Login successful." in response.data
    # Incorrect login credentials should fail.
    response = login(client, "sam", "wrongpassword")
    assert b"Wrong user ID or password." in response.data
    # Correct credentials should login
    response = login(client, "sam")
    assert b"Login successful." in response.data


def test_edit_custom_links(client):
    register("sam", TEST_EMAIL)
    login(client, "sam")
    URL = url_for("admin.edit_custom_links")

    # Access admin page should fail for non-admin user
    response = client.get(URL)
    assert response.status_code == 200

    TEST_INSTA_LINK = "https://instagram.com/testprofile"
    TEST_FACEBOOK_LINK = "https://facebook.com/testprofile"
    TEST_TELEGRAM_LINK = "https://t.me/testprofile"
    TEST_YOUTUBE_LINK = "https://youtube.com/testprofile"
    TEST_DONATE_LINK = "https://donate.com/testprofile"
    TEST_TEST_DRIVE_LINK = "https://testdrive.com/testprofile"

    data = s.CustomLink(
        instagram_url=TEST_INSTA_LINK,
        facebook_url=TEST_FACEBOOK_LINK,
        telegram_url=TEST_TELEGRAM_LINK,
        youtube_url=TEST_YOUTUBE_LINK,
        donate_url=TEST_DONATE_LINK,
        test_drive_url=TEST_TEST_DRIVE_LINK,
    ).model_dump()

    response = client.post(URL, data=data, follow_redirects=True)
    assert "Custom links updated!" in response.text
    assert response.status_code == 200
    # Check data in database
    response = client.get(URL)
    assert TEST_INSTA_LINK in response.text
    assert TEST_FACEBOOK_LINK in response.text
    assert TEST_TELEGRAM_LINK in response.text
    assert TEST_YOUTUBE_LINK in response.text
    assert TEST_DONATE_LINK in response.text
    assert TEST_TEST_DRIVE_LINK in response.text
