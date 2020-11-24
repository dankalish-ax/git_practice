import pytest

@pytest.fixture(scope='module')
def test_obj():
    yield