from time import strftime, sleep

import pytest
from faker import Faker
from pages.account.create_account import CreateAccountPage


@pytest.fixture
def first_name():
    return Faker().first_name()


@pytest.fixture
def last_name():
    return Faker().last_name()


@pytest.fixture
def email():
    return Faker().email()


@pytest.fixture
def password():
    return Faker().password()


@pytest.fixture
def create_account(driver):
    CreateAccountPage(driver)
