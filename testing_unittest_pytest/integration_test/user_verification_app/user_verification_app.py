# user_verification_app.py
import uuid
import sys


class UserVerificationApp:
    def __init__(self):
        # Dictionary to store users and their verification status
        self.users = {}
        # Dictionary to store tokens associated with verified users
        self.tokens = {}

    def _register_user(self, username: str, password: str) -> bool:
        """Register a user by putting their details in the user dictionary."""
        if username in self.users:
            return False

        self.users[username] = {'password': password, 'verified': False}
        return True

    def _verify_user(self, username: str, password: str) -> bool:
        """Verify a user by updating their verified status in the user dictionary."""
        if username in self.users and self.users[username]['password'] == password:
            self.users[username]['verified'] = True
            return True
        return False

    def _generate_token(self, username: str) -> str | None:
        """Generate a random token if the user is verified"""
        if username in self.users and self.users[username]['verified']:
            token = str(uuid.uuid4())  # Generate a unique token
            self.tokens[token] = username
            return token
        return None

    def start_app(self) -> None:
        """Start the user verification application."""
        while True:
            print("""What would you like to do?
            1. Register a new user
            2. Verify a user
            3. Get a token
            4. Exit
            """)
            choice = input("Please enter a number:\n").strip()
            if choice == "1" or choice == "1.":
                username = input("Please enter the new user's username: ")
                password = input("Please enter the new user's password: ")
                if self._register_user(username, password):
                    print(f"New user {username} was registered successfully!")
                else:
                    print(f"User {username} already exists!")
            elif choice == "2" or choice == "2.":
                username = input("Please enter a username to verify: ")
                password = input("Please enter a password to verify: ")
                if self._verify_user(username, password):
                    print(f"User {username} was verified successfully!")
                else:
                    print(f"User {username} was not verified - wrong username or "
                          f"password!")
            elif choice == "3" or choice == "3.":
                username = input("Please enter a username to generate the token for: ")
                token = self._generate_token(username)
                if token is None:
                    print(f"User {username} is not verified.")
                else:
                    print(f"Token for user {username} is: {token}")
            elif choice == "4" or choice == "4.":
                print("Exitting...")
                sys.exit(1)


if __name__ == "__main__":
    app = UserVerificationApp()
    app.start_app()

 # pytest tests/integration_tests.py --cov-report term-missing --cov=user_verification_app

