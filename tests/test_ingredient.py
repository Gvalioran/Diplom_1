import pytest

from praktikum.praktikum import Ingredient


class TestsIngredient:

    @pytest.mark.parametrize("test_ingredient_type, test_ingredient, price",
                             [["Тип", "Булочка", 100], ["type", "pie", 0], ["TYPE", "BURGER", -300]])
    def test_create_new_ingredient(self, test_ingredient_type, test_ingredient, price):
        ingredient = Ingredient(test_ingredient_type, test_ingredient, price)
        assert ingredient.get_type() == test_ingredient_type
        assert ingredient.get_name() == test_ingredient
        assert ingredient.get_price() == price
