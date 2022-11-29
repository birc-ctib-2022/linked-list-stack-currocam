"""Testing our stack implementation."""


import random

import pytest
from stack import EmptyStack, Stack


def test_stack() -> None:
    """I really hope you test your code."""
    stack = Stack()
    x = random.sample(range(10, 300), 5)
    for el in x:
        stack.push(el)
    x.reverse()
    for el in x:
        assert el == stack.pop()


def test_EmptyStack() -> None:
    """I really hope you test your code."""
    stack = Stack()
    stack.push("ashdkjashdjkas")
    stack.pop()
    with pytest.raises(Exception):
        stack.pop()
        


