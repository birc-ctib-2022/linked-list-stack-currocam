"""A linked list implementation of a stack."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar('T')


@dataclass
class Link(Generic[T]):
    """A link in a linked list."""

    head: T
    tail: List[T]


List = Optional[Link[T]]

class EmptyStack(Exception):
    pass

class Stack(Generic[T]):
    """A stack of elements of (generic) type T."""

    def __init__(self) -> None:
        """Create a new stack of values of type T."""
        self.link = None

    def push(self, x: T) -> None:
        """Push x on the top of this stack."""
        self.link = Link(x, self.link)


    def top(self) -> T:
        """Return the top of the stack."""
        if self:
            return self.link.head
        raise EmptyStack

    def pop(self) -> T:
        """Pop the top element off the stack and return it."""
        if self:
            val = self.top()
            self.link = self.link.tail
            return val
        raise EmptyStack

    def is_empty(self) -> bool:
        """Test if the stack is empty."""
        return self.link is None
    def __bool__(self) -> bool:
        return not self.is_empty()
