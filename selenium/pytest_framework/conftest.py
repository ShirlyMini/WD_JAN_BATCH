import pytest
@pytest.fixture()
def setup():
    # setup
    print("Launch browser")
    print("login into application")
    yield True, True
    # teardown(clean up)
    print("Logout")
    print("close browser")

@pytest.fixture(scope='class')
def setup_class():
    # setup
    print("SETUP CLASS")
    yield
    # teardown(clean up)
    print("TEARDOWN CLASS")

@pytest.fixture(scope='module')
def setup_module():
    # setup
    print("SETUP MODULE")
    yield
    # teardown(clean up)
    print("TEARDOWN MODULE")

###############################Marker

def pytest_configure(config):
    config.addinivalue_line("markers", "TC1: describe it as functional testing")
    config.addinivalue_line("markers", "TC2: describe it as sanity testing")