import pytest


class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Serhii"
        self.second_name = "Velychko"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.mark.change
def test_change_name(user):
    assert user.name == "Serhii"


@pytest.mark.change
def test_change_second_name(user):
    assert user.second_name == "Velychko"


@pytest.mark.check
def test_check_name(user):
    assert user.name == "Serhii"


@pytest.mark.check
def test_check_second_name(user):
    assert user.second_name == "Velychko"
