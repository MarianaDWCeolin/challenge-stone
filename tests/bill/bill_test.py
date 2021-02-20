#!/usr/bin/env python3

from challenge_stone_co.bill import split_bill


def test_empty_lists():
    assert split_bill([], []) == {}


def test_empty_emails():
    assert (
        split_bill([{"price": 20, "quantity": 2}, {"price": 300, "quantity": 1}], [])
        == {}
    )


def test_empty_items():
    assert split_bill([], ["someone@example.com"]) == {"someone@example.com": 0}


def test_handle_decimals():
    assert split_bill(
        [{"price": 100, "quantity": 1}],
        ["person1@example.com", "person2@example.com", "person3@example.com"],
    ) == {
        "person1@example.com": 34,
        "person2@example.com": 33,
        "person3@example.com": 33,
    }

    assert split_bill(
        [{"price": 200, "quantity": 1}],
        ["person1@example.com", "person2@example.com", "person3@example.com"],
    ) == {
        "person1@example.com": 67,
        "person2@example.com": 67,
        "person3@example.com": 66,
    }


def test_handle_multiple_items():
    assert split_bill(
        [
            {"price": 200, "quantity": 4},
            {"price": 300, "quantity": 3},
            {"price": 532, "quantity": 33},
        ],
        ["person1@example.com", "person2@example.com", "person3@example.com"],
    ) == {
        "person1@example.com": 6419,
        "person2@example.com": 6419,
        "person3@example.com": 6418,
    }
