#!/usr/bin/env python3

from functools import reduce


def split_bill(items: list, emails: list) -> dict:
    if len(emails) < 1:
        return {}
    total_price = reduce(lambda acc, item: acc + item['price'] * item['quantity'], items, 0)
    amount_due_per_person = total_price // len(emails)
    splitted_bill = dict.fromkeys(emails, amount_due_per_person)
    amount_left_to_pay = total_price - amount_due_per_person * len(emails)
    for index in range(amount_left_to_pay):
        splitted_bill[emails[index]] += 1
    return splitted_bill
