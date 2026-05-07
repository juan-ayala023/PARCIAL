def caminos_sin_memo(m, n):
    if m == 1 or n == 1:
        return 1
    
    return caminos_sin_memo(m-1, n) + caminos_sin_memo(m, n-1)

def caminos_con_memo(m, n, memo=None):
    if memo is None:
        memo = {}
    
    if (m, n) in memo:
        return memo[(m, n)]
    
    if m == 1 or n == 1:
        return 1
    
    resultado = caminos_con_memo(m-1, n, memo) + caminos_con_memo(m, n-1, memo)
    memo[(m, n)] = resultado
    
    return resultado

if __name__ == "__main__":
    print("--- Pruebas sin Memoización ---")
    print(f"Caminos (2x2): {caminos_sin_memo(2, 2)}")
    print(f"Caminos (3x3): {caminos_sin_memo(3, 3)}")
    print(f"Caminos (4x4): {caminos_sin_memo(4, 4)}")
    
    print("\n--- Pruebas con Memoización ---")
    print(f"Caminos (10x10): {caminos_con_memo(10, 10)}")
    print(f"Caminos (25x15): {caminos_con_memo(25, 15)}")