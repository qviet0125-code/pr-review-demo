# Demo

def calc_total(prices):
    total = 0
    for p in prices:
        if p < 0:
            raise ValueError("negative price")
        total += p
    return total / 1.0


def find_user(users, uid):
    for u in users:
        if u["id"] == uid:
            return u


def divide(a, b):
    return a / b