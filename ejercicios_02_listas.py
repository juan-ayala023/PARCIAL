# =============================================================================
# EJERCICIOS — LISTAS ENLAZADAS Y RECURSIVIDAD
# =============================================================================

class Nodo:
    def __init__(self, dato):
        self.dato      = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # ── utilidad de apoyo (iterativa) ────────────────────────────────────────
    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(str(actual.dato))
            actual = actual.siguiente
        print(" → ".join(resultado) if resultado else "Lista vacía")

    # -------------------------------------------------------------------------
    # 1. Contar nodos de forma recursiva
    #    [1, 2, 3, 4] → 4
    # -------------------------------------------------------------------------
    def contar(self):
        def _contar(nodo):
            if nodo is None:
                return 0
            return 1 + _contar(nodo.siguiente)
        return _contar(self.cabeza)

    # -------------------------------------------------------------------------
    # 2. Sumar todos los valores de forma recursiva
    #    [1, 2, 3, 4] → 10
    # -------------------------------------------------------------------------
    def sumar(self):
        def _sumar(nodo):
            if nodo is None:
                return 0
            return nodo.dato + _sumar(nodo.siguiente)
        return _sumar(self.cabeza)

    # -------------------------------------------------------------------------
    # 3. Buscar un valor de forma recursiva
    #    buscar(3) en [1,2,3,4] → True
    #    buscar(9) en [1,2,3,4] → False
    # -------------------------------------------------------------------------
    def buscar(self, valor):
        def _buscar(nodo, valor):
            if nodo is None:
                return False
            if nodo.dato == valor:
                return True
            return _buscar(nodo.siguiente, valor)
        return _buscar(self.cabeza, valor)

    # -------------------------------------------------------------------------
    # 4. Obtener el máximo de forma recursiva
    #    [3, 1, 7, 2] → 7
    # -------------------------------------------------------------------------
    def maximo(self):
        def _maximo(nodo):
            if nodo.siguiente is None:      # caso base: último nodo
                return nodo.dato
            max_resto = _maximo(nodo.siguiente)
            return nodo.dato if nodo.dato > max_resto else max_resto
        if self.cabeza is None:
            return None
        return _maximo(self.cabeza)

    # -------------------------------------------------------------------------
    # 5. Invertir la lista de forma recursiva
    #    [1, 2, 3] → [3, 2, 1]
    # -------------------------------------------------------------------------
    def invertir(self):
        def _invertir(nodo):
            if nodo is None or nodo.siguiente is None:
                return nodo                         # nuevo inicio
            nueva_cabeza = _invertir(nodo.siguiente)
            nodo.siguiente.siguiente = nodo         # el siguiente apunta atrás
            nodo.siguiente = None                   # el actual ya no tiene siguiente
            return nueva_cabeza
        self.cabeza = _invertir(self.cabeza)

    # -------------------------------------------------------------------------
    # 6. Contar cuántos nodos son pares de forma recursiva
    #    [1, 2, 3, 4, 6] → 3
    # -------------------------------------------------------------------------
    def contar_pares(self):
        def _contar_pares(nodo):
            if nodo is None:
                return 0
            es_par = 1 if nodo.dato % 2 == 0 else 0
            return es_par + _contar_pares(nodo.siguiente)
        return _contar_pares(self.cabeza)

    # -------------------------------------------------------------------------
    # 7. Eliminar todos los nodos con un valor dado de forma recursiva
    #    eliminar_valor(3) en [1,3,3,4,3] → [1,4]
    # -------------------------------------------------------------------------
    def eliminar_valor(self, valor):
        def _eliminar(nodo, valor):
            if nodo is None:
                return None
            nodo.siguiente = _eliminar(nodo.siguiente, valor)
            if nodo.dato == valor:
                return nodo.siguiente
            return nodo
        self.cabeza = _eliminar(self.cabeza, valor)

    # -------------------------------------------------------------------------
    # 8. Verificar si la lista está ordenada ascendentemente (recursivo)
    #    [1, 2, 3, 4] → True
    #    [1, 3, 2, 4] → False
    # -------------------------------------------------------------------------
    def esta_ordenada(self):
        def _ordenada(nodo):
            if nodo is None or nodo.siguiente is None:
                return True
            if nodo.dato > nodo.siguiente.dato:
                return False
            return _ordenada(nodo.siguiente)
        return _ordenada(self.cabeza)

    # -------------------------------------------------------------------------
    # 9. Obtener el valor del nodo en la posición k (recursivo, base 0)
    #    posicion(2) en [10, 20, 30, 40] → 30
    # -------------------------------------------------------------------------
    def posicion(self, k):
        def _posicion(nodo, k):
            if nodo is None:
                return None
            if k == 0:
                return nodo.dato
            return _posicion(nodo.siguiente, k - 1)
        return _posicion(self.cabeza, k)

    # -------------------------------------------------------------------------
    # 10. Copiar la lista y retornar una nueva (recursivo)
    #     devuelve una ListaEnlazada con los mismos valores
    # -------------------------------------------------------------------------
    def copiar(self):
        def _copiar(nodo):
            if nodo is None:
                return None
            nuevo = Nodo(nodo.dato)
            nuevo.siguiente = _copiar(nodo.siguiente)
            return nuevo
        nueva_lista = ListaEnlazada()
        nueva_lista.cabeza = _copiar(self.cabeza)
        return nueva_lista


# =============================================================================
# PRUEBAS
# =============================================================================
if __name__ == "__main__":
    lista = ListaEnlazada()
    for v in [3, 1, 7, 2, 4, 6]:
        lista.agregar(v)

    print("=" * 55)
    print("Lista original:")
    lista.mostrar()                                  # 3 → 1 → 7 → 2 → 4 → 6

    print("\nEJERCICIO 1 — Contar nodos")
    print(lista.contar())                            # 6

    print("\nEJERCICIO 2 — Sumar valores")
    print(lista.sumar())                             # 23

    print("\nEJERCICIO 3 — Buscar valor")
    print(lista.buscar(7))                           # True
    print(lista.buscar(9))                           # False

    print("\nEJERCICIO 4 — Máximo")
    print(lista.maximo())                            # 7

    print("\nEJERCICIO 5 — Invertir")
    lista.invertir()
    lista.mostrar()                                  # 6 → 4 → 2 → 7 → 1 → 3

    print("\nEJERCICIO 6 — Contar pares")
    print(lista.contar_pares())                      # 3  (6, 4, 2)

    print("\nEJERCICIO 7 — Eliminar valor 4")
    lista.eliminar_valor(4)
    lista.mostrar()                                  # 6 → 2 → 7 → 1 → 3

    print("\nEJERCICIO 8 — ¿Está ordenada?")
    print(lista.esta_ordenada())                     # False
    lista2 = ListaEnlazada()
    for v in [1, 2, 3, 4, 5]:
        lista2.agregar(v)
    print(lista2.esta_ordenada())                    # True

    print("\nEJERCICIO 9 — Posición k=2")
    print(lista2.posicion(2))                        # 3

    print("\nEJERCICIO 10 — Copiar lista")
    copia = lista2.copiar()
    copia.mostrar()                                  # 1 → 2 → 3 → 4 → 5
    lista2.agregar(99)
    print("Original modificada:")
    lista2.mostrar()                                 # 1 → 2 → 3 → 4 → 5 → 99
    print("Copia sin cambios:")
    copia.mostrar()                                  # 1 → 2 → 3 → 4 → 5
