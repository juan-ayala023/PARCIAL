# ============================================================
#  LISTAS ENLAZADAS + RECURSIVIDAD - Guía de Estudio
#  Parcial Algoritmos y Programación 4
# ============================================================

# ──────────────────────────────────────────────────────────
# CONCEPTO CLAVE: Lista Enlazada
# Cada nodo apunta al siguiente. El último apunta a None.
#
#  [cabeza] → [Nodo1] → [Nodo2] → [Nodo3] → None
# ──────────────────────────────────────────────────────────

class Pedido:
    def __init__(self, cliente, direccion, valor, entregado=False):
        self.cliente   = cliente
        self.direccion = direccion
        self.valor     = valor
        self.entregado = entregado
        self.siguiente = None   # puntero al próximo nodo

    def __str__(self):
        estado = "✓" if self.entregado else "○"
        return f"[{estado}] {self.cliente} - ${self.valor:,} - {self.direccion}"


class ListaPedidos:
    def __init__(self):
        self.cabeza = None   # inicio de la lista

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("  Sin pedidos")
            return
        while actual:
            print(f"  {actual}")
            actual = actual.siguiente

    # ──────────────────────────────────────────────────────
    # MÉTODO 1: agregar  — insertar al FINAL con recursividad
    # ──────────────────────────────────────────────────────
    # Idea: si la lista está vacía, el nuevo nodo ES la cabeza.
    # Si no, avanzamos recursivamente hasta llegar al último
    # nodo (aquel cuyo .siguiente es None) y allí conectamos.

    def agregar(self, cliente, direccion, valor):
        nuevo = Pedido(cliente, direccion, valor)

        # Función auxiliar recursiva
        def _insertar_al_final(nodo):
            if nodo.siguiente is None:      # llegamos al último
                nodo.siguiente = nuevo      # conectamos el nuevo
            else:
                _insertar_al_final(nodo.siguiente)  # seguimos avanzando

        if self.cabeza is None:             # lista vacía
            self.cabeza = nuevo
        else:
            _insertar_al_final(self.cabeza)

    # ──────────────────────────────────────────────────────
    # MÉTODO 2: valor_pendiente — suma de pedidos NO entregados
    # ──────────────────────────────────────────────────────
    # Idea recursiva:
    #   base: nodo es None → retorna 0
    #   recursivo: si el nodo NO está entregado,
    #              suma su valor + llamada al siguiente
    #              si SÍ está entregado, solo llama al siguiente

    def valor_pendiente(self):
        def _sumar(nodo):
            if nodo is None:                # caso base
                return 0
            valor_actual = nodo.valor if not nodo.entregado else 0
            return valor_actual + _sumar(nodo.siguiente)

        return _sumar(self.cabeza)

    # ──────────────────────────────────────────────────────
    # MÉTODO 3: eliminar_entregados — borrar nodos entregados
    # ──────────────────────────────────────────────────────
    # Idea recursiva:
    #   base: nodo es None → retorna None
    #   recursivo: primero resolvemos el resto de la lista
    #              luego decidimos si el nodo actual se queda
    #              (no entregado → lo mantenemos)
    #              (entregado    → lo saltamos, devolvemos siguiente)

    def eliminar_entregados(self):
        def _limpiar(nodo):
            if nodo is None:                # caso base
                return None
            nodo.siguiente = _limpiar(nodo.siguiente)   # resuelve el resto
            if nodo.entregado:
                return nodo.siguiente       # salta este nodo
            else:
                return nodo                 # conserva este nodo

        self.cabeza = _limpiar(self.cabeza)


# ──────────────────────────────────────────────────────────
# PRUEBAS COMPLETAS
# ──────────────────────────────────────────────────────────
print("=" * 50)
print("PRUEBA: agregar pedidos")
print("=" * 50)
lista = ListaPedidos()
lista.agregar("Ana",    "Calle 10 #5-20", 25000)
lista.agregar("Carlos", "Carrera 8 #3-1", 30000)
lista.agregar("Diana",  "Av. El Poblado",  15000)
lista.mostrar()

print("\n" + "=" * 50)
print("PRUEBA: valor_pendiente (todos pendientes = 70000)")
print("=" * 50)
print(f"  Valor pendiente: ${lista.valor_pendiente():,}")  # 70000

# Marcamos la de Ana como entregada
lista.cabeza.entregado = True
print(f"  Después de entregar Ana: ${lista.valor_pendiente():,}")  # 45000

print("\n" + "=" * 50)
print("PRUEBA: eliminar_entregados")
print("=" * 50)
print("Antes:")
lista.mostrar()
lista.eliminar_entregados()
print("Después (Ana eliminada):")
lista.mostrar()

# ──────────────────────────────────────────────────────────
# PATRON GENERAL DE RECURSIVIDAD EN LISTAS ENLAZADAS
# ──────────────────────────────────────────────────────────
# def funcion_recursiva(nodo):
#     if nodo is None:         # CASO BASE siempre primero
#         return valor_neutro  # (0, None, [], False, etc.)
#     
#     # Procesa el nodo actual
#     resultado_actual = hacer_algo(nodo)
#     
#     # Llamada recursiva al siguiente
#     resultado_resto = funcion_recursiva(nodo.siguiente)
#     
#     # Combina y retorna
#     return combinar(resultado_actual, resultado_resto)
