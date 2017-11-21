import ejercicio2
import unittest

class Ejercicio2Test(unittest.TestCase):

    def testPosicionesDeBarcosSinHundirSirecibeUnMapaVacioDeberiaDevolverUnaListaDePosicionesVacios(self):
        mapa = []
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]

        resultado = ejercicio2.posicionesDeBarcosSinHundir(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[])

    def testPosicionesDeBarcosSinHundirSirecibeUnMapaInvalidoDeberiaDevolverUnaListaDePosicionesVacia(self):
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = ""

        resultado = ejercicio2.posicionesDeBarcosSinHundir(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[])

    def testPosicionesDeBarcosSinHundirSiRecibeUnMapaInvalidoConEspaciosDeberiaDevolverUnaListaDePosicionesvacia(self):
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = "       "

        resultado = ejercicio2.posicionesDeBarcosSinHundir(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[])

    def testPosicionesDeBarcosSinHundirSiResiveUnMapaInvalidoConTresPalabrasDeberiaDevolverUnaListaDePosicionesvacia(self):
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = "no soy valido"

        resultado = ejercicio2.posicionesDeBarcosSinHundir(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[])

    def testPosicionesDeBarcosSinHundirSiRecibeMapaInvalidoConPalabrasYComasEntreEllasDeberiaDevolverUnaListaDePsocionesVacio(self):
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = "yo","tambien","soy","invalido"

        resultado = ejercicio2.posicionesDeBarcosSinHundir(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[])
    def testPosicionesDeBarcosSinHundirSirecibeUnMapaConDistintosLongitudDeCadenasDeberiaDevolverUnaListaVacia(self):
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = ["b.b.","....","..bb","b.b"]

        resultado = ejercicio2.posicionesDeBarcosSinHundir(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[])

    def testPosicionesDeBarcosSinHundirSiRecibeUnMapaValidoDeberiaDevolverLasPocicionesDeBarcosSinHundir(self):
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = ["b.b..","b...b",".....","....b"]

        resultado = ejercicio2.posicionesDeBarcosSinHundir(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[(2,1),(2,5)])
    def testPosicionesDeBarcosSinHundirSiLosTirosEstanVaciosDeberiaDevolverLosposicionesDeBarcosSinHundir(self):
        posicionesDeDisparosDePrueba = []
        mapa = ["b..","...","..b"]

        resultado = ejercicio2.posicionesDeBarcosSinHundir(mapa,posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[(1,1),(3,3)])
