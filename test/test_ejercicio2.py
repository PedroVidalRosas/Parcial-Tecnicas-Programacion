import ejercicio2
import unittest

class Ejercicio2Test(unittest.TestCase):
    def testPedroSirecibeUnaListaVaciaDeberiaDevolverUnaListaVacia(self):
        mapa = []
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]

        resultado = ejercicio2.pedro(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[])

    def testPedroSirecibeUnMapaSinNada(self):
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = ""

        resultado = ejercicio2.pedro(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[])

    def testPedroSiRecibeUnMapaConVariosEspacios(self):
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = "       "

        resultado = ejercicio2.pedro(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[])

    def testPedroSiResiveUnaStrDeberiaDevolverUnaListaVacia(self):
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = "no soy valido"

        resultado = ejercicio2.pedro(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[])

    def testPedroSiRecibeUnaCadenaDeStrDeberiaDevolverUnaListaVacia(self):
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = "yo","tambien","soy","invalido"

        resultado = ejercicio2.pedro(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[])
    def testpedroSirecibeUnMapaConDistintosLenDeberiaDevolverUnaListaVacia(self):
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = ["b.b.","....","..bb","b.b"]

        resultado = ejercicio2.pedro(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[])

    def testPedroSiRecibeUnMapaValidoDeberiaDevolverLasPocicionesDeLosBarcosVivos(self):
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = ["b.b..","b...b",".....","....b"]

        resultado = ejercicio2.pedro(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[(2,1),(2,5)])
    def testPedroSiLosTirosEstanVaciosDeberiaDevolverLosBarcosVivos(self):
        posicionesDeDisparosDePrueba = []
        mapa = ["b..","...","..b"]

        resultado = ejercicio2.pedro(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[(1,1),(3,3)])
