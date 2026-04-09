# ============================================================
#  RECURSIVIDAD + MEMOIZACIÓN - Guía de Estudio
#  Parcial Algoritmos y Programación 4
# ============================================================

# ──────────────────────────────────────────────────────────
# ESTRUCTURA DE UNA FUNCIÓN RECURSIVA
#
#  def funcion(n):
#      # 1. CASO(S) BASE  → parar la recursión
#      if n <= 0:
#          return valor_simple
#
#      # 2. CASO RECURSIVO → llama a sí misma con n más pequeño
#      return algo + funcion(n - 1)
#
# SIN caso base → recursión infinita → RecursionError
# ──────────────────────────────────────────────────────────


# ──────────────────────────────────────────────────────────
# 1. ESCALONES SIN MEMO (recursividad pura)
# ──────────────────────────────────────────────────────────
# Subir n escalones de 1 o 2 en 1:
#   escalones(0) = 1   (una forma: no hacer nada)
#   escalones(1) = 1   (solo [1])
#   escalones(n) = escalones(n-1) + escalones(n-2)
#
# Es exactamente la secuencia de Fibonacci desplazada.

def escalones_sin_memo(n):
    """
    Calcula formas de subir n escalones (1 o 2 a la vez).
    Recursividad pura, sin memorización.
    """
    # Casos base
    if n == 0:
        return 1   # hay 1 forma de "no subir nada"
    if n == 1:
        return 1   # solo [1]

    # Caso recursivo
    return escalones_sin_memo(n - 1) + escalones_sin_memo(n - 2)

print("=== escalones_sin_memo ===")
for i in range(8):
    print(f"  n={i}: {escalones_sin_memo(i)} formas")
# n=0:1  n=1:1  n=2:2  n=3:3  n=4:5  n=5:8  n=6:13  n=7:21


# ──────────────────────────────────────────────────────────
# 2. ESCALONES CON MEMO (memoización)
# ──────────────────────────────────────────────────────────
# Problema del sin_memo: recalcula los mismos valores muchas veces.
# escalones(5) llama escalones(4) y escalones(3)
# escalones(4) llama escalones(3) y escalones(2)
# escalones(3) se calcula 2 veces, escalones(2) varias veces...
#
# Solución: guardar resultados ya calculados en un diccionario.
# PATRÓN:
#   1. Al inicio crear memo = {} si no existe
#   2. Antes de calcular, revisar si n ya está en memo
#   3. Si no está, calcularlo y guardarlo en memo[n]
#   4. Retornar memo[n]

def escalones_con_memo(n, memo=None):
    """
    Misma función con memoización para evitar recalcular.
    """
    if memo is None:
        memo = {}   # crear diccionario en la primera llamada

    # Casos base
    if n == 0:
        return 1
    if n == 1:
        return 1

    # Si ya calculamos este valor, lo devolvemos directo
    if n in memo:
        return memo[n]

    # Si no, calculamos, guardamos y retornamos
    memo[n] = escalones_con_memo(n - 1, memo) + escalones_con_memo(n - 2, memo)
    return memo[n]

print("\n=== escalones_con_memo ===")
print(f"  escalones_con_memo(10) = {escalones_con_memo(10)}")   # 89
print(f"  escalones_con_memo(30) = {escalones_con_memo(30)}")   # 1346269
print(f"  escalones_con_memo(40) = {escalones_con_memo(40)}")   # rápido


# ──────────────────────────────────────────────────────────
# 3. COMPARACIÓN DE RENDIMIENTO
# ──────────────────────────────────────────────────────────
import time

n = 35

inicio = time.time()
r1 = escalones_sin_memo(n)
fin = time.time()
print(f"\n  Sin memo  n={n}: {r1} → {(fin-inicio)*1000:.1f} ms")

inicio = time.time()
r2 = escalones_con_memo(n)
fin = time.time()
print(f"  Con memo  n={n}: {r2} → {(fin-inicio)*1000:.3f} ms")


# ──────────────────────────────────────────────────────────
# 4. OTROS EJEMPLOS DE RECURSIVIDAD (para repasar el patrón)
# ──────────────────────────────────────────────────────────

# --- Factorial ---
def factorial(n):
    if n == 0:          # caso base
        return 1
    return n * factorial(n - 1)

print("\n=== factorial ===")
print(f"  5! = {factorial(5)}")   # 120

# --- Suma de lista ---
def suma_lista(lst):
    if len(lst) == 0:   # caso base
        return 0
    return lst[0] + suma_lista(lst[1:])

print("\n=== suma_lista ===")
print(f"  suma([1,2,3,4,5]) = {suma_lista([1,2,3,4,5])}")   # 15

# --- Fibonacci con memo (el clásico) ---
def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

print("\n=== fibonacci con memo ===")
print(f"  fib(10) = {fibonacci(10)}")   # 55
print(f"  fib(50) = {fibonacci(50)}")   # 12586269025


# ──────────────────────────────────────────────────────────
# 5. CHECKLIST PARA EL PARCIAL
# ──────────────────────────────────────────────────────────
# ✅ ¿Definí todos los casos base?
# ✅ ¿La llamada recursiva usa un valor MÁS PEQUEÑO (n-1, n-2)?
# ✅ ¿El memo se crea con memo=None como parámetro por defecto?
# ✅ ¿Verifico `if n in memo` ANTES de calcular?
# ✅ ¿Guardo en memo[n] ANTES de retornar?
# ✅ ¿Paso el memo en cada llamada recursiva?
