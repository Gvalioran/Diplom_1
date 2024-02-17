import pytest

from praktikum.praktikum import Bun


class TestsBun:

    @pytest.mark.parametrize("test_bun, price", [["Булочка", 100], ["pie", 0], ["BURGER", -300]])
    def test_create_new_bun(self, test_bun, price):
        bun = Bun(test_bun, price)
        assert bun.get_name() == test_bun
        assert bun.get_price() == price
