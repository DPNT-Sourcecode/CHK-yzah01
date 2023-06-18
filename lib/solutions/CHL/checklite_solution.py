

# noinspection PyUnusedLocal
# skus = unicode string

def checklite(skus): # AAABBCD

    skus = list(skus)
    sku_qtys = {}
    for item in skus:
        sku_qtys[item] = sku_qtys.get(item, 0) + 1

    prices = {
        "3A": 130,
        "2B": 45,
        "A" : 50,
        "B" : 30,
        "C" : 20,
        "D" : 15
    }

    offer_under_A = int(sku_qtys.get("A")/3)



