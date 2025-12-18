import pytest
from temperature import celsius_to_fahrenheit, celsius_to_kelvin, fahrenheit_to_celsius, fahrenheit_to_kelvin, kelvin_to_celsius, kelvin_to_fahrenheit

def test_celsius_to_fahrenheit():
    # Test freezing point
    assert celsius_to_fahrenheit(0) == 32
    # Test boiling point
    assert celsius_to_fahrenheit(100) == 212
    # Test body temp
    assert round(celsius_to_fahrenheit(37), 1) == 98.6

def test_fahrenheit_to_celsius():
    # Test freezing point
    assert fahrenheit_to_celsius(32) == 0
    # Test negative temperature
    assert fahrenheit_to_celsius(-40) == -40

def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == 273.15

def test_kelvin_to_celsius():
    assert kelvin_to_celsius(273.15) == 0

def test_fahrenheit_to_kelvin():
    assert round(fahrenheit_to_kelvin(32), 2) == 273.15 

def test_kelvin_to_fahrenheit():
    assert round(kelvin_to_fahrenheit(273.15), 2) == 32

    