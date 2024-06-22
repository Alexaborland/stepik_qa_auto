import pytest


@pytest.fixture()
def set_up():
    print('Login completed')
    yield
    print('Logout')

@pytest.fixture(scope='module')
def some():
    print('The start')
    yield
    print('The end')
