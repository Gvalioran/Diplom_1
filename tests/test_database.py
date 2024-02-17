from praktikum.praktikum import Database
import pytest


class TestsIngredient:

    @pytest.mark.parametrize("bun, price, num", [["black bun", 100, 0], ["white bun", 200, 1], ["red bun", 300, 2]])
    def test_database_get_bun(self, bun, price, num):
        assert Database().available_buns()[num].get_name() == bun
        assert Database().available_buns()[num].get_price() == price

    @pytest.mark.parametrize("ingredient, price, test_type, num",
                             [["hot sauce", 100, "SAUCE", 0], ["sour cream", 200, "SAUCE", 1],
                              ["chili sauce", 300, "SAUCE", 2], ["cutlet", 100, "FILLING", 3],
                              ["dinosaur", 200, "FILLING", 4], ["sausage", 300, "FILLING", 5]])
    def test_database_get_ingredient(self, ingredient, price, test_type, num):
        assert Database().available_ingredients()[num].get_name() == ingredient
        assert Database().available_ingredients()[num].get_price() == price
        assert Database().available_ingredients()[num].get_type() == test_type
