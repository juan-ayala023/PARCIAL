"""
═══════════════════════════════════════════════════════════════════════════════
                        PARCIAL 1 - ESTRUCTURAS DE DATOS
                                  EXAMEN C
                    Sistema de Cola de Atención al Cliente
═══════════════════════════════════════════════════════════════════════════════
"""


# ─────────────────────────────────────────────
# PUNTO 1a: Clase Nodo (Cliente)
# ─────────────────────────────────────────────

# ═══════════════════════════════════════════════════════════════════════════════
#                                  SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

class Nodo:
    """Representa a un cliente en la cola del banco."""

    def __init__(self, nombre, tipo, tiempo):
        # Datos del cliente
        self.nombre = nombre          # nombre del cliente
        self.tipo = tipo              # "preferencial" o "normal"
        self.tiempo = tiempo          # minutos estimados de atención
        self.siguiente = None         # apunta al siguiente en la cola


# ─────────────────────────────────────────────
# PUNTO 1b: Clase Lista (Cola)
# ─────────────────────────────────────────────

class Cola:
    """
    Cola de atención bancaria.
    - Preferenciales entran al inicio (antes de los normales).
    - Normales se ubican al final.
    """

    def __init__(self):
        self.cabeza = None   # primer cliente en la cola


    # ─────────────────────────────────────────
    # PUNTO 2: Agregar cliente (con recursividad)
    # ─────────────────────────────────────────

    def agregar(self, nombre, tipo, tiempo):
        nuevo = Nodo(nombre, tipo, tiempo)

        if tipo == "preferencial":
            # Los preferenciales van al inicio, antes de los normales
            nuevo.siguiente = self._primer_normal(self.cabeza)
            # Conectamos el último preferencial con el nuevo
            if self.cabeza is None or self.cabeza.tipo == "normal":
                # Cola vacía o primer nodo ya es normal: el nuevo va al inicio
                nuevo.siguiente = self.cabeza
                self.cabeza = nuevo
            else:
                # Buscamos recursivamente el último preferencial
                self._insertar_preferencial(self.cabeza, nuevo)
        else:
            # Los normales van al final de la cola
            if self.cabeza is None:
                self.cabeza = nuevo
            else:
                self._insertar_al_final(self.cabeza, nuevo)

    def _insertar_preferencial(self, actual, nuevo):
        """Recursivamente busca el último preferencial para insertar después de él."""
        # Si el siguiente es normal o no existe, insertamos aquí
        if actual.siguiente is None or actual.siguiente.tipo == "normal":
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        else:
            # Seguimos avanzando entre los preferenciales
            self._insertar_preferencial(actual.siguiente, nuevo)

    def _insertar_al_final(self, actual, nuevo):
        """Recursivamente llega al último nodo y agrega el nuevo al final."""
        if actual.siguiente is None:
            actual.siguiente = nuevo
        else:
            self._insertar_al_final(actual.siguiente, nuevo)

    def _primer_normal(self, actual):
        """Retorna el primer nodo normal (auxiliar)."""
        if actual is None or actual.tipo == "normal":
            return actual
        return self._primer_normal(actual.siguiente)


    # ─────────────────────────────────────────
    # PUNTO 3: Tiempo de espera (recursivo)
    # ─────────────────────────────────────────

    def tiempo_espera(self, nombre):
        """
        Calcula cuántos minutos espera el cliente antes de ser atendido.
        Suma los tiempos de todos los que están delante de él.
        Retorna -1 si el cliente no existe en la cola.
        """
        return self._calcular_espera(self.cabeza, nombre, 0)

    def _calcular_espera(self, actual, nombre, acumulado):
        # Si llegamos al final sin encontrarlo, no está en la cola
        if actual is None:
            return -1
        # Si encontramos al cliente, devolvemos lo acumulado hasta aquí
        if actual.nombre == nombre:
            return acumulado
        # Acumulamos el tiempo del nodo actual y seguimos
        return self._calcular_espera(actual.siguiente, nombre, acumulado + actual.tiempo)


    # ─────────────────────────────────────────
    # PUNTO 4: Atender siguiente
    # ─────────────────────────────────────────

    def atender(self):
        """
        Retira y retorna el primer cliente de la cola.
        Retorna None si la cola está vacía.
        """
        if self.cabeza is None:
            return None
        atendido = self.cabeza
        self.cabeza = self.cabeza.siguiente  # avanzamos la cabeza
        atendido.siguiente = None            # desconectamos el nodo retirado
        return atendido


    # ─────────────────────────────────────────
    # PUNTO 5: Contar por tipo (recursivo)
    # ─────────────────────────────────────────

    def contar_por_tipo(self):
        """
        Retorna una tupla (preferenciales, normales).
        Usa recursividad para recorrer toda la cola.
        """
        return self._contar(self.cabeza, 0, 0)

    def _contar(self, actual, pref, norm):
        if actual is None:
            return (pref, norm)
        # Sumamos según el tipo del nodo actual
        if actual.tipo == "preferencial":
            return self._contar(actual.siguiente, pref + 1, norm)
        else:
            return self._contar(actual.siguiente, pref, norm + 1)


    # ─────────────────────────────────────────
    # Mostrar cola (para pruebas)
    # ─────────────────────────────────────────

    def mostrar(self):
        print("Cola actual:")
        actual = self.cabeza
        pos = 1
        while actual:
            print(f"  {pos}. {actual.nombre} | {actual.tipo} | {actual.tiempo} min")
            actual = actual.siguiente
            pos += 1
        print()


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    cola = Cola()

    # Agregar clientes
    cola.agregar("Juan", "normal", 10)
    cola.agregar("María", "preferencial", 5)
    cola.agregar("Pedro", "normal", 15)
    cola.agregar("Ana", "preferencial", 8)

    # Orden esperado: María, Ana, Juan, Pedro (preferenciales primero)
    cola.mostrar()

    # Tiempo de espera de Pedro: 5 + 8 + 10 = 23 minutos
    print("Espera de Pedro:", cola.tiempo_espera("Pedro"))

    # Contar por tipo: (2 preferenciales, 2 normales)
    print("Por tipo:", cola.contar_por_tipo())

    # Atender siguiente (María)
    atendido = cola.atender()
    print("Atendido:", atendido.nombre)
