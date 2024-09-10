# Todas as operações que serão utilizadas na calculadora
import math

def Soma(a, b):
    return a + b

def Subtracao(a, b):
    return a - b

def Multiplicacao(a, b):
    return a * b

def Divisao(a, b):
    if b == 0:
        return 'Erro: Divisão por zero'
    return a / b

def Potencia(a, b):
    return a ** b

def RaizQuadrada(a):
    return math.sqrt(a)

def RestoDivisão(a, b):
    return a % b