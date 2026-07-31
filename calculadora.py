"""Calculadora básica — projeto-base do curso de Git e CI/CD (ESCOLA FPFtech)."""


def somar(a):
    soma = 0
    for _ in range(a):
        b =  float(input("Insira um numero: "))
        soma += b

    return soma


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b

def potencia(a, b):
	return pow(a,b)

def raiz(a,b):
	return pow(a,(1/b))