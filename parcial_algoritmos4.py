"""
═══════════════════════════════════════════════════════════════════════════════
        POLITÉCNICO COLOMBIANO JAIME ISAZA CADAVID
        ALGORITMOS Y PROGRAMACIÓN 4  |  PARCIAL  |  ABRIL 6 DE 2026
        PROFESOR: JUAN ESTEBAN GÓMEZ TIRADO
═══════════════════════════════════════════════════════════════════════════════
"""

import re


# ═══════════════════════════════════════════════════════════════════════════════
# PUNTO 1 - VALOR 20%
# Completa las funciones de validación usando expresiones regulares.
# ═══════════════════════════════════════════════════════════════════════════════

def validar_placa_vehiculo(placa):
    """
    Valida si una placa de vehículo colombiana tiene formato correcto.

    Formato válido: 3 letras mayúsculas + 3 dígitos (ej: ABC123)
    También válido con guion: ABC-123

    Ejemplos:
        validar_placa_vehiculo("ABC123")  -> True
        validar_placa_vehiculo("ABC-123") -> True
        validar_placa_vehiculo("AB1234")  -> False
        validar_placa_vehiculo("abc123")  -> False
    """
    # TODO: Implementar con re.match o re.search
    pass

    # ═══════════════════════════════════════════════════════════════════════════
    #                              SOLUCIÓN
    # ═══════════════════════════════════════════════════════════════════════════

    # El patrón exige exactamente 3 letras mayúsculas, guion opcional, 3 dígitos
    # ^ y $ aseguran que no haya nada extra antes ni después
    patron = r'^[A-Z]{3}-?\d{3}$'
    return bool(re.match(patron, placa))


def extraer_hashtags(texto):
    """
    Extrae todos los hashtags de un texto.
    Un hashtag empieza con # seguido de letras, números o guion bajo.

    Ejemplo:
        extraer_hashtags("Hola #python es #genial y #100dias")
        -> ["#python", "#genial", "#100dias"]
    """
    # TODO: Implementar con re.findall
    pass

    # ═══════════════════════════════════════════════════════════════════════════
    #                              SOLUCIÓN
    # ═══════════════════════════════════════════════════════════════════════════

    # \w+ captura letras, dígitos y guion bajo (todo lo que puede seguir al #)
    return re.findall(r'#\w+', texto)


# ═══════════════════════════════════════════════════════════════════════════════
# PUNTO 2 - VALOR 30%
# Sistema de gestión de pedidos para un restaurante de domicilios.
# Cada pedido tiene: cliente, dirección, valor y si está entregado.
# Los pedidos se almacenan en una lista enlazada.
# ═══════════════════════════════════════════════════════════════════════════════

class Pedido:
    def __init__(self, cliente, direccion, valor, entregado=False):
        self.cliente = cliente
        self.direccion = direccion
        self.valor = valor
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
        """
        Agrega un nuevo pedido al FINAL de la lista.
        OBLIGATORIO usar recursividad.
        """
        # TODO: Implementar
        pass

        # ═══════════════════════════════════════════════════════════════════════
        #                              SOLUCIÓN
        # ═══════════════════════════════════════════════════════════════════════

        nuevo = Pedido(cliente, direccion, valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            # Delegamos en el helper recursivo para llegar al final
            self._agregar_recursivo(self.cabeza, nuevo)

    def _agregar_recursivo(self, actual, nuevo):
        if actual.siguiente is None:
            actual.siguiente = nuevo
        else:
            self._agregar_recursivo(actual.siguiente, nuevo)

    def valor_pendiente(self):
        """
        Retorna la suma de valores de pedidos NO entregados.
        OBLIGATORIO usar recursividad.

        Ejemplo:
            Pedido1 (entregado, $25000) + Pedido2 (pendiente, $30000)
            + Pedido3 (pendiente, $15000)
            -> Retorna 45000
        """
        # TODO: Implementar
        pass

        # ═══════════════════════════════════════════════════════════════════════
        #                              SOLUCIÓN
        # ═══════════════════════════════════════════════════════════════════════

        return self._sumar_pendientes(self.cabeza)

    def _sumar_pendientes(self, actual):
        if actual is None:
            return 0
        # Si no está entregado sumamos su valor, si está entregado sumamos 0
        valor_actual = actual.valor if not actual.entregado else 0
        return valor_actual + self._sumar_pendientes(actual.siguiente)

    def eliminar_entregados(self):
        """
        Elimina todos los pedidos que ya fueron entregados.
        OBLIGATORIO usar recursividad.
        Modifica la lista original.
        """
        # TODO: Implementar
        pass

        # ═══════════════════════════════════════════════════════════════════════
        #                              SOLUCIÓN
        # ═══════════════════════════════════════════════════════════════════════

        # El helper retorna el nuevo nodo cabeza después de limpiar entregados
        self.cabeza = self._limpiar(self.cabeza)

    def _limpiar(self, actual):
        if actual is None:
            return None
        # Primero limpiamos el resto de la lista
        actual.siguiente = self._limpiar(actual.siguiente)
        # Si este nodo ya fue entregado, lo saltamos devolviendo su siguiente
        if actual.entregado:
            return actual.siguiente
        return actual


# ═══════════════════════════════════════════════════════════════════════════════
# PUNTO 3 - VALOR 20%
# Un colegio tiene 3 clubes extracurriculares. Cada club tiene un conjunto
# de estudiantes inscritos. Responde las preguntas usando operaciones de conjuntos.
# ═══════════════════════════════════════════════════════════════════════════════

club_ciencias  = {"Ana", "Carlos", "Diana", "Elena", "Felipe"}
club_deportes  = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"}
club_arte      = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}


