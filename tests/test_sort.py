#!/usr/bin/env python3
import pytest
from sort.sort import sort

def test_sort_with_valid_input():
    data = [10, 10, 10, 10]
    assert sort(*data) == "STANDARD"

def test_sort_with_zero_size():
    data = [0, 10, 10, 10]
    try:
        sort(*data)
        assert False, "Expected ValueError for zero width"
    except ValueError as e:
        assert str(e) == "Negative or zero value is not allowed"

def test_sort_with_zero_mass():
    data = [10, 10, 10, 0]
    try:
        sort(*data)
        assert False, "Expected ValueError for zero mass"
    except ValueError as e:
        assert str(e) == "Negative or zero value is not allowed"

def test_sort_with_exceeding_dimension():
    data = [150, 10, 10, 10]
    try:
        assert sort(*data) == "SPECIAL"
    except ValueError as e:
        assert str(e) == "Negative or zero value is not allowed"

def test_sort_with_exceeding_mass():
    data = [10, 10, 10, 20]
    try:
        assert sort(*data) == "SPECIAL"
    except ValueError as e:
        assert str(e) == "Negative or zero value is not allowed"

def test_sort_with_exceeding_dimension_and_mass():
    data = [150, 10, 10, 20]
    try:
        assert sort(*data) == "REJECTED"
    except ValueError as e:
        assert str(e) == "Negative or zero value is not allowed"