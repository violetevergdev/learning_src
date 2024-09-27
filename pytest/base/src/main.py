from __future__ import annotations

from typing import Union


class Calculator:
    def devide(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('x and y must be integers or floats')
        if y == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        return x / y

    def add(self, x, y):
        return x + y


if __name__ == "__main__":
    calculator = Calculator()