def estudiantes_en_todos():
    """
    Retorna el conjunto de estudiantes inscritos en LOS TRES clubes.
    (Intersección de los tres)
    """
    # TODO: Implementar
    pass

    # ═══════════════════════════════════════════════════════════════════════════
    #                              SOLUCIÓN
    # ═══════════════════════════════════════════════════════════════════════════

    # La intersección de tres conjuntos da solo los que están en los tres
    return club_ciencias & club_deportes & club_arte


def solo_un_club():
    """
    Retorna el conjunto de estudiantes que están en EXACTAMENTE un club.

    Pista: Un estudiante está en exactamente un club si está en ese club
    pero NO en los otros dos.

    Ejemplo esperado: {"Elena", "Hugo", "Isabel", "Julia", "Karen"}
    """
    # TODO: Implementar
    pass

    # ═══════════════════════════════════════════════════════════════════════════
    #                              SOLUCIÓN
    # ═══════════════════════════════════════════════════════════════════════════

    # Solo en ciencias: está en ciencias pero no en deportes ni arte
    solo_ciencias  = club_ciencias  - club_deportes - club_arte
    solo_deportes  = club_deportes  - club_ciencias  - club_arte
    solo_arte      = club_arte      - club_ciencias  - club_deportes

    # Unimos los tres grupos de "exclusivos"
    return solo_ciencias | solo_deportes | solo_arte


def clubes_de_estudiante(nombre):
    """
    Retorna una lista con los nombres de los clubes a los que pertenece
    el estudiante.

    Ejemplo:
        clubes_de_estudiante("Carlos") -> ["Ciencias", "Deportes"]
        clubes_de_estudiante("Julia")  -> ["Arte"]
    """
    # TODO: Implementar
    pass

    # ═══════════════════════════════════════════════════════════════════════════
    #                              SOLUCIÓN
    # ═══════════════════════════════════════════════════════════════════════════

    clubes = []
    if nombre in club_ciencias:
        clubes.append("Ciencias")
    if nombre in club_deportes:
        clubes.append("Deportes")
    if nombre in club_arte:
        clubes.append("Arte")
    return clubes


# ═══════════════════════════════════════════════════════════════════════════════
# PUNTO 4 - VALOR 30%
# Tienes una escalera de N escalones. En cada paso puedes subir 1 o 2 escalones.
# ¿De cuántas formas distintas puedes llegar al escalón N?
#
# Ejemplo:
#   N=1: 1 forma  → [1]
#   N=2: 2 formas → [1+1, 2]
#   N=3: 3 formas → [1+1+1, 1+2, 2+1]
#   N=4: 5 formas → [1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2]
# ═══════════════════════════════════════════════════════════════════════════════

