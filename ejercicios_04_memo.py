# =============================================================================
# EJERCICIOS — RECURSIVIDAD CON MEMORIZACIÓN
# =============================================================================
# Patrón obligatorio en todos los ejercicios:
#   1. def funcion(n, memo=None)
#   2. if memo is None: memo = {}
#   3. Casos base antes de consultar memo
#   4. if n in memo: return memo[n]
#   5. memo[n] = calculo recursivo
#   6. return memo[n]
# =============================================================================

# -----------------------------------------------------------------------------
# 1. Fibonacci clásico con memo
#    fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2)
#    fib(10) → 55
# -----------------------------------------------------------------------------
def fibonacci(n, memo=None):
    if memo is None: memo = {}
    if n == 0: return 0
    if n == 1: return 1
    if n in memo: return memo[n]
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# -----------------------------------------------------------------------------
# 2. Escalones (1 o 2 pasos) — el del parcial
#    escalones(0)=1, escalones(1)=1
#    escalones(10) → 89
# -----------------------------------------------------------------------------
def escalones(n, memo=None):
    if memo is None: memo = {}
    if n <= 1: return 1
    if n in memo: return memo[n]
    memo[n] = escalones(n - 1, memo) + escalones(n - 2, memo)
    return memo[n]

# -----------------------------------------------------------------------------
# 3. Escalones con 1, 2 o 3 pasos
#    tribonacci: cuántas formas de subir n escalones subiendo 1, 2 o 3 a la vez
#    tribonacci(4) → 7
# -----------------------------------------------------------------------------
def escalones_3pasos(n, memo=None):
    if memo is None: memo = {}
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    if n in memo: return memo[n]
    memo[n] = (escalones_3pasos(n-1, memo) +
               escalones_3pasos(n-2, memo) +
               escalones_3pasos(n-3, memo))
    return memo[n]

# -----------------------------------------------------------------------------
# 4. Potencia con memo
#    potencia(2, 10) → 1024
#    potencia(3, 5)  → 243
# -----------------------------------------------------------------------------
def potencia(base, exp, memo=None):
    if memo is None: memo = {}
    if exp == 0: return 1
    if exp == 1: return base
    if exp in memo: return memo[exp]
    memo[exp] = base * potencia(base, exp - 1, memo)
    return memo[exp]

# -----------------------------------------------------------------------------
# 5. Número de caminos en una cuadrícula m x n
#    Solo se puede mover hacia la derecha o hacia abajo
#    caminos(3, 3) → 6
# -----------------------------------------------------------------------------
def caminos(m, n, memo=None):
    if memo is None: memo = {}
    if m == 1 or n == 1: return 1           # solo hay un camino en borde
    if (m, n) in memo: return memo[(m, n)]
    memo[(m, n)] = caminos(m - 1, n, memo) + caminos(m, n - 1, memo)
    return memo[(m, n)]

