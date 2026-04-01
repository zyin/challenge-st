#!/usr/bin/env python3

def sort(width: int, height: int, length: int, mass: int) -> str:
    result = ("STANDARD", "SPECIAL", "REJECTED")
    LENGTH_LIMIT = 150           # UNIT = cm
    MASS_LIMIT = 20              # UNIT = kg
    DIMENSION_LIMIT = 1_000_000  # UNIT = cm^3

    # The width, height, length, and mass of the package must be positive integers. If any of these values is zero or negative, the function should raise a ValueError with the message "Negative value is not allowed".
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("Negative or zero value is not allowed")

    volume = width * height * length
    idx = 0
    if volume >= DIMENSION_LIMIT or width >= LENGTH_LIMIT or height >= LENGTH_LIMIT or length >= LENGTH_LIMIT:
        idx = 1

    if mass >= MASS_LIMIT:
        idx += 1

    return result[idx]
