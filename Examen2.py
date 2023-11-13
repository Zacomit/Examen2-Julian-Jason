import unittest

class MiClase:
    def __init__(self, Valencia, Tempo, Tonos, listaCanciones, listaBailabilidad):
        self.Valencia = Valencia
        self.Tempo = Tempo
        self.Tonos = Tonos
        self.listaCanciones = listaCanciones
        self.listaBailabilidad = listaBailabilidad

    def ObtieneValencia(self, numero):
        # Convierte el número en una cadena para contar los dígitos impares
        numero_str = str(numero)
        digitos_impares = [int(digit) for digit in numero_str if int(digit) % 2 != 0]
        return len(digitos_impares)

    def DivisibleTempo(self, numero):
        divisores = [i for i in range(1, numero + 1) if numero % i == 0]
        return divisores

    def ObtieneMasBailable(self, lista):
        if not lista:
            return None
        return max(lista)

    def VerificaListaCanciones(self, lista):
        if any(song is None for song in lista):
            return False
        return True

    def Encuentra(self, lista, elemento): return elemento in lista
    
################################################################################################
#Ejemplo de ejecución
# Crear un objeto de la clase MiClase
objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
# Ejemplo de uso de los métodos
print(objeto.ObtieneValencia(1234567))  # Debería imprimir 4
print(objeto.DivisibleTempo(10))  # Debería imprimir [1, 2, 5, 10]
print(objeto.ObtieneMasBailable([0.8, 0.9, 0.7]))  # Debería imprimir 0.9
print(objeto.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"]))  # Debería imprimir True

################################################################################################
# Pruebas

class TestMiClase(unittest.TestCase):

    def test_obtiene_valencia(self):
        mi_instancia = MiClase(Valencia=1, Tempo=120, Tonos="C", listaCanciones=[...], listaBailabilidad=[...])
        self.assertEqual(mi_instancia.ObtieneValencia(13579), 5)

        mi_instancia_otra_prueba = MiClase(Valencia=2, Tempo=150, Tonos="D", listaCanciones=[...], listaBailabilidad=[...])
        self.assertEqual(mi_instancia_otra_prueba.ObtieneValencia(24680), 0)

    def test_divisible_tempo(self):
        mi_instancia = MiClase(Valencia=1, Tempo=120, Tonos="C", listaCanciones=[...], listaBailabilidad=[...])
        self.assertEqual(mi_instancia.DivisibleTempo(7), [1, 7])

        mi_instancia_otra_prueba = MiClase(Valencia=2, Tempo=150, Tonos="D", listaCanciones=[...], listaBailabilidad=[...])
        self.assertEqual(mi_instancia_otra_prueba.DivisibleTempo(12), [1, 2, 3, 4, 6, 12])

    def test_obtiene_mas_bailable(self):
        mi_instancia = MiClase(Valencia=1, Tempo=120, Tonos="C", listaCanciones=[...], listaBailabilidad=[...])
        self.assertEqual(mi_instancia.ObtieneMasBailable([0.2, 0.5, 0.8]), 0.8)

        mi_instancia_otra_prueba = MiClase(Valencia=2, Tempo=150, Tonos="D", listaCanciones=[...], listaBailabilidad=[...])
        self.assertIsNone(mi_instancia_otra_prueba.ObtieneMasBailable([]))

    def test_verifica_lista_canciones(self):
        mi_instancia = MiClase(Valencia=1, Tempo=120, Tonos="C", listaCanciones=[...], listaBailabilidad=[...])
        self.assertTrue(mi_instancia.VerificaListaCanciones([1, 2, 3]))

        mi_instancia_otra_prueba = MiClase(Valencia=2, Tempo=150, Tonos="D", listaCanciones=[...], listaBailabilidad=[...])
        self.assertFalse(mi_instancia_otra_prueba.VerificaListaCanciones([1, None, 3]))


if __name__ == '__main__':
    unittest.main()
