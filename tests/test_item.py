from src.item import Item
import pytest

@pytest.fixture
def setup_teardown():
    yield
    Item.all.clear()

def test_all_items(setup_teardown):
    item1 = Item("Товар3", 50, 10)
    item2 = Item("Товар4", 75, 7)

    assert len(Item.all) == 2
    assert Item.all[0].name == "Товар3"
    assert Item.all[1].name == "Товар4"
