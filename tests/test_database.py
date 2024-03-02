from praktikum.praktikum import Database
import pytest


class TestsIngredient:

    @pytest.mark.parametrize("bun, num", [["black bun", 0], ["white bun", 1], ["red bun", 2]])
    def test_database_bun_get_name(self, bun, num):
        assert Database().available_buns()[num].get_name() == bun

    @pytest.mark.parametrize("price, num", [[100, 0], [200, 1], [300, 2]])
    def test_database_bun_get_price(self, price, num):
        assert Database().available_buns()[num].get_price() == price

    @pytest.mark.parametrize("ingredient, num", [["hot sauce", 0], ["sour cream", 1], ["chili sauce", 2],
                                                 ["cutlet", 3], ["dinosaur", 4], ["sausage", 5]])
    def test_database_get_ingredient_get_name(self, ingredient, num):
        assert Database().available_ingredients()[num].get_name() == ingredient

    @pytest.mark.parametrize("price, num", [[100, 0], [200, 1], [300, 2], [100, 3], [200, 4], [300, 5]])
    def test_database_get_ingredient_get_price(self, price, num):
        assert Database().available_ingredients()[num].get_price() == price

    @pytest.mark.parametrize("test_type, num", [["SAUCE", 0], ["SAUCE", 1], ["SAUCE", 2],
                                                ["FILLING", 3], ["FILLING", 4], ["FILLING", 5]])
    def test_database_get_ingredient_get_type(self, test_type, num):
        assert Database().available_ingredients()[num].get_type() == test_type