def escalones_sin_memo(n):
    """
    Calcula de cuántas formas se puede subir una escalera de n escalones.
    En cada paso puedes subir 1 o 2 escalones.

    Implementar con recursividad pura (sin memorización).

    Casos base:
        n == 0 -> 1 (hay una forma de "no subir")
        n == 1 -> 1

    Caso recursivo:
        escalones(n) = escalones(n-1) + escalones(n-2)
    """
    # TODO: Implementar
    pass

    # ═══════════════════════════════════════════════════════════════════════════
    #                              SOLUCIÓN
    # ═══════════════════════════════════════════════════════════════════════════

    # Casos base
    if n == 0 or n == 1:
        return 1
    # Para llegar al escalón n, el último salto fue de 1 (venía de n-1)
    # o de 2 (venía de n-2) → sumamos ambas posibilidades
    return escalones_sin_memo(n - 1) + escalones_sin_memo(n - 2)


def escalones_con_memo(n, memo=None):
    """
    Misma función pero usando un diccionario para guardar resultados
    ya calculados y evitar recalcular.

    Ejemplo:
        escalones_con_memo(10) -> 89
        escalones_con_memo(30) -> 1346269  (sin memo esto tardaría mucho)
    """
    # TODO: Implementar
    pass

    # ═══════════════════════════════════════════════════════════════════════════
    #                              SOLUCIÓN
    # ═══════════════════════════════════════════════════════════════════════════

    # Inicializamos el diccionario en la primera llamada
    if memo is None:
        memo = {}

    # Si ya lo calculamos antes, lo devolvemos directo
    if n in memo:
        return memo[n]

    # Casos base
    if n == 0 or n == 1:
        return 1

    # Calculamos y guardamos en memo antes de retornar
    memo[n] = escalones_con_memo(n - 1, memo) + escalones_con_memo(n - 2, memo)
    return memo[n]


# ═══════════════════════════════════════════════════════════════════════════════
# PRUEBAS
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":

    print("=" * 60)
    print("PUNTO 1 - EXPRESIONES REGULARES")
    print("=" * 60)

    print("\nValidar placas:")
    print("  ABC123  :", validar_placa_vehiculo("ABC123"))   # True
    print("  ABC-123 :", validar_placa_vehiculo("ABC-123"))  # True
    print("  AB1234  :", validar_placa_vehiculo("AB1234"))   # False
    print("  abc123  :", validar_placa_vehiculo("abc123"))   # False

    print("\nExtraer hashtags:")
    resultado = extraer_hashtags("Hola #python es #genial y #100dias")
    print(" ", resultado)  # ['#python', '#genial', '#100dias']

    print("\n" + "=" * 60)
    print("PUNTO 2 - LISTA ENLAZADA DE PEDIDOS")
    print("=" * 60)

    lista = ListaPedidos()
    lista.agregar("Luisa", "Cra 10 #45-20", 25000)
    lista.agregar("Mario", "Cll 80 #32-11", 30000)
    lista.agregar("Sofi",  "Av Poblado #5", 15000)

    # Marcar el primero como entregado
    lista.cabeza.entregado = True

    print("\nPedidos actuales:")
    lista.mostrar()

    print(f"\nValor pendiente: ${lista.valor_pendiente():,}")  # 45000

    lista.eliminar_entregados()
    print("\nDespués de eliminar entregados:")
    lista.mostrar()

    print("\n" + "=" * 60)
    print("PUNTO 3 - CONJUNTOS DE CLUBES")
    print("=" * 60)

    print("\nEstudiantes en los 3 clubes:", estudiantes_en_todos())
    print("Solo en un club           :", solo_un_club())
    print("Clubes de Carlos          :", clubes_de_estudiante("Carlos"))
    print("Clubes de Julia           :", clubes_de_estudiante("Julia"))

    print("\n" + "=" * 60)
    print("PUNTO 4 - ESCALONES")
    print("=" * 60)

    print("\nSin memo:")
    for i in range(1, 8):
        print(f"  N={i}: {escalones_sin_memo(i)} formas")

    print("\nCon memo:")
    print("  N=10:", escalones_con_memo(10))   # 89
    print("  N=30:", escalones_con_memo(30))   # 1346269
