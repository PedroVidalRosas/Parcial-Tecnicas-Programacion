import ejercicio3
import unittest

class Ejercicio3Test(unittest.TestCase):
    def testCalcularGanadorSirecibeUnaListaVaciaDeberiaDevolverUnaListaVacia(self):
        tupla = []

        resultado = ejercicio3.calcularGanador(tupla)

        self.assertEqual(resultado,"")

    def testCalcularGanadorSiRecibeA1yB0DeberiaDevolverA(self):
        tupla = [("a", 1, "b", 0)]

        resultado = ejercicio3.calcularGanador(tupla)

        self.assertEqual(resultado,"a")

    def testCalcularGanadorSiReciveMasLIstas(self):
        tupla = [("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]

        resultado = ejercicio3.calcularGanador(tupla)

        self.assertEqual(resultado,"c")

    def testCalcularGanadorSiRecibeTodosEmpatadosDeberiaDevolverAlfabeticamenteElprimero(self):
        tupla = [("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]

        resultado = ejercicio3.calcularGanador(tupla)

        self.assertEqual(resultado,"Almagro")

    def testCalcularGanador(self):
        tupla = [("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]

        resultado = ejercicio3.calcularGanador(tupla)

        self.assertEqual(resultado,"a")
