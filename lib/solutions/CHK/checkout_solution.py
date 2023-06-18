

# noinspection PyUnusedLocal
# skus = unicode string

def multi_offers(basket, base_item, offer_qty): # b, A, [5,3]

    curr_qty = basket.get(base_item, 0)

    for q in offer_qty:
        sp_item = str(q) + base_item # 5A
        sp_item_qty = int(curr_qty/q)
        basket[sp_item] = sp_item_qty
        curr_qty = curr_qty - (sp_item_qty * q)
    basket[base_item] = curr_qty


def other_item_free(basket, base_item, qty, free_item):
    free_items_qty = int(basket.get(base_item, 0) / qty)
    basket[free_item] = max(basket.get(free_item, 0) - free_items_qty, 0)

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

    other_item_free(sku_qtys, "E", 2, "B")
    multi_offers(sku_qtys, "A", [5,3])
    multi_offers(sku_qtys, "F", [3])
    multi_offers(sku_qtys, "B", [2])

    total_val = 0
    for item in sku_qtys:
        total_val = total_val + (sku_qtys[item] * prices[item])

    return total_val



