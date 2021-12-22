from argparse import ArgumentParser
import pickle


def get_argument():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('amount')
    args = argument_parser.parse_args()
    amount = float(args.amount)
    return amount


def get_balance_amounts():
    file_name = "balance.p"
    amount = get_argument()
    with open(file_name, "ab") as f:
        pickle.dump(amount, f)

    with open(file_name, "rb") as f:
        balance_amounts = []
        while True:
            try:
                a = pickle.load(f)
                balance_amounts.append(a)
            except EOFError as e:
                break
    return balance_amounts
