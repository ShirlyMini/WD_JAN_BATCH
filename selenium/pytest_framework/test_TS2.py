import pytest


class Test_Suite1:
    @pytest.mark.TC1
    @pytest.mark.skip()
    def test_TC1(self,setup_module, setup):
        print("this is test case 1")

    @pytest.mark.TC2
    @pytest.mark.skipif(4<5, reason="cond is true skipping test case")
    def test_TC2(self,setup):
        print("this is test case 2")