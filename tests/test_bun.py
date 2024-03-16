import pytest

from praktikum.praktikum import Bun


class TestsBun:

    @pytest.mark.parametrize("test_bun", ["Булочка", "pie", "BURGER"])
    def test_create_new_bun_get_name(self, test_bun):
        bun = Bun(test_bun, 100)
        assert bun.get_name() == test_bun

    @pytest.mark.parametrize("price", [100, 0, -300])
    def test_create_new_bun_get_price(self, price):
        bun = Bun("BURGER", price)
        assert bun.get_price() == price
