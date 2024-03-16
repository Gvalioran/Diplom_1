import pytest

from praktikum.praktikum import Ingredient


class TestsIngredient:

    @pytest.mark.parametrize("test_ingredient_type", ["Тип", "type", "TYPE"])
    def test_create_new_ingredient_get_type(self, test_ingredient_type):
        ingredient = Ingredient(test_ingredient_type, "BURGER", 100)
        assert ingredient.get_type() == test_ingredient_type

    @pytest.mark.parametrize("test_ingredient", ["Булочка", "pie", "BURGER"])
    def test_create_new_ingredient_get_name(self, test_ingredient):
        ingredient = Ingredient("Тип", test_ingredient, 100)
        assert ingredient.get_name() == test_ingredient

    @pytest.mark.parametrize("price", [100, 0, -300])
    def test_create_new_ingredient_get_price(self, price):
        ingredient = Ingredient("Тип", "BURGER", price)
        assert ingredient.get_price() == price
