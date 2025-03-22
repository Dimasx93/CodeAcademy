# test_token_access.py
from user_verification_app import UserVerificationApp

def test_verified_user_gets_token():
    # Initialize the application
    app = UserVerificationApp()

    # The customer has the following username and password
    username = "alice"
    password = "pass123"

    # The customer inputs valid username and password to register new user
    app._register_user(username, password)

    # The user verifies the newly created user
    app._verify_user(username, password)

    # The user generates a token for the newly created and verified user
    token = app._generate_token(username)
    assert token is not None


def test_unverified_user_does_not_get_token():
    # Initialize the application
    app = UserVerificationApp()

    # The customer inputs valid username and password to register new user
    username = "alice"
    password = "pass123"

    # The customer inputs valid username and password to register new user
    app._register_user(username, password)

    # (The customer forgets to verify their newly created user)

    # The customer tries to generate a token for the newly created and verified user
    # and fails
    token = app._generate_token(username)
    assert token is None


# test_register_user.py

def test_register_user_correct_length():
    app = UserVerificationApp()
    username = "alice"
    password = "pass123"

    # No users when app is new
    assert len(app.users) == 0

    app._register_user(username, password)

    # Exactly one user after registering one
    assert len(app.users) == 1


def test_register_user_correctly_registered():
    app = UserVerificationApp()

    username = "alice"
    password = "pass123"

    app._register_user(username, password)

    # User exists
    assert username in app.users
    # Password correctly added
    assert app.users[username]["password"] == password

def test_verify_user_already_registered():
    app = UserVerificationApp()

    username = "alice"
    password = "pass123"
    app._register_user(username, password)
    res = app._register_user(username, password)

    assert  res == False

def test_user_is_not_verified():
    app = UserVerificationApp()
    username = "alice"
    password = "pass123"
    res = app._verify_user(username,password)

    assert  res == False



