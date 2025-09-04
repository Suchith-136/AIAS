from Task_4 import ShoppingCart

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 1.5)
    cart.add_item("banana", 2.0)
    assert cart.items == {"apple": 1.5, "banana": 2.0}

def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("apple", 1.5)
    cart.add_item("banana", 2.0)
    cart.remove_item("apple")
    assert cart.items == {"banana": 2.0}

def test_remove_item_not_in_cart():
    cart = ShoppingCart()
    cart.add_item("apple", 1.5)
    cart.remove_item("banana")  # Should not raise error
    assert cart.items == {"apple": 1.5}

def test_total_cost():
    cart = ShoppingCart()
    cart.add_item("apple", 1.5)
    cart.add_item("banana", 2.0)
    cart.add_item("orange", 3.0)
    assert cart.total_cost() == 6.5

def test_total_cost_empty_cart():
    cart = ShoppingCart()
    assert cart.total_cost() == 0