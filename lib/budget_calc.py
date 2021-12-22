from lib.input_amount import get_balance_amounts


def calculate_balance():
    balance_amounts = get_balance_amounts()
    total_balance = sum(balance_amounts)
    print(balance_amounts, f"\ntotal sum: {total_balance}")
