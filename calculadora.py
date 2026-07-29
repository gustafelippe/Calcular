"""Calculadora básica — projeto-base do curso de Git e CI/CD (ESCOLA FPFtech)."""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

LIST DE ALTERAR