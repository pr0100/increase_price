import math


def increase_price(d):
    for key in d:
        d[key] = round(d[key] * 1.15)
        if d[key] % 10 > 5:
            d[key] = math.ceil(d[key] / 10) * 10
        if d[key] % 10 < 5:
            d[key] = math.floor(d[key] / 10) * 10
    return d


dict = {
    "apple": 800,
    "banana": 600,
    "milk": 120}
increase_price(dict)
print(dict)
