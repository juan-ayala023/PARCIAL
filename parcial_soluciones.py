# ============================================================
#  PARCIAL COMPLETO — Algoritmos y Programación 4
#  Politécnico Colombiano Jaime Isaza Cadavid
# ============================================================

import re
import time

# ╔══════════════════════════════════════════════════════════╗
# ║  PUNTO 1  (20%)  —  Expresiones Regulares               ║
# ╚══════════════════════════════════════════════════════════╝

def validar_placa_vehiculo(placa):
    """
    Valida si una placa de vehículo colombiana tiene formato correcto.
    Formato válido: 3 letras mayúsculas + 3 dígitos (ej: ABC123)
    También válido con guion: ABC-123
    """
    patron = r"^[A-Z]{3}-?\d{3}$"
    return bool(re.match(patron, placa))


def extraer_hashtags(texto):
    """
    Extrae todos los hashtags de un texto.
    Un hashtag empieza con # seguido de letras, números o guion bajo.
    """
    return re.findall(r"#\w+", texto)


# ── Pruebas Punto 1 ──────────────────────────────────────
print("=" * 55)
print("PUNTO 1 — Expresiones Regulares")
print("=" * 55)
print(f"validar_placa_vehiculo('ABC123')  → {validar_placa_vehiculo('ABC123')}")    # True
print(f"validar_placa_vehiculo('ABC-123') → {validar_placa_vehiculo('ABC-123')}")   # True
print(f"validar_placa_vehiculo('AB1234')  → {validar_placa_vehiculo('AB1234')}")    # False
print(f"validar_placa_vehiculo('abc123')  → {validar_placa_vehiculo('abc123')}")    # False

print()
print(f"extraer_hashtags('Hola #python es #genial y #100dias')")
print(f"  → {extraer_hashtags('Hola #python es #genial y #100dias')}")
# ["#python", "#genial", "#100dias"]


# ╔══════════════════════════════════════════════════════════╗
# ║  PUNTO 2  (30%)  —  Lista Enlazada + Recursividad       ║
# ╚══════════════════════════════════════════════════════════╝

class Pedido:
    def __init__(self, cliente, direccion, valor, entregado=False):
        self.cliente   = cliente
        self.direccion = direccion
        self.valor     = valor
        self.entregado = entregado
        self.siguiente = None

    def __str__(self):
        estado = "✓" if self.entregado else "○"
        return f"[{estado}] {self.cliente} - ${self.valor:,} - {self.direccion}"


class ListaPedidos:
    def __init__(self):
        self.cabeza = None

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("  Sin pedidos")
            return
        while actual:
            print(f"  {actual}")
            actual = actual.siguiente

    def agregar(self, cliente, direccion, valor):
        """Agrega un nuevo pedido al FINAL de la lista. Usa recursividad."""
        nuevo = Pedido(cliente, direccion, valor)

        def _insertar(nodo):
            if nodo.siguiente is None:
                nodo.siguiente = nuevo
            else:
                _insertar(nodo.siguiente)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            _insertar(self.cabeza)

    def valor_pendiente(self):
        """Retorna la suma de valores de pedidos NO entregados. Usa recursividad."""
        def _sumar(nodo):
            if nodo is None:
                return 0
            valor_actual = nodo.valor if not nodo.entregado else 0
            return valor_actual + _sumar(nodo.siguiente)

        return _sumar(self.cabeza)

    def eliminar_entregados(self):
        """Elimina todos los pedidos ya entregados. Usa recursividad."""
        def _limpiar(nodo):
            if nodo is None:
                return None
            nodo.siguiente = _limpiar(nodo.siguiente)
            return nodo.siguiente if nodo.entregado else nodo

        self.cabeza = _limpiar(self.cabeza)


