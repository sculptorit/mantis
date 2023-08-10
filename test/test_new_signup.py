import random
import string


def new_random_user(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_new_signup(app):
    username = new_random_user("user_", 15)
    email = username + "@localhost"
    password = "password"
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, email, password)
    assert app.soap.can_login(username, password)
