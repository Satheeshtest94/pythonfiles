import pytest


@pytest.fixture(scope="class")
def fixtureconcept():
    print("Before test case")
    yield
    print("After test case")