# ── Pruebas Punto 2 ──────────────────────────────────────
print("\n" + "=" * 55)
print("PUNTO 2 — Lista Enlazada")
print("=" * 55)
lista = ListaPedidos()
lista.agregar("Ana",    "Calle 10 #5-20", 25000, )
lista.agregar("Carlos", "Carrera 8 #3-1", 30000)
lista.agregar("Diana",  "Av. El Poblado", 15000)

# Marcar primer pedido como entregado
lista.cabeza.entregado = True

print("Lista actual:")
lista.mostrar()
print(f"\nValor pendiente: ${lista.valor_pendiente():,}")   # 45000

lista.eliminar_entregados()
print("\nDespués de eliminar entregados:")
lista.mostrar()


# ╔══════════════════════════════════════════════════════════╗
# ║  PUNTO 3  (20%)  —  Conjuntos                           ║
# ╚══════════════════════════════════════════════════════════╝

club_ciencias = {"Ana", "Carlos", "Diana", "Elena", "Felipe"}
club_deportes = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"}
club_arte     = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}


def estudiantes_en_todos():
    """Retorna el conjunto de estudiantes inscritos en LOS TRES clubes."""
    return club_ciencias & club_deportes & club_arte


def solo_un_club():
    """Retorna el conjunto de estudiantes que están en EXACTAMENTE un club."""
    solo_ciencias = club_ciencias  - club_deportes - club_arte
    solo_deportes = club_deportes  - club_ciencias  - club_arte
    solo_arte     = club_arte      - club_ciencias  - club_deportes
    return solo_ciencias | solo_deportes | solo_arte


def clubes_de_estudiante(nombre):
    """Retorna lista con los nombres de los clubes del estudiante."""
    clubes = []
    if nombre in club_ciencias:
        clubes.append("Ciencias")
    if nombre in club_deportes:
        clubes.append("Deportes")
    if nombre in club_arte:
        clubes.append("Arte")
    return clubes


# ── Pruebas Punto 3 ──────────────────────────────────────
print("\n" + "=" * 55)
print("PUNTO 3 — Conjuntos")
print("=" * 55)
print(f"Estudiantes en los 3 clubes: {estudiantes_en_todos()}")
print(f"Solo en un club: {solo_un_club()}")
print(f"Clubes de Carlos: {clubes_de_estudiante('Carlos')}")
print(f"Clubes de Julia:  {clubes_de_estudiante('Julia')}")


# ╔══════════════════════════════════════════════════════════╗
# ║  PUNTO 4  (30%)  —  Recursividad + Memoización          ║
# ╚══════════════════════════════════════════════════════════╝

def escalones_sin_memo(n):
    """
    Calcula formas de subir n escalones (1 o 2 a la vez).
    Recursividad pura sin memorización.
    Casos base: n==0 → 1, n==1 → 1
    """
    if n == 0:
        return 1
    if n == 1:
        return 1
    return escalones_sin_memo(n - 1) + escalones_sin_memo(n - 2)


def escalones_con_memo(n, memo=None):
    """
    Misma función con memoización para evitar recalcular.
    Guarda resultados en un diccionario memo.
    """
    if memo is None:
        memo = {}

    if n == 0:
        return 1
    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = escalones_con_memo(n - 1, memo) + escalones_con_memo(n - 2, memo)
    return memo[n]


# ── Pruebas Punto 4 ──────────────────────────────────────
print("\n" + "=" * 55)
print("PUNTO 4 — Recursividad + Memoización")
print("=" * 55)
for i in range(6):
    print(f"  escalones_sin_memo({i}) = {escalones_sin_memo(i)}")

print()
print(f"  escalones_con_memo(10) = {escalones_con_memo(10)}")    # 89
print(f"  escalones_con_memo(30) = {escalones_con_memo(30)}")    # 1346269

# Comparación de velocidad
t1 = time.time(); escalones_sin_memo(35); t1 = time.time() - t1
t2 = time.time(); escalones_con_memo(35); t2 = time.time() - t2
print(f"\n  Velocidad n=35  sin memo: {t1*1000:.1f} ms  |  con memo: {t2*1000:.3f} ms")
