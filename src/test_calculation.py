import pytest
import calculation


# class caltest(unittest.testcase):
#     def test_add_num_and_double(self):
#         cal = calculation.cal()
#         self.assertequal(cal.add_num_and_double(1, 1), 4)
#
#     def test_add_num_and_double_raise(self):
#         cal = calculation.cal()
#         with self.assertraises(valueerror):
#             cal.add_num_and_double("1", "1")
#
#
# if __name__ == "__main__":
#     unittest.main()
#


# def test_add_num_and_double():
#     cal = calculation.Cal()
#     assert cal.add_num_and_double(1, 1) == 4
#


class TestCal:
    def setup_method(self, method):
        print(f"method={method}")
        self.cal = calculation.Cal()

    def teardown_method(self, method):
        print(f"method={method}")
        del self.cal

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double("1", "1")
