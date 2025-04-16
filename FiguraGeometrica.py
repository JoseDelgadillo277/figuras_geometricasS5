"""Módulo para el cálculo de áreas de figuras geométricas utilizando clases abstractas."""

from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    """Clase abstracta que define la interfaz para calcular áreas."""

    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de una figura."""
        pass  # noqa: W0107


class Rectangulo(FiguraGeometrica):
    """Representa un rectángulo con base y altura."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura


class Triangulo(FiguraGeometrica):
    """Representa un triángulo con base y altura."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triángulo."""
        return (self.base * self.altura) / 2


class Circulo(FiguraGeometrica):
    """Representa un círculo con un radio dado."""

    def __init__(self, radio):
        self.pi = 3.14159
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        return self.pi * (self.radio ** 2)


# Variables globales
BASE_RECTANGULO = 10
ALTURA_RECTANGULO = 5
BASE_TRIANGULO = 7
ALTURA_TRIANGULO = 4
RADIO_CIRCULO = 3


def main():
    """Función principal para crear figuras y mostrar sus áreas."""
    rectangulo = Rectangulo(BASE_RECTANGULO, ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO, ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
    print(f"El área del triángulo es: {triangulo.calcular_area()}")
    print(f"El área del círculo es: {circulo.calcular_area()}")


if __name__ == "__main__":
    main()
