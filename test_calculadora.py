import pytest
from main import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(6, 2) == 3
    assert divide(6, 0) == "Erro: Divisao por zero"  # Mensagem em português
