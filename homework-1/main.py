from src.item import Item

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    print(f"{item1.name}: {item1.calculate_total_price()}")  # Смартфон: 200000 (Общая стоимость без скидки)
    print(f"{item2.name}: {item2.calculate_total_price()}")  # Ноутбук: 100000 (Общая стоимость без скидки)

    # Устанавливаем новый уровень цен (скидку)
    Item.set_discount_rate(0.8)
    # Применяем скидку
    item1.apply_discount()

    print(f"{item1.name}: {item1.price}")  # Смартфон: 8000.0 (Цена с учетом скидки)
    print(f"{item2.name}: {item2.price}")  # Ноутбук: 20000 (Без изменений)

    print(Item.all)  # [item1, item2]

