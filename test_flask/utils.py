from svarog.models import User

TEST_ADMIN_NAME = "bob"
TEST_ADMIN_EMAIL = "bob@test.com"
TEST_ADMIN_PASSWORD = "password"


def register(username=TEST_ADMIN_NAME, email=TEST_ADMIN_EMAIL, password=TEST_ADMIN_PASSWORD):
    user = User(username=username, email=email)
    user.password = password
    user.is_admin = True
    user.save()
    return user.id


def login(client, username=TEST_ADMIN_NAME, password=TEST_ADMIN_PASSWORD):
    return client.post("/admin/login", data=dict(user_id=username, password=password), follow_redirects=True)


def logout(client):
    return client.get("/admin/logout", follow_redirects=True)
