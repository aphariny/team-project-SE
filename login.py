"""Simple demonstration login module for the team shopping project."""

USERS = {
    "admin": "admin123",
    "student": "pass123",
}

def login(username: str, password: str) -> str:
    """Return a simple login status message."""
    if USERS.get(username) == password:
        return "Login successful"
    return "Invalid credentials"


if __name__ == "__main__":
    print(login("admin", "admin123"))
    print(login("student", "wrong"))
