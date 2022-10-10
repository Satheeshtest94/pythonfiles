import pytest

@pytest.mark.usefixtures("fixtureconcept")
class Test_secondclass:

    @pytest.mark.sanity
    def test_thirdTestcase(self):
        print("This is the third test case")
#pre defined test cases
    @pytest.mark.skip
    @pytest.mark.sanity
    def test_fourthTestcase(self):
        print("This is the fourth test case")

    @pytest.mark.sanity
    def test_fourthTestcase(self):
        print("This is the latest test case")

    @pytest.mark.regression
    def test_fifthTestcase(self):
        print("This is the fifth test case")

