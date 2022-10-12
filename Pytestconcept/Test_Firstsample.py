import pytest
#class level fixture
@pytest.mark.usefixtures("fixtureconcept")
class Test_firstclass:

    @pytest.mark.sanity
    #@pytest.mark.run(order = 2)
    def test_firstTestcase(self):
        print("This is the first test case")

    @pytest.mark.sanity
    #@pytest.mark.run(order=1)
    def test_secondTestcase(self):
        print("This is the second test case")



# """
# #method level fixture
# import pytest
#
#
# class Test_firstclass:
#
#     @pytest.mark.sanity
#     #@pytest.mark.run(order = 2)
#     def test_firstTestcase(self,fixtureconcept):
#         print("This is the first test case")
#
#     @pytest.mark.sanity
#     #@pytest.mark.run(order=1)
#     def test_secondTestcase(self,fixtureconcept):
#         print("This is the second test case")
#     @pytest.fixture()
#     def fixtureconcept(self):
#         print("Before test case")
#         yield
#         print("After test case") """
