import ejercicio1
import unittest

class ejercicioTest(unittest.TestCase):
    def testRotarNoTieneNadaDeberiaDevolverListaVacia(self):
        #arrange
        palabra = ""

        #act
        resultado = ejercicio1.rotar(palabra)

        #assert
        self.assertEqual(resultado,[])

    def testRotarSiRecibeVariosEspaciosDeberiaDevolverListaVacia(self):
        palabra = "   "

        resultado = ejercicio1.rotar(palabra)

        self.assertEqual(resultado,[])

    def testRotarSirecibeUnaLetraDeberiaDevolverUnaListaConElElemento(self):
        palabra = 'a'

        resultado = ejercicio1.rotar(palabra)

        self.assertEqual(resultado,['a'])

    def testRotarRecibeAUnaPalabraConDosLetrasDebreriaDevolverUnaListaConDosPalabrasRotadas(self):
        palabra = "ab"

        resultado = ejercicio1.rotar(palabra)

        self.assertEqual(resultado,['ab','ba'])

    def testRotarSirecibeLapalabraConUnaPalabraDeTresLetrasDeberiaDevolverUnaListaConTresPalabrasRotadas(self):
        palabra = "paz"

        resultado = ejercicio1.rotar(palabra)

        self.assertEqual(resultado,['paz','azp','zpa'])

    def testRotarRecibeUnaPalabrasConDosLetrasConUnEspacioYUnaLetraDeberiaDevolverUnaListaConCuatroPalabrasRotadasSinImportarleElEspacio(self):
        palabra = "so l"

        resultado = ejercicio1.rotar(palabra)

        self.assertEqual(resultado,['so l','o ls',' lso','lso '])

    def testRotarSiRecibeUnaPalabraConCincoLetrasDeberiaDevolverUnaListaConCincoPalabrasRotadas(self):
        palabra = "rotar"

        resultadp = ejercicio1.rotar(palabra)

        self.assertEqual(resultadp, ['rotar','otarr','tarro','arrot','rrota'])