# -----------------------------------------------------------------------------
# 6. Suma de dígitos de forma recursiva con memo
#    suma_digitos(1234) → 10
#    suma_digitos(999)  → 27
# -----------------------------------------------------------------------------
def suma_digitos(n, memo=None):
    if memo is None: memo = {}
    if n < 10: return n                     # un solo dígito
    if n in memo: return memo[n]
    memo[n] = (n % 10) + suma_digitos(n // 10, memo)
    return memo[n]

# -----------------------------------------------------------------------------
# 7. Número de formas de hacer cambio (monedas)
#    monedas disponibles: [1, 5, 10]
#    cambio(15) → 6 formas
# -----------------------------------------------------------------------------
def cambio(monto, monedas=None, i=0, memo=None):
    if monedas is None: monedas = [1, 5, 10]
    if memo is None: memo = {}
    if monto == 0: return 1
    if monto < 0 or i >= len(monedas): return 0
    clave = (monto, i)
    if clave in memo: return memo[clave]
    # usar la moneda actual o saltarla
    memo[clave] = (cambio(monto - monedas[i], monedas, i, memo) +
                   cambio(monto, monedas, i + 1, memo))
    return memo[clave]

# -----------------------------------------------------------------------------
# 8. Máximo de una lista de forma recursiva con memo
#    maximo_lista([3,1,9,2,7]) → 9
# -----------------------------------------------------------------------------
def maximo_lista(lst, i=0, memo=None):
    if memo is None: memo = {}
    if i == len(lst) - 1: return lst[i]    # caso base: último elemento
    if i in memo: return memo[i]
    max_resto = maximo_lista(lst, i + 1, memo)
    memo[i] = lst[i] if lst[i] > max_resto else max_resto
    return memo[i]

# -----------------------------------------------------------------------------
# 9. Longitud de la subsecuencia creciente más larga (LIS simplificado)
#    Para cada índice, ¿hasta qué largo puede llegar una secuencia creciente?
#    lis([3, 1, 4, 1, 5, 9, 2, 6]) → 4  (por ej: 1,4,5,9 o 1,4,5,6)
# -----------------------------------------------------------------------------
def lis(lst, i=0, prev=-float('inf'), memo=None):
    if memo is None: memo = {}
    if i == len(lst): return 0
    clave = (i, prev)
    if clave in memo: return memo[clave]
    # opción 1: no incluir lst[i]
    sin = lis(lst, i + 1, prev, memo)
    # opción 2: incluir lst[i] solo si es mayor al anterior
    con = 0
    if lst[i] > prev:
        con = 1 + lis(lst, i + 1, lst[i], memo)
    memo[clave] = max(sin, con)
    return memo[clave]

# -----------------------------------------------------------------------------
# 10. Suma de subconjunto (¿existe un subconjunto que sume exactamente target?)
#     subset_sum([3, 1, 5, 9, 2], 7) → True   (5+2 o 3+1+... )
#     subset_sum([3, 1, 5, 9, 2], 20) → False
# -----------------------------------------------------------------------------
def subset_sum(lst, target, i=0, memo=None):
    if memo is None: memo = {}
    if target == 0: return True
    if target < 0 or i >= len(lst): return False
    clave = (i, target)
    if clave in memo: return memo[clave]
    # incluir el elemento actual o no incluirlo
    memo[clave] = (subset_sum(lst, target - lst[i], i + 1, memo) or
                   subset_sum(lst, target,           i + 1, memo))
    return memo[clave]


# =============================================================================
# PRUEBAS
# =============================================================================
if __name__ == "__main__":
    print("=" * 55)
    print("EJERCICIO 1 — Fibonacci")
    print("=" * 55)
    print(f"fib(10) = {fibonacci(10)}")              # 55
    print(f"fib(30) = {fibonacci(30)}")              # 832040

    print("\nEJERCICIO 2 — Escalones (1 o 2 pasos)")
    print(f"escalones(10) = {escalones(10)}")        # 89
    print(f"escalones(30) = {escalones(30)}")        # 1346269

    print("\nEJERCICIO 3 — Escalones (1, 2 o 3 pasos)")
    print(f"escalones_3pasos(4)  = {escalones_3pasos(4)}")    # 7
    print(f"escalones_3pasos(10) = {escalones_3pasos(10)}")   # 274

    print("\nEJERCICIO 4 — Potencia con memo")
    print(f"potencia(2, 10) = {potencia(2, 10)}")    # 1024
    print(f"potencia(3, 5)  = {potencia(3, 5)}")     # 243

    print("\nEJERCICIO 5 — Caminos en cuadrícula")
    print(f"caminos(3, 3) = {caminos(3, 3)}")        # 6
    print(f"caminos(4, 4) = {caminos(4, 4)}")        # 20

    print("\nEJERCICIO 6 — Suma de dígitos")
    print(f"suma_digitos(1234) = {suma_digitos(1234)}")  # 10
    print(f"suma_digitos(999)  = {suma_digitos(999)}")   # 27

    print("\nEJERCICIO 7 — Cambio de monedas")
    print(f"cambio(15) = {cambio(15)}")              # 6
    print(f"cambio(10) = {cambio(10)}")              # 4

    print("\nEJERCICIO 8 — Máximo de lista")
    print(f"maximo_lista([3,1,9,2,7]) = {maximo_lista([3,1,9,2,7])}")  # 9

    print("\nEJERCICIO 9 — LIS (subsecuencia creciente más larga)")
    print(f"lis([3,1,4,1,5,9,2,6]) = {lis([3,1,4,1,5,9,2,6])}")       # 4

    print("\nEJERCICIO 10 — Suma de subconjunto")
    print(f"subset_sum([3,1,5,9,2], 7)  = {subset_sum([3,1,5,9,2], 7)}")   # True
    print(f"subset_sum([3,1,5,9,2], 20) = {subset_sum([3,1,5,9,2], 20)}")  # False
