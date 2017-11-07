import ejercicio1
import unittest

class ejercicioTest(unittest.TestCase):
    def testRotarNoTieneNadaDeberiaDevolverListaVacia(self):
        #arrange
        palabra = ""

        #act
        resultado = ejercicio1.rotar(palabra)

        #assert
        self.assertEquals(resultado,[])

    def testRotarSiRecibeVariosEspaciosDeberiaDevolverListaVacia(self):
        palabra = "   "

        resultado = ejercicio1.rotar(palabra)

        self.assertEquals(resultado,[])

    def testRotarSirecibeUnaLetraDeberiaDevolverLoMismo(self):
        palabra = 'a'

        resultado = ejercicio1.rotar(palabra)

        self.assertEquals(resultado,['a'])

    def testRotarSiRecibeabDebreriadevolverabba(self):
        palabra = "ab"

        resultado = ejercicio1.rotar(palabra)

        self.assertEqual(resultado,['ab','ba'])

    def testRotarSirecibeLapalabraPazdeberiaDevolverPazAzpZpa(self):
        palabra = "paz"

        resultado = ejercicio1.rotar(palabra)

        self.assertEqual(resultado,['paz','azp','zpa'])

    def testRotarSiRecibelapalabrasol(self):
        palabra = "so l"

        resultado = ejercicio1.rotar(palabra)

        self.assertEqual(resultado,['so l','o ls',' lso','lso '])

    def testRotarSiRecibePalabraRotar(self):
        palabra = "rotar"

        resultadp = ejercicio1.rotar(palabra)

        self.assertEqual(resultadp, ['rotar','otarr','tarro','arrot','rrota'])
