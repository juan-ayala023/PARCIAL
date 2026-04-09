import re

# =============================================================================
# 1. EXPRESIONES REGULARES (VALOR 20%)
# =============================================================================

def validar_placa_vehiculo(placa):
    """
    Valida si una placa de vehículo colombiana tiene formato correcto.
    Formato válido: 3 letras mayúsculas + 3 dígitos (ej: ABC123).
    También válido con guion: ABC-123.
    """
    # Explicación del patrón:
    # ^[A-Z]{3} -> Empieza con exactamente 3 letras mayúsculas.
    # -?        -> El guion es opcional (0 o 1 vez).
    # \d{3}$    -> Termina con exactamente 3 dígitos.
    patron = r"^[A-Z]{3}-?\d{3}$"
    return bool(re.match(patron, placa))

def extraer_hashtags(texto):
    """
    Extrae todos los hashtags de un texto.
    Un hashtag empieza con # seguido de letras, números o guion bajo.
    """
    # \w+ captura letras, números y guiones bajos (underscore).
    return re.findall(r"#\w+", texto)

# =============================================================================
# 2. LISTAS ENLAZADAS Y RECURSIVIDAD (VALOR 30%)
# =============================================================================

class Pedido:
    """Clase que representa un pedido individual."""
    def __init__(self, cliente, direccion, valor, entregado=False):
        self.cliente = cliente
        self.direccion = direccion
        self.valor = valor
        self.entregado = entregado
        self.siguiente = None

    def __str__(self):
        """Formato de impresión del pedido."""
        estado = "✓" if self.entregado else "○"
        return f"[{estado}] {self.cliente} - ${self.valor:,} - {self.direccion}"

class ListaPedidos:
    """Clase para gestionar la lista enlazada de pedidos."""
    def __init__(self):
        self.cabeza = None

    def mostrar(self):
        """Muestra los pedidos de forma iterativa."""
        actual = self.cabeza
        if actual is None:
            print(" Sin pedidos")
            return
        while actual:
            print(f" {actual}")
            actual = actual.siguiente

    # --- MÉTODOS RECURSIVOS OBLIGATORIOS ---

    def agregar(self, cliente, direccion, valor):
        """Agrega un pedido al FINAL de la lista usando recursividad."""
        nuevo = Pedido(cliente, direccion, valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            self._agregar_recursivo(self.cabeza, nuevo)

    def _agregar_recursivo(self, actual, nuevo):
        """Función auxiliar para navegar hasta el final de la lista."""
        if actual.siguiente is None:
            actual.siguiente = nuevo
        else:
            self._agregar_recursivo(actual.siguiente, nuevo)

    def valor_pendiente(self):
        """Retorna la suma de valores de pedidos NO entregados (Recursivo)."""
        return self._suma_recursiva_pendiente(self.cabeza)

    def _suma_recursiva_pendiente(self, actual):
        """Suma solo si entregado es False."""
        if actual is None:
            return 0
        monto = actual.valor if not actual.entregado else 0
        return monto + self._suma_recursiva_pendiente(actual.siguiente)

    def eliminar_entregados(self):
        """Elimina pedidos entregados modificando la lista original (Recursivo)."""
        self.cabeza = self._eliminar_recursivo(self.cabeza)

    def _eliminar_recursivo(self, actual):
        """Procesa la eliminación de nodos basándose en el estado 'entregado'."""
        if actual is None:
            return None

        # Primero procesamos el resto de la lista (post-orden)
        actual.siguiente = self._eliminar_recursivo(actual.siguiente)

        # Si el nodo actual debe ser eliminado, retornamos el siguiente
        if actual.entregado:
            return actual.siguiente

        # Si no, mantenemos el nodo actual
        return actual

# =============================================================================
# 3. CONJUNTOS - CLUBES EXTRACURRICULARES (VALOR 20%)
# =============================================================================

club_ciencias = {"Ana", "Carlos", "Diana", "Elena", "Felipe"}
club_deportes = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"}
club_arte     = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}

