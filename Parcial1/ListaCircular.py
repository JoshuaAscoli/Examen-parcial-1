from Nodo import Nodo
class ListaCircularDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.primero:

            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.primero.siguiente = self.primero
            self.primero.anterior = self.ultimo

        else:

            nuevo_nodo.siguiente = self.primero
            nuevo_nodo.anterior = self.ultimo
            self.primero.anterior = nuevo_nodo
            self.ultimo.siguiente = nuevo_nodo
            self.primero = nuevo_nodo

    def imprimir_lista(self):
        resultado = " "
        contador = 0
        if not self.primero:
            return

        actual = self.primero
        while actual:
            resultado += str(actual.dato)
            if actual.siguiente != self.primero:
                contador += 1
                resultado += f"x^{contador} -> "

            actual = actual.siguiente
            if actual == self.primero:
                contador += 1
                return resultado

    def imprimir_lista_con_valor(self,dato):
        resultado = " "
        contador = 0
        if not self.primero:
            return

        actual = self.primero
        while actual:
            resultado += str(actual.dato)
            if actual.siguiente != self.primero:
                contador += 1
                resultado += f"({dato})^{contador} -> "

            actual = actual.siguiente
            if actual == self.primero:
                contador += 1
                return resultado

    def eliminar(self, dato):
        if not self.primero:
            return

        actual = self.primero
        while actual.dato != dato:
            actual = actual.siguiente
            if actual == self.primero:
                return

        if actual == self.primero:
            self.primero = actual.siguiente
            self.ultimo.siguiente = self.primero
            self.primero.anterior = self.ultimo
        elif actual == self.ultimo:
            self.ultimo = actual.siguiente
            self.ultimo.siguiente = self.ultimo
            self.primero.anterior = self.primero
        else:
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior

    def actualizar(self, dato_viejo, dato_nuevo):
        if not self.primero:
            return

        actual = self.primero
        while actual.dato != dato_viejo:
            actual = actual.siguiente
            if actual == self.primero:
                return

        actual.dato = dato_nuevo

    def buscar(self, dato):
        if not self.primero:
            return None

        actual = self.primero
        while actual.dato != dato:
            actual = actual.dato.siguiente
            if actual == self.primero:
                return None

        return actual.dato
    def vacio(self):
        if self.primero and self.ultimo is None:
            print('NO HAY DATOS ')