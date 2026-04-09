"""
═══════════════════════════════════════════════════════════════════════════════
                        PARCIAL - CONJUNTOS
                    Validador de Sudoku + Sistema de Permisos
═══════════════════════════════════════════════════════════════════════════════
"""

NUMEROS_VALIDOS = {1, 2, 3, 4, 5, 6, 7, 8, 9}

TABLERO = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]


# ═══════════════════════════════════════════════════════════════════════════════
#                                  SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────
# PUNTO 1.1: Validar una fila
# ─────────────────────────────────────────────

def validar_fila(tablero, num_fila):
    """
    Retorna True si la fila contiene exactamente los números 1-9 sin repetir.
    Convertimos la fila a un set y comparamos con NUMEROS_VALIDOS.
    """
    fila = tablero[num_fila]
    # Si hay repetidos, el set tendrá menos de 9 elementos y no igualará
    return set(fila) == NUMEROS_VALIDOS


# ─────────────────────────────────────────────
# PUNTO 1.2: Validar una columna
# ─────────────────────────────────────────────

def validar_columna(tablero, num_columna):
    """
    Retorna True si la columna contiene exactamente los números 1-9 sin repetir.
    Extraemos todos los valores de esa columna en las 9 filas.
    """
    columna = {tablero[fila][num_columna] for fila in range(9)}
    return columna == NUMEROS_VALIDOS


# ─────────────────────────────────────────────
# PUNTO 1.3: Validar un subcuadro 3x3
# ─────────────────────────────────────────────

def validar_subcuadro(tablero, fila_inicio, col_inicio):
    """
    Retorna True si el subcuadro 3x3 contiene exactamente los números 1-9.
    fila_inicio y col_inicio son la esquina superior izquierda (0, 3 o 6).
    Recorremos las 3 filas y 3 columnas del bloque.
    """
    numeros = set()
    for f in range(fila_inicio, fila_inicio + 3):
        for c in range(col_inicio, col_inicio + 3):
            numeros.add(tablero[f][c])
    return numeros == NUMEROS_VALIDOS


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO BASE - NO MODIFICAR
# ═══════════════════════════════════════════════════════════════════════════════

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Conjunto:
    def __init__(self, elementos=None):
        self.cabeza = None
        self.tamaño = 0
        if elementos:
            for e in elementos:
                self.agregar(e)

    def esta_vacio(self):
        return self.cabeza is None

    def pertenece(self, x):
        """Retorna True si x está en el conjunto."""
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False

    def agregar(self, x):
        """Agrega x si no existe."""
        if self.pertenece(x):
            return False
        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamaño += 1
        return True

    def __str__(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "{" + ", ".join(elementos) + "}"


# ─────────────────────────────────────────────
# PUNTO 2.1: Verificar si es subconjunto
# ─────────────────────────────────────────────

def es_subconjunto(conjunto_a, conjunto_b):
    """
    Retorna True si conjunto_a es subconjunto de conjunto_b (A ⊆ B).
    Recorremos cada elemento de A y verificamos que esté en B.
    Si alguno no está, ya no es subconjunto.
    """
    actual = conjunto_a.cabeza
    while actual:
        if not conjunto_b.pertenece(actual.dato):
            return False   # encontramos un elemento de A que no está en B
        actual = actual.siguiente
    return True   # todos los elementos de A están en B


# ─────────────────────────────────────────────
# PUNTO 2.2: Verificar permisos de usuario
# ─────────────────────────────────────────────

def tiene_permisos(permisos_usuario, permisos_requeridos):
    """
    Retorna True si el usuario tiene TODOS los permisos requeridos.
    Es lo mismo que verificar si requeridos ⊆ usuario.
    """
    return es_subconjunto(permisos_requeridos, permisos_usuario)


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("PARTE 1: VALIDADOR DE SUDOKU")
    print("=" * 60)

    print("\n📋 Validando filas:")
    for i in range(9):
        resultado = validar_fila(TABLERO, i)
        print(f"  Fila {i+1}: {'✓' if resultado else '✗'}")

    print("\n📋 Validando columnas:")
    for j in range(9):
        resultado = validar_columna(TABLERO, j)
        print(f"  Columna {j+1}: {'✓' if resultado else '✗'}")

    print("\n📋 Validando subcuadros 3x3:")
    for fi in [0, 3, 6]:
        for ci in [0, 3, 6]:
            resultado = validar_subcuadro(TABLERO, fi, ci)
            print(f"  Subcuadro ({fi+1},{ci+1}): {'✓' if resultado else '✗'}")

    print("\n" + "=" * 60)
    print("PARTE 2: SISTEMA DE PERMISOS")
    print("=" * 60)

    # Definir roles
    admin = Conjunto(["leer", "escribir", "eliminar", "crear_usuarios"])
    editor = Conjunto(["leer", "escribir"])
    viewer = Conjunto(["leer"])

    print(f"\n👤 Roles definidos:")
    print(f"  Admin: {admin}")
    print(f"  Editor: {editor}")
    print(f"  Viewer: {viewer}")

    print(f"\n🔍 Verificando subconjuntos:")
    print(f"  ¿Viewer ⊆ Editor? {es_subconjunto(viewer, editor)}")   # True
    print(f"  ¿Editor ⊆ Admin? {es_subconjunto(editor, admin)}")     # True
    print(f"  ¿Admin ⊆ Editor? {es_subconjunto(admin, editor)}")     # False

    print(f"\n🔐 Verificando permisos:")

    accion_editar = Conjunto(["leer", "escribir"])
    accion_admin = Conjunto(["crear_usuarios", "eliminar"])

    print(f"  Acción editar requiere: {accion_editar}")
    print(f"  Acción admin requiere: {accion_admin}")

    print(f"\n  ¿Editor puede editar? {tiene_permisos(editor, accion_editar)}")           # True
    print(f"  ¿Viewer puede editar? {tiene_permisos(viewer, accion_editar)}")             # False
    print(f"  ¿Admin puede hacer acción admin? {tiene_permisos(admin, accion_admin)}")    # True
    print(f"  ¿Editor puede hacer acción admin? {tiene_permisos(editor, accion_admin)}") # False
