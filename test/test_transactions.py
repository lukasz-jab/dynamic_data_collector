import time


def test_transactions(app):
    app.navigation.open_home()
    t_end = time.time() + 10
    dirty_transactions_1min = []
    while time.time() < t_end:
        transaction = app.transaction.get()
        dirty_transactions_1min.append(transaction)
    transactions_1min = set(dirty_transactions_1min)
    print()
    print("Len dirty: " + str(len(dirty_transactions_1min)))
    print(("Len clean: ") + str(len(transactions_1min)))
