

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # AAABBCD
    if skus == "" or skus is None:
        return -1

    skus = list(skus)

    sku_qtys = {}
    for item in skus:
        if item not in {"A", "B", "C", "D"}:
            return -1
        sku_qtys[item] = sku_qtys.get(item, 0) + 1

    prices = {
        "3A": 130,
        "2B": 45,
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15
    }

    offers_under_A = int(sku_qtys.get("A") / 3)
    offers_under_B = int(sku_qtys.get("B") / 2)

    sku_qtys["3A"] = offers_under_A
    sku_qtys["2B"] = offers_under_B

    sku_qtys["A"] = sku_qtys["A"] % 3
    sku_qtys["B"] = sku_qtys["B"] % 2

    total_val = 0
    for item in sku_qtys:
        total_val = total_val + (sku_qtys[item] * prices[item])

    return total_val