def estudiantes_en_todos():
    """Retorna la intersección de los tres clubes."""
    return club_ciencias & club_deportes & club_arte

def solo_un_club():
    """Retorna estudiantes en EXACTAMENTE un club."""
    # Un estudiante está en exactamente uno si está en él pero no en los otros dos.
    solo_ciencias = club_ciencias - (club_deportes | club_arte)
    solo_deportes = club_deportes - (club_ciencias  | club_arte)
    solo_arte     = club_arte     - (club_ciencias  | club_deportes)
    return solo_ciencias | solo_deportes | solo_arte

def clubes_de_estudiante(nombre):
    """Retorna nombres de clubes a los que pertenece el estudiante."""
    resultado = []
    if nombre in club_ciencias: resultado.append("Ciencias")
    if nombre in club_deportes: resultado.append("Deportes")
    if nombre in club_arte:     resultado.append("Arte")
    return resultado

# =============================================================================
# 4. RECURSIVIDAD CON MEMORIZACIÓN (VALOR 30%)
# =============================================================================

def escalones_sin_memo(n):
    """Recursividad pura para el problema de la escalera."""
    # Casos base:
    if n == 0 or n == 1:
        return 1
    # Caso recursivo:
    return escalones_sin_memo(n - 1) + escalones_sin_memo(n - 2)

def escalones_con_memo(n, memo=None):
    """Misma lógica pero evitando recalcular usando un diccionario."""
    if memo is None:
        memo = {}

    # Casos base
    if n <= 1:
        return 1

    # Si ya se calculó, se retorna del diccionario
    if n in memo:
        return memo[n]

    # Cálculo y almacenamiento
    memo[n] = escalones_con_memo(n - 1, memo) + escalones_con_memo(n - 2, memo)
    return memo[n]

# =============================================================================
# BLOQUE PRINCIPAL PARA EJECUCIÓN (MAIN)
# =============================================================================

if __name__ == "__main__":
    print("--- 1. PRUEBAS REGEX ---")
    print(f"Placa ABC123 válida:  {validar_placa_vehiculo('ABC123')}")
    print(f"Placa ABC-123 válida: {validar_placa_vehiculo('ABC-123')}")
    print(f"Placa AB1234 válida:  {validar_placa_vehiculo('AB1234')}")
    print(f"Placa abc123 válida:  {validar_placa_vehiculo('abc123')}")
    print(f"Hashtags: {extraer_hashtags('Hola #python es #genial y #100dias')}")

    print("\n--- 2. PRUEBAS LISTA ENLAZADA (RECURSIVA) ---")
    lista = ListaPedidos()
    lista.agregar("Juan Esteban", "Cl 10", 25000)
    lista.agregar("Maria Gomez",  "Av 80", 30000)
    lista.agregar("Pedro Perez",  "Cl 45", 15000)

    # Marcar a Juan como entregado
    lista.cabeza.entregado = True

    print("Lista inicial:")
    lista.mostrar()
    print(f"Valor pendiente (esperado 45000): {lista.valor_pendiente()}")

    lista.eliminar_entregados()
    print("Lista tras eliminar entregados:")
    lista.mostrar()

    print("\n--- 3. PRUEBAS CONJUNTOS ---")
    print(f"En los tres clubes:            {estudiantes_en_todos()}")
    print(f"Estudiantes en solo un club:   {solo_un_club()}")
    print(f"Clubes de Carlos:              {clubes_de_estudiante('Carlos')}")
    print(f"Clubes de Julia:               {clubes_de_estudiante('Julia')}")

    print("\n--- 4. PRUEBAS ESCALONES ---")
    print(f"Escalones N=10 (sin memo): {escalones_sin_memo(10)}")
    print(f"Escalones N=10 (con memo): {escalones_con_memo(10)}")
    print(f"Escalones N=30 (con memo): {escalones_con_memo(30)}")
