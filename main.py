
from math import sqrt

#### Fonction secondaire


def isprime(p):

    """
    Détermine si un entier p est un nombre premier.
    Args:
        p (int): Entier à tester.
    Returns:
        bool: True si p est premier, False sinon.
    """
    if p < 2:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for i in range(3, int(sqrt(p)) + 1, 2):
        if p % i == 0:
            return False
    return True

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    """
    Fonction principale pour tester la fonction isprime sur les entiers de 0 à 99.
    """
    premiers = [str(n) for n in range(100) if isprime(n)]
    print(", ".join(premiers))


if __name__ == "__main__":
    main()
