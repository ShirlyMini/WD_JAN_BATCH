import pytest


class Test_Suite1:
    @pytest.mark.TC1
    def test_TC1(self, setup_module):
        print("this is test case 1")

    @pytest.mark.TC2
    def test_TC2(self):
        print("this is test case 2")