#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule la factorielle d’un entier n de manière récursive.

    Paramètres:
    n (int): Un entier positif ou nul dont on veut calculer la factorielle.

    Retourne:
    int: La factorielle de n (n!), égale à 1 si n == 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
