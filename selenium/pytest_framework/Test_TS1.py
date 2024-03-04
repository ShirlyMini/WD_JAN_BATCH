import pytest
class Test_Suite1:
    @pytest.mark.TC1
    @pytest.mark.xfail
    def test_TC1(self,setup, setup_class,setup_module):
        var1 = setup[0]
        var2 = setup[1]
        print("this is test case 1", var1, var2)
        # assert False

    @pytest.mark.TC2
    def test_TC2(self,setup):
        print("this is test case 2")

    @pytest.mark.parametrize("a,b,c", [(1,2,3), (20,30,40),(100,200,300)])
    def test_addition(self, a,b,c):
        print(f"{a}+{b}+{c}={a + b +c}")

    @pytest.mark.parametrize("a", ["apple", "orange", "kiwi"])
    def test_print(self, a):
        print(f"{a}")

