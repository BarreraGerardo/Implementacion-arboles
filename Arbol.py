class Nodo:
    def __init__(self, valor):
        self.dato = valor
        self.izquierdo = None
        self.derecho = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.dato:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierdo)
        elif valor > nodo_actual.dato:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecho)

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None:
            return False
        if valor == nodo_actual.dato:
            return True
        elif valor < nodo_actual.dato:
            return self._buscar_recursivo(valor, nodo_actual.izquierdo)
        else:
            return self._buscar_recursivo(valor, nodo_actual.derecho)

    def inorder_traversal(self):
        if self.raiz is None:
            return

        pila = []
        nodo_actual = self.raiz

        while pila or nodo_actual:
            while nodo_actual:
                pila.append(nodo_actual)
                nodo_actual = nodo_actual.izquierdo

            nodo_actual = pila.pop()
            print(nodo_actual.dato, end=" ")

            nodo_actual = nodo_actual.derecho

# Ejemplo de uso
arbol = Arbol()
valores = [5, 3, 7, 4, 2, 6, 8]

for valor in valores:
    arbol.insertar(valor)

print("Inorder traversal del árbol:")
arbol.inorder_traversal()
print()

# Buscando un valor en el árbol
buscar_valor = 4
if arbol.buscar(buscar_valor):
    print(f"El valor {buscar_valor} está en el árbol.")
else:
    print(f"El valor {buscar_valor} no está en el árbol.")