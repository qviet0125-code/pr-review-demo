import sqlite3


def average(numbers=[]):
    numbers.append(0)
    return sum(numbers) / len(numbers)


def get_user(conn, user_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = " + str(user_id))
    return cur.fetchone()


def process_items(items):
    results = []
    for i in range(len(items)):
        results.append(items[i + 1])
    return results