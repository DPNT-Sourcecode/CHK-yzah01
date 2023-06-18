

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if skus == "":
        return 0

    if skus is None or type(skus) is not str:
        return -1

    skus = list(skus)

    sku_qtys = {}
    for item in skus:
        if item not in {"A", "B", "C", "D", "E", "F"}:
            return -1
        sku_qtys[item] = sku_qtys.get(item, 0) + 1

    prices = {
        "5A": 200,
        "3A": 130,
        "2B": 45,
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "3F": 20
    }

    qty_5A = int(sku_qtys.get("A", 0) / 5)
    item_A_left = sku_qtys.get("A", 0) - (qty_5A*5)
    qty_3A = int(item_A_left / 3)

    qty_free_B = int(sku_qtys.get("E", 0) / 2)

    sku_qtys["B"] = max(sku_qtys.get("B", 0) - qty_free_B, 0)

    qty_2B = int(sku_qtys.get("B", 0) / 2)


    sku_qtys["5A"] = qty_5A
    sku_qtys["3A"] = qty_3A
    sku_qtys["2B"] = qty_2B

    sku_qtys["A"] = sku_qtys.get("A", 0) - ((qty_5A * 5) + (qty_3A * 3))

    sku_qtys["B"] = max(sku_qtys.get("B", 0) - (qty_2B * 2), 0)

    qty_3F = int(sku_qtys.get("F", 0) / 3)
    qty_F = sku_qtys.get("F", 0) - (qty_3F * 3)

    sku_qtys["3F"] = qty_3F
    sku_qtys["F"] = qty_F

    total_val = 0
    for item in sku_qtys:
        total_val = total_val + (sku_qtys[item] * prices[item])

    return total_val

