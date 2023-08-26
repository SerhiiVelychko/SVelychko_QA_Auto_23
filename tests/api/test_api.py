import pytest


class User:
    def __init__(self) -> None:
        self.name = "Serhii"
        self.second_name = "Velychko"


@pytest.fixture
def user():
    yield User()


@pytest.mark.change
def test_remove_name(user):
    user.name = ""
    assert user.name == ""


@pytest.mark.check
def test_name(user):
    assert user.name == "Serhii"


@pytest.mark.check
def test_second_name(user):
    assert user.second_name == "Velychko"
