# main.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: Divisao por zero"  # Mensagem em português
    return a / b

if __name__ == "__main__":
    print("Calculadora em Python")
    # Teste simples
    print(f"Adição: 2 + 3 = {add(2, 3)}")
    print(f"Subtração: 5 - 3 = {subtract(5, 3)}")
    print(f"Multiplicação: 4 * 3 = {multiply(4, 3)}")
    print(f"Divisão: 6 / 2 = {divide(6, 2)}")
