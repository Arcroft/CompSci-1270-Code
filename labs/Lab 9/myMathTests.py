# Ashlyn Croft
# 22Jul25
# Lab 9
# myMath Unit Tests
# unit tests to identify and debug errors in the myMath module

# I think this works. Idk, This turn and burn schedule has me fried.
# I started working on a literary text analysis script, cause things started to click.
# But there's just too much too fast across all my classes.

import pytest
from myMath import *

def test_add():
    """Test the add function"""
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    assert add(5.5, 2.5) == 8.0
    assert add(-5, 10) == 5

def test_subtract():
    """Test the subtract function"""
    assert subtract(5, 3) == 2
    assert subtract(10, 15) == -5
    assert subtract(0, 0) == 0
    assert subtract(-5, -3) == -2
    assert subtract(7.5, 2.5) == 5.0

def test_multiply():
    """Test the multiply function"""
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0
    assert multiply(-3, -4) == 12
    assert multiply(2.5, 4) == 10.0

def test_divide():
    """Test the divide function"""
    assert divide(10, 2) == 5
    assert divide(15, 3) == 5
    assert divide(-10, 2) == -5
    assert divide(7, 2) == 3.5
    
    # should raise an exception
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_power():
    """Test the power function"""
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(10, 1) == 10
    assert power(-2, 3) == -8
    assert power(4, 0.5) == 2.0

def test_factorial():
    """Test the factorial function"""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(4) == 24
    
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime():
    """Test the is_prime function"""
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(25) == False
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-5) == False

def test_sum_of_digits():
    """Test the sum_of_digits function"""
    assert sum_of_digits(123) == 6
    assert sum_of_digits(456) == 15
    assert sum_of_digits(0) == 0
    assert sum_of_digits(9) == 9

def test_gcd():
    """Test the gcd function"""
    assert gcd(12, 8) == 4
    assert gcd(15, 25) == 5
    assert gcd(7, 3) == 1
    assert gcd(0, 5) == 5
    assert gcd(48, 18) == 6

def test_fib():
    """Test the fib function"""
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8


def test_lcm():
    """Test the lcm function"""
    assert lcm(4, 6) == 12
    assert lcm(15, 20) == 60
    assert lcm(7, 3) == 21
    assert lcm(12, 8) == 24






def test_square_root():
    """Test the square_root function"""
    assert square_root(4) == 2.0
    assert square_root(9) == 3.0
    assert square_root(16) == 4.0
    assert square_root(0) == 0.0
    assert abs(square_root(2) - 1.4142135623730951) < 1e-10
    



def test_abs_diff():
    """Test the abs_diff function"""
    assert abs_diff(5, 3) == 2
    assert abs_diff(3, 5) == 2
    assert abs_diff(-5, 3) == 8
    assert abs_diff(0, 0) == 0
    assert abs_diff(-10, -5) == 5

def test_log():
    """Test the log function"""
    assert abs(log(100, 10) - 2.0) < 1e-10
    assert abs(log(8, 2) - 3.0) < 1e-10
    assert abs(log(1, 10) - 0.0) < 1e-10
    
    with pytest.raises(ValueError):
        log(0, 10)
    
    with pytest.raises(ValueError):
        log(-5, 10)

def test_mod():
    """Test the mod function"""
    assert mod(10, 3) == 1
    assert mod(15, 4) == 3
    assert mod(20, 5) == 0
    assert mod(-7, 3) == 2  



def test_mean():
    """Test the mean function"""
    assert mean([1, 2, 3, 4, 5]) == 3.0
    assert mean([10, 20, 30]) == 20.0
    assert mean([5]) == 5.0
    assert mean([-2, 0, 2]) == 0.0
    


def test_median():
    """Test the median function"""
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 3, 4]) == 2.5
    assert median([5, 1, 3]) == 3
    assert median([10]) == 10
    assert median([1, 1, 1]) == 1

def test_mode():
    """Test the mode function"""
    assert mode([1, 2, 2, 3, 3, 3]) == 3
    assert mode([1, 1, 2, 2]) in [1, 2]  
    assert mode([5]) == 5
    assert mode([1, 2, 3, 1]) == 1
    


def test_celsius_to_fahrenheit():
    """Test the celsius_to_fahrenheit function"""
    # Formula should be: F = C * 9/5 + 32
    assert celsius_to_fahrenheit(0) == 32.0  # Freezing point
    assert celsius_to_fahrenheit(100) == 212.0  # Boiling point
    assert celsius_to_fahrenheit(-40) == -40.0  # Where C and F are equal
    assert celsius_to_fahrenheit(20) == 68.0  # Room temperature

def test_fahrenheit_to_celsius():
    """Test the fahrenheit_to_celsius function"""
    # Formula should be: C = (F - 32) * 5/9
    assert abs(fahrenheit_to_celsius(32) - 0.0) < 1e-10  # Freezing point
    assert abs(fahrenheit_to_celsius(212) - 100.0) < 1e-10  # Boiling point
    assert abs(fahrenheit_to_celsius(-40) - (-40.0)) < 1e-10  # Where C and F are equal
    assert abs(fahrenheit_to_celsius(68) - 20.0) < 1e-10  # Room temperature

def test_inverse():
    """Test the inverse function"""
    assert inverse(2) == 0.5
    assert inverse(4) == 0.25
    assert inverse(-2) == -0.5
    assert inverse(0.5) == 2.0
    


def test_triangular_number():
    """Test the triangular_number function"""
    assert triangular_number(1) == 1
    assert triangular_number(2) == 3
    assert triangular_number(3) == 6
    assert triangular_number(4) == 10
    assert triangular_number(5) == 15
    assert triangular_number(0) == 0


def test_edge_cases():
    """Test various edge cases that might reveal bugs"""
    
    # sum_of_digits with negative numbers
    try:
        result = sum_of_digits(-123)
        print(f"sum_of_digits(-123) = {result}")
    except:
        print("sum_of_digits fails with negative numbers")
    
    # temperature conversions with known values
    try:
        c_to_f = celsius_to_fahrenheit(0)
        f_to_c = fahrenheit_to_celsius(32)
        print(f"0°C to °F: {c_to_f} (should be 32)")
        print(f"32°F to °C: {f_to_c} (should be 0)")
    except:
        print("Temperature conversion issues")

if __name__ == "__main__":
    test_edge_cases()