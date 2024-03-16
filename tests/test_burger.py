from unittest.mock import Mock

from praktikum.burger import Burger


class TestsBurger:

    def test_set_buns_get_name(self):
        mock = Mock()
        mock.get_name.return_value = "Булочка"
        burger = Burger()
        burger.set_buns(mock)
        assert burger.bun.get_name() == mock.get_name()

    def test_set_buns_get_price(self):
        mock = Mock()
        mock.get_price.return_value = 412
        burger = Burger()
        burger.set_buns(mock)
        assert burger.bun.get_price() == mock.get_price()

    def test_set_buns_burger_get_price(self):
        mock = Mock()
        mock.get_price.return_value = 412
        burger = Burger()
        burger.set_buns(mock)
        assert burger.get_price() == mock.get_price() * 2

    def test_add_ingredient_get_name(self):
        mock = Mock()
        mock.get_name.return_value = "Горчичный"
        burger = Burger()
        burger.add_ingredient(mock)
        assert burger.ingredients[0].get_name() == mock.get_name()

    def test_add_ingredient_get_price(self):
        mock = Mock()
        mock.get_price.return_value = 322
        burger = Burger()
        burger.add_ingredient(mock)
        assert burger.ingredients[0].get_price() == mock.get_price()

    def test_add_ingredient_get_type(self):
        mock = Mock()
        mock.get_type.return_value = "SAUCE"
        burger = Burger()
        burger.add_ingredient(mock)
        assert burger.ingredients[0].get_type() == mock.get_type()

    def test_remove_ingredient(self):
        mock = Mock()
        burger = Burger()
        burger.add_ingredient(mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        first_ingredient = Mock()
        last_ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(last_ingredient)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == last_ingredient and burger.ingredients[1] == first_ingredient

    def test_get_price(self):
        mock = Mock()
        burger = Burger()
        mock.get_price.return_value = 412
        burger.set_buns(mock)
        burger.add_ingredient(mock)
        assert burger.get_price() == mock.get_price() * 3

    def test_get_receipt(self):
        mock = Mock()
        burger = Burger()
        mock.get_name.return_value = "Тест"
        mock.get_price.return_value = 231
        mock.get_type.return_value = "FILLING"
        burger.set_buns(mock)
        burger.add_ingredient(mock)
        expected_result = "(==== Тест ====)\n= filling Тест =\n(==== Тест ====)\n\nPrice: 693"
        assert burger.get_receipt() == expected_result
